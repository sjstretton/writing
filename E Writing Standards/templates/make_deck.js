// Four-slide concept deck for the Climate Fiscal Policy Briefs.
// Usage: node make_deck.js <spec.json> <out.pptx>
// The spec (one per paper, in 1.Presentation/slides.json) holds:
//   series, title, subtitle, message           -> slide 1 (dark): the one-line finding
//   problem: {title, stats:[{value,label}], text} -> slide 2: the problem, big numbers
//   mechanism: {title, image, caption, points[]} -> slide 3: how it works, with a figure
//   action: {title, results[], todo[]}           -> slide 4 (dark): results and what to do
// Paths to images are relative to the spec file.
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
    objects: [{ text: { text: spec.series, options: { x: 0.5, y: 5.15, w: 9, h: 0.3, fontSize: 10, color: C.accent3, isTextBox: true } } }],
    slideNumber: { x: 9.2, y: 5.15, w: 0.4, h: 0.3, fontSize: 10, color: C.accent3 },
  });
  pres.defineSlideMaster({
    title: "LIGHT",
    background: { color: C.background1 },
    objects: [{ text: { text: spec.series, options: { x: 0.5, y: 5.15, w: 9, h: 0.3, fontSize: 10, color: C.accent5, isTextBox: true } } }],
    slideNumber: { x: 9.2, y: 5.15, w: 0.4, h: 0.3, fontSize: 10, color: C.accent5 },
  });

  // Slide 1: title and the one-line finding
  pres.addSection({ title: "Finding" });
  let s = pres.addSlide({ masterName: "DARK", sectionTitle: "Finding" });
  s.addText(spec.title, { x: 0.5, y: 0.7, w: 9, h: 1.3, fontFace: "Cambria", fontSize: 36, bold: true, color: C.background1, isTextBox: true, valign: "bottom", margin: 0 });
  s.addText(spec.subtitle, { x: 0.5, y: 2.05, w: 9, h: 0.6, fontSize: 18, color: C.accent3, isTextBox: true, margin: 0 });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 3.0, w: 9, h: 1.6, fill: { color: C.accent1 }, rectRadius: 0.12, objectName: "message card" });
  s.addText(spec.message, { x: 0.8, y: 3.1, w: 8.4, h: 1.4, fontSize: 18, color: C.background1, isTextBox: true, valign: "middle", margin: 0 });
  s.addText("Stephen J. Stretton, writing in a personal capacity", { x: 0.5, y: 4.7, w: 9, h: 0.3, fontSize: 11, color: C.background2, isTextBox: true, margin: 0 });
  s.addNotes(spec.notes1 || spec.message);

  // Slide 2: the problem, with big numbers
  pres.addSection({ title: "Problem" });
  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "Problem" });
  s.addText(spec.problem.title, { x: 0.5, y: 0.35, w: 9, h: 0.8, fontFace: "Cambria", fontSize: 28, bold: true, color: C.text2, isTextBox: true, margin: 0 });
  const stats = spec.problem.stats;
  const cw = (9 - 0.3 * (stats.length - 1)) / stats.length;
  stats.forEach((st, i) => {
    const x = 0.5 + i * (cw + 0.3);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.35, w: cw, h: 1.9, fill: { color: C.background2 }, rectRadius: 0.1, objectName: "stat card " + (i + 1) });
    s.addText(st.value, { x: x + 0.15, y: 1.45, w: cw - 0.3, h: 0.95, fontFace: "Cambria", fontSize: 40, bold: true, color: i === 0 ? C.accent4 : C.accent2, isTextBox: true, align: "left", margin: 0 });
    s.addText(st.label, { x: x + 0.15, y: 2.4, w: cw - 0.3, h: 0.8, fontSize: 13, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
  });
  s.addText(spec.problem.text, { x: 0.5, y: 3.5, w: 9, h: 1.4, fontSize: 15, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
  s.addNotes(spec.notes2 || spec.problem.text);

  // Slide 3: the mechanism, with a figure
  pres.addSection({ title: "Mechanism" });
  s = pres.addSlide({ masterName: "LIGHT", sectionTitle: "Mechanism" });
  s.addText(spec.mechanism.title, { x: 0.5, y: 0.35, w: 9, h: 0.8, fontFace: "Cambria", fontSize: 28, bold: true, color: C.text2, isTextBox: true, margin: 0 });
  const img = path.resolve(base, spec.mechanism.image);
  if (spec.mechanism.layout === "wide") {
    // Figure across the slide, points as cards underneath
    const ih = spec.mechanism.imageHeight || 2.3;
    const iw = Math.min(9, ih * (spec.mechanism.aspect || 3.1));
    s.addImage({ path: img, x: 0.5 + (9 - iw) / 2, y: 1.15, w: iw, h: ih, altText: spec.mechanism.caption, objectName: "figure" });
    s.addText(spec.mechanism.caption, { x: 0.5, y: 1.15 + ih + 0.02, w: 9, h: 0.3, fontSize: 10, italic: true, color: C.accent5, isTextBox: true, margin: 0 });
    const pts = spec.mechanism.points;
    const pw = (9 - 0.3 * (pts.length - 1)) / pts.length;
    const py = 1.15 + ih + 0.4;
    pts.forEach((p, i) => {
      const x = 0.5 + i * (pw + 0.3);
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: py, w: pw, h: 4.95 - py, fill: { color: C.background2 }, rectRadius: 0.08, objectName: "point card " + (i + 1) });
      s.addText(p, { x: x + 0.12, y: py + 0.08, w: pw - 0.24, h: 4.95 - py - 0.16, fontSize: 12, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
    });
  } else {
    const iw = spec.mechanism.imageWidth || 5.6;
    const ih = spec.mechanism.imageHeight || 3.3;
    s.addImage({ path: img, x: 0.5, y: 1.3, w: iw, h: ih, altText: spec.mechanism.caption, objectName: "figure" });
    s.addText(spec.mechanism.caption, { x: 0.5, y: 1.3 + ih + 0.05, w: iw, h: 0.4, fontSize: 10, italic: true, color: C.accent5, isTextBox: true, margin: 0 });
    const tx = 0.5 + iw + 0.3;
    s.addText(spec.mechanism.points.map((p, i, a) => ({ text: p, options: { bullet: true, breakLine: i < a.length - 1, paraSpaceAfter: 8 } })),
      { x: tx, y: 1.3, w: 9.5 - tx, h: 3.6, fontSize: 14, color: C.text1, isTextBox: true, valign: "top", margin: 0 });
  }
  s.addNotes(spec.notes3 || spec.mechanism.points.join(" "));

  // Slide 4: results and what to do
  pres.addSection({ title: "Action" });
  s = pres.addSlide({ masterName: "DARK", sectionTitle: "Action" });
  s.addText(spec.action.title, { x: 0.5, y: 0.35, w: 9, h: 0.8, fontFace: "Cambria", fontSize: 28, bold: true, color: C.background1, isTextBox: true, margin: 0 });
  s.addText("What follows", { x: 0.5, y: 1.25, w: 4.3, h: 0.4, fontSize: 16, bold: true, color: C.accent3, isTextBox: true, margin: 0 });
  s.addText(spec.action.results.map((p, i, a) => ({ text: p, options: { bullet: true, breakLine: i < a.length - 1, paraSpaceAfter: 6 } })),
    { x: 0.5, y: 1.7, w: 4.3, h: 3.3, fontSize: 14, color: C.background1, isTextBox: true, valign: "top", margin: 0 });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 5.1, y: 1.25, w: 4.4, h: 3.7, fill: { color: C.accent1 }, rectRadius: 0.1, objectName: "action card" });
  s.addText("What to do", { x: 5.35, y: 1.4, w: 3.9, h: 0.4, fontSize: 16, bold: true, color: C.background1, isTextBox: true, margin: 0 });
  s.addText(spec.action.todo.map((p, i, a) => ({ text: p, options: { bullet: { type: "number" }, breakLine: i < a.length - 1, paraSpaceAfter: 6 } })),
    { x: 5.35, y: 1.85, w: 3.9, h: 3.0, fontSize: 14, color: C.background1, isTextBox: true, valign: "top", margin: 0 });
  s.addNotes(spec.notes4 || spec.action.todo.join(" "));

  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("wrote " + out);
}
main().catch((e) => { console.error(e); process.exit(1); });
