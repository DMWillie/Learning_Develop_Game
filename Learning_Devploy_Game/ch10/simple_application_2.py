"""
    作者:北辰
    日期:09/06/2019
    功能:简单GUI程序--第2步,利用面向对象编程
"""

from tkinter import Tk, Label, Button, LEFT, RIGHT

class MyGame:
    def __init__(self, mainwin):
        lbl = Label(mainwin, text="Hello World!", bg='yellow')
        exit_button = Button(mainwin, text='Exit',
                             command=self.exit_btn_callback)
        # pack the widgets
        lbl.pack(side=LEFT)
        exit_button.pack(side=RIGHT)

    def exit_btn_callback(self):
        """Callback function to handle the button click event."""
        mainwin.destroy()

if __name__ == '__main__':
    # Create the main window or Tk instance.
    mainwin = Tk()
    mainwin.geometry("140x40")  # 将大小指定为宽*高
    game_app = MyGame(mainwin)
    mainwin.mainloop()