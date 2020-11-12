import checkGenerator
import cm_timer
import splitIntoFaces


splitIntoFaces.splitWDILL()
pathik = ''


with cm_timer.cm_timer() as cm_object:
    for i in checkGenerator.checkFace(getFinalFace=True,outputEveryLine=False):
        print(i)
