from io import BytesIO
import fitz

def convert_to_pdf(imglist):
    doc = fitz.open()  # empty output PDF
    paper_height, paper_width = fitz.paper_size("A6")
    for file in imglist:
        with fitz.open("JPEG", file) as img  :
            rect = img[0].rect  # pic dimension
        page = doc.new_page(width=paper_width, height=paper_height)
        page.insert_image(rect, stream=file) 
        #rect where to place the image on current page. 
    binary_pdf = BytesIO()
    doc.save(binary_pdf)
    binary_pdf = binary_pdf.getvalue()
    # remove any BytesIO class variables except content
    return binary_pdf