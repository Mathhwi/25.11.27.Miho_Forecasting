# -*- coding: utf-8 -*-
"""
GitHub Pages Setup Script
"""
import os
import shutil
import subprocess

# Change to the meeting materials folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Working directory: {os.getcwd()}")

# Copy HTML to index.html for GitHub Pages
if os.path.exists("25_11_27.html"):
    shutil.copy("25_11_27.html", "index.html")
    print("[OK] Created index.html from 25_11_27.html")
elif os.path.exists("figure_gallery.html"):
    shutil.copy("figure_gallery.html", "index.html")
    print("[OK] Created index.html from figure_gallery.html")
else:
    print("[ERROR] No HTML file found")

# List files
print("\nFiles to upload:")
for f in os.listdir("."):
    if not f.endswith(".py"):
        print(f"  - {f}")

# Git commands
print("\n" + "=" * 50)
print("Running Git commands...")
print("=" * 50)

commands = [
    'git init',
    'git add .',
    'git commit -m "Initial commit: Flood Arrival Time Analysis Figures"',
    'git branch -M main',
    'git remote add origin https://github.com/Mathhwi/25.11.27.Miho_Forecasting.git',
    'git push -u origin main'
]

for cmd in commands:
    print(f"\n> {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode != 0 and 'remote add' not in cmd:
        print(f"[WARNING] Command may have failed with code {result.returncode}")

print("\n" + "=" * 50)
print("DONE!")
print("=" * 50)
print("\nNext steps:")
print("1. Go to: https://github.com/Mathhwi/25.11.27.Miho_Forecasting")
print("2. Click 'Settings' > 'Pages'")
print("3. Source: 'Deploy from a branch'")
print("4. Branch: 'main' / '/ (root)'")
print("5. Click 'Save'")
print("\nYour page will be available at:")
print("https://mathhwi.github.io/25.11.27.Miho_Forecasting/")

