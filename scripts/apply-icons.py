#!/usr/bin/env python3
"""Apply generated launcher icons to a freshly generated Capacitor Android project."""
from pathlib import Path
from PIL import Image
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "android" / "app" / "src" / "main" / "res"
ICON = ROOT / "assets" / "icon.png"
FOREGROUND = ROOT / "assets" / "icon-foreground.png"

# Legacy launcher icon sizes
for folder, size in {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}.items():
    dest = RES / folder
    dest.mkdir(parents=True, exist_ok=True)
    Image.open(ICON).convert("RGBA").resize((size, size), Image.Resampling.LANCZOS).save(dest / "ic_launcher.png")
    Image.open(ICON).convert("RGBA").resize((size, size), Image.Resampling.LANCZOS).save(dest / "ic_launcher_round.png")

# Adaptive launcher icon for Android 8+
for folder in ["mipmap-mdpi", "mipmap-hdpi", "mipmap-xhdpi", "mipmap-xxhdpi", "mipmap-xxxhdpi"]:
    size = {"mipmap-mdpi":108,"mipmap-hdpi":162,"mipmap-xhdpi":216,"mipmap-xxhdpi":324,"mipmap-xxxhdpi":432}[folder]
    dest = RES / folder
    fg = Image.open(FOREGROUND).convert("RGBA").resize((size,size),Image.Resampling.LANCZOS)
    fg.save(dest / "ic_launcher_foreground.png")

adaptive = RES / "mipmap-anydpi-v26"
adaptive.mkdir(parents=True, exist_ok=True)
(adaptive / "ic_launcher.xml").write_text(
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
    '    <background android:drawable="@android:color/black"/>\n'
    '    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>\n'
    '</adaptive-icon>\n', encoding="utf-8")
(adaptive / "ic_launcher_round.xml").write_text(
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
    '    <background android:drawable="@android:color/black"/>\n'
    '    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>\n'
    '</adaptive-icon>\n', encoding="utf-8")

print("Launcher icons applied.")
