import face_recognition
import os
from PIL import Image
pathik = ''
def resizeAll():
    def listdir_nohidden(path):
        for f in os.listdir(path):
            if not f.startswith('.'):
                yield f
    path = f"{pathik}/faces/"
    size = 128,128
    files = listdir_nohidden(path)
    for file in files:
        if file!="known_faces":
            size = 128,128
            img = Image.open(path+file)
            imgResize=img.resize(size)
            imgResize.save(path+file,"PNG")

def resizeWDILL():
    size = (256,256)
    img = Image.open("WDILL.jpg")
    imgResize=img.resize(size)
    imgResize.save("WDILL.jpg")


if __name__ == '__main__':
    resizeWDILL()
