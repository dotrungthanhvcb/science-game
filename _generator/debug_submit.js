const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Parse all IDs from index.html
const idRegex = /id=["']([^"']+)["']/g;
const ids = new Set();
let match;
while ((match = idRegex.exec(html)) !== null) {
  ids.add(match[1]);
}

console.log("Total unique IDs in HTML:", ids.size);

// Check if all IDs accessed in submitAndFinishQuiz and openQuizResultModal exist
const accessedIds = [
  'modal-quick-nav',
  'modal-confirm-submit',
  'btn-replay-wrong',
  'result-screen',
  'btn-res-review-wrong',
  'btn-res-review-wrong-text',
  'apps-script-url',
  'sync-status',
  'user-name',
  'student-class',
  'modal-quiz-result',
  'modal-res-tag',
  'modal-res-score',
  'modal-res-correct',
  'modal-res-wrong',
  'modal-res-time',
  'modal-lbl-score',
  'modal-lbl-correct',
  'modal-lbl-wrong',
  'modal-lbl-time',
  'modal-res-title',
  'modal-res-desc',
  'modal-res-stars',
  'modal-res-icon',
  'modal-mascot-speech',
  'btn-modal-review-wrong',
  'btn-modal-review-wrong-text',
  'btn-modal-replay-wrong',
  'btn-modal-review-all-text',
  'btn-modal-card-mode-text',
  'btn-modal-replay-wrong-text',
  'btn-modal-lead-text',
  'btn-modal-back-home-text'
];

accessedIds.forEach(id => {
  if (!ids.has(id)) {
    console.error(`MISSING ID in HTML: ${id} ❌`);
  } else {
    console.log(`Found ID: ${id} ✅`);
  }
});
