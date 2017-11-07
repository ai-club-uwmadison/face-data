import cv2
from glob import glob
from face import faceRetriever
import numpy as np
import time
import os
import sys
import random
PATH = "{}/frames/*/*.jpg"

print(sys.argv[1])
for name in ['alliot','david','krittisak', 'nat']:
    filenames = sorted(glob(PATH.format(name)))
    if sys.argv[1] == "-1":
        print('reversed')
        filenames = reversed(filenames)
    else:
        print('not reversed')
    for filename in filenames:
        try:
            img = cv2.imread(filename)
            if np.prod(np.array(img).shape) != 128*128*3:
                faces = faceRetriever(img)
                faces_found = 0
                for face in faces:
                    # if np.var(np.array(face[0])) < 2000:
                    # continue
                    if faces_found > 0:
                        filename = filename[:-4] + '_{}.jpg'.format(faces_found)
                    cv2.imwrite(filename, face[0])
                    print(filename)
                    # time.sleep(5)
                    faces_found += 1
                if faces_found == 0:
                    print("removing {}".format(filename))
                    os.remove(filename)
        except Exception as e:
            print(e)
            print("error with {}".format(filename))
            pass