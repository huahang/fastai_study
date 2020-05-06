#!/usr/bin/env python3

import fastai
import fastai.vision

folders = ['black', 'grizzly', 'teddys']
files = ['urls_black.csv', 'urls_grizzly.csv', 'urls_teddys.csv']

for i in range(0, 3):
    path = fastai.vision.Path('data/bears')
    dest = path/folders[i]
    dest.mkdir(parents=True, exist_ok=True)
    path.ls()
    fastai.vision.download_images(path/files[i], dest, max_pics=200)
