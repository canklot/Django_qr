from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw
from barcode import Code128
from barcode.writer import ImageWriter
import qrcode
from .pdf_logic import img_list_to_pdf


def convert_list_to_qr(lines):
    qr_images = []
    for line in lines:
        img = qrcode.make(line, version=2)
        # version 2	is 25x25 and supports 47 chars
        font_type = ImageFont.truetype("calibri.ttf", 24)
        ImageDraw.Draw(img).text((40, 300), line, font=font_type)
        # writes text under the QR code
        fomatted_img = BytesIO()
        img.save(fomatted_img, format="JPEG",quality=75)
        fomatted_img = fomatted_img.getvalue()
        qr_images.append(fomatted_img)
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
