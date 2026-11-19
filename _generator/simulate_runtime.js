const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('index.html', 'utf8');

const elements = {};
function getEl(id) {
  if (!elements[id]) {
    elements[id] = {
      id: id,
      value: '',
      textContent: '',
      innerHTML: '',
      style: {},
      classList: {
        _set: new Set(),
        add(c) { this._set.add(c); },
        remove(c) { this._set.delete(c); },
        toggle(c, force) {
          if (force !== undefined) {
            if (force) this._set.add(c);
            else this._set.delete(c);
          } else {
            if (this._set.has(c)) this._set.delete(c);
            else this._set.add(c);
          }
        },
        contains(c) { return this._set.has(c); }
      },
      querySelectorAll() { return []; },
      querySelector() { return null; },
      appendChild() {},
      setAttribute() {},
      getAttribute() { return null; },
      addEventListener() {}
    };
  }
  return elements[id];
}

class MockAudioContext {
  createOscillator() {
    return {
      type: '',
      frequency: { setValueAtTime() {}, exponentialRampToValueAtTime() {} },
      connect() {},
      start() {},
      stop() {}
    };
  }
  createGain() {
    return {
      gain: { setValueAtTime() {}, exponentialRampToValueAtTime() {} },
      connect() {}
    };
  }
}

const mockWindow = {
  scrollTo() {},
  addEventListener() {},
  setInterval(fn, ms) { return 1; },
  clearInterval() {},
  setTimeout(fn, ms) { fn(); return 1; },
  clearTimeout() {},
  AudioContext: MockAudioContext,
  webkitAudioContext: MockAudioContext,
  localStorage: {
    _data: {},
    getItem(k) { return this._data[k] || null; },
    setItem(k, v) { this._data[k] = v; },
    removeItem(k) { delete this._data[k]; }
  },
  console: console,
  document: {
    getElementById(id) { return getEl(id); },
    querySelectorAll() { return []; },
    querySelector() { return null; },
    createElement(tag) { return getEl('created_' + tag + '_' + Math.random()); },
    addEventListener() {}
  },
  lucide: { createIcons() {} },
  confetti() {}
};

mockWindow.window = mockWindow;
mockWindow.document.defaultView = mockWindow;

const scriptMatch = html.match(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/i);
const script = scriptMatch[1];

const context = vm.createContext(mockWindow);

try {
  vm.runInContext(script, context);
  console.log("Initial script evaluation: SUCCESS ✅");
} catch(e) {
  console.error("Initial script evaluation ERROR ❌:", e);
  process.exit(1);
}

// Now test submitAndFinishQuiz
try {
  context.currentDeck = [
    { id: 1, q: "Câu 1", ans: "A", topic: "Địa Lý", diff: 1, type: "MC", a: "1", b: "2", c: "3", d: "4", explain: "Giải thích 1" },
    { id: 2, q: "Câu 2", ans: "B", topic: "Địa Lý", diff: 1, type: "MC", a: "1", b: "2", c: "3", d: "4", explain: "Giải thích 2" }
  ];
  context.userAnswersMap = {
    1: { chosenKey: "A", chosenText: "1" },
    2: { chosenKey: "C", chosenText: "3" }
  };
  context.elapsedSeconds = 120;
  
  console.log("Calling submitAndFinishQuiz()...");
  context.submitAndFinishQuiz();
  console.log("submitAndFinishQuiz(): SUCCESS ✅");

  const modalResult = elements['modal-quiz-result'];
  console.log("modal-quiz-result classes:", Array.from(modalResult.classList._set));
  console.log("modal-quiz-result active?", modalResult.classList.contains('active'));
  console.log("modal-res-score text:", elements['modal-res-score'].textContent);
  console.log("modal-res-correct text:", elements['modal-res-correct'].textContent);
  console.log("modal-res-wrong text:", elements['modal-res-wrong'].textContent);
  console.log("modal-res-title text:", elements['modal-res-title'].textContent);

  console.log("\nTesting openReviewScreen('wrong', 'list')...");
  context.openReviewScreen('wrong', 'list');
  console.log("openReviewScreen('wrong', 'list'): SUCCESS ✅");

  console.log("\nTesting switchReviewMode('card')...");
  context.switchReviewMode('card');
  console.log("switchReviewMode('card'): SUCCESS ✅");

} catch(e) {
  console.error("Runtime test ERROR ❌:", e);
  process.exit(1);
}

console.log("\nALL RUNTIME TESTS PASSED! 🎉");
