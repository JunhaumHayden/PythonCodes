import zlib

import PyPDF2

# Abrir o arquivo PDF
with open("enunciado_signed.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    # Acessar a primeira página
    page = reader.pages[0]

    # Acessar o objeto 8 diretamente a partir da lista de objetos da página
    # Supondo que o objeto 8 seja um dicionário com o stream
    obj8 = reader.get_object(90)  # Utilize o índice correto para acessar o objeto

    # Se o objeto contém um stream e um filtro FlateDecode
    print(obj8.get_data())
    print(obj8.get("/Filter") == "/FlateDecode" and "/Length" in obj8)
    if obj8.get("/Filter") == "/FlateDecode" and "/Length" in obj8:
        stream_data = obj8.get_data()  # Extrair o stream comprimido

        # Descomprimir o stream usando zlib
        try:
            decompressed_data = zlib.decompress(stream_data)
            print(
                "Conteúdo descomprimido do stream:",
                decompressed_data.decode("utf-8", errors="ignore"),
            )
        except zlib.error as e:
            print("Erro ao descomprimir o stream:", e)

    elif obj8.get("/Filter") == "/FlateDecode":
        stream_data = obj8.get_data()  # Extrair o stream comprimido

        # Descomprimir o stream usando zlib
        try:
            decompressed_data = zlib.decompress(stream_data)
            print(
                "Conteúdo descomprimido do stream:",
                decompressed_data.decode("utf-8", errors="ignore"),
            )
        except zlib.error as e:
            print("Erro ao descomprimir o stream:", e)
