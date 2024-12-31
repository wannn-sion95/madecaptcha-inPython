from captcha.image import ImageCaptcha

image = ImageCaptcha(width=400, height=100)
captcha_text = input("Masukkan teks captcha: ")

data = image.generate(captcha_text)

image.write(captcha_text, 'wannnSion.png')

from PIL import Image
img =Image.open('wannnSion.png')
img.show()
