from PIL import Image

open_image = Image.open("image 2.jpg")
convert_to_bw = open_image.convert("1")
convert_to_bw.show()
convert_to_bw.save("B_W.jpg")
