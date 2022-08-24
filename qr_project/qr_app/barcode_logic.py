from io import BytesIO
import qrcode
from .pdf_logic import convert_to_pdf

from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image

def convert_list_to_qr(lines):
    qr_images = []
    for line in lines:
        img = qrcode.make(line)
        fomatted_img = BytesIO()
        img.save(fomatted_img, format="png") 
        # If required I guess I can create svg files for better quality
        fomatted_img = fomatted_img.getvalue()
        qr_images.append(fomatted_img)
    pdf = convert_to_pdf(qr_images)  
    return pdf

def convert_list_to_barcode(lines):
    barcode_image_list = []
    for line in lines:
        barcode_image =BytesIO()
        Code128(line, writer=ImageWriter()).write(barcode_image,{"font_size": 6})
        barcode_image_list.append(barcode_image)
        image = Image.open(barcode_image) #debug
        image.show() #debug
    pdf = convert_to_pdf(barcode_image_list)  
    return pdf