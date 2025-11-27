# -*- coding: utf-8 -*-
import os
import shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Working directory: {os.getcwd()}")

# Copy 25_11_27.html to index.html
if os.path.exists("25_11_27.html"):
    shutil.copy("25_11_27.html", "index.html")
    print("[OK] Copied 25_11_27.html -> index.html")

# Remove figure_gallery.html
if os.path.exists("figure_gallery.html"):
    os.remove("figure_gallery.html")
    print("[OK] Removed figure_gallery.html")

commands = [
    'git add .',
    'git commit -m "Use 25_11_27.html as index"',
    'git push'
]

for cmd in commands:
    print(f"\n> {cmd}")
    os.system(cmd)

print("\n[DONE] Changes pushed to GitHub!")
print("Refresh: https://mathhwi.github.io/25.11.27.Miho_Forecasting/")

