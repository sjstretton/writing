// Theme deck (about 8-12 slides) for a series of Climate Fiscal Policy Briefs.
// Same theme, colours, fonts and masters as make_deck.js.
// Usage: node make_theme_deck.js <spec.json> <out.pptx>   (needs pptxgenjs and PPTX_SKILL)
// The spec (one per series, in <series>/1.Presentation/slides-theme.json) holds:
//   series: footer line;  title: deck title (metadata);  slides: ordered list, each with "type":
//   title     {title, subtitle, message}                       dark: title and one-line message
//   statement {title, text, points[], dark?}                    a claim in large type, optional points
//   stats     {title, stats:[{value,label}], text}              big numbers (2-4) and a short paragraph
//   table     {title, header[], rows[][], colW[], note, fontSize?}  a comparison table
//   figure    {title, image, caption, points[], layout?, imageWidth?, imageHeight?, aspect?}
//             layout "side" (default): figure left, bullets right; "wide": figure across, points as cards
//   twocol    {title, left:{heading, points[]}, right:{heading, points[]}, text?}
//   closing   {title, todo[], papers[]}                         dark: what to do, and the papers
// Every slide may carry "notes". Paths to images are relative to the spec file.
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const THEME = {
  name: "Climate Fiscal",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B1B1B", lt1: "FFFFFF", dk2: "1E3A2B", lt2: "EEF3EE",
    accent1: "2E7D32", accent2: "1F4E79", accent3: "97BC62", accent4: "C62828",
    accent5: "6B7B6E", accent6: "F2B705", hlink: "1F4E79", folHlink: "6B7B6E",
  },
};

const bullets = (items, opts = {}) =>
  items.map((p, i, a) => ({ text: p, options: { bullet: opts.number ? { type: "number" } : true, breakLine: i < a.length - 1, paraSpaceAfter: opts.space || 6 } }));

