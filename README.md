# sawit-machine-vision

### img2rgb

```
from PIL import Image
im = Image.open("/home/vickydasta/Downloads/Lenna.png")
rgb_im = im.convert('RGB')
r,g,b = rgb_im.getpixel((1, 1))
print(r,g,b)
```





