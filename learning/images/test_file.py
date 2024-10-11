from PIL import Image

mac = Image.open('example.jpg')
type(mac)
print(mac.size)
print(mac.filename)
print(mac.format_description)
# mac.show()
# mac.crop((0, 0, 200, 610)).show()
computer = mac.crop((100, 100, 476, 210))

# mac.paste(im=computer, box=(0, 0))
# mac.show()
# computer.show()
# mac.resize((100,100)).show()
mac.putalpha(100)
mac.show()