async function main() {
  const specPath = process.argv[2];
  const out = process.argv[3];
  const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
  const base = path.dirname(specPath);
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.author = "Stephen J. Stretton";
  pres.title = spec.title;
  const C = pres.SchemeColor;

  pres.defineSlideMaster({
    title: "DARK",
    background: { color: C.text2 },
    objects: [{ text: { text: spec.series, options: { x: 0.5, y: 5.15, w: 8.6, h: 0.3, fontSize: 10, color: C.accent3, isTextBox: true } } }],
    slideNumber: { x: 9.2, y: 5.15, w: 0.4, h: 0.3, fontSize: 10, color: C.accent3 },
  });
  pres.defineSlideMaster({
    title: "LIGHT",
    background: { color: C.background1 },
    objects: [{ text: { text: spec.series, options: { x: 0.5, y: 5.15, w: 8.6, h: 0.3, fontSize: 10, color: C.accent5, isTextBox: true } } }],
    slideNumber: { x: 9.2, y: 5.15, w: 0.4, h: 0.3, fontSize: 10, color: C.accent5 },
  });

  const heading = (s, text, dark) =>
    s.addText(text, { x: 0.5, y: 0.35, w: 9, h: 0.8, fontFace: "Cambria", fontSize: 28, bold: true, color: dark ? C.background1 : C.text2, isTextBox: true, margin: 0, valign: "middle" });

  const builders = {
    title(s, d) {
      s.addText(d.title, { x: 0.5, y: 0.7, w: 9, h: 1.3, fontFace: "Cambria", fontSize: 36, bold: true, color: C.background1, isTextBox: true, valign: "bottom", margin: 0 });
      s.addText(d.subtitle, { x: 0.5, y: 2.05, w: 9, h: 0.6, fontSize: 18, color: C.accent3, isTextBox: true, margin: 0 });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 3.0, w: 9, h: 1.6, fill: { color: C.accent1 }, rectRadius: 0.12, objectName: "message card" });
      s.addText(d.message, { x: 0.8, y: 3.1, w: 8.4, h: 1.4, fontSize: 18, color: C.background1, isTextBox: true, valign: "middle", margin: 0 });
      s.addText("Stephen J. Stretton, writing in a personal capacity", { x: 0.5, y: 4.7, w: 9, h: 0.3, fontSize: 11, color: C.background2, isTextBox: true, margin: 0 });
      return d.message;
    },
    statement(s, d) {
      const dark = !!d.dark;
      heading(s, d.title, dark);
      const hasPts = d.points && d.points.length;
      s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: 1.35, w: 0.08, h: hasPts ? 1.5 : 3.2, fill: { color: C.accent1 }, objectName: "accent bar" });
      s.addText(d.text, { x: 0.8, y: 1.35, w: 8.7, h: hasPts ? 1.5 : 3.2, fontFace: "Cambria", fontSize: hasPts ? 20 : 24, color: dark ? C.background1 : C.text2, isTextBox: true, valign: "middle", margin: 0 });
      if (hasPts) {
        const pw = (9 - 0.3 * (d.points.length - 1)) / d.points.length;
        d.points.forEach((p, i) => {
          const x = 0.5 + i * (pw + 0.3);
          s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 3.15, w: pw, h: 1.8, fill: { color: dark ? C.accent1 : C.background2 }, rectRadius: 0.08, objectName: "point card " + (i + 1) });
          s.addText(p, { x: x + 0.15, y: 3.25, w: pw - 0.3, h: 1.6, fontSize: 13, color: dark ? C.background1 : C.text1, isTextBox: true, valign: "top", margin: 0 });
        });
      }
      return d.text;
    },
    stats(s, d) {
      heading(s, d.title);
      const cw = (9 - 0.3 * (d.stats.length - 1)) / d.stats.length;
      const vsize = d.stats.length > 3 ? 32 : 40;
      d.stats.forEach((st, i) => {
        const x = 0.5 + i * (cw + 0.3);
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.35, w: cw, h: 1.9, fill: { color: C.background2 }, rectRadius: 0.1, objectName: "stat card " + (i + 1) });
        s.addText(st.value, { x: x + 0.15, y: 1.45, w: cw - 0.3, h: 0.95, fontFace: "Cambria", fontSize: vsize, bold: true, color: i === 0 ? C.accent4 : C.accent2, isTextBox: true, align: "left", margin: 0 });
        s.addText(st.label, { x: x + 0.15, y: 2.4, w: cw - 0.3, h: 0.8, fontSize: 13, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
      });
      if (d.text) s.addText(d.text, { x: 0.5, y: 3.5, w: 9, h: 1.4, fontSize: 15, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
      return d.text || d.stats.map((x) => x.value + " " + x.label).join("; ");
    },
    table(s, d) {
      heading(s, d.title);
      const fsz = d.fontSize || 11;
      const head = d.header.map((h) => ({ text: h, options: { bold: true, color: C.background1, fill: { color: C.text2 }, fontSize: fsz } }));
      const body = d.rows.map((r, ri) => r.map((c, ci) => ({ text: c, options: { fontSize: fsz, color: C.text1, bold: ci === 0, fill: { color: ri % 2 ? C.background1 : C.background2 } } })));
      s.addTable([head, ...body], { x: 0.5, y: 1.3, w: 9, colW: d.colW, border: { type: "solid", pt: 0.5, color: "D5DDD6" }, valign: "middle", margin: [3, 5, 3, 5], autoPage: false });
      if (d.note) s.addText(d.note, { x: 0.5, y: 4.75, w: 9, h: 0.35, fontSize: 10, italic: true, color: C.accent5, isTextBox: true, margin: 0 });
      return d.note || d.title;
    },
    figure(s, d) {
      heading(s, d.title);
      const img = path.resolve(base, d.image);
      if (d.layout === "wide") {
        const ih = d.imageHeight || 2.3;
        const iw = Math.min(9, ih * (d.aspect || 3.1));
        s.addImage({ path: img, x: 0.5 + (9 - iw) / 2, y: 1.15, w: iw, h: ih, altText: d.caption, objectName: "figure" });
        s.addText(d.caption, { x: 0.5, y: 1.15 + ih + 0.02, w: 9, h: 0.3, fontSize: 10, italic: true, color: C.accent5, isTextBox: true, margin: 0 });
        const pw = (9 - 0.3 * (d.points.length - 1)) / d.points.length;
        const py = 1.15 + ih + 0.4;
        d.points.forEach((p, i) => {
          const x = 0.5 + i * (pw + 0.3);
          s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: py, w: pw, h: 4.95 - py, fill: { color: C.background2 }, rectRadius: 0.08, objectName: "point card " + (i + 1) });
          s.addText(p, { x: x + 0.12, y: py + 0.08, w: pw - 0.24, h: 4.95 - py - 0.16, fontSize: 12, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
        });
      } else {
        const iw = d.imageWidth || 5.6;
        const ih = d.imageHeight || 3.1;
        s.addImage({ path: img, x: 0.5, y: 1.3, w: iw, h: ih, altText: d.caption, objectName: "figure" });
        s.addText(d.caption, { x: 0.5, y: 1.3 + ih + 0.05, w: iw, h: 0.4, fontSize: 10, italic: true, color: C.accent5, isTextBox: true, margin: 0 });
        const tx = 0.5 + iw + 0.3;
        s.addText(bullets(d.points, { space: 8 }), { x: tx, y: 1.3, w: 9.5 - tx, h: 3.6, fontSize: 14, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
      }
      return d.points.join(" ");
    },
    twocol(s, d) {
      heading(s, d.title);
      const top = 1.3;
      const bottom = d.text ? 4.2 : 4.95;
      [d.left, d.right].forEach((col, i) => {
        const x = i === 0 ? 0.5 : 5.1;
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: top, w: 4.4, h: bottom - top, fill: { color: i === 0 ? C.background2 : C.background1 }, line: { color: C.accent1, width: i === 0 ? 0 : 1.25 }, rectRadius: 0.1, objectName: (i === 0 ? "left" : "right") + " column" });
        s.addText(col.heading, { x: x + 0.2, y: top + 0.12, w: 4.0, h: 0.4, fontSize: 16, bold: true, color: i === 0 ? C.accent2 : C.accent1, isTextBox: true, margin: 0 });
        s.addText(bullets(col.points), { x: x + 0.2, y: top + 0.6, w: 4.0, h: bottom - top - 0.7, fontSize: 13, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
      });
      if (d.text) s.addText(d.text, { x: 0.5, y: 4.3, w: 9, h: 0.65, fontSize: 14, color: C.text2, italic: true, isTextBox: true, valign: "top", margin: 0 });
      return d.text || d.title;
    },
    closing(s, d) {
      heading(s, d.title, true);
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 1.25, w: 4.6, h: 3.7, fill: { color: C.accent1 }, rectRadius: 0.1, objectName: "action card" });
      s.addText("What to do", { x: 0.75, y: 1.4, w: 4.1, h: 0.4, fontSize: 16, bold: true, color: C.background1, isTextBox: true, margin: 0 });
      s.addText(bullets(d.todo, { number: true }), { x: 0.75, y: 1.85, w: 4.1, h: 3.0, fontSize: d.todoFontSize || 13, color: C.background1, isTextBox: true, valign: "top", margin: 0 });
      s.addText("The papers", { x: 5.4, y: 1.25, w: 4.1, h: 0.4, fontSize: 16, bold: true, color: C.accent3, isTextBox: true, margin: 0 });
      s.addText(d.papers.map((p, i, a) => ({ text: p, options: { breakLine: i < a.length - 1, paraSpaceAfter: 8 } })),
        { x: 5.4, y: 1.7, w: 4.1, h: 3.25, fontSize: 12, color: C.background1, isTextBox: true, valign: "top", margin: 0 });
      return d.todo.join(" ");
    },
  };
  const darkTypes = { title: true, closing: true };

  spec.slides.forEach((d, i) => {
    const build = builders[d.type];
    if (!build) throw new Error("slide " + (i + 1) + ": unknown type " + d.type);
    const dark = darkTypes[d.type] || (d.type === "statement" && d.dark);
    const s = pres.addSlide({ masterName: dark ? "DARK" : "LIGHT" });
    const fallback = build(s, d);
    s.addNotes(d.notes || fallback || d.title);
  });

  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("wrote " + out + " (" + spec.slides.length + " slides)");
}
main().catch((e) => { console.error(e); process.exit(1); });
