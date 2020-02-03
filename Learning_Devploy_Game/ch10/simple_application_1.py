"""
    作者:北辰
    日期:09/06/2019
    功能:简单GUI程序--第1步
"""

from tkinter import Tk, Label, Button, LEFT, RIGHT

if __name__ == '__main__':
    # Create the main window or Tk instance.
    mainwin = Tk()
    mainwin.geometry("140x40")  # 将大小指定为宽*高
    # Create a label widget and 'pack' it in a row (or column)
    lbl = Label(mainwin, text="Hello World!", bg='yellow')
    lbl.pack(side=LEFT)
    # 'Exit' button that calls mainwin.destory when clicked
    exit_button = Button(mainwin, text='Exit', command=mainwin.destroy)
    exit_button.pack(side=RIGHT)
    mainwin.mainloop()