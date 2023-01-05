import platform
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
from datetime import datetime

from e_hanco import hanco

DT_NOW = datetime.now()


class hanco_gui:

    # フォント関連設定値
    font_type: str = ""      # フォントタイプ
    font_size: int = 0       # フォントサイズ
    # 画像設定値
    img_size: tuple = (300, 300)
    # ハンコ画像
    hanco_img = None
    # 各Box
    tk_company_box = None     # 社名テキスト
    tk_date_box = None        # 日付テキスト
    tk_name_box = None        # 名前テキスト
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
            raise Exception("対応するプラットフォームではありません")

        # 判子を初期化
        self.hanco_img = hanco.drawing(self.font_type)

    def hanco_thumbnail_update(self):
        thumbnail = self.hanco_img.resize((150, 150))
        thumbnail = ImageTk.PhotoImage(thumbnail)
        self.canvas = tk.Canvas(bg="white", width=150, height=150)
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=thumbnail, anchor=tk.NW)
        self.canvas.update()

        self.root.mainloop()

    def hanco_save(self):
        # pathを指定
        save_file_path = filedialog.asksaveasfile(
            title="名前を付けて判子を保存",
            filetypes=[("PNG", ".png")],
            initialdir="./",
            defaultextension="png"
        )

        # 保存先を指定した場合は保存処理を実行する
        if save_file_path is not None:
            self.hanco_img.save(save_file_path.name)

    def button_event(self, event):
        command = str(event.widget["text"])
        if command == "update":
            self.hanco_img = hanco.drawing(
                self.font_type,
                company_name=self.tk_company_box.get(),
                seal_date=self.tk_date_box.get(),
                seal_name=self.tk_name_box.get())
            self.hanco_thumbnail_update()
        if command == "save":
            self.hanco_save()

    def tk_init(self):
        self.root.title(u"e-Hanco")
        self.root.geometry("300x200")
        self.root.resizable(width=False, height=False)

        # フレームの作成
        frame_left = tk.Frame(self.root)
        frame_right = tk.Frame(self.root)

        thumbnail = self.hanco_img.resize((150, 150))
        thumbnail = ImageTk.PhotoImage(thumbnail)
        self.canvas = tk.Canvas(bg="white", width=150,
                                height=150)
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=thumbnail, anchor=tk.NW)
        self.canvas.pack(in_=frame_left)

        self.tk_company_box = tk.Entry(width=12)
        self.tk_company_box.insert(tk.END, "会社名")
        self.tk_company_box.pack(in_=frame_right)

        self.tk_date_box = tk.Entry(width=12)
        self.tk_date_box.insert(tk.END, f"日付")
        self.tk_date_box.pack(in_=frame_right)

        self.tk_name_box = tk.Entry(width=12)
        self.tk_name_box.insert(tk.END, "名前")
        self.tk_name_box.pack(in_=frame_right)

        Button = tk.Button(text='update', width=8)
        Button.bind("<ButtonPress>", self.button_event)
        Button.pack(in_=frame_right)

        Button = tk.Button(text='save', width=8)
        Button.bind("<ButtonPress>", self.button_event)
        Button.pack(in_=frame_right)

        frame_left.pack(side=tk.LEFT, expand=True)
        frame_right.pack(side=tk.RIGHT, expand=True)

        self.root.mainloop()
