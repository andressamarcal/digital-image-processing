###########################################################################################
# ALUNA: Andressa Gabrielly Macedo Marçal                                                 #
# RA: 262878                                                                              #
# MO443/MC920                                                                             #
###########################################################################################

import cv2
import numpy as np


def set_pixel(im, x, y, new):
    im[x, y] = new


def stevenson(im):  # algoritmo de stevenson para pontilhamento de imagem

    w32 = 32/200.0
    w12 = 12/200.0
    w26 = 26/200.0
    w30 = 30/200.0
    w16 = 16/200.0
    w5 = 5/200.0
    width, height = im.shape

    for y in range(0, height-2):
        for x in range(0, width-2):
            old_pixel = im[x, y]
            if old_pixel < 128:
                new_pixel = 0
            else:
                new_pixel = 255
            set_pixel(im, x, y, new_pixel)
            quant_err = old_pixel-new_pixel
            set_pixel(im, x+1, y, im[x+1, y] + w32 * quant_err)
            set_pixel(im, x+2, y, im[x+2, y] + w12 * quant_err)
            set_pixel(im, x-2, y+1, im[x-2, y+1] + w26 * quant_err)
            set_pixel(im, x-1, y+1, im[x-1, y+1] + w30 * quant_err)
            set_pixel(im, x, y+1, im[x, y+1] + w16 * quant_err)
            set_pixel(im, x+1, y+1, im[x+1, y+1] + w12 * quant_err)
            set_pixel(im, x+2, y+1, im[x+2, y+1] + w26 * quant_err)
            set_pixel(im, x-2, y+2, im[x-2, y+2] + w12 * quant_err)
            set_pixel(im, x-1, y+2, im[x-1, y+2] + w5 * quant_err)
            set_pixel(im, x, y+2, im[x, y+2] + w12 * quant_err)
            set_pixel(im, x+1, y+2, im[x+1, y+2] + w12 * quant_err)
            set_pixel(im, x+2, y+2, im[x+2, y+2] + w5 * quant_err)
    return im


def burkes(im):  # algoritmo de burkes para pontilhamento de imagem

    w8 = 8.0/32.0
    w4 = 4.0/32.0
    w2 = 2.0/32.0
    width, height = im.shape

    for y in range(0, height-2):
        for x in range(0, width-2):
            old_pixel = im[x, y]
            if old_pixel < 128:
                new_pixel = 0
            else:
                new_pixel = 255
            set_pixel(im, x, y, new_pixel)
            quant_err = old_pixel-new_pixel
            set_pixel(im, x+1, y, im[x+1, y] + w8 * quant_err)
            set_pixel(im, x+2, y, im[x+2, y] + w4 * quant_err)
            set_pixel(im, x-2, y+1, im[x-2, y+1] + w2 * quant_err)
            set_pixel(im, x-1, y+1, im[x-1, y+1] + w4 * quant_err)
            set_pixel(im, x, y+1, im[x, y+1] + w8 * quant_err)
            set_pixel(im, x+1, y+1, im[x+1, y+1] + w4 * quant_err)
            set_pixel(im, x+2, y+1, im[x+2, y+1] + w2 * quant_err)


def sierra(im):   # algoritmo de Sierra para pontilhamento de imagem

    w5 = 5/32.0
    w4 = 4/32.0
    w3 = 3/32.0
    w2 = 2/32.0
    width, height = im.shape

    for y in range(0, height-2):
        for x in range(0, width-2):
            old_pixel = im[x, y]
            if old_pixel < 128:
                new_pixel = 0
            else:
                new_pixel = 255
            set_pixel(im, x, y, new_pixel)
            quant_err = old_pixel-new_pixel
            set_pixel(im, x+1, y, im[x+1, y] + w5 * quant_err)
            set_pixel(im, x+2, y, im[x+2, y] + w3 * quant_err)
            set_pixel(im, x-2, y+1, im[x-2, y+1] + w2 * quant_err)
            set_pixel(im, x-1, y+1, im[x-1, y+1] + w4 * quant_err)
            set_pixel(im, x, y+1, im[x, y+1] + w5 * quant_err)
            set_pixel(im, x+1, y+1, im[x+1, y+1] + w4 * quant_err)
            set_pixel(im, x+2, y+1, im[x+2, y+1] + w2 * quant_err)
            set_pixel(im, x-2, y+2, im[x-2, y+2] + w2 * quant_err)
            set_pixel(im, x-1, y+2, im[x-1, y+2] + w3 * quant_err)
            set_pixel(im, x, y+2, im[x, y+2] + w2 * quant_err)
    return im


def stucki(im):   # algoritmo de Stucki para pontilhamento de imagem
    
    w8 = 8/42.0
    w7 = 7/42.0
    w5 = 5/42.0
    w4 = 4/42.0
    w2 = 2/42.0
    w1 = 1/42.0
    width, height = im.shape
    
    for y in range(0, height-2):
        for x in range(0, width-2):
            old_pixel = im[x, y]
            if old_pixel < 128:
                new_pixel = 0
            else:
                new_pixel = 255
            set_pixel(im, x, y, new_pixel)
            quant_err = old_pixel-new_pixel
            set_pixel(im, x+1, y, im[x+1, y] + w7 * quant_err)
            set_pixel(im, x+2, y, im[x+2, y] + w5 * quant_err)
            set_pixel(im, x-2, y+1, im[x-2, y+1] + w2 * quant_err)
            set_pixel(im, x-1, y+1, im[x-1, y+1] + w4 * quant_err)
            set_pixel(im, x, y+1, im[x, y+1] + w8 * quant_err)
            set_pixel(im, x+1, y+1, im[x+1, y+1] + w4 * quant_err)
            set_pixel(im, x+2, y+1, im[x+2, y+1] + w2 * quant_err)
            set_pixel(im, x-2, y+2, im[x-2, y+2] + w1 * quant_err)
            set_pixel(im, x-1, y+2, im[x-1, y+2] + w2 * quant_err)
            set_pixel(im, x, y+2, im[x, y+2] + w4 * quant_err)
            set_pixel(im, x+1, y+2, im[x+1, y+2] + w2 * quant_err)
            set_pixel(im, x+2, y+2, im[x+2, y+2] + w1 * quant_err)
    return im


