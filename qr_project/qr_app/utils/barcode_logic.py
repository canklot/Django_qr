from io import BytesIO

from PIL import ImageFont, ImageDraw
from barcode import Code128
from barcode.writer import ImageWriter
import qrcode

from .pdf_logic import img_list_to_pdf


def convert_list_to_qr(lines):
    qr_images = []
    for line in lines:
        # Version 2	supports 47 characters and produces 25x25 pixel matrix
        img = qrcode.make(line, version=2)
        font_type = ImageFont.truetype("calibri.ttf", 24)
        # Writes text under the QR code
        ImageDraw.Draw(img).text((40, 300), line, font=font_type)
        formatted_img = BytesIO()
        img.save(formatted_img, format="JPEG", quality=75)
        formatted_img = formatted_img.getvalue()
        qr_images.append(formatted_img)
    pdf = img_list_to_pdf(qr_images)
    return pdf


def convert_list_to_barcode(lines):
    barcode_image_list = []
    for line in lines:
        barcode_image = BytesIO()
        Code128(line, writer=ImageWriter(format="JPEG")).write(
            barcode_image, {"font_size": 6,
                            "text_distance": 2})
        barcode_image_list.append(barcode_image)
    pdf = img_list_to_pdf(barcode_image_list)
    return pdf
