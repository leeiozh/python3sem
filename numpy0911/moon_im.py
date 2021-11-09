from PIL import Image
import numpy as np

img = Image.open("lunar03_raw.jpg")
data = np.array(img)

minimum, maximum = np.min(data), np.max(data)
m = 255. / (maximum - minimum)
b = 0. - m * minimum
data = data * m
data += b

res_img = Image.fromarray(data.astype(np.uint8))
res_img.save("lunar03_new.jpg")
