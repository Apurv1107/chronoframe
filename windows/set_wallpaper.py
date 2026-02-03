import ctypes
from pathlib import Path

# Base directory (chronoframe/)
BASE_DIR = Path(__file__).resolve().parent.parent
WALLPAPER_PATH = BASE_DIR / "output" / "wallpaper.png"

SPI_SETDESKWALLPAPER = 20

ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER,
    0,
    str(WALLPAPER_PATH),
    3
)

print("Wallpaper applied.")
