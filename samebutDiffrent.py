from captcha.image import ImageCaptcha
from PIL import Image

def generate_captcha():
    try:
        image = ImageCaptcha(width=300, height=100)
        captcha_text = input("Masukkan teks captcha: ")

        data = image.generate(captcha_text)
        image.write(captcha_text, 'renata.png')

        with Image.open('renata.png') as img:
            img.show()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    generate_captcha()
