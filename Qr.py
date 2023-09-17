import qrcode

print(
  """\033[34m


    QRCode generator
  
  """
  
)

print()

bsize = int(input("Enter the box size: "))

bord = int(input("Enter the border size: "))

info = input('type what your want to be shown when scanned: ')

fill = input("What color do you want the lines to be: ")

bacck = input("What color do you want the background to be: ")
    
    



qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=bsize,
    border=bord,
)
qr.add_data(info)
qr.make(fit=True)

img = qr.make_image(fill_color=fill, back_color=bacck)
img.save("result.png")
print("done")
