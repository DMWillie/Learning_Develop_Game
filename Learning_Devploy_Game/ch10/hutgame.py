"""
    作者:北辰
    日期:14/06/2019
    功能:兽人之袭GUI程序
    版本:10.0.0
"""

from tkinter import Tk, Label, Radiobutton, PhotoImage, IntVar
from tkinter import messagebox
import random

class HutGame:
    def __init__(self, parent):
        """A game where the player selects a hut where 'Sir Foo' to rest...
        The program initially puts 'enemy' or a 'friend' inside each hut.
        Some huts could also be left 'unoccupied'. You are asked to select
        a hut. You win if the hut occupant is either a 'friend' OR if the
        hut is not occupied,

        :param parent: The parent tkinter widget.
        :ivar list huts: List to store occupant types (as strings)
        :ivar int hut_width: The width of the application window in pixels.
        :ivar int hut_height: The height of the application window in pixels
        :ivar PhotoImage village_image: Background image for the app
        :ivar PhotoImage hut_image: The hut image for the radio buttons.
        :ivar Tk container: The main widget serving as a parent for others.
               In this example it is just the main Tk instance.
        :ivar str result: The string to declare the result via a messagebox.
        """
        self.village_image = PhotoImage(file="D:\pythonCode\Learning_Devploy_Game\ch10\Jungle_small.gif")
        self.hut_image = PhotoImage(file="D:\pythonCode\Learning_Devploy_Game\ch10\Hut_small.gif")
        self.hut_width = 40
        self.hut_height = 56
        self.container = parent

        self.huts = []
        self.result = ""
        # The preparatory work that populates the self.huts list
        # (no UI involved)
        self.occupy_huts()
        # Setup the user interface
        self.setup()

    def occupy_huts(self):
        """Randomly occupy the huts: enemy or friend or keep unoccupied."""
        occupants = ['enemy', 'friend', 'unoccupied']
        while len(self.huts) < 5:
            computer_choice = random.choice(occupants)
            self.huts.append(computer_choice)
        # Alternatively you can also use list comprehension like so:
        # self.huts = [random.choice(occupants) for _ in range(5)]
        print("Hut occupants are:",self.huts)

    def create_widgets(self):
        """Create various widgets in the tkinter main window."""
        self.var = IntVar() # 整数变量类
        self.background_label = Label(self.container,
                                      image=self.village_image)
        txt = "Select a hut to enter. You win if:\n"
        txt += "The hut is unoccupied or the occupant is a friend!"
        self.info_label = Label(self.container, text=txt, bg='yellow')
        # Create a dictionary for radio button config options.
        r_btn_config = { 'variable':self.var,
            'bg': '#A8884C',
            'activebackground': 'yellow',
            'image' : self.hut_image,
            'height': self.hut_height,
            'width': self.hut_width,
            'command': self.radio_btn_pressed }
        self.r1 = Radiobutton(self.container, r_btn_config, value=1)
        self.r2 = Radiobutton(self.container, r_btn_config, value=2)
        self.r3 = Radiobutton(self.container, r_btn_config, value=3)
        self.r4 = Radiobutton(self.container, r_btn_config, value=4)
        self.r5 = Radiobutton(self.container, r_btn_config, value=5)

    # Handle Events
    def radio_btn_pressed(self):
        """Command callback when radio button is pressed...."""
        self.enter_hut(self.var.get())

    def enter_hut(self, hut_number):
        """Enter the selected hut and determine the winner...."""
        print("Entering hut #:",hut_number)
        hut_occupant = self.huts[hut_number-1]
        print("Hut occupant is: ", hut_occupant)

        if hut_occupant == 'enemy':
            self.result = "Enemy sighted in Hut # %d \n\n" % hut_number
            self.result += "YOU LOSE :( Better luck next time!"
        elif hut_occupant == 'unoccupied':
            self.result = "Hut # %d is unoccupied\n\n" % hut_number
            self.result += "Congratulations! YOU WIN!!!"
        else:
            self.result = "Friend sighted in Hut # %d \n\n" % hut_number
            self.result += "Congratulations! YOU WIN!!!"

        # Announce the winner!
        self.announce_winner(self.result)

    def announce_winner(self, data):
        """Declare the winner by displaying a tkinter messagebox...."""
        messagebox.showinfo("Winner Announcement", message=data)

    def setup(self):
        """Calls methods to setuo the user interface."""
        self.create_widgets()
        self.setup_layout()

    def setup_layout(self):
        """Use the grid geometry manager to place widgets."""
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(4, weight=1)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.info_label.grid(row=0, column=0, columnspan=5, sticky='nsew')
        self.r1.grid(row=1, column=0)
        self.r2.grid(row=1, column=4)
        self.r3.grid(row=2, column=3)
        self.r4.grid(row=3, column=0)
        self.r5.grid(row=4, column=4)

if __name__ == '__main__':
    # Create Tk instance. This is popularly called 'root' But let's
    # call it mainwin (the 'main window' of the application. )
    mainwin = Tk()
    WIDTH = 494
    HEIGHT = 307
    mainwin.geometry("%sx%s" % (WIDTH, HEIGHT))
    mainwin.resizable(0, 0)
    mainwin.title("Attack of the Orcs Game")
    game_app = HutGame(mainwin)
    mainwin.mainloop()