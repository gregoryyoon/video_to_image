import argparse
import cv2
from imutils.video import VideoStream
import imutils
import numpy as np
import os


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-a", "--aaa",
	help="exam 1")
ap.add_argument("-b", "--bbb",
	help="exam 2 ")
args = vars(ap.parse_args())



def get_output_folder_name(use_cam):
	
	output_folder_name = os.path.dirname(os.path.realpath(__file__))

	if use_cam == 0 :
		output_folder_name = output_folder_name + os.path.sep + args.get("video", False).strip()
		if os.path.isfile(output_folder_name) != True :
			raise Exception("MyError no file exist")
	else :
		output_folder_name = output_folder_name + os.path.sep + "cam"

	output_folder_name = output_folder_name + "_images"

	if os.path.exists(output_folder_name) != True :
		os.mkdir(output_folder_name, 755)

	return output_folder_name 

try :
	
	use_cam = 0
	output_folder_name = ""
	frame_count = 0	

	if not args.get("video", False) :
		use_cam = 1
	else :
		use_cam = 0

	if args.get("video", False).strip() == "cam" :
		use_cam = 1

	if use_cam == 1 :
		vs = VideoStream(src=0).start()
	else:
		vs = cv2.VideoCapture(args["video"])

	output_folder_name = get_output_folder_name(use_cam)
	
	while True:

		frame = vs.read()

		# handle the frame from VideoCapture or VideoStream
		if use_cam == 0 :
			frame = frame[1]

		if frame is None:
			break
		
		cv2.imshow("Frame", frame)
		
		out_file_name = output_folder_name + os.path.sep + "out_" + str(frame_count) + ".jpg"
		cv2.imwrite(out_file_name, frame)

		key = cv2.waitKey(1)
		#print(key)
		if key == ord("q"):
			break

		frame_count += 1

		print(out_file_name + " is written")
	
except Exception as ex: 
	print("exception occured" + str(ex))
finally:
	print("finally occured")

# if we are not using a video file, stop the camera video stream
if use_cam == 1 :
	vs.stop()
else :
	if vs is not None :
		vs.release()

cv2.destroyAllWindows()





