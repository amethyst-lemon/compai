# compai
## Brief description
Image processing aapp for converting an image to a line drawing. App UI is made with the help of Streamlit.

Main features:
- Image upload
- Converting, procssing the image
- Algorithm values are adjusted with UI
- Displaying the original and processed image
- Processed image download

## How it works
User starts the app and uploads any image. A number of algorithms process the image. These algorithms are listed in the next section. Each algorithm has sliders to adjust their intensity. All slider changes are visible immediately as the image is process in real time. After the user is satisfied with the resuslts they can download the processed image.

## What algorithms are used to process the image
The used algorithms are listed in their use order as in how they follow each other to process the uploaded image.

## Libaries used

- streamlit | App UI is built using this libary, input sliders and checkboxes, image upload and download options are implemented with streamlit components

- PIL | Image processing

- cv2 | Image processing algorithms

- numpy | Converting image to array, for later image processing

- io | Converting image fpr download

## Set up / running the app

1. Step
Download the app.py file from this repository

2. Step
Install required dependencies

pip install streamlit pillow opencv-python numpy

3. Step 
Run project from its file location.
Opening the file in a code editor like Visual Studio Code, then using the built-in terminal to run python file

streamlit run app.py

## Mini How-to tutorial

1. Step 
Run the app
*add image with arrows and stuff*

2. Step
Upload an image
*add image with arrows and stuff*

3. Step
Adjust the algorithm sliders
*add image with arrows and stuff*

4. Step
Download the processed image when satisfied with algorith processing results
*add image with arrows and stuff*

## Future updates
Adding different image processing options like adding noise, adding a watermark ...
