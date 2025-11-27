# -*- coding: utf-8 -*-
import os
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Working directory: {os.getcwd()}")

commands = [
    'git add .',
    'git commit -m "Update HTML file"',
    'git push'
]

for cmd in commands:
    print(f"\n> {cmd}")
    os.system(cmd)

print("\n[DONE] Changes pushed to GitHub!")
print("Refresh: https://mathhwi.github.io/25.11.27.Miho_Forecasting/")

