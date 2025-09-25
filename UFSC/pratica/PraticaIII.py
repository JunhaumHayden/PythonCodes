from PIL import Image
from Cuif import Cuif
import math

def PSNR(original,decodificada,b):
    try:
        mse = MSE(original,decodificada) 
        psnr = 10*math.log10(((2**b-1)**2)/mse)
        return psnr
    except ZeroDivisionError:
        return "Infinito"

def MSE(ori, dec):
    nsymbols = ori.width * ori.height * 3
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))
    return 0

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

    cuif.show()
    
    #Abre um arquivo Cuif e gera o objeto Cuif
    #cuif1 = Cuif.openCUIF('lena1.cuif')
    
    # Converte arquivo Cuif em BMP e mostra
    #cuif1.saveBMP("lena1.bmp")
    #cuif1.show()
    #img1 = Image.open("lena1.bmp")

    # Cálculo do PSNR
    #psnr = PSNR(img, img1, 8)
    #print(f'Cálculo do PSNR: {psnr}')

  

