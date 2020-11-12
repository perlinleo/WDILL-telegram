import face_recognition
import os
from PIL import Image
from mylib import resize
from mylib import splitIntoFaces


tolerance = 0.5

counter = 10000
counterProccessing = 1
groupCounter=0

def newPerson(file,**kwargs):
    img=Image.open(f"{library}/{file}")
    if(kwargs.get("noNameMode",True)==True):
        os.makedirs(f"{library}/known_faces/person#{str(counter)}")
        img.save(f"{library}/known_faces/person#{str(counter)}/main.jpg")
        os.makedirs(f"{library}/known_faces/person#{str(counter)}/faceEncodings")
    
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

#splitIntoFaces.splitIntoFaces()
#resize.resizeAll()


library = os.environ.get('FACESLIB')
workspace = os.environ.get('FACEWORK')


#path = "/root/env/megasuperfacedetectionbot/faces/"
for file in listdir_nohidden(library):
    os.system("clear")
    print("item#"+str(counter))
    
    if file == "known_faces":
        continue
    splitIntoFaces.getOneFace(f"{library}/{file}")
    try:
        splitIntoFaces.getOneFace(f"{library}/{file}")
    except:
        print("No face found in "+file)
        continue
    newPerson(file,noNameMode=True)
    counter+=1    
    print (str(counter))
    os.remove(f"{library}/{file}")
    
        
