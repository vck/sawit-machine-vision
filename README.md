# sawit-machine-vision

### img2rgb

```
from PIL import Image
im = Image.open("/home/vickydasta/Downloads/Lenna.png")
rgb_im = im.convert('RGB')
r,g,b = rgb_im.getpixel((1, 1))
print(r,g,b)
```
### disain sistem 

- hardware: Raspberry Pi 3 model B, pi camera
- software: Python, PIL, Flask, Bootstrap, PiCamera

```
user --> capture command --> backend --> raspberry pi --> camera --> image --> PIL --> feature extraction (RGB, gray value) --> return extracted feature to user interface & save it into database for further processing
```

### antarmuka

client dibangun dengan bootstrap agar mobile friendly.



