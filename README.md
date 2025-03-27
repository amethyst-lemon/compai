# compai
## Brief description
Image processing app for converting an image to a line drawing. App UI is made with the help of Streamlit.

Apps intended use case is turning a photo of a sketch or line art (traditional art) into digital line art (digital line art).

**Main features:**
- Image upload
- Converting, procssing the image
- Function values are adjusted with UI
- Displaying the original and processed image
- Processed image download

## Testing documentation

List of test cases used to test the app can be found in this Google Sheets:
https://docs.google.com/spreadsheets/d/1QBoAoyROR_iTpx-67E4MiH7pd02aBIgdXVKdnF74ltQ/edit?usp=sharing

## How it works
User starts the app and uploads any image. A number of mathematical functions and algorithms process the image. These functions and algorithms are listed in the next section. Each of them has sliders to adjust their intensity and way of interacting with the image. All slider changes are visible immediately as the image is process in real time. After the user is satisfied with the resuslts they can download the processed image.

## What functions and algorithms are used to process the image
The mathmatical functions and alorithms used are listed in order of use in the app.

- *Greyscale | cv2.cvtColor* - Converting image to grayscale. Used so that the following methods applied work as inteded. Greyscale images are used for computervision to make image processing better. 
- *Gaussian blur | cv2.GaussianBlur* - Mathmatical function for image blurring. In computervision it is often used to reduce overall image noise and fine details.
- *Canny | cv2.Canny* - Edge detection algorithm. This algorithm was picked after previous testing on multiple image types. The other looked at edge detection algorithms were - Sobel, Roberts and Prewitt. This one had the best results for the inteded use case.


## What follows funtions and algorithms
After functions and algothims have worked on the image, morphological operation are performed on the image. 

- *Dilation | cv2.dilate* - Dilation is performed on the image after Canny has detected edges. This operation is performed to create new lines by closing the what the Canny algorithm has detected. This gives new bold lines.
- *Erosion | cv2.morphologyEx* - Erosion is performed after dilation to close help close small, open spots in lines created. 

Smoothing is performed after all morphological operations have been completed. This is done with Gaussian blur.

- *Mask creation | cv2.bitwise_not* - An option to invert the image colors is given with a checkmark option in the UI. If checked then final image is inverted in colors. From black lines on a white background to white lines on a black background.
- *Image creation | Image.fromarray* - Creating image from the previously manipulated data. 

## Libaries used

- *streamlit* - App UI is built using this libary, input sliders and checkboxes, image upload and download options are implemented with streamlit components
- *PIL (Image)* - Image processing
- *cv2* - Image processing algorithms
- *numpy* - Converting image to array, for later image processing
- *io* - Converting image for download, for input output operations

## Future updates
**Future updates could include:**
- Adding noise
- Adding watermark
- Adding color editing

## Set-up / running the app

**To use the app just open this link**

https://compai-uni-app.streamlit.app/


Link to demo video of how to use the web version of application:
https://drive.google.com/file/d/18b5UqeIQJdu2ON-Osxh5NbFdGEfVrXbr/view?usp=sharing

## Local app set-up

**1. Step**

Download the app.py file from this repository

**2. Step**

Install required dependencies

```pip install streamlit pillow opencv-python numpy```

**3. Step** 

Run project from its file location.
Opening the file in a code editor like Visual Studio Code, then using the built-in terminal to run python file

```streamlit run app.py```


Link to demo video of how to use the application with a local set-up:
https://drive.google.com/file/d/1zELWafWsVDylg82o3dPKP7Nf5pKPDe4w/view?usp=sharing

## Mini How-to tutorial

**1. Step** 

Run the app

Follow the instructions under ***Set-up / running the app section***

**2. Step**

Upload an image


<img src="https://i.imgur.com/yfJ1GBH.png" width="800">

**3. Step**

Adjust the algorithm sliders


<img src="https://i.imgur.com/NQxUN51.png" width="800">

**4. Step**

Download the processed image when satisfied with algorithm processing results


<img src="https://i.imgur.com/J0PjH4m.png" width="800">

## Image processing examples

<img src="https://i.imgur.com/wXv9Pnx.png" width="800">


<img src="https://i.imgur.com/G4XVBIN.png" width="800">

