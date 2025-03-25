import streamlit as st
from PIL import Image
import cv2
import numpy as np
import io

# Streamlit UI
st.title("Image Processing App - Covert image to Line drawing")
st.markdown("Upload an image and adjust the settings to process it.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to NumPy array
    img_array = np.array(image)
    
    # Convert to grayscale
    grayscale = st.checkbox("Convert to Grayscale", value=True, help="Check this box to convert the image to grayscale before processing.")
    if grayscale:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    # Gaussian Blur (Noise Reduction)
    blur_value = st.slider("Smoothing with Gaussian Blur", 1, 15, 5, step=2,  help="Higher values apply stronger blurring, which helps reduce noise before edge detection.")
    if blur_value > 1:
        img_array = cv2.GaussianBlur(img_array, (blur_value, blur_value), 0)

    # Edge Detection (Canny)
    canny_threshold1 = st.slider("Canny Edge Detection - Threshold 1", 0, 255, 55, help="Lower values detect more edges, making the image more detailed.")
    canny_threshold2 = st.slider("Canny Edge Detection - Threshold 2", 0, 255, 100, help="Higher values remove weak edges, making the lines cleaner and sharper.")
    edges = cv2.Canny(img_array, canny_threshold1, canny_threshold2)

    # Morphological Operations
    dilation_kernel_size = st.slider("Dilation Kernel Size", 1, 10, 3, help="Larger values make the lines thicker, useful for emphasizing edges.")
    dilation_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (dilation_kernel_size, dilation_kernel_size))
    morphed_edges = cv2.dilate(edges, dilation_kernel, iterations=3)

    closing_kernel_size = st.slider("Closing Kernel Size", 1, 10, 5, help="Larger values help close small gaps in the edges, making the lines smoother.")
    closing_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (closing_kernel_size, closing_kernel_size))
    closed_edges = cv2.morphologyEx(morphed_edges, cv2.MORPH_CLOSE, closing_kernel)

    # Final smoothing
    smoothed_edges = cv2.GaussianBlur(closed_edges, (5, 5), 0)

    # Option to invert the image (white lines on black or black lines on white)
    invert_colors = st.checkbox("Invert Colors", value=True, help="Check this box to swap black and white in the final processed image.")
    if invert_colors:
        processed_image = cv2.bitwise_not(smoothed_edges)
    else:
        processed_image = smoothed_edges

    # Convert back to PIL image for display & download
    processed_pil = Image.fromarray(processed_image)

    # Display processed image
    st.image(processed_pil, caption="Processed Image", use_column_width=True)

    # Convert image to bytes for download
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
