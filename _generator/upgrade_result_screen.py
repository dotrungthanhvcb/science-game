import re

INDEX_PATH = "/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Replace action-buttons with Figma AI 3D buttons
old_actions = re.search(r'<div class=\"action-buttons\">.*?</div>\s*</div>\s*(?=<div style=\"text-align:center; font-size:0.85rem; color:var\(--text-muted\); margin-top:14px;\" id=\"sync-status\">)', text, re.DOTALL)

if old_actions:
    new_actions = """<div class="action-buttons flex flex-col gap-3 my-4">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
        <button type="button" class="btn-3d btn-3d-cyan py-3 px-4 text-xs font-black shadow-md flex items-center justify-center gap-2" onclick="openReviewScreen()">
          <i data-lucide="eye" style="width:16px; height:16px;"></i>
          <span>XEM LẠI CHI TIẾT BÀI LÀM</span>
        </button>
        <button type="button" class="btn-3d btn-3d-amber py-3 px-4 text-xs font-black shadow-md flex items-center justify-center gap-2" onclick="openLeaderboardModal()">
          <i data-lucide="trophy" style="width:16px; height:16px;"></i>
          <span>XEM BẢNG SAO TUẦN NÀY 🌟</span>
        </button>
      </div>

      <div class="flex items-center justify-center gap-2 flex-wrap">
        <button type="button" class="btn-3d btn-3d-purple py-2 px-3.5 text-xs font-bold" onclick="replayMistakes()" id="btn-replay-wrong">
          <i data-lucide="rotate-ccw" style="width:14px; height:14px;"></i>
          <span>Ôn lại câu sai</span>
        </button>
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50" onclick="launchFireworks()" title="Bắn pháo hoa ăn mừng">
          <span>🎊 Bắn Pháo Hoa</span>
        </button>
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50" onclick="openHistoryScreen()">
          <i data-lucide="bar-chart-2" style="width:14px; height:14px;"></i>
          <span>Lịch Sử</span>
        </button>
        <button type="button" class="btn-3d py-2 px-3.5 text-xs font-bold bg-emerald-50 border border-emerald-300 text-emerald-800 hover:bg-emerald-100" onclick="syncAllHistoryToSheets()">
          <i data-lucide="cloud" style="width:14px; height:14px;"></i>
          <span>Đồng bộ Sheets</span>
        </button>
        <button type="button" class="btn-3d btn-3d-cyan py-2 px-4 text-xs font-bold" onclick="showScreen('home-screen')">
          <i data-lucide="home" style="width:14px; height:14px;"></i>
          <span>Về Phòng Lab</span>
        </button>
      </div>
    </div>"""

    text = text.replace(old_actions.group(0), new_actions + "\n    ")
    
    # Make mascot avatar dance on result screen
    text = text.replace('class="animate-bounce"', 'class="animate-mascot-dance"')

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print("Upgraded result-screen action buttons and mascot animation.")
else:
    print("Could not find old_actions!")
