# ChronoFrame

ChronoFrame is a cross-platform dynamic wallpaper engine that visualizes time, goals, and personal progress directly on your screen.  
It turns your wallpaper into a living dashboard that updates automatically and keeps your long-term goals visible at a glance.

---

## ✨ Features

### Current (v0.1.0 – Windows)
- 📅 Year progress visualization (days passed vs remaining)
- 🖼️ Auto-generated desktop wallpaper
- 🔁 Automatic daily updates
- ⚙️ Lightweight, script-based system (no GPU required)
- 📁 Simple JSON-based data storage

### Planned
- 📊 Multiple progress widgets (streaks, study hours, goals)
- 🎨 Themes and layout customization
- 📱 Android live wallpaper engine
- ☁️ Cross-device sync (Windows ↔ Android)
- 🔒 Offline-first, privacy-friendly design

---

## 🧠 Project Philosophy

ChronoFrame is designed as a **passive accountability system**.

Instead of notifications or reminders, it:
- Keeps progress visible
- Encourages consistency
- Integrates naturally into daily device usage

No distractions. Just awareness.

---

## 🏗️ Tech Stack

### Windows
- **Python 3.11**
- **Pillow (PIL)** – image generation
- **datetime** – time calculations
- **Windows Task Scheduler** – automation

### Android (planned)
- **Kotlin**
- **WallpaperService API**
- **WorkManager**
- **Jetpack Compose**

### Sync (planned)
- JSON-first data model  
- Optional cloud backend (Firebase / Supabase)

---

## 📂 Project Structure

```text
chronoframe/
│
├── windows/
│   ├── generate_wallpaper.py
│   ├── set_wallpaper.py
│   ├── requirements.txt
│   └── README.md
│
├── data/
│   └── stats.json
│
├── assets/
│   ├── fonts/
│   └── backgrounds/
│
├── output/
│   └── wallpaper.png
│
├── .gitignore
└── README.md
