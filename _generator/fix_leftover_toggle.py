with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

bad_snippet = """// 1-Click VI / EN Language Switcher

  const btnVi = document.getElementById('lang-btn-vi');
  const btnEn = document.getElementById('lang-btn-en');
  if (btnVi && btnEn) {
    if (lang === 'vi') {
      btnVi.className = 'px-2.5 py-1 rounded-lg font-black transition bg-cyan-600 text-white shadow-sm flex items-center gap-1';
      btnEn.className = 'px-2.5 py-1 rounded-lg font-black transition text-slate-400 hover:text-white flex items-center gap-1';
    } else {
      btnEn.className = 'px-2.5 py-1 rounded-lg font-black transition bg-cyan-600 text-white shadow-sm flex items-center gap-1';
      btnVi.className = 'px-2.5 py-1 rounded-lg font-black transition text-slate-400 hover:text-white flex items-center gap-1';
    }
  }
  playSound('click');
}"""

if bad_snippet in text:
    text = text.replace(bad_snippet, "")
    with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned up leftover toggle fragment.")
else:
    print("bad_snippet not matched directly!")
