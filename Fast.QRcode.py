import qrcode
from tkinter import Tk, filedialog
from urllib.parse import urlparse
from pathlib import Path
import os

os.system("title Fast.QRcode")

url = input("Enter URL: ")

cia_name = Path(urlparse(url).path).name
base_name = Path(cia_name).stem

Tk().withdraw()
output = filedialog.asksaveasfilename(
    defaultextension=".png",
    filetypes=[("PNG files", "*.png")],
    initialfile=f"{base_name}-QR_CODE.png"
)

if output:
    img = qrcode.make(url)
    img.save(output)
    print(f"Saved to {output}")