from mylib import cm_timer
from mylib import checkGenerator
from mylib import splitIntoFaces


splitIntoFaces.splitWDILL()
pathik = ''


with cm_timer.cm_timer() as cm_object:
    for i in checkGenerator.checkFace(getFinalFace=True,outputEveryLine=False):
        print(i)
