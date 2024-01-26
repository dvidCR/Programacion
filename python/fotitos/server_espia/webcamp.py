import cv2

#pip install opencv-python
class webcam():
    
	@staticmethod
	def getPhoto():    
		cap = cv2.VideoCapture(0)

		leido, frame = cap.read()

		if leido == True:
			cv2.imwrite("foto.png", frame)
			print("Foto tomada correctamente")
		else:
			print("Error al acceder a la cámara")

		"""
			Finalmente liberamos o soltamos la cámara
		"""
		cap.release()
  
webcam.getPhoto()