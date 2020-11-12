import face_recognition
import os
from PIL import Image
import pickle
import gzip
#pathik = "/root/env/megasuperfacedetectionbot/"
pathik = ""
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
	#path=f"{pathik}faces/known_faces/"
	path="faces/known_faces/"
	WDILL = face_recognition.load_image_file("WDILL.jpg")
	WDILLenc=face_recognition.face_encodings(WDILL)
	files = listdir_nohidden(path)
	for file in files:
		faces = listdir_nohidden(path+file+"/faceEncodings/")
		for face in faces:
			with gzip.open(path+file+"/faceEncodings/"+face, 'rb') as f:
				try:
					imageEncoding = pickle.load(f)
					analyze=((1-(face_recognition.face_distance(imageEncoding,WDILLenc))[0])*100)
					f.close()
				except:
					errorCounter+=1
					#analyze=analyzeValues(percentage)
		if(kwargs.get("outputEveryLine",True)==True):
			yield ("You look like "+file+" with "+str(analyze)+"chance")
		if (analyze>maxValue):
			maxValue=analyze
			mostLikely=file
			#percentage=[]
	yield "end"
	yield "end"
	#answer = str("most likely you look like "+(mostLikely)+" with "+str(maxValue)+"chance\nErrors:"+str(errorCounter))
	answer = "most likely you look like " + str(mostLikely) + " with " + str(maxValue)+" percent chance \n Errors:" +str(errorCounter)
	yield answer
	if(kwargs.get("getFinalFace",False)==True):
		im1 = Image.open(path+mostLikely+"/main.jpg")
		im1 = im1.save(f"{pathik}mostLikely.jpg")

    

for i in checkFace(getFinalFace=True,outputEveryLine=False):
        print(i)