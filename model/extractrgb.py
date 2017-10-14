from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
import csv

data = []
image_name = [name for name in os.listdir("data/raw/") if "F" in name]

for image in os.listdir("data/raw/"):
   if "F" in image:
      im = Image.open("data/raw/"+image)
      rgb_im = im.convert('RGB')
      R, G, B = rgb_im.getpixel((1, 1))
      res = (R+G+B)/3
      data.append(round(res, 2))


writer = csv.writer(open('data_rgb.csv', 'w+'))
writer.writerow(("filename", "rbg"))
for i in range(len(data)):
   writer.writerow((image_name[i], round(data[i], 2)))



#fig = plt.figure()
#ax = plt.subplot(111)
#ax.bar(range(len(image_name)), data, width=0.8)
#ax.set_xticklabels(np.arange(len(image_name))+0.8/2)
#ax.set_xticklabels(image_name, rotation=90)
#plt.show()

  



