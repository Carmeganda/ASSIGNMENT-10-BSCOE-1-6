#Assignment 10

#Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read
#Note: 
#	- Search how to generate QRCode
#	- Search how to read QRCode using webcam
#	- Search how to create and write to text file
#	- Your source code should be in github before Feb 19
#	- Create a demo of your program (1-2 min) and send it directly to my messenger

import QRCode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=12,
    border=6,
)
qr.add_data("Marie Carmela Sato Ramirez live in Sta. Cruz Occidental Mindoro . 18 years old, CEO of USA Bank")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("MCSR.png")

