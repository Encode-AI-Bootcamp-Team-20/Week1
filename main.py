#!/usr/bin/env python3
import sys, subprocess

scripts = {
    "alexey.py": "Asshole Chef",
    "agolikov.py": "Polish Chef",
    "miguel.py": "The Drama Artist"
}

while True:
    names = []
    for script in scripts:
        names.append(script)
        print(str(len(names))+") "+scripts[script])
    n = int(input("> "))
    if n > 0 and n <= len(names):
        subprocess.run([sys.executable, names[n-1]])