def jarvis(im):   # algoritmo de Jarvis, Judice e Ninke para pontilhamento de imagem

    w1 = 1/48.0
    w3 = 3/48.0
    w5 = 5/48.0
    w7 = 7/48.0
    
    width, height = im.shape
    
    for y in range(0, height-2):
        for x in range(0, width-2):
            old_pixel = im[x, y]
            if old_pixel < 128:
                new_pixel = 0
            else:
                new_pixel = 255
            set_pixel(im, x, y, new_pixel)
            quant_err = old_pixel-new_pixel
            set_pixel(im, x+1, y, im[x+1, y] + w7 * quant_err)
            set_pixel(im, x+2, y, im[x+2, y] + w5 * quant_err)
            set_pixel(im, x-2, y+1, im[x-2, y+1] + w3 * quant_err)
            set_pixel(im, x-1, y+1, im[x-1, y+1] + w5 * quant_err)
            set_pixel(im, x, y+1, im[x, y+1] + w7 * quant_err)
            set_pixel(im, x+1, y+1, im[x+1, y+1] + w5 * quant_err)
            set_pixel(im, x+2, y+1, im[x+2, y+1] + w3 * quant_err)
            set_pixel(im, x-2, y+2, im[x-2, y+2] + w1 * quant_err)
            set_pixel(im, x-1, y+2, im[x-1, y+2] + w3 * quant_err)
            set_pixel(im, x, y+2, im[x, y+2] + w5 * quant_err)
            set_pixel(im, x+1, y+2, im[x+1, y+2] + w3 * quant_err)
            set_pixel(im, x+2, y+2, im[x+2, y+2] + w1 * quant_err)
    return im


def floyd(im):  # Metodo Floyd-Steinberg para pontilhamento de imagem
    
    w7 = 7/16.0
    w3 = 3/16.0
    w5 = 5/16.0
    w1 = 1/16.0

    for y in range(0, height-1):
        for x in range(1, width-1):
            old_pixel = im[x, y]
            if old_pixel < 127:
                new_pixel = 0
            else:
                new_pixel = 255
            set_pixel(im, x, y, new_pixel)
            quant_err = old_pixel-new_pixel
            set_pixel(im, x+1, y, im[x+1, y]+quant_err * w7)
            set_pixel(im, x-1, y+1, im[x-1, y+1] + quant_err * w3)
            set_pixel(im, x, y+1, im[x, y+1] + quant_err * w5)
            set_pixel(im, x+1, y+1, im[x+1, y+1] + quant_err * w1)

    return im


# adicione o caminho para acessar a imagem
img = cv2.imread(
    "/home/andressa/Documentos/testes/input/baboon.png")

img2 = img.copy()
width, height, z = img.shape

# mostra a altura, largura e canais de cores da imagem
print(img.shape)

#transforma em tons de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 




#####################################################

#						ATENÇÃO						#

# A parti daqui, RETIRAR COMENTÁRIO do filtro referente ao 
# canal RGB para aplica-lo

# O mesmo serve para o gray

####################################################







# pega o canal azul e envia para o algoritmo
blue = img[:, :, 0]  

blue = floyd(blue)  
#blue = stucki(blue) 
#blue = sierra(blue)   
#blue = burkes(blue)
#blue = stevenson(blue)
#blue = jarvis(blue)  


# pega o canal verde e envia para o algoritmo
green = img[:, :, 1] 

green = floyd(green)  
#green = stucki(green) 
#green = stevenson(green)
#green = sierra(green)   
#green = burkes(green)
#green = jarvis(green)  



#pega canal vermelho e envia para o algoritmo
red = img[:, :, 2] 

red = floyd(red)
#red = stucki(red)
#red = stevenson(red)
#red = sierra(red)   
r#ed = burkes(red)
#red = jarvis(red)  


#mesclando os 3 canais de cores (R,G,B)
image = cv2.merge((blue, green, red))  


#exibe resultado com aplicação do filtro com pontilhado em colorido
cv2.imshow('merged_rgb', image) 


#aplica filtro com pontilhado em tons de cinza
gray2 = floyd(gray) 
#gray2 = stucki(gray) 
#gray2 = stevenson(gray) 
#gray2 = sierra(gray) 
#gray2 = burkes(gray) 
#gray2 = jarvis(gray) 


# salva resultado do processamento
#cv2.imwrite('output/out_dithering_gray.jpg', gray2)
#cv2.imwrite('output/out_dithering_color.jpg', img2)

#exibe resultado do pontilhado gray
cv2.imshow('original_gray', gray2)

#exibe imagem original para fins comparativos
cv2.imshow('original', img2)

cv2.waitKey(0)