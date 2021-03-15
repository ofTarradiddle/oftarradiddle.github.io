
   
# Improting Image class from PIL module  
from PIL import Image  
  
import os 
os.getcwd()
os.listdir()  
# Opens a image in RGB mode  
im = Image.open(r"c:\Users\Rocky\Desktop\logo horizontal.JPG")  
  
# Size of the image in pixels (size of orginal image)  
# (This is not mandatory)  
width, height = im.size  

newsize = (120, 30) 
im1 = im.resize(newsize) 
im1 = im1.save("smalllogohor.jpg")
im1.show()
