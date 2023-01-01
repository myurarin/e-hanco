import os
import sys
import platform
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import time

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

CompanyBox = None
DateBox = None
NameBox = None
canvas = None


root = tk.Tk()
#  ---------- ---------- ハンコ描画処理 ---------- ----------


def hanco_drawing(
        company_name: str = "株式会社○○",
        seal_date: str = "22.12.5",
        seal_name: str = "名字 名前"):
    global hanco_img

    hanco_img = Image.new('RGBA', (300, 300), color_white)

    draw = ImageDraw.Draw(hanco_img)
    # 外枠を作成
    draw.ellipse((0, 0, 300, 300), fill=color_red, outline=color_red)
    # 内枠を作成
    draw.ellipse((10, 10, 290, 290), fill=color_white, outline=color_white)

    # 線を作成
    draw.line((10, 100, 290, 100), fill=color_red, width=10)
    draw.line((10, 200, 290, 200), fill=color_red, width=10)

    # テキストを入力
    corp_font = ImageFont.truetype(font_type, font_size)
    message = company_name
    w, h = draw.textsize(message, corp_font)
    width = hanco_img.size[0]
    height = hanco_img.size[1]
    draw.text((((width - w)/2), 50), message, font=corp_font, fill=color_red)

    date_font = ImageFont.truetype(font_type, 60)
    message = seal_date
    w, h = draw.textsize(message, date_font)
    width = hanco_img.size[0]
    height = hanco_img.size[1]
    draw.text((((width - w)/2), ((height - h)/2)),
              message, font=date_font, fill=color_red)

    name_font = ImageFont.truetype(font_type, 48)
    message = seal_name
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
            pixel = hanco_img.getpixel((x, y))

            if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                continue

            trans.putpixel((x, y), pixel)

    # trans.save('hanco.png')


def window_hanco_drawing():
    global hanco_img
    global canvas
    thumbnail = hanco_img.resize((150, 150))
    thumbnail = ImageTk.PhotoImage(thumbnail)
    canvas = tk.Canvas(bg="black", width=150, height=150)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=thumbnail, anchor=tk.NW)
    canvas.update()

    root.mainloop()


def button_event(event):
    global hanco_img
    command = str(event.widget["text"])
    if command == "update":
        global CompanyBox
        global DateBox
        global NameBox
        hanco_drawing(CompanyBox.get(), DateBox.get(), NameBox.get())
        window_hanco_drawing()
    if command == "save":
        hanco_img.show()


def tk_window_init():
    global hanco_img
    global CompanyBox
    global DateBox
    global NameBox
    global canvas
    global root

    root.title(u"eHanco")
    root.geometry("400x200")
    root.resizable(width=False, height=False)

    thumbnail = hanco_img.resize((150, 150))
    thumbnail = ImageTk.PhotoImage(thumbnail)
    canvas = tk.Canvas(bg="black", width=150,
                       height=150)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=thumbnail, anchor=tk.NW)

    CompanyBox = tk.Entry(width=10)
    CompanyBox.insert(tk.END, "会社名")
    CompanyBox.pack()

    DateBox = tk.Entry(width=10)
    DateBox.insert(tk.END, "日付")
    DateBox.pack()

    NameBox = tk.Entry(width=10)
    NameBox.insert(tk.END, "名前")
    NameBox.pack()

    Button = tk.Button(text='update', width=8)
    Button.bind("<ButtonPress>", button_event)
    Button.pack()

    Button = tk.Button(text='save', width=8)
    Button.bind("<ButtonPress>", button_event)
    Button.pack()

    root.mainloop()


if __name__ == "__main__":
    hanco_drawing()
    tk_window_init()
