from fastai.vision import *

folders = ['black', 'grizzly', 'teddys']
files = ['urls_black.csv', 'urls_grizzly.csv', 'urls_teddys.csv']

for i in range(0, 3):
    path = Path('data/bears')
    dest = path/folders[i]
    dest.mkdir(parents=True, exist_ok=True)
    path.ls()
    download_images(path/files[i], dest, max_pics=200)
