import os
import ctypes
from PIL import Image, ImageDraw, ImageFont

resolution = (1920, 1080)

photoname = 'base.jpg'

msglist = ["Note",
           "Note",
           "Note",
           "Note"]

img = Image.new('RGB', resolution, (0, 0, 0))  # 新建画布对象

draw = ImageDraw.Draw(img)  # 新建画布绘画对象

myfont = ImageFont.truetype('simhei.ttf', 100)  # 定义字体

W, H = resolution

l = len(msglist)

i = 0

for msg in msglist:
    w, h = draw.textsize(msg, myfont)

    draw.text((W/5, (H-h)/4+(H-h)/2/l*i), msg, (255, 255, 255),
              font=myfont, align='center')  # 居中文本

    i = i + 1

img.save(photoname)

path = os.path.join(os.getcwd(), photoname)

ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
