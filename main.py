import face_recognition
import os
from PIL import Image
import resize
import splitIntoFaces
pathik = '/root/env/megasuperfacedetectionbot/'

tolerance = 0.7
def newPerson(file):
    img=Image.open(path+file)
    print("A new person appears?")
    img.show()
    name=str(input("Input name:"))
    os.makedirs(path+"known_faces/"+name)
    if(input("main/new")=='main'):
        img.save(path+"known_faces/"+name+"/main.jpg")
    else:
        img.save(path+"known_faces/"+name+"/"+file)
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

splitIntoFaces.splitIntoFaces()
resize.resizeAll()


path = f"{pathik}/faces/"
files = listdir_nohidden(path)
for file in files:
    if file == "known_faces":
        continue
    image = face_recognition.load_image_file(path+file)
    try:
        imageEncoding = face_recognition.face_encodings(image)[0]
    except:
        print("No face found in "+file)
        continue
    knownFaces = listdir_nohidden(path+"/known_faces/")
    personFound = False
    for face in knownFaces:
    #    img = Image.open(path+"known_faces/"+face)
     #   img.show()
        faceImage = face_recognition.load_image_file(path+"known_faces/"+face+"/main.jpg")
        print(face)
        faceEncoding=face_recognition.face_encodings(faceImage)[0]
        personName= face.split('.')[0]
        results = face_recognition.face_distance([imageEncoding],faceEncoding)
        if(results<tolerance):
             if not os.path.exists(path+"known_faces/"+personName):
                   os.makedirs(path+"known_faces/"+personName)
             os.rename((path+file),(path+"known_faces/"+personName+'/'+file))        
             personFound=True
    if personFound==False:
        newPerson(file)
    os.remove(path+file)
        
