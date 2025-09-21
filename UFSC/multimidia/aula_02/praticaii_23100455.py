# Aluno: Carlos Hayden Junior
# Matrícula: 23100455

from urllib.request import urlopen

from PIL import Image  # package pillow


def criarImagemRGB():
    img = Image.new("RGB", (512, 256))
    raster = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i, j] = (220, 219, 97, 255)

    # obtendo o pixel 0,0
    (r, g, b) = img.getpixel((0, 0))
    print("Pixel (0,0) com getpixel:", r, g, b)

    # outra forma
    print("Pixel (0,0): com raster", raster[0, 0])

    return img


def criarImagemCinza():
    img = Image.new("L", (256, 256))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i, j] = i
    y = img.getpixel((5, 5))
    print(y)
    return img


def criarImagemBinaria():
    # checkerboard pattern.
    img = Image.new("1", (500, 500))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ((int(i / 50) + int(j / 50)) % 2 == 0):
                raster[i, j] = 0
            else:
                raster[i, j] = 1
    y = img.getpixel((0, 0))
    print(y)
    return img


# 1. Reduza a resolução da imagem para ficar com a metade altura e da largura da imagem rgb.png e apresente esta imagem.
def reduzir_resolucao(img):
    """Reduz a resolução da imagem pela metade (altura e largura)."""
    largura_original, altura_original = img.size
    nova_largura = largura_original // 2
    nova_altura = altura_original // 2
    img_reduzida = Image.new(img.mode, (nova_largura, nova_altura))
    raster_original = img.load()
    raster_reduzida = img_reduzida.load()

    for i in range(nova_largura):
        for j in range(nova_altura):
            # Pega o pixel da imagem original correspondente ao novo pixel
            pixel_original = raster_original[i * 2, j * 2]
            raster_reduzida[i, j] = pixel_original
    return img_reduzida


# 2. Transforme a imagem rgb.png em tons de cinza e a apresente.
def transformar_cinza(img):
    """Transforma a imagem RGB ou RGBA em tons de cinza."""
    largura, altura = img.size
    img_cinza = Image.new("L", (largura, altura))
    raster_original = img.load()
    raster_cinza = img_cinza.load()

    for i in range(largura):
        for j in range(altura):
            pixel = raster_original[i, j]
            r, g, b = pixel[:3]  # Usar apenas componentes R, G, B
            tom_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
            raster_cinza[i, j] = tom_cinza
    return img_cinza


# 3. Transforme a imagem rgb.png em imagem binária e a apresenta.
def transformar_binaria(img, threshold=128):
    """Transforma a imagem RGB em imagem binária."""
    largura, altura = img.size
    img_binaria = Image.new("1", (largura, altura))
    raster_binaria = img_binaria.load()

    # Converte a imagem de entrada (deve ser RGB) para tons de cinza DENTRO desta função
    img_cinza = transformar_cinza(img)
    raster_cinza = img_cinza.load()

    for i in range(largura):
        for j in range(altura):
            if raster_cinza[i, j] > threshold:
                raster_binaria[i, j] = 1  # Branco
            else:
                raster_binaria[i, j] = 0  # Preto
    return img_binaria


# 4. Reduza o número de bits por pixel da imagem rgb.png para 3 bits.
def reduzir_bits(img):
    """Reduz o número de bits por pixel para 3 bits."""
    largura, altura = img.size
    img_reduzida_bits = Image.new("RGB", (largura, altura))
    raster_original = img.load()
    raster_reduzida = img_reduzida_bits.load()

    mascara = 0b11100000  # 224 em decimal

    for i in range(largura):
        for j in range(altura):
            pixel = raster_original[i, j]
            r, g, b = pixel[:3]  # Usar apenas componentes R, G, B
            r_reduzido = r & mascara
            g_reduzido = g & mascara
            b_reduzido = b & mascara
            raster_reduzida[i, j] = (r_reduzido, g_reduzido, b_reduzido)
    return img_reduzida_bits


# 5. Realizar a separação (split) dos canais RGB da imagem rgb.png, apresentando 3 imagens, R, G, B, a partir da imagem original.
def separar_canais(img):
    """Realiza a separação dos canais RGB da imagem."""
    largura, altura = img.size
    img_r = Image.new("RGB", (largura, altura))
    img_g = Image.new("RGB", (largura, altura))
    img_b = Image.new("RGB", (largura, altura))

    raster_original = img.load()
    raster_r = img_r.load()
    raster_g = img_g.load()
    raster_b = img_b.load()

    for i in range(largura):
        for j in range(altura):
            pixel = raster_original[i, j]
            r, g, b = pixel[:3]  # Usar apenas componentes R, G, B
            raster_r[i, j] = (r, 0, 0)
            raster_g[i, j] = (0, g, 0)
            raster_b[i, j] = (0, 0, b)

    return img_r, img_g, img_b


if __name__ == '__main__':
    img = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/RGB.png"))
    print("Largura:", img.width, "Altura:", img.height)
    # img.show()
    # criarImagemRGB().show()
    # criarImagemCinza().show()
    # criarImagemBinaria().show()

    # Chama as funções e exibe as imagens
    print("Imagem Original:")
    img.show()

    print("\nImagem com resolução reduzida:")
    img_reduzida = reduzir_resolucao(img)
    img_reduzida.show()

    print("\nImagem em tons de cinza:")
    img_cinza = transformar_cinza(img)
    img_cinza.show()

    print("\nImagem binária:")
    img_binaria = transformar_binaria(img)
    img_binaria.show()

    print("\nImagem com bits reduzidos:")
    img_reduzida_bits = reduzir_bits(img)
    img_reduzida_bits.show()

    print("\nCanais RGB separados:")
    img_r, img_g, img_b = separar_canais(img)
    print("Canal Vermelho (R):")
    img_r.show()
    print("Canal Verde (G):")
    img_g.show()
    print("Canal Azul (B):")
    img_b.show()
