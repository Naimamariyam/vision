import numpy as np
import cv2
b = np.zeros([440,440],dtype = 'uint8')
for j in range(55,440,110):
        for i in range (55,440,110):   
            b[j-55:j,i-55:i] = 255
            b[j:j+55,i:i+55] = 255 
cv2.imshow('checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
