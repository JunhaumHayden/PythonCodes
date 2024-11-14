import PyPDF2
from PyPDF2 import PdfFileReader

# Abrir o arquivo PDF
with open("enunciado_signed.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    fields = reader.get_fields()
    print(fields)
