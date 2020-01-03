try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\nevan\AppData\Local\Tesseract-OCR\tesseract.exe'

img = Image.open('img.png')
text = tess.image_to_string(Image.open('img.png'))
print(text)
