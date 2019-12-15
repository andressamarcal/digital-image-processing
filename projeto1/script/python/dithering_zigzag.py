def zigzag(img):
	N_img = img.shape[0] #numero de linhas = altura
	M_img = img.shape[1] #numero de colunas = largura

	img = img 

	for i in range(N_img):
		if(i%2 == 0): #se for linha par, percorre da esq para dir
			for j in range(M_img):
				zigzag(img, i, j, N_img, M_img)
		if(i%2 == 1): #se for linha impar, percorre dir para esq 
			for j in range(M_img-1, -1, -1):
				zigzag(img, i, j, N_img, M_img)
	return img 



img1 = cv2.imread("baboon.png", 0) 

res = zigzag(img1)
cv2.imwrite("baboon_leftt_right.png", res)

"""
cv2.imshow("Zigue Zague", res)
cv2.waitKey(0)
"""
