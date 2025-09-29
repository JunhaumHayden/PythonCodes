from PIL import Image
from Cuif import Cuif
import math

def PSNR(original, decoded, bits_per_channel=8):
    """
    Calcula o Peak Signal-to-Noise Ratio (PSNR) entre duas imagens.
    """
    try:
        mse = MSE(original, decoded)
        if mse == 0:
            return float('inf') # Return infinity if MSE is 0
        max_pixel_value = (2**bits_per_channel) - 1
        psnr = 10 * math.log10((max_pixel_value**2) / mse)
        return psnr
    except ValueError as e:
        print(f"Erro no cálculo do PSNR: {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado no cálculo do PSNR: {e}")
        return None

def MSE(original, decoded):
    """
    Calcula o Mean Squared Error (MSE) entre duas imagens.
    """
    sum_squared_error = 0
    # Ensure images have the same dimensions
    if original.size != decoded.size:
        raise ValueError("As imagens devem ter as mesmas dimensões.")

    width, height = original.size
    # Assuming RGB images, 3 color channels
    nsymbols = width * height * 3

    for i in range(width):
        for j in range(height):
            original_r, original_g, original_b = original.getpixel((i, j))
            decoded_r, decoded_g, decoded_b = decoded.getpixel((i, j))
            sum_squared_error += (original_r - decoded_r)**2 + (original_g - decoded_g)**2 + (original_b - decoded_b)**2

    # Avoid division by zero if image is empty
    if nsymbols == 0:
        return 0
    return sum_squared_error / nsymbols

if __name__ == "__main__":
    filepath = 'lena.bmp'
    img = Image.open(filepath)
    matriculas = [23100455]
    
    # instancia objeto Cuif, convertendo imagem em CUIF.1
    cuif = Cuif(img,1,matriculas)
    
    # imprime cabeçalho Cuif
    cuif.printHeader()
    
    #gera o arquivo Cuif.1
    cuif.save('lena1.cuif')
    
    #Abre um arquivo Cuif e gera o objeto Cuif
    cuif1 = Cuif.openCUIF('lena1.cuif')
    
    # Converte arquivo Cuif em BMP e mostra
    cuif1.saveBMP("lena1.bmp")
    cuif1.show()
    img1 = Image.open("lena1.bmp")

    # Cálculo do PSNR
    psnr = PSNR(img, img1, 8)
    print(f'Cálculo do PSNR: {psnr}')

    # instancia objeto Cuif, convertendo imagem em CUIF.2
    cuif = Cuif(img, 2, matriculas)

    # imprime cabeçalho Cuif
    cuif.printHeader()

    # gera o arquivo Cuif.2
    cuif.save('lena2.cuif')

    # Abre um arquivo Cuif e gera o objeto Cuif
    cuif2 = Cuif.openCUIF('lena2.cuif')

    # Converte arquivo Cuif em BMP e mostra
    cuif2.saveBMP("lena2.bmp")
    cuif2.show()
    # Cálculo do PSNR
    img2 = Image.open("lena2.bmp")
    psnr = PSNR(img, img2, 8)
    print(f'Cálculo do PSNR para CUIF.2: {psnr}')
  

