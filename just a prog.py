from PIL import Image 
  
filename = "realNikhil.png"
with Image.open(filename) as image: 
    width, height = image.size 
