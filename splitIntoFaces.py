import face_recognition
import os
from PIL import Image


def reformate(numbers):
    result = [numbers[3],numbers[0],numbers[1],numbers[2]]
    print (result)
    return result
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

path = "./image_to_split/"

files = listdir_nohidden(path)
print(files)

for fileName in files:
    image = face_recognition.load_image_file(path+fileName)
    face_loc=face_recognition.face_locations(image)
    head,tail = os.path.split(fileName)
    if not os.path.exists(path+head):
        os.makedirs(path+head)
    for i in range(len(face_loc)):
        imgfile = path+fileName
        img = Image.open(imgfile)
        croppedImg = img.crop(reformate(face_loc[i]))
        croppedImg.save("./faces/"+head+str(i)+tail)
    print(face_loc) 
