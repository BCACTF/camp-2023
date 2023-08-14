from PIL import Image
import numpy as np

original = Image.open("flag.png")
original = np.array(original)
width = original.shape[0]
height = original.shape[1]
original = original.flatten()

flagfile = open("flag.txt", "r")
flag = flagfile.read()
flagfile.close()

flag = [ord(c) for c in flag]
flag = np.array(flag, dtype=np.uint8)
flagbits = np.unpackbits(flag)
mod = []

# embed the flag into the least significant bits of the image
for i in range(len(original)):
    if i < len(flagbits):
        mod.append((original[i] & ~1) | flagbits[i])
    else:
        mod.append(original[i])
    
mod = np.array(mod, dtype=np.uint8)
mod = np.reshape(mod, (width, height, 3))
mod = Image.fromarray(mod)
mod.save("flag_enc.png")
