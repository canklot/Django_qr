from io import BytesIO
import qrcode
from .pdf_logic import convert_to_pdf

def convert_list_to_qr(lines):
    qr_images = []
    for line in lines:
        img = qrcode.make(line)
        fomatted_img = BytesIO()
        img.save(fomatted_img, format="png")    
        fomatted_img = fomatted_img.getvalue()
        qr_images.append(fomatted_img)
    pdf = convert_to_pdf(qr_images)  
    return pdf