#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("[Usage] trim-empty-lines.py: <file to trim>")
    exit(1)

file = open(sys.argv[1], 'r')
lines = file.readlines()

for line in lines:
    line = line.strip()
    if len(line) != 0:
        print(line)
