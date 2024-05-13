''' This script is used for the skin color detection of the input images(skin-disease images ) and transforming their skin
    tone to different/darker colour and save the images with different skin tone to the output images folder path given in output_dir.
    The function change_skin is used to change the skin tone of the input images to the desired skin tone while preserving
    the texture and quality of the images. This is very important for our task because we want only the skin tones to be changed
    while the disease affected areas should remain the same.
    
    In the input folder, provide the directory of the images that you want to process. The script will process all the images
    in the input folder, change their skin tone to the desired skin tone which is given as the second argument in the 
    change_skin function. We can give any RGB value depending on which skin tone we want in the output image.
    The output images are saved in the output_dir folder.
    
    Once the darker skin tone images are generated, I have used these images to generate more images since the dataset
    available is very small. I have re-used the sliding window approach used by the other student https://github.com/aequitas-aod/synthesizer_image
    Specifically, I have used the code from the file 'generate_images.ipynb' to generate more images from the darker skin tone images.
    And I have saved the images. Finally I have done the multi-class classification using the generated images.
     '''

from skinDetection import change_skin
import os

# Get the full path to the input folder. This is the folder of the images that we want to process
script_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(script_dir, 'Images/esantema-virale/')

# Define the output directory. This folder stores the dark images
output_dir = os.path.join(script_dir, 'output/Dark/esantema-virale')

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open and process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        # Get the full path to the input image
        image_path = os.path.join(input_folder, filename)
        # Define the full path for the output image with .png extension
        output_image_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.png')

        # Open the input image
        with open(image_path, 'rb') as inputImage:
            # Perform the skin change operation
            result = change_skin(inputImage, [82, 58, 44])

        # Write the result to the output image file
        with open(output_image_path, 'wb') as resultFile:
            resultFile.write(result)
print('Done')