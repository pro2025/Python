# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 22:47:05 2023

@author: TARRA NIKHITHA
"""

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
    
  
# driver code 
if __name__ == "__main__": 
    main()
    