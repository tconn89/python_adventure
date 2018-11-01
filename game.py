from tkinter import *

class Window(Frame):
    def __init__(self, master=none):
        Frame.__init__(self, master)
        quitButton = Button(self, text="Quit",command=quit)
        lbl = Label(self,text="Bail out!")

        self.master = master
        def init_window(self):
            quitButton.pack()
            lbl.pack()
            self.master.title("Nice Try, Ty!")
            self.pack(fill=BOTH, expand=1)
            print('Game Started')
        init_window(self)

root = Tk()
root.geometry("800x600")
app = Window(root)
app.__init__

root.mainloop()
