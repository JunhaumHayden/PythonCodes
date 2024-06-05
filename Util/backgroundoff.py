#Removendo fundo de imagem com Python
#pip install pillow
#pip install rembg

from rembg import remove
from PIL import Image



#importa imagem original
img = Image.open('/Users/hayden/workspace/pythonCode/Util/img.jpg')
#Remove fundo da imagem
img_without_back = remove(img)

#salvar imagem sem fundo
img_without_back.save('/Users/hayden/workspace/pythonCode/Util/img_without_back.png')