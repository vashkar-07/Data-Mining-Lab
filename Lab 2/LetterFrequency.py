from ctypes import sizeof
from math import nan
import pandas as pd
import string
import matplotlib.pyplot as plt
from matplotlib import font_manager


BengaliLetterList = ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ',	'এ', 'ঐ', 'ও', 'ঔ', 'ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 'ণ', 'ট', 'ঠ', 
 	'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'য়', 'র', 'ল', 'শ', 'ষ', 'স', 'হ']
df = pd.read_csv('2-song-lyrics.csv')

data = df.values.tolist()
txt = ''

for i, val in enumerate(data):
    if val[-1] != nan:
        txt += str(val[-1])

#tokens = re.split('\\s?.,;:n।-+_()',txt)

tokens = txt.translate(str.maketrans('','',string.punctuation)).split()

dk = {}

for i in BengaliLetterList:
    dk[i] = 0

for i in tokens:
    try:
        dk[i[0]] += 1
    except KeyError:
        pass

# font_dirs = ['/home/vashkar/Downloads']
# font_files = font_manager.findSystemFonts(fontpaths=font_dirs)

plt.bar(dk.keys(), dk.values(), color ='maroon')
plt.xticks(list(dk.keys()), dk.keys(), fontname='kalpurush', rotation='vertical')

plt.title("Letter Frequency")
plt.show()

