import face_recognition
import os
from PIL import Image

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f
path = "./faces/"
size = 128,128
files = listdir_nohidden(path)
for file in files:
    if file!="known_faces":
          img = Image.open(path+file)
          imgResize=img.resize(size)
          imgResize.save(path+file,"PNG")
