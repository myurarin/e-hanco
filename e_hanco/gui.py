import os
import sys
import platform
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import time


class hanco_gui:

    # フォント関連設定値
    font_type: str = ""      # フォントタイプ
    font_size: int = 0       # フォントサイズ
    # 色設定値
    color_white: tuple = (255, 255, 255)  # 白設定値
    color_red: tuple = (255, 0, 0)
    # 画像設定値
    img_size: tuple = (300, 300)
    # ハンコ画像
    hanco_img = Image.new('RGBA', img_size, color_white)
    # 各Box内のテキスト値
    tk_company_box_txt: str = ""     # 社名テキスト
    tk_date_box_txt: str = ""        # 日付テキスト
    tk_name_box_txt: str = ""        # 名前テキスト
    # GUI表示画像
    canvas = None
    # tkinter root
    root = tk.Tk()

    def __init__(self) -> None:

        # フォントの選択
        pf = platform.system()
        if pf == 'Linux':
            self.font_type = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
        else:
            # 対応するフォントが見つからないので
            raise FileNotFoundError("対応するフォントが見つかりません")
