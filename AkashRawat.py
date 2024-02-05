#please install necessary libraries
import rembg
from PIL import Image
from io import BytesIO

# this function will take our input of image path
def remove_bg(input, output):  
    with open(input, 'rb') as input_file:
        data = input_file.read()

    #removing background of image
    output_data = rembg.remove(data)  

    with BytesIO(output_data) as output_file:
        img = Image.open(output_file)
        img.save(output)


 
 #calling our function
image_path = "image.jpeg"
output_image_path = "image_no_background.png"
remove_bg(image_path, output_image_path)



