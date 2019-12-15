def left_rigth(img):
	N_img = img.shape[0] #numero de linhas = altura
	M_img = img.shape[1] #numero de colunas = largura

	img = img 
	
	for i in range(N_img):
		for j in range(M_img): # percorre da esquerda para a direita no sentido ordenado
			left_rigth(img, i, j, N_img, M_img)
	return img



img1 = cv2.imread("baboon.png", 0)

res = left_rigth(img1)
cv2.imwrite("baboon_leftt_right.png", res)

"""
cv2.imshow("Esquerda para Direita", res)
cv2.waitKey(0)
"""
