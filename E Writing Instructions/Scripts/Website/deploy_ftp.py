"""Upload the built website to the web server by FTP, using only Python's standard library.

Deploy-Website.bat runs this when WinSCP is not installed. It reads the login from
_ftp.txt (host, user, password, remote, protocol = ftp or ftps), uploads every file in
B Working Papers/A.Website/_site whose size differs from the server copy (or is missing
there), creating folders as needed, then deletes the files retired from the site.

Usage:  python deploy_ftp.py <_ftp.txt> <_site folder> [--all]
        --all   upload every file, even if the server copy has the same size
"""
import ftplib
import sys
from pathlib import Path

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
            sys.exit(f"_ftp.txt has no {k} = ... line")
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


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cfg = read_cfg(sys.argv[1])
    site = Path(sys.argv[2])
    upload_all = "--all" in sys.argv
    remote = "/" + cfg.get("remote", "/public_html").strip("/")
    if not (site / "index.html").exists():
        sys.exit(f"No built site at {site} - run Compile-Website.bat first")

    ftp = connect(cfg)
    print(f"Connected to {cfg['host']} as {cfg['user']}; uploading to {remote}")
    made, sent, same = set(), 0, 0
    for f in sorted(p for p in site.rglob("*") if p.is_file()):
        rel = f.relative_to(site).as_posix()
        target = f"{remote}/{rel}"
        if not upload_all and remote_size(ftp, target) == f.stat().st_size:
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
    ftp.quit()
    print("Done.")


if __name__ == "__main__":
    main()
