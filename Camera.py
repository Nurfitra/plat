import cv2
import sys
import numpy as np
import Main
import DetectChars
import DetectPlates
import PossiblePlate

cap = cv2.VideoCapture(0)
# Create the haar cascade
Cascade = cv2.CascadeClassifier("plat-nomor.xml")

def main(action):
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()

		# Our operations on the frame come here
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		plates = Cascade.detectMultiScale(
			#gray,
			frame,
			scaleFactor=1.1,
			minNeighbors=10,
			minSize=(30, 30),
			#flags = cv2.CV_HAAR_SCALE_IMAGE
		)

		#print("Found {0} plates".format(len(plates)))

		# Draw a rectangle around the plates
		for (x, y, w, h) in plates:
			#cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			cv2.rectangle(frame, (x, y), (w+x, h+y), (0, 255, 0), 2)
	    		plate_ori = frame[y:y+h, x:x+w]
		if len(plates) > 0:
			Main.main(plate_ori)
			#print pytesseract.image_to_string(Image.open('plat.jpg'))
			# Now we split the image to 5000 cells, each 20x20 size
			#cv2.imshow("invert", final_transparent_image)

		# Display the resulting frame
		#cv2.imshow('frame', frame)


		if action == "stop":
			break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
    main(sys.argv[1])
