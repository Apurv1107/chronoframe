from PIL import Image, ImageDraw, ImageFont
from datetime import date
from pathlib import Path
import json

# Base directory (chronoframe/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

FONT_PATH = ASSETS_DIR / "fonts" / "InterVariable.ttf"
BG_PATH = ASSETS_DIR / "backgrounds" / "default.png"
STATS_PATH = DATA_DIR / "stats.json"
OUTPUT_PATH = OUTPUT_DIR / "wallpaper.png"

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)

# Load stats
with open(STATS_PATH, "r", encoding="utf-8") as f:
    stats = json.load(f)

# Year progress
today = date.today()
start = date(today.year, 1, 1)
end = date(today.year, 12, 31)
progress = (today - start).days / (end - start).days

# Canvas
WIDTH, HEIGHT = 1920, 1080
img = Image.open(BG_PATH).resize((WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

try:
    font_big = ImageFont.truetype(str(FONT_PATH), 56)
    font_small = ImageFont.truetype(str(FONT_PATH), 32)
except OSError:
    font_big = ImageFont.load_default()
    font_small = ImageFont.load_default()


# Progress bar
BAR_X, BAR_Y = 260, 520
BAR_W, BAR_H = 1400, 30
fill_w = int(BAR_W * progress)

draw.rectangle(
    (BAR_X, BAR_Y, BAR_X + BAR_W, BAR_Y + BAR_H),
    outline="#94a3b8",
    width=3
)
draw.rectangle(
    (BAR_X, BAR_Y, BAR_X + fill_w, BAR_Y + BAR_H),
    fill="#22c55e"
)

# Text
draw.text(
    (BAR_X, BAR_Y - 80),
    f"Year Progress: {int(progress * 100)}%",
    fill="#f8fafc",
    font=font_big
)

draw.text(
    (BAR_X, BAR_Y + 60),
    today.strftime("%A, %d %B %Y"),
    fill="#cbd5f5",
    font=font_small
)

draw.text(
    (BAR_X, BAR_Y + 110),
    f"Streak: {stats.get('current_streak', 0)} days",
    fill="#94a3b8",
    font=font_small
)

# Save
img.save(OUTPUT_PATH)
print("Wallpaper generated:", OUTPUT_PATH)