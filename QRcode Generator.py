import pyqrcode
from pyqrcode import QRCode
s = "https://www.youtube.com/"  #youtube
url = pyqrcode.create(s)
url.svg("youtube.svg", scale = 10)