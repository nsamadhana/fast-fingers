try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nevan\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\pytesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('img.png')))