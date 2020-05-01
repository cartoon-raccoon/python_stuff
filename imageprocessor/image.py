from PIL import Image
import os
# from pathlib import Path

directory = 'C:/Users/user/Documents/Python Stuff/imageprocessor/pokedex'
# path = Path(directory)
# path.mkdir(parents = True, exist_ok = True)

for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
        im = Image.open(directory + '/' + filename)
        filename = filename[:-4]
        im.save(f'{directory}/{filename}.png','png')
    else:
        continue
