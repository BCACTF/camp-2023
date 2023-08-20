'''
@author Mudasir

some util function(s) to generate flag and copy it to video
'''

from PIL import Image, ImageDraw, ImageFont
import io

FLAG = 'camp{wH@7s_an_3xTr@_f!l3_aNYw@y$_r3dhi8ib28bf}'

def generate_flag():
    final_bytes = io.BytesIO()
    img = Image.new('RGB', (600, 100), color = (0, 0, 0))
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('arial.ttf', 20)
    d.text((40,30), FLAG, font=fnt, fill=(255,255,255))
    # img.save('flag.png')
    img.save(final_bytes, format='PNG')
    final_bytes = final_bytes.getvalue()

    with open('funfile', '+ab') as f2:
        f2.write(final_bytes)

generate_flag()