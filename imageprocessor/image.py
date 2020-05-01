from PIL import Image
import sys
import os

path = 'C:/Users/user/Documents/Python Stuff/imageprocessor/pokedex'
directory = '/new'
if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    if filename.endswith('.jpg'):
        im = Image.open(path + '/' + filename)
        filename = filename[:-4]
        im.save(f'{directory}/{filename}.png','png')
    else:
        continue
