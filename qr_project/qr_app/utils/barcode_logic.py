from io import BytesIO
import qrcode
from .pdf_logic import convert_to_pdf

from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def convert_list_to_qr(lines):
    qr_images = []
    for line in lines:
        img = qrcode.make(line,version=2)
        font_type = ImageFont.truetype("calibri.ttf", 24)
        ImageDraw.Draw(img).text((40, 300), line, font=font_type)
        # Writes text under the QR code
        fomatted_img = BytesIO()
        img.save(fomatted_img, format="JPEG")
        fomatted_img = fomatted_img.getvalue()
        qr_images.append(fomatted_img)
    pdf = convert_to_pdf(qr_images)
    return pdf


def convert_list_to_barcode(lines):
    barcode_image_list = []
    for line in lines:
        barcode_image = BytesIO()
        Code128(line, writer=ImageWriter()).write(
            barcode_image, {"font_size": 6, 
                            "text_distance": 2})
        barcode_image_list.append(barcode_image)
    pdf = convert_to_pdf(barcode_image_list)
    return pdf
