import pdf_parser

with open("enunciado_signed.pdf", "rb") as f:
    pdf = pdf_parser.parse(f)

for page in pdf.pages:
    for text in page.extract_text():
        print(text)
metadata = pdf.metadata
print(metadata)

for obj in pdf.objects:
    print(obj.type, obj.id)
