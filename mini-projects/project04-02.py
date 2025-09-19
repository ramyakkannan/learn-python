# generate QR code - customizable version
# https://www.youtube.com/watch?v=yVl_G-F7m8c&t=700s - PROGRAMMING WITH MOSH


import qrcode

toqr = input("text or url: ")
filename = input("your filename.jpg: ")

box_size = int(input("box size between 1 to 10: "))
border_size = int(input("border size between 1 to 10: "))


print("To check QR size: ", box_size, border_size)
print("to check inputs: ", filename, toqr)

my_code = qrcode.QRCode(box_size=box_size, border=border_size)

my_code.add_data(toqr)


my_image = qrcode.make(toqr)

my_image = my_code.make_image(
    back_color=(253, 245, 231),
    fill_color=(112, 73, 36)
)

my_image.save(filename)

print(f"{filename} QR code created!")

# FUTURE DEV IDEAS
# customize colours with a picker?
# load fav palettes into another file to call?
