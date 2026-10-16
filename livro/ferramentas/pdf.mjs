// Converte o HTML do livro em PDF A5 com números de página, usando o Chromium do Playwright.
// Uso: node pdf.mjs <entrada.html> <saida.pdf>
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
let playwright;
try {
  playwright = require("playwright");
} catch {
  const globalRoot = execSync("npm root -g").toString().trim();
  playwright = require(`${globalRoot}/playwright`);
}

const [, , entrada, saida] = process.argv;
const browser = await playwright.chromium.launch();
const page = await browser.newPage();
await page.goto(pathToFileURL(entrada).href, { waitUntil: "load" });
await page.pdf({
  path: saida,
  format: "A5",
  printBackground: true,
  displayHeaderFooter: true,
  headerTemplate: "<span></span>",
  footerTemplate:
    '<div style="width:100%;text-align:center;font-family:Charter,Georgia,serif;font-size:8pt;color:#777"><span class="pageNumber"></span></div>',
  margin: { top: "16mm", bottom: "18mm", left: "15mm", right: "15mm" },
});
await browser.close();
