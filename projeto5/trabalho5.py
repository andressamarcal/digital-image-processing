import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def return_svd (image, k):
	#retorna svd de U, S, V
	U, S, V = np.linalg.svd(image[:, :, k])
	return U, S, V

def compress(image, k):
	#aplica compressão
	#utiliza formula
	new_image = np.zeros((image.shape[0], image.shape[1], image.shape[2]))
	for i in range (new_image.shape[2]): 
		U, S, V = return_svd(image, i)
		new_U = U[:, 0:k]
		new_S = S[0:k]
		new_V = V[0:k, :]
		#np diag extrai da diagonal principal de S
		#np dot calcula o produto escalar de U, S e V
		new_image[:, :, i] = np.dot(np.dot(new_U, np.diag(new_S)), new_V)
	return new_image


def rmse_images(image, new_image): 
	#aplicando a formula
	rmse = np.sqrt(np.mean((image-new_image)**2))
	return rmse

def plot_ (x, rmse, ratio, nome): 

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx()
	ax1.plot(x, rmse, 'g-')
	ax2.plot(x, ratio, 'b-')
	plt.title('Gráfico da imagem ' + nome , fontsize=14)
	ax1.set_xlabel('K')
	ax1.set_ylabel('RMSE', color='g')
	ax2.set_ylabel('Compress Ratio', color='b')
	plt.show()

def main(arq):
	#testando de k=1 a k=250 
	k = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 250]
	ratio = np.zeros((len(k)))
	rmse = np.zeros((len(k)))
	for i in range (len(k)):
		image = cv2.imread(arq)
		new_image = compress(image, k[i])
		t = rmse_images(image, new_image)
		rmse[i] = t
		cv2.imwrite(str(arq +'compress'+str(k[i]) + '.png'), new_image)
		original_bytes = os.path.getsize(arq)
		compress_bytes = os.path.getsize(str(arq +'compress'+str(k[i]) + '.png'))
		p = np.float(compress_bytes)/np.float(original_bytes)
		print (arq + ": k = " + str(k[i]) + ". RMSE: " + str(t) + ". Ratio: " + str(p) + ".")
		ratio[i] = p
	plot_(k, rmse, ratio, arq)

print(' ##################		INICIALIZANDO	 ########################### ')

print("----------------------------------------------------------------------------")
main("baboon.png")
print("----------------------------------------------------------------------------")
main("monalisa.png")
print("----------------------------------------------------------------------------")
main("peppers.png")
print("----------------------------------------------------------------------------")
main("watch.png")
print("----------------------------------------------------------------------------")

print(' #####################		FINALIZADO		###########################')
