import face_recognition
import os
from PIL import Image
import resize
import splitIntoFaces


tolerance = 0.5

counter = 10000
counterProccessing = 1
groupCounter=0

def newPerson(file,**kwargs):
    img=Image.open(path+file)
    if(kwargs.get("noNameMode",True)==True):
        os.makedirs(path+"known_faces/"+"person#"+str(counter))
        img.save(path+"known_faces/"+"person#"+str(counter)+"/main.jpg")
        os.makedirs(path+"known_faces/"+"person#"+str(counter)+"/faceEncodings")
    
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

#splitIntoFaces.splitIntoFaces()
#resize.resizeAll()


#path = "/root/env/megasuperfacedetectionbot/faces/"
path = "faces/"
files = listdir_nohidden(path)
for file in files:
    os.system("clear")
    print("item#"+str(counter))
    
    if file == "known_faces":
        continue
    image = face_recognition.load_image_file(path+file)
    try:
        imageEncoding = face_recognition.face_encodings(image)[0]
    except:
        print("No face found in "+file)
        continue
    newPerson(file,noNameMode=True)
    counter+=1    
    print (str(counter))
    os.remove(path+file)
    
        
