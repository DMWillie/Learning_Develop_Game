"""
    作者:北辰
    日期:13/06/2019
    功能:简单GUI程序,使用bind()方法代替命令回调
"""

from tkinter import Tk, Label, Button, LEFT, RIGHT

def exit_btn_callback(evt):
    """Callback function to handle the button click event."""
    print("Inside exit_btn_callback. Event object is: ",evt)
    mainwin.destory()

if __name__ == '__main__':
    # Create the main window or Tk instance.
    mainwin = Tk()
    mainwin.geometry("140x40")
    # Create a label widget and 'pack' it in a row (or column)
    lbl = Label(mainwin, text="Hello World!", bg='yellow')
    lbl.pack(side=LEFT)
    exit_button = Button(mainwin,text="Exit")
    # Bind the button click event to function exit_btn_callback
    exit_button.bind("<Button-1>",exit_btn_callback)
    exit_button.pack(side=RIGHT)

    mainwin.mainloop()