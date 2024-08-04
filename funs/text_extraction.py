import pytesseract
from PIL import Image as PILImage
def extract_text_from_image(image_stream):
    """
    Extract text from a given image file stream.
    
    Parameters:
    image_stream (stream): The input image file stream.

    Returns:
    str: Extracted text.
    """
    # Open the image file stream
    image = PILImage.open(image_stream)

    # Perform OCR on the image and extract text
    text = pytesseract.image_to_string(image)

    return text
