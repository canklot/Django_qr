from io import BytesIO
import fitz  # PyMuPDF


""" This function puts every image on a new pdf page  
    and return pdf file stream """


def img_list_to_pdf(imglist):
    doc = fitz.open()  # Empty output PDF
    paper_height, paper_width = fitz.paper_size("A6")

    for file in imglist:
        with fitz.open("JPEG", file) as img:
            rect = img[0].rect  # pic dimensions
        page = doc.new_page(width=paper_width, height=paper_height)
        # Rect specifies where to place the image on current page
        page.insert_image(rect, stream=file)

    binary_pdf = BytesIO()
    doc.save(binary_pdf)
    # Use getvalue to get just the binary data from BytesIO instance
    binary_pdf = binary_pdf.getvalue()

    return binary_pdf
