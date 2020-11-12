import face_recognition
import os
from PIL import Image
pathik = '/root/env/megasuperfacedetectionbot/'


def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

def analyzeValues(values):
    return int((sum(values)/len(values)))

def checkFace(fileName):
    finalString=""
    maxValue=0
    percentage=[]
    mostLikely="unknown"
    path=f"{pathik}/faces/known_faces/"
    img=Image.open(fileName)
    WDILL = face_recognition.load_image_file(fileName)
    WDILLenc=face_recognition.face_encodings(WDILL)
    files = listdir_nohidden(path)
    for file in files:
        #print(file)
        faces = listdir_nohidden(path+file+'/')
        for face in faces:
            image = face_recognition.load_image_file(path+file+'/'+face)
            imageEncoding = (face_recognition.face_encodings(image))[0]
            percentage.append((1-(face_recognition.face_distance(imageEncoding,WDILLenc))[0])*100)
        analyze=analyzeValues(percentage)
        finalString+="You look like "+file+" with "+str(analyze)+"% chance\n"
        
        if analyze>maxValue:
            maxValue=analyze
            mostLikely=file
        percentage=[]
    finalString+="most likely you look like "+(mostLikely)+" with "+str(maxValue)+"% Chance\n"
    return finalString

