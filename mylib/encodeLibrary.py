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

library = os.environ.get('FACESLIB')
workspace = os.environ.get('FACEWORK')

for person in listdir_nohidden(library):
    counter1+=1
    with gzip.open(f"{library}/{person}/faceEncodings/main.fee", 'wb') as f:
        os.system("clear")
            #get better
            #print("item#"+str(counter)+"of person #"+str(counter1))
        try:
            fPhoto=face_recognition.load_image_file(f"{library}/{person}/main.jpg")
            faceEncoding=face_recognition.face_encodings(fPhoto)[0]
            pickle.dump(faceEncoding,f)
        except:
            print("error!")
            counter+=1
        f.close
