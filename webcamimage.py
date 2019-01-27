import cv2, time, pandas
from datetime import datetime

def webCam():
	webcam = cv2.VideoCapture(0)

	cv2.namedWindow("test")	

	img_counter = 0

	f = open("imgcntr.txt", 'r')
	imgcnt = f.read()
	imgcnt = imgcnt.split() 
	img_counter = int(imgcnt[0])
	f.close()


	while True:
		ret, frame = webcam.read()
		cv2.imshow("test", frame)
		if not ret:
			break
		key = cv2.waitKey(1)

		if key == ord(' '):
			img_name = "opencv_frame_{}.png".format(img_counter)
			cv2.imwrite(img_name, frame)
			print("{} saved to folder".format(img_counter))
			img_counter += 1
		
		if key == ord('q'):
			f = open("imgcntr.txt", 'w')
			f.write(str(img_counter))
			f.close()
			break

	webcam.release()

	cv2.destroyAllWindows()