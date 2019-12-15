import cv2
import numpy as np
#from matplotlib.pyplot import imshow, show
import re
import os


def readImage(filename):
    """
    Method to read new images

    :param filename: The file location of the image
    :return: img: A list of ints with the matrix of pixels of the image

    """
    #   read the image
    try:
        image_matrix = cv2.imread(filename, 1)
        img = image_matrix.astype(dtype='uint8')
    except Exception:
        return np.array([])

    #   return the image readed
    return img


def storeImage(filename, image_matrix):
    """
    Method to store new images

    :param filename: The file location of the image
    :param image_matrix: A list of ints with the matrix of pixels of the image
    :return: None

    """
    try:
        cv2.imwrite(filename, image_matrix)
    except Exception:
        print("A imagem nao foi salva!")


def writePlans(img):
    """

        Method to show specific planes of the image

        Parameters
        ----------
            img : list
                A list of ints with the matrix of pixels of the image

        Returns
        -------
            Nothing

    """

    first_plane = np.empty(img.shape)
    second_plane = np.empty(img.shape)
    third_plane = np.empty(img.shape)    
    fourth_plane = np.empty(img.shape)    
    fifth_plane = np.empty(img.shape)    
    sixth_plane = np.empty(img.shape)  
    seventh_plane = np.empty(img.shape)
    last_plane = np.empty(img.shape)
    

    first_plane[:, :, 2] = ((img[:, :, 2] >> 0) % 2) * 255
    first_plane[:, :, 1] = ((img[:, :, 1] >> 0) % 2) * 255
    first_plane[:, :, 0] = ((img[:, :, 0] >> 0) % 2) * 255
    cv2.imshow('Primeiro Plano',first_plane)
    #show()

    second_plane[:, :, 2] = ((img[:, :, 2] >> 1) % 2) * 255
    second_plane[:, :, 1] = ((img[:, :, 1] >> 1) % 2) * 255
    second_plane[:, :, 0] = ((img[:, :, 0] >> 1) % 2) * 255
    cv2.imshow('Segundo Plano',second_plane)
    #show()

    third_plane[:, :, 2] = ((img[:, :, 2] >> 2) % 2) * 255
    third_plane[:, :, 1] = ((img[:, :, 1] >> 2) % 2) * 255
    third_plane[:, :, 0] = ((img[:, :, 0] >> 2) % 2) * 255
    cv2.imshow('Terceiro Plano',third_plane)
    #show()

    fourth_plane[:, :, 2] = ((img[:, :, 2] >> 3) % 2) * 255
    fourth_plane[:, :, 1] = ((img[:, :, 1] >> 3) % 2) * 255
    fourth_plane[:, :, 0] = ((img[:, :, 0] >> 3) % 2) * 255
    cv2.imshow('Quarto Plano',fourth_plane)
    #show()

    fifth_plane[:, :, 2] = ((img[:, :, 2] >> 4) % 2) * 255
    fifth_plane[:, :, 1] = ((img[:, :, 1] >> 4) % 2) * 255
    fifth_plane[:, :, 0] = ((img[:, :, 0] >> 4) % 2) * 255
    cv2.imshow('Quinto Plano',fifth_plane)

    sixth_plane[:, :, 2] = ((img[:, :, 2] >> 5) % 2) * 255
    sixth_plane[:, :, 1] = ((img[:, :, 1] >> 5) % 2) * 255
    sixth_plane[:, :, 0] = ((img[:, :, 0] >> 5) % 2) * 255
    cv2.imshow('Sexto Plano',sixth_plane)

    seventh_plane[:, :, 2] = ((img[:, :, 2] >> 6) % 2) * 255
    seventh_plane[:, :, 1] = ((img[:, :, 1] >> 6) % 2) * 255
    seventh_plane[:, :, 0] = ((img[:, :, 0] >> 6) % 2) * 255
    cv2.imshow('Sétimo Plano',seventh_plane)

    last_plane[:, :, 2] = ((img[:, :, 2] >> 7) % 2) * 255
    last_plane[:, :, 1] = ((img[:, :, 1] >> 7) % 2) * 255
    last_plane[:, :, 0] = ((img[:, :, 0] >> 7) % 2) * 255
    cv2.imshow('Último Plano',last_plane)
    #show()


def txtToBin(filename):
    """

        Method to convert a string text in binary code.

        Parameters
        ----------
            filename : str
                The file location of the text

        Returns
        -------
            binarray : str
                The string representation of the text in binary code

    """

    with open(filename, 'r') as txtFile:
        text = txtFile.read()

    binarray = ''.join(format(ord(char), '08b') for char in text)

    return binarray


def changeNewLine(originalFile, destFile):
    """

    :param originalFile: The file location of the input text
    :param destFile: The file location of the output text
    :return: Nothing

    """
    with open(originalFile, 'r') as myfile:
        data = myfile.read()

    data = re.sub(r"[^a-zA-Z0-9]", "", data)

    file = open(destFile, 'w')
    file.write(data)
    file.close()


def writeText(filename, data):
    """

        Method to write text into a file.

        Parameters
        ----------
            filename : str
                The file location of the input text
            data : str
                The text to be write into the file

        Returns
        -------
            Nothing

    """

    with open(filename, 'w+') as writeFile:
        writeFile.write(data)


