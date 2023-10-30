# import required libraries 
import numpy as np 
from PIL import Image as im 
  
# defi#ne a main function 
def main():
    array = np.arange(0, 737280, 1, np.uint8) 
    print(array.shape) 
      
    array = np.reshape(array, (1024, 720))  
      
    # show the shape of the array 
    print(array.shape) 
  
    # show the array 
    print(array) 
      
    # creating image object of 
    # above array 
    data = im.fromarray(array) 
      
    # saving the final output  
    # as a PNG file 
    data.save('first_pic.png') 
    
def inner():
    import cv2 
    import numpy as np 
      
    # creating an array using np.full  
    # 255 is code for white color 
    array_created = np.full((500, 500, 3), 
                            255, dtype = np.uint8) 
      
    # displaying the image 
    cv2.imshow("image", array_created)

def duo():
    main(),inner()
  
# driver code 
if __name__ == "__main__": 
    duo()
    
