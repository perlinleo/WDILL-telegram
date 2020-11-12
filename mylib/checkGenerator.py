import face_recognition
import os
from PIL import Image
import pickle
import gzip
#получаем из переменных окружения местоположения рабочей папки и бд с лицами и шифровками
library = os.environ.get('FACESLIB')
workspace = os.environ.get('FACEWORK')

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

def analyzeValues(values):
    try: 
        return int((sum(values)/len(values)))
    except: 
        return 0



def checkFace(**kwargs):
	errorCounter=0
	maxValue=0
	mostLikely="unknown"
	analyze = -1
	WDILL = face_recognition.load_image_file(f"{workspace}/WDILL.jpg")
	WDILLenc=face_recognition.face_encodings(WDILL)
	persons = listdir_nohidden(library)
	for person in persons:
		with gzip.open(f"{library}/{person}/faceEncodings/main.fee", 'rb') as f:
			try:
				imageEncoding = pickle.load(f)
				analyze=((1-(face_recognition.face_distance(imageEncoding,WDILLenc))[0])*100)
				f.close()
			except:
				errorCounter+=1
		if(kwargs.get("outputEveryLine",True)==True):
			yield (f"You look like {person} with {str(analyze)}% chance")
		if (analyze>maxValue):
			maxValue=analyze
			mostLikely=person
	answer = f"most likely you look like {str(mostLikely)} with {str(maxValue)} percent chance \n Errors:{str(errorCounter)}"
	yield answer
	if(kwargs.get("getFinalFace",False)==True):
		im1 = Image.open(f"{library}/{mostLikely}/main.jpg")
		im1 = im1.save(f"{workspace}/mostLikely.jpg")

    

for i in checkFace(getFinalFace=True,outputEveryLine=False):
    print(i)