import cv2
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from seam_carving import SeamCarver
def object_removal(filename_input, filename_output, filename_mask):
    obj = SeamCarver(filename_input, 0, 0, object_mask=filename_mask)
    obj.save_result(filename_output)



window_name = "image"
drawing = False
ix,iy = -1,-1
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
            cv2.circle(mask,(x,y),5,(255,255,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        cv2.circle(mask,(x,y),5,(255,255,255),-1)
img = cv2.imread("image.jpg")
mask = np.zeros_like(img)
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name,draw_circle)

while(1):
    cv2.imshow(window_name,img)
    k = cv2.waitKey(1) & 0xFF
    if k == 13:
        print('Removing!!!!')
        object_removal(img, "removed.jpg", cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY))
        img = cv2.imread("removed.jpg")
        mageBGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        mgplot = plt.imshow(mageBGR)

        plt.show()
        break

cv2.destroyAllWindows()