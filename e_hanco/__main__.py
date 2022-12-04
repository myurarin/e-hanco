import os
import sys
import platform
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk

# フォントを選択
try:
    pf = platform.system()
    if pf == 'Linux':
        font_type = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
    else:
        # 対応するフォントが見つからないので
        raise FileNotFoundError("対応するフォントが見つかりません")
except:
    print("フォントが見当たりません")
    exit()

font_size = 28

color_white = (255, 255, 255)
color_red = (255, 0, 0)
img_size = (300, 300)

hanco_img = Image.new('RGBA', (300, 300), color_white)


#  ---------- ---------- ハンコ描画処理 ---------- ----------
def hanco_drawing():
    global hanco_img

    draw = ImageDraw.Draw(hanco_img)
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

    date_font = ImageFont.truetype(font_type,36)
    message = "２１．１２．２６"
    w, h = draw.textsize(message, date_font)
    width = hanco_img.size[0]
    height = hanco_img.size[1]
    draw.text((((width - w)/2), ((height - h)/2)), message, font=date_font, fill=color_red)

    name_font = ImageFont.truetype(font_type,54)
    message = "名字　名前"
    w, h = draw.textsize(message, name_font)
    width = hanco_img.size[0]
    height = hanco_img.size[1]
    draw.text((((width - w)/2), 200), message, font=name_font, fill=color_red)

    # hanco_img.show()
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

    # trans.save('hanco.png')

def ButtonEvent(event):
    hanco_img.show()

def tk_window_init():
    global hanco_img
    root = tk.Tk()
    root.title(u"eHanco")
    root.geometry("400x300")
    root.resizable(width=False, height=False)

    # yomikomi_gazo = Image.open(hanco_img)
    hanco_img = hanco_img.resize((150, 150))
    yomikomi_gazo = ImageTk.PhotoImage(hanco_img)

    canvas = tk.Canvas(bg="black", width=hanco_img.height, height=hanco_img.width)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=yomikomi_gazo, anchor=tk.NW)

    EditBox1 = tk.Entry(width=20)
    EditBox1.insert(tk.END,"会社名")
    # EditBox1.place(x=5, y=10)
    EditBox1.pack()

    EditBox2 = tk.Entry(width=20)
    EditBox2.insert(tk.END,"日付")
    # EditBox2.place(x=5, y=10)
    EditBox2.pack()

    EditBox3 = tk.Entry(width=20)
    EditBox3.insert(tk.END,"名前")
    # EditBox2.place(x=5, y=10)
    EditBox3.pack()

    Button_1 = tk.Button(text=u'更新', width=10)
    Button_1.bind("<Button-1>",ButtonEvent) 
    Button_1.pack()

    Button_2 = tk.Button(text=u'出力', width=10)
    Button_2.bind("<Button-1>",ButtonEvent) 
    Button_2.pack()

    root.mainloop()

if __name__ == "__main__":
    hanco_drawing()
    tk_window_init()