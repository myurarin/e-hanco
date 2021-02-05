import os
import sys
import platform
from PIL import Image, ImageDraw, ImageFont

# フォントを選択
try:
    pf = platform.system()
    if pf == 'Linux':
        font_type = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
    else:
        # 対応するフォントが見つからないので
        raise Exception
except:
    print("フォントが見当たりません")
    exit()

font_size = 36

color_white = (255, 255, 255)
color_red = (255, 0, 0)
img_size = (300, 300)

hanco_img = Image.new('RGBA', (300, 300), color_white)
draw = ImageDraw.Draw(hanco_img)

#  ---------- ---------- ハンコ描画処理 ---------- ----------
# 外枠を作成
draw.ellipse((0, 0, 300, 300), fill=color_red, outline=color_red)
# 内枠を作成
draw.ellipse((10, 10, 290, 290), fill=color_white, outline=color_white)

# 線を作成
draw.line((10, 100, 290, 100), fill=color_red, width=10)
draw.line((10, 200, 290, 200), fill=color_red, width=10)

# テキストを入力
corp_font = ImageFont.truetype(font_type,font_size)
message = "株式会社○○"
w, h = draw.textsize(message, corp_font)
width = hanco_img.size[0]
height = hanco_img.size[1]
draw.text((((width - w)/2), 50), message, font=corp_font, fill=color_red)

date_font = ImageFont.truetype(font_type,40)
message = "２１．２．６"
w, h = draw.textsize(message, date_font)
width = hanco_img.size[0]
height = hanco_img.size[1]
draw.text((((width - w)/2), ((height - h)/2)), message, font=date_font, fill=color_red)

name_font = ImageFont.truetype(font_type,60)
message = "名前"
w, h = draw.textsize(message, name_font)
width = hanco_img.size[0]
height = hanco_img.size[1]
draw.text((((width - w)/2), 200), message, font=name_font, fill=color_red)

#  ---------- ---------- 透過処理 ---------- ----------
trans = Image.new('RGBA', hanco_img.size, (0, 0, 0, 0))
width = hanco_img.size[0]
height = hanco_img.size[1]
for x in range(width):
    for y in range(height):
        pixel = hanco_img.getpixel( (x, y) )
        
        if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
            continue
        
        trans.putpixel((x, y), pixel)

trans.save('hanco.png')