def encodeImage(imageMatrix, binaryText, bitPlane):
    """

        Method to encode a string text in binary code into the image.

        Parameters
        ----------
            imageMatrix : list
                A list of ints with the matrix of pixels of the image to be modified

            binaryText : str
                The binary representation of the text to be encoded

            bitPlane : int
                The bit plane where the text will be encoded

        Returns
        -------
            encodedImage : list
                A list of ints with the matrix of pixels of the image with text encoded

    """

    height, width, channel = imageMatrix.shape

    count = 0
    encodedImage = imageMatrix
    mask = 1 << bitPlane

    for h in range(height):
        for w in range(width):
            for c in range(channel):
                if count < len(binaryText):
                    bit = int(binaryText[count])
                    encodedImage[h][w][c] = (
                        imageMatrix[h][w][c] & ~(mask)) | (bit << bitPlane)

                    count = count + 1
                else:
                    # ja encodou o texto todo
                    return encodedImage

    return encodedImage


def decodeImage(imageMatrix, bitPlane):
    """

        Method to decode the text inside the image to a text string.

        Parameters
        ----------
            imageMatrix : list
                A list of ints with the matrix of pixels of the image to be modified

            bitPlane : int
                The bit plane where the text is encoded

        Returns
        -------
            text : str
                The decode text from the image
    """

    height, width, channel = imageMatrix.shape
    count = 0

    mask = 1 << bitPlane
    bits = ''
    text = ''

    for h in range(height):
        for w in range(width):
            for c in range(channel):
                pixel = imageMatrix[h][w][c]

                bit = ((pixel & mask) >> bitPlane) % 2
                bits = str(bits) + str(bit)
                count = count + 1

                if count == 8:
                    # chars.append(chr(int(bits,2)))
                    char = chr(int(bits, 2))
                    text = text + str(char)
                    bits = ''
                    count = 0

    return text


def main():
    # path para a pasta
    pathIn = '/home/andressa/Documentos/mestrado/trabalho4/imagens/'
    pathTxt = '/home/andressa/Documentos/mestrado/trabalho4/textos/'
    pathOut = '/home/andressa/Documentos/mestrado/trabalho4/output/'

    operation = input("\n:: Esteganografia - Trabalho 4 ::\n"
                    "\n** Encode ** \n\n** Decode **\n\nDigite o nome da opcao desejada: ")
    
    if operation == 'Encode' or operation == 'encode':
        
        #########################################
        #   Leitura dos argumentos de entrada   #
        #########################################
        
        # input da imagem
        imageInput = input("Digite o nome da imagem (com sua extensão): ")
        imageInput = pathIn + imageInput

        # input do texto a ser codificado
        txtInput = input("Insira o nome do arquivo de texto a ser inserido:(ex: nome.txt) ")
        txtInput = pathTxt + txtInput

        # plane of the bit will be modify
        bitPlane = int(input("Insira o numero do plano de bits que você deseja modificar(numero de 0 a 7): "))

        # output da imagem
        imageOutput = input("Digite o nome da nova imagem(com sua extensão): ")
        imageOutput = pathOut + imageOutput

        #########################################
        #    Leitura dos arquivos de entrada    #
        #########################################
        
        #   conversao da imagem para a matrix que a representa
        print("\nLendo a imagem ...\n")
        imageMatrix = readImage(imageInput)

        #   eliminamos as quebras de linha do arquivo texto
        print("\nEliminando espaço e caracteres especiais do texto a ser codificado ...\n")
        changeNewLine(txtInput, txtInput)

        #   conversao do texto (escrito) para binario
        binText = txtToBin(txtInput)

        ####################################
        #    Codifica o texto na imagem    #
        ####################################
        
        print("\n.: Codificando o texto na imagem :.\n")
        encodedImgMatrix = encodeImage(imageMatrix, binText, bitPlane)

        ###############################
        #    Armazena a nova image    #
        ###############################
        
        print("\nArmazenando imagem modificada ...\n")
        storeImage(imageOutput, encodedImgMatrix)
        print("Imagem salva com sucesso!\n")
        
        # debug
        # write_plans(encodedImgMatrix)

    elif operation == 'Decode' or operation == 'decode':
        
        #########################################
        #   Leitura dos argumentos de entrada   #
        #########################################
        
        # leitura da imagem a ser decodificada
        imageInput = input("Digite o nome da imagem (com sua extensão): ")
        imageInput = pathOut + imageInput

        # plane of the modified bit
        bitPlane = int(input("Insira o plano de bits que você deseja modificar( de 0 a 7): "))

        # output text
        txtOutput = input(
            "Insira o nome do arquivo em que deseja salvar o texto: ")
        txtOutput = pathOut + txtOutput

        #########################################
        #    Leitura dos arquivos de entrada    #
        #########################################
        
        #   conversao da imagem para a matrix que a representa
        print("\nLendo a imagem ...\n")
        imageMatrix = readImage(imageInput)

        ######################################
        #    Decodifica o texto da imagem    #
        ######################################
        
        print("\n.: Decodificando :.\n")
        decodedText = decodeImage(imageMatrix, bitPlane)

        print("\nEscrevendo ...\n")
        writeText(txtOutput, decodedText)

        print("\n Concluído!\n")

    else:
        print("Operação não suportada!")


if __name__ == '__main__':
    main()
