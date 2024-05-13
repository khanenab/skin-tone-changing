This project is used for the skin color detection of the input images(skin-disease images ) and transforming their skin 
tone to different/given RGB of the desired skin tone. The functionality can be achieved by running the __init__ script file to change the skin tone form fair to darker color and save the images
with different skin tones to the output images folder path given in output_dir.
The function change_skin is used to change the skin tone of the input images to the desired skin tone while preserving
the texture and quality of the images. This is very important for our task because we want only the skin tones to be changed
while the disease-affected areas should remain the same.
  
In the input folder, provide the directory of the images that you want to process. The script will process all the images
in the input folder, and change their skin tone to the desired skin tone which is given as the second argument in the 
change_skin function. We can give any RGB value depending on which skin tone we want in the output image.
The output images are saved in the output_dir folder.
  
Once the darker skin tone images are generated, I have used these images to generate more images since the dataset
available is very small. I have re-used the sliding window approach used by the other student https://github.com/aequitas-aod/synthesizer_image
Specifically, I have used the code from the file 'generate_images.ipynb' to generate more images from both fair as well as the darker skin tone images.
And I have saved the images which is the dataset for our bias detection classification task. Finally, I have done the multi-class classification
using the generated images which is done in the other project here https://github.com/khanenab/skin_disease_classifier.
