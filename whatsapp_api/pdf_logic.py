import fitz
from io import BytesIO

def spilit_pages(pdf_in):
    original= fitz.open(pdf_in) 
    new_pdf = fitz.open()         
    new_pdf_list = []
    for x in range(original.page_count):
        new_pdf.insert_pdf(pdf_in, to_page = x)
        binary_pdf = BytesIO()
        new_pdf.save(binary_pdf)
        new_pdf_list.append(binary_pdf)
    return new_pdf_list
        