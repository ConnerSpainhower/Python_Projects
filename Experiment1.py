import cv2
import numpy as np

# load the input images between either covid, pneumonia, or healthy
healthy = cv2.imread('healthy3.jpg')
covid = cv2.imread('covid3.jpg')
pneumonia = cv2.imread('pneumonia3.jpg')

# convert the images to grayscale
img1 = cv2.cvtColor(healthy, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(covid, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(pneumonia, cv2.COLOR_BGR2GRAY)
# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

HandC, diff1 = mse(img1, img2)
HandP, diff2 = mse(img1, img3)
PandC, diff3 = mse(img3, img2)
print("MSE for the healthy and covid images:",HandC)
print("MSE for the healthy and pneumonia images:",HandP)
print("MSE for the pneumonia and covid images:",PandC)

cv2.imshow("Healthy and Covid", diff1)
cv2.imshow("Healthy and Pneumonia", diff2)
cv2.imshow("Pneumonia and Covid", diff3)
cv2.waitKey(0)
cv2.destroyAllWindows()