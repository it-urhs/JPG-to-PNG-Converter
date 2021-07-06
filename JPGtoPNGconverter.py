import sys
import os
from PIL import Image

#taking files as arguments
path = sys.argv[1]
directory = sys.argv[2]

#checking if new file exist if not then creating one
if not os.path.exists(directory):
    os.makedirs(directory)

#for looping and converting
for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]   #for removing jpg from filename
  img = Image.open(f'{path}{filename}')        #coz folder can not be the same always  therfore using fstring
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it.
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')