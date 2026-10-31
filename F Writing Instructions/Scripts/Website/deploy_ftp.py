"""Upload the built website to the web server by FTP, using only Python's standard library.

Push-Website.bat runs this when WinSCP is not installed. It reads the login from
FTP-Login.txt at the top of the repository (host, user, password, remote, protocol = ftp or ftps), uploads every file in
D Website/_site whose size differs from the server copy (or is missing
there), creating folders as needed, then deletes the files retired from the site.
Web pages (.html, .css, .js, .json, .xml) are always uploaded: an edited page can keep
the same size, and a size check alone would skip it.

Before uploading it checks that the remote folder already exists and already holds the
site (index.html); otherwise it stops rather than creating a new folder the web server
never serves. Afterwards it reads research.html back from the server and, if FTP-Login.txt
has a "url = https://..." line, from the live website, and says whether each matches
the built copy.

Usage:  python deploy_ftp.py <FTP-Login.txt> <_site folder> [--all] [--check]
        --all     upload every file, even if the server copy has the same size
        --check   upload nothing: just show where the site is and whether it matches
"""
import io
import urllib.request
import ftplib
import sys
from pathlib import Path

ALWAYS = {".html", ".css", ".js", ".json", ".xml"}
PROBE = "research.html"

RETIRED = [
    "papers/SustainabilityLinkedLending.pdf",
    "papers/MDBClimateEnvelope.docx",
    "papers/GeoprosperityIntro.docx",
    "papers/CombinedOverview.docx",
]


def read_cfg(path):
    cfg = {}
    for line in Path(path).read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        cfg[k.strip().lower()] = v.strip()
    for k in ("host", "user", "password"):
        if not cfg.get(k):
            sys.exit(f"FTP-Login.txt has no {k} = ... line")
    return cfg


def connect(cfg):
    port = int(cfg.get("port", 21))
    if cfg.get("protocol", "ftp").lower() == "ftps":
        ftp = ftplib.FTP_TLS()
        ftp.connect(cfg["host"], port, timeout=60)
        ftp.login(cfg["user"], cfg["password"])
        ftp.prot_p()
    else:
        ftp = ftplib.FTP()
        ftp.connect(cfg["host"], port, timeout=60)
        ftp.login(cfg["user"], cfg["password"])
    ftp.set_pasv(True)
    return ftp


def remote_size(ftp, path):
    try:
        ftp.voidcmd("TYPE I")
        return ftp.size(path)
    except ftplib.all_errors:
        return None


def ensure_dir(ftp, path, made):
    parts = [p for p in path.split("/") if p]
    cur = ""
    for p in parts:
        cur += "/" + p
        if cur in made:
            continue
        try:
            ftp.mkd(cur)
        except ftplib.error_perm:
            pass  # already exists
        made.add(cur)


def is_dir(ftp, path):
    here = ftp.pwd()
    try:
        ftp.cwd(path)
        return True
    except ftplib.all_errors:
        return False
    finally:
        ftp.cwd(here)


def server_bytes(ftp, path):
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {path}", buf.write)
    except ftplib.all_errors:
        return None
    return buf.getvalue()


def live_bytes(url):
    req = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read()
    except Exception as e:  # noqa: BLE001 - report any failure and carry on
        print(f"  could not fetch {url}: {e}")
        return None


def check(ftp, cfg, site, remote):
    """Compare research.html as built, on the server and on the live website."""
    local = (site / PROBE).read_bytes()
    on_server = server_bytes(ftp, f"{remote}/{PROBE}")
    if on_server is None:
        print(f"  {remote}/{PROBE} is not on the server.")
    elif on_server == local:
        print(f"  {remote}/{PROBE} on the server matches the built copy.")
    else:
        print(f"  {remote}/{PROBE} on the server DIFFERS from the built copy.")
    url = cfg.get("url")
    if not url:
        print('  Add a line "url = https://your-site" to FTP-Login.txt to check the live website too.')
        return
    live = live_bytes(url.rstrip("/") + f"/{PROBE}?nocache=1")
    if live is None:
        return
    if live == local:
        print(f"  The live website's {PROBE} matches the built copy.")
    elif on_server == local:
        print(f"  The live website's {PROBE} is NOT the uploaded one, although the server folder {remote} has it.")
        print("  So the website is served from a different folder (or a cache): set remote = to the folder")
        print("  your host names as this domain's document root, or purge the host's cache.")
    else:
        print(f"  The live website's {PROBE} differs from the built copy.")


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cfg = read_cfg(sys.argv[1])
    site = Path(sys.argv[2])
    upload_all = "--all" in sys.argv
    check_only = "--check" in sys.argv
    remote = "/" + cfg.get("remote", "/public_html").strip("/")
    if not (site / "index.html").exists():
        sys.exit(f"No built site at {site} - run Compile-Website.bat first")

    ftp = connect(cfg)
    print(f"Connected to {cfg['host']} as {cfg['user']}; login folder {ftp.pwd()}; site folder {remote}")
    if not is_dir(ftp, remote):
        top = ", ".join(sorted(ftp.nlst("/"))) or "(empty)"
        ftp.quit()
        sys.exit(f"The folder {remote} does not exist on the server, so nothing was uploaded.\n"
                 f"Folders at the top of this FTP login: {top}\n"
                 f"Set remote = in FTP-Login.txt to the folder that holds the website (often / for an FTP login"
                 f" that opens inside public_html).")
    if remote_size(ftp, f"{remote}/index.html") is None:
        ftp.quit()
        sys.exit(f"{remote} has no index.html, so it is probably not the folder the website is served from.\n"
                 f"Nothing was uploaded. Check remote = in FTP-Login.txt.")
    if check_only:
        check(ftp, cfg, site, remote)
        ftp.quit()
        return
    made, sent, same = set(), 0, 0
    for f in sorted(p for p in site.rglob("*") if p.is_file()):
        rel = f.relative_to(site).as_posix()
        target = f"{remote}/{rel}"
        if (not upload_all and f.suffix.lower() not in ALWAYS
                and remote_size(ftp, target) == f.stat().st_size):
            same += 1
            continue
        ensure_dir(ftp, target.rsplit("/", 1)[0], made)
        with open(f, "rb") as fh:
            ftp.storbinary(f"STOR {target}", fh)
        sent += 1
        print(f"  uploaded {rel}")
    print(f"Uploaded {sent} files; {same} already up to date.")

    for rel in RETIRED:
        try:
            ftp.delete(f"{remote}/{rel}")
            print(f"  deleted retired file {rel}")
        except ftplib.error_perm:
            pass  # already gone
    print("Checking the result:")
    check(ftp, cfg, site, remote)
    ftp.quit()
    print("Done.")


if __name__ == "__main__":
    main()
