import numpy as np
import cv2
import sys

filename = sys.argv[1]
print(filename)
print(np.var(np.array(cv2.imread(filename))))