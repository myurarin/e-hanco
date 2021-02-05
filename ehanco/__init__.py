import os
import sys
import platform
from PIL import Image, ImageDraw

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

color_white = (255, 255, 255)
color_red = (255, 0, 0)

hanco_img = Image.new('RGB', (300, 300), color_white)
draw = ImageDraw.Draw(hanco_img)

# 外枠を作成
draw.ellipse((0, 0, 300, 300), fill=color_red, outline=color_red)
# 内枠を作成
draw.ellipse((10, 10, 290, 290), fill=color_white, outline=color_white)

draw.line((10, 100, 290, 100), fill=color_red, width=10)
draw.line((10, 200, 290, 200), fill=color_red, width=10)

hanco_img.show()
# hanco_img.save('hanco.jpg', quality=95)