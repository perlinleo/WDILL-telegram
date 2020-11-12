import face_recognition
import os
from PIL import Image
#pathik = '/root/env/megasuperfacedetectionbot/'
pathik = ''
def reformate(numbers):
        result = [numbers[3],numbers[0],numbers[1],numbers[2]]
        print (result)
        return result

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

def splitIntoFaces():
    path = f"{pathik}/image_to_split/"

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
            croppedImg.save(f"{pathik}/faces/"+head+str(i)+tail)
        print(face_loc) 

def getOneFace(imageLocation):
    image = face_recognition.load_image_file(imageLocation)
    face_loc=face_recognition.face_locations(image)
    img = Image.open(imageLocation)
    croppedImg = img.crop([face_loc[0][3],face_loc[0][0],face_loc[0][1],face_loc[0][2]])
    croppedImg.save(imageLocation)

def splitWDILL():
    image = face_recognition.load_image_file("WDILL.jpg")
    face_loc=face_recognition.face_locations(image)
    for i in range(len(face_loc)):
        imgfile = "WDILL.jpg"
        img = Image.open(imgfile)
        croppedImg = img.crop(reformate(face_loc[i]))
        croppedImg.save("WDILL.jpg")
        print(face_loc) 

if __name__ == '__main__':
    getOneFace("/Users/blacksnow/Downloads/botdemo-master/workspace/602x338_cmsv2_9d113afe-20a2-571c-ab2d-07cf02a8751c-5115656.jpg")