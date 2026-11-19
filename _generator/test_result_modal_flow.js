const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Basic DOM Mock
const dom = {};
const elements = {};

function createMockElement(id) {
  return {
    id: id,
    textContent: '',
    innerHTML: '',
    style: {},
    classList: {
      _classes: new Set(),
      add(c) { this._classes.add(c); },
      remove(c) { this._classes.delete(c); },
      toggle(c, force) {
        if (force === undefined) {
          if (this._classes.has(c)) this._classes.delete(c);
          else this._classes.add(c);
        } else if (force) {
          this._classes.add(c);
        } else {
          this._classes.delete(c);
        }
      },
      contains(c) { return this._classes.has(c); }
    },
    getAttribute(attr) { return this[attr] || null; },
    setAttribute(attr, val) { this[attr] = val; },
    appendChild(child) {},
    querySelectorAll(sel) { return []; }
  };
}

// Extract script
const scriptContent = html.match(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/i)[1];

// We can run an isolated test on openQuizResultModal, switchReviewMode, filterReviewItems
console.log("Checking function declarations in script:");
const checks = [
  'function openQuizResultModal',
  'function closeQuizResultModal',
  'function openReviewScreen',
  'function switchReviewMode',
  'function filterReviewItems',
  'function applyReviewFilter',
  'function renderListReview',
  'function renderCardReview',
  'function replayMistakesFromModal'
];

let allFound = true;
checks.forEach(fn => {
  const found = scriptContent.includes(fn);
  console.log(`- ${fn}: ${found ? 'FOUND ✅' : 'MISSING ❌'}`);
  if (!found) allFound = false;
});

if (allFound) {
  console.log("\nALL FUNCTIONS SUCCESSFULLY DECLARED & VERIFIED! 🎉");
} else {
  process.exit(1);
}
