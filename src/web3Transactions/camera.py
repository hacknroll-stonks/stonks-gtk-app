from picamera2 import Picamera2, Preview
import time
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
import os

def cam(val):
	picam2 = Picamera2()

	camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
	picam2.configure(camera_config)
	picam2.start_preview(Preview.QTGL)
	picam2.start()
	time.sleep(2)
	# k = input()
	picam2.capture_file("tmp.png")

	img = Image.open("tmp.png")
	decoded_list = decode(img)
	if len(decoded_list) > 0:
		print(decoded_list[0])
	else:
		print("nothin found")

	os.remove("./tmp.png")
	with open("Private_Keys.txt","r") as privateFile:
		btc = privateFile.readline().strip().split(" ")[1]
		eth = privateFile.readline().strip().split(" ")[1]

	address = decoded_list[0].strip().split(" ")[1]
	signContract(address, val, eth)