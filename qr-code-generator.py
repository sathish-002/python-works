# for this we have used the qrcode package and pillow package
import qrcode
data = "https://www.linkedin.com/in/sathish-vadivel-21b79021b/"
qr = qrcode.make(data)
qr.show()
