import streamlit as st
from PIL import Image
import cv2
import numpy as np
import io

# Streamlit UI
st.title("Image Upload and Processing App")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to grayscale using OpenCV
    img_array = np.array(image)  # Convert PIL image to NumPy array
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

     # Step 2: Apply Gaussian Blur to remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Step 3: Perform edge detection using Canny
    edges = cv2.Canny(blurred, threshold1=55, threshold2=100)

    # Step 4: Apply morphological operation to improve edges
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morphed_edges = cv2.dilate(edges, kernel, iterations=3)

    # Step 5: Fill gaps and strengthen lines using morphological closing
    kernel_closing = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    closed_edges = cv2.morphologyEx(morphed_edges, cv2.MORPH_CLOSE, kernel_closing)

    # Step 6: Smooth the edges using Gaussian Blur
    smoothed_edges = cv2.GaussianBlur(closed_edges, (5, 5), 0)

    # Step 7: Invert the edge image (white lines on black background)
    inverted_edges = cv2.bitwise_not(smoothed_edges)

    # Convert back to PIL image for downloading
    processed_pil = Image.fromarray(inverted_edges)

    # Display processed image
    st.image(processed_pil, caption="Grayscale Image", use_column_width=True)

    # Convert image to bytes
    img_bytes = io.BytesIO()
    processed_pil.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    # Add download button
    st.download_button(
        label="Download Processed Image",
        data=img_bytes,
        file_name="processed_image.png",
        mime="image/png"
    )
