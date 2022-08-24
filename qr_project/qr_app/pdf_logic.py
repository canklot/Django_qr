from io import BytesIO
import os, fitz
from PIL import Image

def convert_to_pdf(imglist):
    doc = fitz.open()  # PDF with the pictures
    for file in imglist:
        img = fitz.open("jpg", file)  # open pic as document. Convert this to use with
        rect = img[0].rect  # pic dimension
        pdfbytes = img.convert_to_pdf()  # make a PDF stream
        img.close()  # no longer needed. Remove after with
        imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
        paper_height, paper_width = fitz.paper_size("A6")
        page = doc.new_page(width = paper_width, height = paper_height)  # new page with ...# pic dimension
        page.show_pdf_page(rect, imgPDF, 0)  # image fills the page
    #doc.save("all-my-pics.pdf") # Just for debugging 
    binary_pdf = BytesIO()
    doc.save(binary_pdf)
    binary_pdf = binary_pdf.getvalue()
    return binary_pdf

""" im = Image.open("qr_project/qr_app/static/never.jpg")
fomatted_img = BytesIO()
im.save(fomatted_img, format="png")
fomatted_img = fomatted_img.getvalue()
imglist = []
imglist.append(fomatted_img) """

""" with open("qr_project/qr_app/static/never.jpg", "rb") as f:
        #mybytearray = bytearray()
        mybytearray=f.read()
imglist = []
imglist.append(mybytearray) """


    
#convert_to_pdf(imglist)  # Just for debugging 