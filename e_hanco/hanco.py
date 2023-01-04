from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

DT_NOW = datetime.now()

COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

def drawing(
        font_type: str,
        img_size: tuple = (300, 300),
        company_name: str = "株式会社○○",
        seal_date: str = f"{DT_NOW.year}.{DT_NOW.month}.{DT_NOW.day}",
        seal_name: str = "名字 名前") -> Image.Image:
    hanco_img = Image.new('RGBA', img_size, COLOR_WHITE)

    draw = ImageDraw.Draw(hanco_img)
    # 外枠を作成
    draw.ellipse((0, 0, 300, 300), fill=COLOR_RED, outline=COLOR_RED)
    # 内枠を作成
    draw.ellipse((10, 10, 290, 290), fill=COLOR_WHITE, outline=COLOR_WHITE)

    # 線を作成
    draw.line((10, 100, 290, 100), fill=COLOR_RED, width=10)
    draw.line((10, 200, 290, 200), fill=COLOR_RED, width=10)

    # テキストを入力
    corp_font = ImageFont.truetype(font_type, 28)
    w, h = draw.textsize(company_name, corp_font)
    width = hanco_img.size[0]
    height = hanco_img.size[1]
    draw.text((((width - w)/2), 50), company_name, font=corp_font, fill=COLOR_RED)

    date_font = ImageFont.truetype(font_type, 60)
    w, h = draw.textsize(seal_date, date_font)
    width = hanco_img.size[0]
    height = hanco_img.size[1]
    draw.text((((width - w)/2), ((height - h)/2)),
              seal_date, font=date_font, fill=COLOR_RED)

    name_font = ImageFont.truetype(font_type, 48)
    w, h = draw.textsize(seal_name, name_font)
    width = hanco_img.size[0]
    height = hanco_img.size[1]
    draw.text((((width - w)/2), 200), seal_name, font=name_font, fill=COLOR_RED)

    #  ---------- ---------- 透過処理 ---------- ----------
    trans = Image.new('RGBA', hanco_img.size, (0, 0, 0, 0))
    width = hanco_img.size[0]
    height = hanco_img.size[1]
    for x in range(width):
        for y in range(height):
            pixel = hanco_img.getpixel((x, y))

            if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                continue

            trans.putpixel((x, y), pixel)

    return trans

if __name__ == "__main__":
    pil_img = drawing("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")
    print(pil_img)
    pil_img.show()