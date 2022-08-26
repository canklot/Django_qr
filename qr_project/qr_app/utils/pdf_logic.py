from io import BytesIO
import fitz

def convert_to_pdf(imglist):
    doc = fitz.open()  # PDF with the pictures
    for file in imglist:
        # open pic as document. Convert this to use with
        img = fitz.open("jpg", file)
        rect = img[0].rect  # pic dimension
        pdfbytes = img.convert_to_pdf()  # make a PDF stream
        img.close()  # no longer needed. Remove after with
        imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
        paper_height, paper_width = fitz.paper_size("A6")
        # new page with ...# pic dimension
        page = doc.new_page(width=paper_width, height=paper_height)
        page.show_pdf_page(rect, imgPDF, 0)  # image fills the page
    binary_pdf = BytesIO()
    doc.save(binary_pdf)
    binary_pdf = binary_pdf.getvalue()
    return binary_pdf