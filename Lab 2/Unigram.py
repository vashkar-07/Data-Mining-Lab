from ctypes import sizeof
from math import nan
import pandas as pd
import string
import matplotlib.pyplot as plt
from matplotlib import font_manager


df = pd.read_csv('2-song-lyrics.csv')

data = df.values.tolist()
txt = ''

for i, val in enumerate(data):
    if val[-1] != nan:
        txt += str(val[-1])

#tokens = re.split('\\s?.,;:n।-+_()',txt)

tokens = txt.translate(str.maketrans('','',string.punctuation)).split()

dk = {}

for i in tokens:
    try:
        dk[i] += 1
    except KeyError:
        dk[i] = 1

dk = dict(sorted(dk.items(), key=lambda item: item[1]))
dk = {k: v for k, v in dk.items() if v > 200}

# font_dirs = ['/home/vashkar/Downloads']
# font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

plt.bar(dk.keys(), dk.values(), color ='maroon')
plt.xticks(list(dk.keys()), dk.keys(), fontname='kalpurush', rotation='vertical')

plt.title("Unigram")
plt.show()

