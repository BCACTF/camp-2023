'''
@author Mudasir

some util functions to generate flag and copy it to video
'''

from PIL import Image, ImageDraw, ImageFont

FLAG = 'camp{wH@7s_an_3xTr@_f!l3_aNYw@y$_r3dhi8ib28bf}'

def generate_flag():
    img = Image.new('RGB', (600, 100), color = (0, 0, 0))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('arial.ttf', 20)
    d.text((40,30), FLAG, font=fnt, fill=(255,255,255))
    img.save('flag.png')

def copy_img_to_video():
    with open('flag.png', 'rb') as f:
        flag = f.read()
        with open('funnyfile', '+ab') as f2:
            f2.write(flag)

generate_flag()
copy_img_to_video()