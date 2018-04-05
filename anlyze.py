try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import win_unicode_console
from PIL import Image, ImageEnhance, ImageFilter
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
win_unicode_console.enable()



enhancer_level = raw_input("Enhancer Level: ")
image_name = raw_input("Image Name: ")
z = Image.open(image_name)
z = z.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(z)
z = enhancer.enhance(float(enhancer_level))
z = z.convert('1')
z.save('temp2.png')
print "========================"
print "      "
print "Processing Image......"
print "Name: " + image_name
print "Enhancer Level: " +str(enhancer_level)
print "      "
print "========================"
x = pytesseract.image_to_string(z)
print x
