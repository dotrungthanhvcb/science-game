import re

with open("/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update TOPIC_EN_MAP
old_topic_en = """const TOPIC_EN_MAP = {
  'Động Vật': 'Animal Kingdom',
  'Thực Vật': 'Plants & Nature',
  'Vũ Trụ & Thời Tiết': 'Space & Weather',
  'Cơ Thể Người': 'Human Body & Health',
  'Con người & Sức khỏe': 'Human Body & Health',
  'Địa Lý Việt Nam': 'Geography & Earth',
  'Lịch Sử & Văn Hóa': 'History & Culture',
  'Vật Chất & Hiện Tượng': 'Matter & Physics',
  'Vật chất & Năng lượng': 'Matter & Energy',
  'Vật lý & Năng lượng': 'Physics & Energy',
  'Thực vật & Động vật': 'Plants & Animals',
  'Trái Đất & Bầu trời': 'Earth & Sky'
};"""

new_topic_en = """const TOPIC_EN_MAP = {
  'Động Vật': 'Animal Kingdom',
  'Thực Vật': 'Plants & Nature',
  'Vũ Trụ & Bầu Trời': 'Space & Astronomy',
  'Vũ Trụ & Thời Tiết': 'Space & Astronomy',
  'Vũ Trụ': 'Space & Astronomy',
  'Cơ Thể Người': 'Human Body & Health',
  'Con người & Sức khỏe': 'Human Body & Health',
  'Sức Khỏe': 'Human Body & Health',
  'Địa Lý': 'Geography & Earth',
  'Địa Lý Việt Nam': 'Geography & Earth',
  'Địa Lý & Trái Đất': 'Geography & Earth',
  'Lịch Sử & Văn Hóa': 'History & Culture',
  'Vật Chất & Năng Lượng': 'Matter & Energy',
  'Vật Chất & Hiện Tượng': 'Matter & Physics',
  'Vật chất & Năng lượng': 'Matter & Energy',
  'Vật lý & Năng lượng': 'Physics & Energy',
  'Thực vật & Động vật': 'Plants & Animals',
  'Trái Đất & Bầu trời': 'Earth & Sky'
};"""

if old_topic_en in content:
    content = content.replace(old_topic_en, new_topic_en)
    print("Replaced TOPIC_EN_MAP")
else:
    print("Warning: old TOPIC_EN_MAP not found exactly")

# 2. Update normalizeQuestion to include curriculum_topic
old_norm = """    source: sourceName,
    topic: q.topic || "Khác",
    sub: q.sub || "","""

new_norm = """    source: sourceName,
    topic: q.topic || "Khác",
    curriculum_topic: q.curriculum_topic || q.topic || "Khác",
    sub: q.sub || "","""

if old_norm in content:
    content = content.replace(old_norm, new_norm)
    print("Replaced normalizeQuestion topic/curriculum_topic")
else:
    print("Warning: old normalizeQuestion snippet not found")

# 3. Add isTopicMatch helper function
is_topic_match_func = """
// =========================================================================
// HELPER SO KHỚP CHỦ ĐỀ THÔNG MINH (BILINGUAL & ALIAS MATCHING)
// =========================================================================
function isTopicMatch(qTopic, filterTopic) {
  if (!filterTopic || filterTopic === 'all') return true;
  if (!qTopic) return false;
  if (qTopic === filterTopic) return true;
  
  const geoTerms = ['Địa Lý', 'Địa Lý Việt Nam', 'Địa Lý & Trái Đất', 'Địa Lý VN', 'Geography'];
  if (geoTerms.includes(filterTopic) && (geoTerms.includes(qTopic) || qTopic === 'Trái Đất & Bầu trời')) return true;
  if (geoTerms.includes(qTopic) && (geoTerms.includes(filterTopic) || filterTopic === 'Trái Đất & Bầu trời')) return true;

  const spaceTerms = ['Vũ Trụ & Bầu Trời', 'Vũ Trụ & Thời Tiết', 'Vũ Trụ', 'Space'];
  if (spaceTerms.includes(filterTopic) && (spaceTerms.includes(qTopic) || qTopic === 'Trái Đất & Bầu trời')) return true;
  if (spaceTerms.includes(qTopic) && (spaceTerms.includes(filterTopic) || filterTopic === 'Trái Đất & Bầu trời')) return true;

  const healthTerms = ['Cơ Thể Người', 'Con người & Sức khỏe', 'Sức Khỏe', 'Health'];
  if (healthTerms.includes(filterTopic) && healthTerms.includes(qTopic)) return true;
  if (healthTerms.includes(qTopic) && healthTerms.includes(filterTopic)) return true;

  const physicsTerms = ['Vật Chất & Năng Lượng', 'Vật Chất & Hiện Tượng', 'Vật chất & Năng lượng', 'Vật lý & Năng lượng', 'Physics', 'Matter'];
  if (physicsTerms.includes(filterTopic) && physicsTerms.includes(qTopic)) return true;
  if (physicsTerms.includes(qTopic) && physicsTerms.includes(filterTopic)) return true;

  const plantTerms = ['Thực Vật', 'Plants'];
  if (plantTerms.includes(filterTopic) && (plantTerms.includes(qTopic) || qTopic === 'Thực vật & Động vật')) return true;
  if (plantTerms.includes(qTopic) && (plantTerms.includes(filterTopic) || filterTopic === 'Thực vật & Động vật')) return true;

  const animalTerms = ['Động Vật', 'Animals'];
  if (animalTerms.includes(filterTopic) && (animalTerms.includes(qTopic) || qTopic === 'Thực vật & Động vật')) return true;
  if (animalTerms.includes(qTopic) && (animalTerms.includes(filterTopic) || filterTopic === 'Thực vật & Động vật')) return true;

  return false;
}
"""

if "function isTopicMatch" not in content:
    content = content.replace("function initMasterPool() {", is_topic_match_func + "\nfunction initMasterPool() {")
    print("Added isTopicMatch function")

# 4. Update TOPIC_CONFIG
old_topic_config = """const TOPIC_CONFIG = [
  { id: 'all', name: 'Tất Cả', lucide: 'sparkles' },
  { id: 'Động Vật', name: 'Động Vật', lucide: 'paw-print' },
  { id: 'Thực Vật', name: 'Thực Vật', lucide: 'sprout' },
  { id: 'Vũ Trụ & Thời Tiết', name: 'Vũ Trụ & Thời Tiết', lucide: 'rocket' },
  { id: 'Cơ Thể Người', name: 'Cơ Thể Người', lucide: 'heart-pulse' },
  { id: 'Địa Lý Việt Nam', name: 'Địa Lý VN', lucide: 'map-pin' },
  { id: 'Lịch Sử & Văn Hóa', name: 'Lịch Sử & Văn Hóa', lucide: 'landmark' },
  { id: 'Vật Chất & Hiện Tượng', name: 'Vật Lý & Năng Lượng', lucide: 'atom' }
];"""

new_topic_config = """const TOPIC_CONFIG = [
  { id: 'all', name: 'Tất Cả', name_en: 'All Topics', lucide: 'sparkles' },
  { id: 'Địa Lý', name: 'Địa Lý & Trái Đất', name_en: 'Geography', lucide: 'map-pin' },
  { id: 'Vũ Trụ & Bầu Trời', name: 'Vũ Trụ & Thiên Văn', name_en: 'Space', lucide: 'rocket' },
  { id: 'Động Vật', name: 'Động Vật', name_en: 'Animals', lucide: 'paw-print' },
  { id: 'Thực Vật', name: 'Thực Vật', name_en: 'Plants', lucide: 'sprout' },
  { id: 'Cơ Thể Người', name: 'Cơ Thể Người', name_en: 'Human Body', lucide: 'heart-pulse' },
  { id: 'Vật Chất & Năng Lượng', name: 'Vật Lý & Năng Lượng', name_en: 'Physics', lucide: 'atom' }
];"""

if old_topic_config in content:
    content = content.replace(old_topic_config, new_topic_config)
    print("Replaced TOPIC_CONFIG")
else:
    print("Warning: old TOPIC_CONFIG not found exactly")

# 5. Update getTopicSvg
old_get_topic_svg = """  if (topic === 'Động Vật') {
    bgGradient = 'linear-gradient(135deg, #FF6B6B 0%, #FFA07A 100%)';
    iconEmoji = '🦁';
    title = 'Thế Giới Động Vật';
  } else if (topic === 'Thực Vật') {
    bgGradient = 'linear-gradient(135deg, #10B981 0%, #059669 100%)';
    iconEmoji = '🌿';
    title = 'Thế Giới Thực Vật';
  } else if (topic === 'Vũ Trụ & Thời Tiết') {
    bgGradient = 'linear-gradient(135deg, #3A0CA3 0%, #4361EE 100%)';
    iconEmoji = '🌍';
    title = 'Vũ Trụ & Thời Tiết';
  } else if (topic === 'Cơ Thể Người') {
    bgGradient = 'linear-gradient(135deg, #EF4444 0%, #F43F5E 100%)';
    iconEmoji = '🫀';
    title = 'Cơ Thể Người & Sức Khỏe';
  } else if (topic === 'Địa Lý Việt Nam') {
    bgGradient = 'linear-gradient(135deg, #0284C7 0%, #06B6D4 100%)';
    iconEmoji = '🗺️';
    title = 'Địa Lý Non Sông Việt Nam';
  } else if (topic === 'Lịch Sử & Văn Hóa') {
    bgGradient = 'linear-gradient(135deg, #D97706 0%, #F59E0B 100%)';
    iconEmoji = '📜';
    title = 'Lịch Sử & Văn Hóa';
  } else if (topic === 'Vật Chất & Hiện Tượng') {
    bgGradient = 'linear-gradient(135deg, #8B5CF6 0%, #6366F1 100%)';
    iconEmoji = '🧲';
    title = 'Vật Chất & Hiện Tượng';
  }"""

new_get_topic_svg = """  if (topic === 'Động Vật') {
    bgGradient = 'linear-gradient(135deg, #FF6B6B 0%, #FFA07A 100%)';
    iconEmoji = '🦁';
    title = 'Thế Giới Động Vật';
  } else if (topic === 'Thực Vật') {
    bgGradient = 'linear-gradient(135deg, #10B981 0%, #059669 100%)';
    iconEmoji = '🌿';
    title = 'Thế Giới Thực Vật';
  } else if (topic === 'Vũ Trụ & Bầu Trời' || topic === 'Vũ Trụ & Thời Tiết' || topic === 'Vũ Trụ') {
    bgGradient = 'linear-gradient(135deg, #3A0CA3 0%, #4361EE 100%)';
    iconEmoji = '🚀';
    title = 'Vũ Trụ & Bầu Trời';
  } else if (topic === 'Cơ Thể Người' || topic === 'Con người & Sức khỏe') {
    bgGradient = 'linear-gradient(135deg, #EF4444 0%, #F43F5E 100%)';
    iconEmoji = '🫀';
    title = 'Cơ Thể Người & Sức Khỏe';
  } else if (topic === 'Địa Lý' || topic === 'Địa Lý Việt Nam' || topic === 'Địa Lý & Trái Đất') {
    bgGradient = 'linear-gradient(135deg, #0284C7 0%, #06B6D4 100%)';
    iconEmoji = '🗺️';
    title = 'Địa Lý & Trái Đất';
  } else if (topic === 'Lịch Sử & Văn Hóa') {
    bgGradient = 'linear-gradient(135deg, #D97706 0%, #F59E0B 100%)';
    iconEmoji = '📜';
    title = 'Lịch Sử & Văn Hóa';
  } else if (topic === 'Vật Chất & Năng Lượng' || topic === 'Vật Chất & Hiện Tượng' || topic === 'Vật chất & Năng lượng') {
    bgGradient = 'linear-gradient(135deg, #8B5CF6 0%, #6366F1 100%)';
    iconEmoji = '⚡';
    title = 'Vật Chất & Năng Lượng';
  }"""

if old_get_topic_svg in content:
    content = content.replace(old_get_topic_svg, new_get_topic_svg)
    print("Replaced getTopicSvg")
else:
    print("Warning: old getTopicSvg not found exactly")

# 6. Update LAB_CARDS_DATA and FILTER_PILLS
old_lab_cards = """const LAB_CARDS_DATA = [
  {
    topic: 'Động Vật',
    icon: '🦁',
    iconBg: 'bg-amber-100 border-amber-200',
    title_vi: 'Thế Giới Động Vật',
    title_en: 'Animal Kingdom',
    desc_vi: 'Động vật có vú, chim muông & côn trùng',
    desc_en: 'Mammals, birds, insects & marine life',
    count_vi: '200 Câu',
    count_en: '200 Questions',
    status_vi: '● Sẵn sàng thi',
    status_en: '● Ready to play',
    statusClass: 'text-cyan-600',
    badgeBg: 'bg-amber-100 text-amber-800'
  },
  {
    topic: 'Vũ Trụ & Thời Tiết',
    icon: '🚀',
    iconBg: 'bg-indigo-100 border-indigo-200',
    title_vi: 'Vũ Trụ & Thời Tiết',
    title_en: 'Space & Solar System',
    desc_vi: 'Hệ Mặt Trời, sao Hỏa, các hành tinh',
    desc_en: 'Planets, Mars, Sun & galaxy mysteries',
    count_vi: '180 Câu',
    count_en: '180 Questions',
    status_vi: '● Sẵn sàng thi',
    status_en: '● Ready to play',
    statusClass: 'text-cyan-600',
    badgeBg: 'bg-indigo-100 text-indigo-800'
  },
  {
    topic: 'Thực Vật',
    icon: '🌿',
    iconBg: 'bg-emerald-100 border-emerald-200',
    title_vi: 'Thực Vật & Tự Nhiên',
    title_en: 'Plants & Nature',
    desc_vi: 'Quang hợp, hạt mầm, rừng xanh',
    desc_en: 'Photosynthesis, seeds, forests & flora',
    count_vi: '120 Câu',
    count_en: '120 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-emerald-100 text-emerald-800'
  },
  {
    topic: 'Cơ Thể Người',
    icon: '🫀',
    iconBg: 'bg-rose-100 border-rose-200',
    title_vi: 'Cơ Thể Người & Y Sinh',
    title_en: 'Human Body & Health',
    desc_vi: '5 giác quan, tuần hoàn máu & sức khỏe',
    desc_en: '5 senses, blood circulation & biology',
    count_vi: '140 Câu',
    count_en: '140 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-rose-100 text-rose-800'
  },
  {
    topic: 'Địa Lý Việt Nam',
    icon: '🗺️',
    iconBg: 'bg-teal-100 border-teal-200',
    title_vi: 'Địa Lý Non Sông VN',
    title_en: 'Vietnam Geography',
    desc_vi: 'Sông Hồng, Trường Sơn, danh lam thắng cảnh',
    desc_en: 'Red River, Truong Son range, landscapes',
    count_vi: '160 Câu',
    count_en: '160 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-teal-100 text-teal-800'
  },
  {
    topic: 'Vật Chất & Hiện Tượng',
    icon: '⚡',
    iconBg: 'bg-purple-100 border-purple-200',
    title_vi: 'Vật Chất & Hiện Tượng',
    title_en: 'Matter & Physics',
    desc_vi: 'Âm thanh, ánh sáng, nam châm & chuyển động',
    desc_en: 'Sound, light, magnetism & motion',
    count_vi: '150 Câu',
    count_en: '150 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-purple-100 text-purple-800'
  }
];

const FILTER_PILLS = [
  { id: 'all', vi: 'Tất Cả Labs', en: 'All Labs' },
  { id: 'Động Vật', vi: '🦁 Động Vật', en: '🦁 Animals' },
  { id: 'Vũ Trụ & Thời Tiết', vi: '🚀 Vũ Trụ', en: '🚀 Space' },
  { id: 'Thực Vật', vi: '🌿 Thực Vật', en: '🌿 Plants' },
  { id: 'Cơ Thể Người', vi: '🫀 Sức Khỏe', en: '🫀 Health' },
  { id: 'Địa Lý Việt Nam', vi: '🗺️ Địa Lý', en: '🗺️ Geography' },
  { id: 'Vật Chất & Hiện Tượng', vi: '⚡ Vật Chất', en: '⚡ Physics' }
];"""

new_lab_cards = """const LAB_CARDS_DATA = [
  {
    topic: 'Địa Lý',
    icon: '🗺️',
    iconBg: 'bg-teal-100 border-teal-200',
    title_vi: 'Địa Lý & Trái Đất',
    title_en: 'Geography & Earth',
    desc_vi: 'Bản đồ, sông ngòi, núi non, đại dương & khí hậu',
    desc_en: 'Maps, rivers, mountains, oceans & climate',
    count_vi: '77 Câu',
    count_en: '77 Questions',
    status_vi: '● Sẵn sàng thi',
    status_en: '● Ready to play',
    statusClass: 'text-cyan-600',
    badgeBg: 'bg-teal-100 text-teal-800'
  },
  {
    topic: 'Vũ Trụ & Bầu Trời',
    icon: '🚀',
    iconBg: 'bg-indigo-100 border-indigo-200',
    title_vi: 'Vũ Trụ & Thiên Văn',
    title_en: 'Space & Astronomy',
    desc_vi: 'Hệ Mặt Trời, sao Hỏa, các hành tinh & thiên hà',
    desc_en: 'Planets, Mars, Sun & galaxy mysteries',
    count_vi: '49 Câu',
    count_en: '49 Questions',
    status_vi: '● Sẵn sàng thi',
    status_en: '● Ready to play',
    statusClass: 'text-cyan-600',
    badgeBg: 'bg-indigo-100 text-indigo-800'
  },
  {
    topic: 'Động Vật',
    icon: '🦁',
    iconBg: 'bg-amber-100 border-amber-200',
    title_vi: 'Thế Giới Động Vật',
    title_en: 'Animal Kingdom',
    desc_vi: 'Động vật có vú, chim muông & côn trùng',
    desc_en: 'Mammals, birds, insects & wildlife',
    count_vi: '106 Câu',
    count_en: '106 Questions',
    status_vi: '● Sẵn sàng thi',
    status_en: '● Ready to play',
    statusClass: 'text-cyan-600',
    badgeBg: 'bg-amber-100 text-amber-800'
  },
  {
    topic: 'Thực Vật',
    icon: '🌿',
    iconBg: 'bg-emerald-100 border-emerald-200',
    title_vi: 'Thực Vật & Tự Nhiên',
    title_en: 'Plants & Nature',
    desc_vi: 'Quang hợp, hạt mầm, rừng xanh & muôn hoa',
    desc_en: 'Photosynthesis, seeds, forests & flora',
    count_vi: '46 Câu',
    count_en: '46 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-emerald-100 text-emerald-800'
  },
  {
    topic: 'Cơ Thể Người',
    icon: '🫀',
    iconBg: 'bg-rose-100 border-rose-200',
    title_vi: 'Cơ Thể Người & Sức Khỏe',
    title_en: 'Human Body & Health',
    desc_vi: '5 giác quan, tuần hoàn máu & dinh dưỡng',
    desc_en: '5 senses, organs, blood & nutrition',
    count_vi: '103 Câu',
    count_en: '103 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-rose-100 text-rose-800'
  },
  {
    topic: 'Vật Chất & Năng Lượng',
    icon: '⚡',
    iconBg: 'bg-purple-100 border-purple-200',
    title_vi: 'Vật Chất & Năng Lượng',
    title_en: 'Matter & Energy',
    desc_vi: 'Âm thanh, ánh sáng, nam châm & chuyển động',
    desc_en: 'Sound, light, magnetism & motion',
    count_vi: '119 Câu',
    count_en: '119 Questions',
    status_vi: '✓ Đã mở',
    status_en: '✓ Unlocked',
    statusClass: 'text-emerald-600',
    badgeBg: 'bg-purple-100 text-purple-800'
  }
];

const FILTER_PILLS = [
  { id: 'all', vi: 'Tất Cả Labs', en: 'All Labs' },
  { id: 'Địa Lý', vi: '🗺️ Địa Lý', en: '🗺️ Geography' },
  { id: 'Vũ Trụ & Bầu Trời', vi: '🚀 Vũ Trụ', en: '🚀 Space' },
  { id: 'Động Vật', vi: '🦁 Động Vật', en: '🦁 Animals' },
  { id: 'Thực Vật', vi: '🌿 Thực Vật', en: '🌿 Plants' },
  { id: 'Cơ Thể Người', vi: '🫀 Sức Khỏe', en: '🫀 Health' },
  { id: 'Vật Chất & Năng Lượng', vi: '⚡ Vật Chất', en: '⚡ Physics' }
];"""

if old_lab_cards in content:
    content = content.replace(old_lab_cards, new_lab_cards)
    print("Replaced LAB_CARDS_DATA and FILTER_PILLS")
else:
    print("Warning: old LAB_CARDS_DATA not found exactly")

# 7. Update getFilteredPool topic filter check
old_pool_topic = "    // 4. Kiểm tra bộ lọc chủ đề\n    if (selectedTopic !== 'all' && q.topic !== selectedTopic) return false;"
new_pool_topic = "    // 4. Kiểm tra bộ lọc chủ đề (hỗ trợ so khớp đa tầng)\n    if (selectedTopic !== 'all' && !isTopicMatch(q.topic, selectedTopic) && !isTopicMatch(q.curriculum_topic, selectedTopic)) return false;"

if old_pool_topic in content:
    content = content.replace(old_pool_topic, new_pool_topic)
    print("Replaced getFilteredPool topic check")
else:
    print("Warning: old getFilteredPool topic check not found")

# 8. Update Smart Fallback in startQuiz
old_fallback = """  // SMART FALLBACK
  if (pool.length < targetCount && sizeVal !== 'all') {
    const needed = targetCount - pool.length;
    let fallbackCandidates = MASTER_POOL.filter(q => {
      if (pool.includes(q)) return false;
      const qSrc = q.source || "Khác";
      for (let s of selectedSources) {
        if (s === "Khác" && (qSrc === "Khác" || qSrc === "Khác (Kho câu hỏi cũ)")) return true;
        if (qSrc === s) return true;
      }
      return false;
    });
    if (fallbackCandidates.length < needed) {
      const extraCandidates = MASTER_POOL.filter(q => !pool.includes(q) && !fallbackCandidates.includes(q));
      fallbackCandidates = [...fallbackCandidates, ...extraCandidates];
    }
    const bonus = [...fallbackCandidates].sort(() => Math.random() - 0.5).slice(0, needed);
    pool = [...pool, ...bonus];
  }"""

new_fallback = """  // SMART FALLBACK
  if (pool.length < targetCount && sizeVal !== 'all') {
    const needed = targetCount - pool.length;
    let fallbackCandidates = [];
    // 1. Ưu tiên giữ đúng chủ đề người dùng đã chọn từ MASTER_POOL (nới lỏng grade/diff)
    if (selectedTopic !== 'all') {
      fallbackCandidates = MASTER_POOL.filter(q => {
        if (pool.includes(q)) return false;
        return isTopicMatch(q.topic, selectedTopic) || isTopicMatch(q.curriculum_topic, selectedTopic);
      });
    }
    // 2. Nếu vẫn chưa đủ, lấy thêm từ cùng nguồn
    if (fallbackCandidates.length < needed) {
      const sourceCandidates = MASTER_POOL.filter(q => {
        if (pool.includes(q) || fallbackCandidates.includes(q)) return false;
        const qSrc = q.source || "Khác";
        for (let s of selectedSources) {
          if (s === "Khác" && (qSrc === "Khác" || qSrc === "Khác (Kho câu hỏi cũ)")) return true;
          if (qSrc === s) return true;
        }
        return false;
      });
      fallbackCandidates = [...fallbackCandidates, ...sourceCandidates];
    }
    // 3. Nếu vẫn chưa đủ, lấy thêm từ MASTER_POOL
    if (fallbackCandidates.length < needed) {
      const extraCandidates = MASTER_POOL.filter(q => !pool.includes(q) && !fallbackCandidates.includes(q));
      fallbackCandidates = [...fallbackCandidates, ...extraCandidates];
    }
    const bonus = [...fallbackCandidates].sort(() => Math.random() - 0.5).slice(0, needed);
    pool = [...pool, ...bonus];
  }"""

if old_fallback in content:
    content = content.replace(old_fallback, new_fallback)
    print("Replaced Smart Fallback in startQuiz")
else:
    print("Warning: old Smart Fallback not found exactly")

# 9. Update filterLabPills to use isTopicMatch
old_filter_pills = """  document.querySelectorAll('.topic-lab-card').forEach(card => {
    const cardTopic = card.getAttribute('data-topic');
    if (topicId === 'all' || cardTopic === topicId || (cardTopic && cardTopic.includes(topicId))) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });"""

new_filter_pills = """  document.querySelectorAll('.topic-lab-card').forEach(card => {
    const cardTopic = card.getAttribute('data-topic');
    if (topicId === 'all' || isTopicMatch(cardTopic, topicId)) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });"""

if old_filter_pills in content:
    content = content.replace(old_filter_pills, new_filter_pills)
    print("Replaced filterLabPills card matching")
else:
    print("Warning: old filterLabPills not found exactly")

# 10. Update renderTopics with bilingual support
old_render_topics = """function renderTopics() {
  const container = document.getElementById('topics-list');
  if (!container) return;
  container.innerHTML = '';
  TOPIC_CONFIG.forEach(t => {
    const pill = document.createElement('div');
    pill.className = `topic-pill ${t.id === selectedTopic ? 'selected' : ''}`;
    pill.onclick = () => selectTopic(t.id, pill);
    pill.innerHTML = `
      <span class="icon" style="display:inline-flex; align-items:center; justify-content:center;">
        <i data-lucide="${t.lucide}" style="width:18px; height:18px; stroke-width:2.5;"></i>
      </span>
      <span>${t.name}</span>
    `;
    container.appendChild(pill);
  });
  refreshLucideIcons();
}"""

new_render_topics = """function renderTopics(lang) {
  const container = document.getElementById('topics-list');
  if (!container) return;
  const isEn = (lang === 'en' || currentLanguageMode === 'en');
  container.innerHTML = '';
  TOPIC_CONFIG.forEach(t => {
    const pill = document.createElement('div');
    pill.className = `topic-pill ${t.id === selectedTopic ? 'selected' : ''}`;
    pill.onclick = () => selectTopic(t.id, pill);
    const displayName = isEn ? (t.name_en || t.name) : t.name;
    pill.innerHTML = `
      <span class="icon" style="display:inline-flex; align-items:center; justify-content:center;">
        <i data-lucide="${t.lucide}" style="width:18px; height:18px; stroke-width:2.5;"></i>
      </span>
      <span>${displayName}</span>
    `;
    container.appendChild(pill);
  });
  refreshLucideIcons();
}"""

if old_render_topics in content:
    content = content.replace(old_render_topics, new_render_topics)
    print("Replaced renderTopics with bilingual support")
else:
    print("Warning: old renderTopics not found exactly")

# 11. Call renderTopics in applyLanguageToUI
if "renderTopicLabCards(lang);" in content and "renderTopics(lang);" not in content:
    content = content.replace("renderTopicLabCards(lang);", "renderTopicLabCards(lang);\n  renderTopics(lang);")
    print("Added renderTopics(lang) call in applyLanguageToUI")

with open("/Users/thanhdotrung/.gemini/antigravity/scratch/science-quiz/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully.")
