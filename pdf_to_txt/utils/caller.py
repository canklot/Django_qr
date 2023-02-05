from fitzclimc import gettext
import io
import os

memory_file = io.BytesIO()
gettext("./pdf_to_txt/utils/3page.pdf" ,memory_file)

with open("./pdf_to_txt/utils/output.txt", "wb") as f:
    f.write(memory_file.getbuffer())

#print(memory_file.getvalue())