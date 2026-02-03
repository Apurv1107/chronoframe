from PIL import Image, ImageDraw, ImageFont
from datetime import date
from pathlib import Path
import json
import calendar

# ========================
# PATH SETUP
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

FONT_PATH = ASSETS_DIR / "fonts" / "Inter-Regular.ttf"
BG_PATH = ASSETS_DIR / "backgrounds" / "default.png"
STATS_PATH = DATA_DIR / "stats.json"
OUTPUT_PATH = OUTPUT_DIR / "wallpaper.png"

OUTPUT_DIR.mkdir(exist_ok=True)

# ========================
# LOAD DATA
# ========================
with open(STATS_PATH, "r", encoding="utf-8") as f:
    stats = json.load(f)

# ========================
# TIME CALCULATIONS
# ========================
today = date.today()
start = date(today.year, 1, 1)
end = date(today.year, 12, 31)

days_passed = (today - start).days
total_days = (end - start).days
days_left = total_days - days_passed

year_progress = days_passed / total_days

# ========================
# CANVAS
# ========================
WIDTH, HEIGHT = 1920, 1080

if BG_PATH.exists():
    img = Image.open(BG_PATH).resize((WIDTH, HEIGHT))
else:
    img = Image.new("RGB", (WIDTH, HEIGHT), "#0f172a")

draw = ImageDraw.Draw(img)

# ========================
# FONTS (with fallback)
# ========================
try:
    font_big = ImageFont.truetype(str(FONT_PATH), 56)
    font_mid = ImageFont.truetype(str(FONT_PATH), 36)
    font_small = ImageFont.truetype(str(FONT_PATH), 26)
except OSError:
    font_big = font_mid = font_small = ImageFont.load_default()

# ========================
# COLORS
# ========================
WHITE = "#f8fafc"
MUTED = "#94a3b8"
GREEN = "#22c55e"
OUTLINE = "#64748b"

# ========================
# WIDGET 1 — YEAR PROGRESS
# ========================
BAR_X, BAR_Y = 200, 200
BAR_W, BAR_H = 1400, 30
fill_w = int(BAR_W * year_progress)

draw.text((BAR_X, BAR_Y - 70),
          f"Year Progress: {int(year_progress * 100)}%",
          fill=WHITE, font=font_big)

draw.rectangle((BAR_X, BAR_Y, BAR_X + BAR_W, BAR_Y + BAR_H),
               outline=OUTLINE, width=3)
draw.rectangle((BAR_X, BAR_Y, BAR_X + fill_w, BAR_Y + BAR_H),
               fill=GREEN)

draw.text((BAR_X, BAR_Y + 50),
          f"{days_left} days left in {today.year}",
          fill=MUTED, font=font_mid)

# ========================
# WIDGET 2 — MONTH GRID
# ========================
grid_x, grid_y = 200, 330
cell_w, cell_h = 120, 50
gap = 10

months = list(calendar.month_abbr)[1:]
current_month = today.month

for i, month in enumerate(months):
    row = i // 3
    col = i % 3

    x = grid_x + col * (cell_w + gap)
    y = grid_y + row * (cell_h + gap)

    is_current = (i + 1) == current_month
    fill = GREEN if is_current else None
    outline = GREEN if is_current else OUTLINE
    text_color = "#022c22" if is_current else MUTED

    draw.rectangle((x, y, x + cell_w, y + cell_h),
                   outline=outline, width=2, fill=fill)

    bbox = draw.textbbox((0, 0), month.upper(), font=font_small)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(
    (x + (cell_w - w) / 2, y + (cell_h - h) / 2),
    month.upper(),
    fill=text_color,
    font=font_small
    )

# ========================
# WIDGET 3 — STUDY TRACKER
# ========================
study_x, study_y = 1100, 330
study_today = stats.get("study_hours_today", 0)
study_target = stats.get("daily_target_hours", 1)
study_ratio = min(study_today / study_target, 1.0)

draw.text((study_x, study_y - 50),
          f"Study Today: {study_today} / {study_target} hrs",
          fill=WHITE, font=font_mid)

bar_w = 500
bar_fill = int(bar_w * study_ratio)

draw.rectangle((study_x, study_y, study_x + bar_w, study_y + 20),
               outline=OUTLINE, width=2)
draw.rectangle((study_x, study_y, study_x + bar_fill, study_y + 20),
               fill=GREEN)

# ========================
# WIDGET 4 — STREAK
# ========================
draw.text((study_x, study_y + 60),
          f"Current Streak: {stats.get('current_streak', 0)} days",
          fill=MUTED, font=font_small)

# ========================
# FOOTER DATE
# ========================
draw.text((200, HEIGHT - 80),
          today.strftime("%A, %d %B %Y"),
          fill=MUTED, font=font_small)

# ========================
# SAVE
# ========================
img.save(OUTPUT_PATH)
print("Wallpaper generated:", OUTPUT_PATH)
