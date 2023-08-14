from PIL import Image
import numpy as np
import math


original = Image.open("flag_enc.png")
original = np.array(original)
width = original.shape[0]
height = original.shape[1]
original = original.flatten()

# extract the LSBs
lsbs = []
for i in range(len(original)):
    lsbs.append(original[i] & 1)

# convert to bytes
lsbs = np.array(lsbs)
lsbs = np.packbits(lsbs)

# convert to string
lsbs = lsbs.tobytes()
print(lsbs)


