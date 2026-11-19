const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// We will check for any syntax errors or TDZ issues if anything runs at top level
const scriptMatch = html.match(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/i);
const script = scriptMatch[1];

// Find all top-level statements that execute immediately
const lines = script.split('\n');
console.log("Total script lines:", lines.length);

// Let's check for any duplicate declarations of let / const
const declarations = {};
const declRegex = /^\s*(let|const|var)\s+([a-zA-Z0-9_$]+)/;

lines.forEach((line, idx) => {
  const m = line.match(declRegex);
  if (m) {
    const type = m[1];
    const name = m[2];
    if (declarations[name]) {
      console.warn(`Line ${idx+1}: Redeclaration of '${name}' (previously at line ${declarations[name].line} as ${declarations[name].type})`);
    } else {
      declarations[name] = { line: idx + 1, type: type };
    }
  }
});

console.log("Total top-level variables declared:", Object.keys(declarations).length);
