with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_quit = """<div class="modal-overlay" id="modal-quit">
  <div class="modal-box">
    <div class="modal-icon">🚪</div>
    <div class="modal-title">Dừng Bài Thi?</div>
    <div class="modal-desc">Bé có chắc muốn rời khỏi lượt ôn này không? Kết quả hiện tại sẽ không được lưu nếu thoát ngang.</div>
    <div class="modal-actions">
      <button class="modal-btn-cancel" onclick="closeQuitModal()">Tiếp tục làm</button>
      <button class="modal-btn-confirm" style="background:var(--danger);" onclick="confirmQuit()">Đồng ý thoát</button>
    </div>
  </div>
</div>"""

new_quit = """<div class="modal-overlay" id="modal-quit">
  <div class="modal-box text-center p-6 bg-white rounded-3xl border-4 border-slate-800 shadow-2xl max-w-sm">
    <div class="text-4xl mb-2 animate-bounce">🚪</div>
    <div class="font-baloo font-bold text-xl text-slate-900 mb-2">Dừng Bài Thi?</div>
    <div class="text-xs text-slate-600 font-medium mb-5 leading-relaxed">Bé có chắc muốn dừng bài thám hiểm này để về Trang Chủ không? Điểm số lượt thi này sẽ không được lưu nếu thoát ngang.</div>
    <div class="flex items-center justify-center gap-3">
      <button type="button" class="btn-3d px-4 py-2.5 rounded-full text-xs font-bold bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-300 transition" onclick="closeQuitModal()">
        Tiếp tục làm
      </button>
      <button type="button" class="btn-3d px-5 py-2.5 rounded-full text-xs font-black bg-rose-600 hover:bg-rose-700 text-white shadow-md transition" onclick="confirmQuit()">
        Đồng ý thoát ➔
      </button>
    </div>
  </div>
</div>"""

if old_quit in text:
    text = text.replace(old_quit, new_quit)
    with open('/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Polished modal-quit styling.")
else:
    print("old_quit not found")
