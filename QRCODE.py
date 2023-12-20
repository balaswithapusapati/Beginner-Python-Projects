
import qrcode

def GENERATE_QRCODE(text):
    qr = qrcode.QRCode (
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save("image1.png")

text = input("Enter your URL: ")
GENERATE_QRCODE(text)
