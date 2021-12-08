'''
Program : Face Detection with Haar Cascades

'''
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
	ret , frame = cap.read()

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

		face_gray = gray[y:y+h,x:x+w]
		face_clr = frame[y:y+h,x:x+w]

		eyes = eye_cascade.detectMultiScale(face_gray)

		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(face_clr,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

	cv2.imshow("Image",frame)

	k = cv2.waitKey(1)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()



