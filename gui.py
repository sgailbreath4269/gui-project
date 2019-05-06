from tkinter import *


class myApp:

    def __init__(self, myMaster):
        self.buttons_frame = Frame(myMaster)
        self.buttons_frame.pack()
        button_width = 25
        buttons_frame_padx = "3m"
        buttons_frame_pady = "2m"
        buttons_frame_ipadx = "3m"
        buttons_frame_ipady = "1m"

        self.buttons_frame = Frame(myMaster)
        self.buttons_frame.pack(
            side=TOP,
            ipadx=buttons_frame_ipadx,
            ipady=buttons_frame_ipady,
            padx=buttons_frame_padx,
            pady=buttons_frame_pady)

        self.top_buttons_frame = Frame(self.buttons_frame)
        self.top_buttons_frame.pack(side=TOP)

        self.bottom_buttons_frame = Frame(self.buttons_frame)
        self.bottom_buttons_frame.pack(side=BOTTOM)

        self.text1 = Label(self.top_buttons_frame, text="greeting/farewell language converter gui")
        self.text1.pack()

        self.text2 = Label(self.top_buttons_frame, text="type 'hello' or 'goodbye'")
        self.text2.pack()

        self.e = Entry(self.top_buttons_frame)
        self.e.pack()

        self.e.focus_set()

        self.v = IntVar()
        self.v.set(0)

        self.rad1 = Radiobutton(self.bottom_buttons_frame,
                                text="English to Spanish",
                                variable=self.v,
                                value=1)
        self.rad2 = Radiobutton(self.bottom_buttons_frame,
                                text="English to German",
                                variable=self.v,
                                value=2)
        self.rad3 = Radiobutton(self.bottom_buttons_frame,
                                text="English to French",
                                variable=self.v,
                                value=3)
        self.rad4 = Radiobutton(self.bottom_buttons_frame,
                                text="English to Norwegian",
                                variable=self.v,
                                value=4)

        self.rad1.pack()
        self.rad1.select()
        self.rad2.pack()
        self.rad2.deselect()
        self.rad3.pack()
        self.rad3.deselect()
        self.rad4.pack()
        self.rad4.deselect()

        self.button1 = Button(self.bottom_buttons_frame)
        self.button1.configure(text="convert", background="turquoise")
        self.button1["width"] = button_width
        self.button1.pack()
        self.button1.focus_force()
        self.button1.bind("<Button-1>", self.button1Click)

        self.text3 = Label(self.bottom_buttons_frame, text="Converted greeting/farewell below")
        self.text3.pack()

        self.text4 = Label(self.bottom_buttons_frame, text="")
        self.text4.pack()

    def button1Click(self, event):
        getv = self.v.get()
        gete = self.e.get()
        num = ""
        if getv == 1:
            if self.e.get() == 'hello':
                new = 'hola'
            elif self.e.get() == 'goodbye':
                new = 'adios'

        elif getv == 2:
            if self.e.get() == 'hello':
                new = 'hallo'
            elif self.e.get() == 'goodbye':
                new ='auf wiedersehen'

        elif getv == 3:
            if self.e.get() == 'hello':
                new = 'bonjour'
            elif self.e.get() == 'goodbye':
                new = 'au revoir'

        elif getv == 4:
            if self.e.get() == 'hello':
                new = 'hallo'
            elif self.e.get() == 'goodbye':
                new = 'ha det'

        self.text4.configure(text=new)


def main():
    root = Tk()
    myapp = myApp(root)
    root.mainloop()


main()
