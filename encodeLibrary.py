import face_recognition
import os
import pickle 
import gzip

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.') and not f.startswith("faceEncodings"):
            yield f

counter = 0
counter1 = 0
path = "./faces/known_faces"
for person in listdir_nohidden(path):
    counter1+=1
    for face in listdir_nohidden(path+"/"+person):
        with gzip.open(path+"/"+person+"/faceEncodings/"+face[:-4]+".fee", 'wb') as f:
            os.system("clear")
            print("item#"+str(counter)+"of person #"+str(counter1))
            try:
                fPhoto=face_recognition.load_image_file(path+"/"+person+"/"+face)
                faceEncoding=face_recognition.face_encodings(fPhoto)[0]
                pickle.dump(faceEncoding,f)
            except:
                print("error!")
            f.close
            counter+=1
