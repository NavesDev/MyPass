import pystray
from PIL import Image

def appIconCreate():
    img = Image.open('assets/appIcon.ico')
    icon = pystray.Icon("MyPass")
    icon.icon = img
    icon.run()