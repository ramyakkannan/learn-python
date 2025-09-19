# generate QR code - simple version
# https://www.youtube.com/watch?v=yVl_G-F7m8c&t=700s - PROGRAMMING WITH MOSH


import qrcode

datatoqr = input("Enter text or URL: ").strip()
filename = input("Enter filename.jpg: ").strip()

print(f"The file name is {filename} and data to QR code is {datatoqr}")

img = qrcode.make(datatoqr)
img.save(filename)

print(f"QR Code saved as {filename}")
