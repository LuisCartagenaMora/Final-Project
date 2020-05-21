"""
Luis G. Cartagena Mora
#108370
CECS-3210
Seccion 21
SP-20
-------------------------------------
This program consists of a GUI called Custom Sneakers
where the user will be able to build their own
sneakers whether it be a word the user wants to
embed on the side of the sneaker or change the color of
any part of the sneaker.
"""

from tkinter import *
import turtle
from tkinter.ttk import Combobox
from tkinter.ttk import Entry
from tkinter.ttk import Button
from tkinter.ttk import Label

from ttkthemes import themed_tk as tk


class Sneaker:
    """ class Sneaker: Contains the methods that allow the user
        whether to press "START" or "QUIT". """

    def quit_program(self):
        """quit_program: Exits program"""
        root.destroy()
        exit()

    def quit_selection(self):
        """quit_selection: Erases all onscreen widgets"""
        widget.radiobutton1.pack_forget()
        widget.radiobutton2.pack_forget()
        widget.radiobutton3.pack_forget()
        widget.color_label1.pack_forget()
        widget.color_label2.pack_forget()
        widget.color_label3.pack_forget()
        widget.color_label4.pack_forget()
        widget.color_label5.pack_forget()
        widget.instruction_label1.pack_forget()
        widget.instruction_label2.pack_forget()
        widget.instruction_label3.pack_forget()
        widget.material_label1.pack_forget()
        widget.material_label2.pack_forget()
        widget.material_label3.pack_forget()
        widget.material_label4.pack_forget()
        widget.material_label5.pack_forget()
        widget.entry1.pack_forget()
        widget.entry2.pack_forget()
        widget.entry3.pack_forget()
        widget.entry4.pack_forget()
        widget.entry5.pack_forget()
        widget.combo1.pack_forget()
        widget.combo2.pack_forget()
        widget.combo3.pack_forget()
        widget.combo4.pack_forget()
        widget.combo5.pack_forget()
        # widget.exit_button.destroy()
        widget.color_button1.pack_forget()
        widget.color_button2.pack_forget()
        widget.color_button3.pack_forget()
        widget.color_button4.pack_forget()
        widget.color_button5.pack_forget()

        widget.overview()


class Design:
    """class Design: Contains methods used to draw 3 styles of sneaker.
                     Low-Top, Mid-Top and High-Top"""
    def style1_clicked(self):
        """method style1_clicked: When selected will draw design.
            If deselected, destroys drawing and replaces with next choice."""
        t.reset()
        self.drawing1()

    def style2_clicked(self):
        """method style2_clicked: When selected will draw design.
            If deselected, destroys drawing and replaces with next choice."""
        t.reset()
        self.drawing2()

    def style3_clicked(self):
        """method style3_clicked: When selected will draw design.
            If deselected, destroys drawing and replaces with next choice."""
        t.reset()
        self.drawing3()

    def drawing1(self):
        """method drawing1: drawing1 will contain the drawing for the low-top sneaker."""
        lbl = Label(canvas, text="Low - Top").place(x=165, y=270)
        # Hides turtle from user.
        t.hideturtle()

        # Draws low-top sneaker sole.
        # Colors in parameter will by the user's choice.
        widget.sole_color()
        t.begin_fill()

        t.penup()
        t.goto(100, 0)
        t.pendown()
        for i in range(2):
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(200)
        t.end_fill()

        # Draw low-top sneaker outsole.
        # Colors in parameter will by the user's choice.
        widget.outsole_color()
        t.begin_fill()
        for i in range(2):
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(50)
        t.end_fill()

        # Draws low-top sneaker toebox.
        # Colors in parameter will by the user's choice.
        widget.toebox_color()
        t.begin_fill()
        t.left(110)
        t.forward(40)
        t.left(140)
        t.forward(40)
        t.left(110)
        t.forward(27)
        t.end_fill()

        # Draws upper layer of low-top sneaker.
        # Colors in parameter will by the user's choice.
        widget.upper_color()
        t.begin_fill()
        t.goto(73, 0)
        t.left(70)
        t.forward(39)
        t.left(90)
        t.forward(100)
        t.left(110)
        t.forward(15)
        t.right(90)
        t.forward(92)
        t.left(90)
        t.forward(56)
        t.left(90)
        t.forward(173)
        t.end_fill()

        # Draws low-top sneaker heel.
        # Colors in parameter will by the user's choice.
        t.penup()
        t.goto(-99.5, 40)
        t.pendown()
        widget.heel_color()
        t.begin_fill()
        for i in range(10):
            t.right(i + 3)
            t.forward(i + 1.7)
        t.right(105)
        t.forward(42)
        t.right(90)
        t.forward(47)
        t.end_fill()

    def drawing2(self):
        """method drawing2: drawing1 will contain the drawing for the mid-top sneaker."""
        Label(canvas, text="Mid - Top").place(x=165, y=270)
        t.hideturtle()
        widget.sole_color()
        t.begin_fill()

        t.penup()
        t.goto(100, 0)
        t.pendown()
        for i in range(2):
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(200)
        t.end_fill()

        # Draw low-top sneaker outsole.
        # Colors in parameter will by the user's choice.
        widget.outsole_color()
        t.begin_fill()
        for i in range(2):
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(50)
        t.end_fill()

        # Draws low-top sneaker toebox.
        # Colors in parameter will by the user's choice.
        widget.toebox_color()
        t.begin_fill()
        t.left(110)
        t.forward(40)
        t.left(140)
        t.forward(40)
        t.left(110)
        t.forward(27)
        t.end_fill()

        # Draws upper layer of low-top sneaker.
        # Colors in parameter will by the user's choice.
        widget.upper_color()
        t.begin_fill()
        t.goto(73, 0)
        t.left(70)
        t.forward(39)
        t.left(90)
        t.forward(110)
        t.left(20)
        t.forward(83)
        t.left(90)
        t.forward(74)
        t.left(90)
        t.forward(173)
        t.end_fill()

        # Draws low-top sneaker heel.
        # Colors in parameter will by the user's choice.
        t.penup()
        t.goto(-99.5, 40)
        t.pendown()
        widget.heel_color()
        t.begin_fill()
        for i in range(10):
            t.right(i + 3)
            t.forward(i + 1.7)
        t.right(105)
        t.forward(42)
        t.right(90)
        t.forward(47)
        t.end_fill()


    def drawing3(self):
        """method drawing3: drawing1 will contain the drawing for the high-top sneaker."""
        lbl = Label(canvas, text="High-Top").place(x=165, y=270)
        # lbl.pack()
        t.hideturtle()
        # Draws high-top sneaker sole.
        widget.sole_color()
        t.begin_fill()
        t.penup()
        t.goto(100, 0)
        t.pendown()
        for i in range(2):
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(200)
        t.end_fill()

        # Draw mid-top sneaker outsole.
        widget.outsole_color()
        t.begin_fill()
        for i in range(2):
            t.right(90)
            t.forward(25)
            t.right(90)
            t.forward(50)
        t.end_fill()

        # Draws high-top sneaker toebox.
        widget.toebox_color()
        t.begin_fill()
        t.left(110)
        t.forward(40)
        t.left(140)
        t.forward(40)
        t.left(110)
        t.forward(27)
        t.end_fill()

        # Draws upper layer of high-top sneaker.
        widget.upper_color()
        t.begin_fill()
        t.goto(73, 0)
        t.left(70)
        t.forward(39)
        t.left(90)
        t.forward(100)
        t.right(70)
        t.forward(74)
        t.left(90)
        t.forward(92)
        t.left(90)
        t.forward(98)
        t.left(90)
        for i in range(12):
            t.right(i+0.9)
            t.forward(i+0.8)
        t.left(77)
        t.forward(123)
        t.end_fill()

        # Draw high-top sneaker heel
        t.penup()
        t.goto(-100, 47)
        t.pendown()
        widget.heel_color()
        t.begin_fill()
        for i in range(12):
            t.right(i + 0.9)
            t.forward(i + 0.8)
        t.right(103)
        t.forward(51)
        t.right(90)
        t.forward(47)
        t.end_fill()


class Widget:

    def __init__(self):
        """__init__: Initializes the window object."""
        frame_style = Frame(root, bg="black")
        frame_style.pack(side=LEFT, padx=15)
        frame_material = Frame(root, bg="black")
        frame_material.pack(side=LEFT, anchor=CENTER, padx=15, pady=15)
        frame_color = Frame(root, bg="black")
        frame_color.pack(side=LEFT, padx=15, pady=15)

        # Creates the widgets used to select a sneaker style
        self.instruction_label3 = Label(frame_style, text="Pick a style:")
        self.instruction_label3.pack()
        self.radiobutton1 = Button(frame_style, text="Low-Top", command=design.style1_clicked)
        self.radiobutton1.pack(pady=10)

        self.radiobutton2 = Button(frame_style, text="Mid-Top", command=design.style2_clicked)
        self.radiobutton2.pack(pady=10)

        self.radiobutton3 = Button(frame_style, text="High-Top", command=design.style3_clicked)
        self.radiobutton3.pack(pady=10)

        # Creates the "Pick a material" widget.
        self.instruction_label2 = Label(frame_material, text="Pick a material:")
        self.instruction_label2.pack(pady=5)
        self.material_label1 = Label(frame_material, text="Sole")
        self.material_label1.pack()
        self.materials = ["Rubber", "Polyurethane", "PVC"]
        self.combo1 = Combobox(frame_material, values=self.materials, state="readonly")
        self.combo1.bind("<<ComboboxSelected>>", self.sole_material)
        self.combo1.pack(pady=5)

        self.material_label2 = Label(frame_material, text="Outsole")
        self.material_label2.pack()
        self.materials = ["Rubber", "Polyurethane"]
        self.combo2 = Combobox(frame_material, values=self.materials, state="readonly")
        self.combo2.bind("<<ComboboxSelected>>", self.outsole_material)
        self.combo2.pack(pady=5)

        self.material_label3 = Label(frame_material, text="Toebox")
        self.material_label3.pack()
        self.materials = ["Polyester", "Cotton", "Leather", "Suede"]
        self.combo3 = Combobox(frame_material, values=self.materials, state="readonly")
        self.combo3.bind("<<ComboboxSelected>>", self.toebox_material)
        self.combo3.pack(pady=5)

        self.material_label4 = Label(frame_material, text="Upper")
        self.material_label4.pack()
        self.materials = ["Polyester", "Cotton", "Leather", "Suede"]
        self.combo4 = Combobox(frame_material, values=self.materials, state="readonly")
        self.combo4.bind("<<ComboboxSelected>>", self.upper_material)
        self.combo4.pack(pady=5)

        self.material_label5 = Label(frame_material, text="Heel")
        self.material_label5.pack()
        self.materials = ["Polyester", "Cotton", "Leather", "Suede"]
        self.combo5 = Combobox(frame_material, values=self.materials, state="readonly")
        self.combo5.bind("<<ComboboxSelected>>", self.heel_material)
        self.combo5.pack()

        # Creates the widgets used to pick a color.
        self.instruction_label1 = Label(frame_color, text="Pick a color:")
        self.instruction_label1.pack(pady=5)
        self.color_label1 = Label(frame_color, text="Sole")
        self.color_label1.pack()
        self.entry1 = Entry(frame_color)
        self.entry1.pack(pady=5)
        self.color_button1 = Button(frame_color, text="Enter", command=self.sole_color)
        # self.color_button1.pack()

        self.color_label2 = Label(frame_color, text="Outsole")
        self.color_label2.pack()
        self.entry2 = Entry(frame_color)
        self.entry2.pack(pady=5)
        self.color_button2 = Button(frame_color, text="Enter", command=self.outsole_color)
        # self.color_button2.pack()

        self.color_label3 = Label(frame_color, text="Toebox")
        self.color_label3.pack()
        self.entry3 = Entry(frame_color)
        self.entry3.pack(pady=5)
        self.color_button3 = Button(frame_color, text="Enter", command=self.toebox_color)
        # self.color_button3.pack()

        self.color_label4 = Label(frame_color, text="Upper")
        self.color_label4.pack()
        self.entry4 = Entry(frame_color)
        self.entry4.pack(pady=5)
        self.color_button4 = Button(frame_color, text="Enter", command=self.upper_color)
        # self.color_button4.pack()

        self.color_label5 = Label(frame_color, text="Heel")
        self.color_label5.pack()
        self.entry5 = Entry(frame_color)
        self.entry5.pack(pady=5)
        self.color_button5 = Button(frame_color, text="Enter", command=self.heel_color)
        # self.color_button5.pack()

        # Creates a button used to pass to the review screen
        Button(canvas, text="NEXT", command=sneaker.quit_selection).place(x=315, y=270)



    def sole_color(self):
        """method sole_color: Colors the sole of the sneaker."""
        color1 = self.entry1.get()
        t.color("black", color1)

    def outsole_color(self):
        """method outsole_color: Colors the outsole of the sneaker."""
        color2 = self.entry2.get()
        t.color("black", color2)

    def toebox_color(self):
        """method toebox_color: Colors the toebox of the sneaker."""
        color3 = self.entry3.get()
        t.color("black", color3)

    def upper_color(self):
        """method upper_color: Colors the upper section of the sneaker."""
        color4 = self.entry4.get()
        t.color("black", color4)

    def heel_color(self):
        """method heel_color: Colors the heel of the sneaker."""
        color5 = self.entry5.get()
        t.color("black", color5)

    def sole_material(self, event):
        """method sole_material: Gets the material chosen for the sole of the sneaker."""
        self.material1 = self.combo1.get()

    def outsole_material(self, event):
        """method outsole_material: Gets the material chosen for the outsole of the sneaker."""
        self.material2 = self.combo2.get()

    def toebox_material(self, event):
        """method toebox_material: Gets the material chosen for the toebox of the sneaker."""
        self.material3 = self.combo3.get()

    def upper_material(self, event):
        """method upper_material: Gets the material chosen for the upper section of the sneaker."""
        self.material4 = self.combo4.get()

    def heel_material(self, event):
        """method heel_material: Gets the material chosen for the heel of the sneaker."""
        self.material5 = self.combo5.get()

    def overview(self):
        """method overview: Lets the user see what materials were chosen for each
                            individual section of the sneaker."""
        self.final_label = Label(root, text="Materials of the final product.")
        self.final_label.pack()
        self.final_label.place(x=140, y=310)

        self.final_label = Label(root, text="Sole:")
        self.final_label.pack()
        self.final_label.place(x=160, y=330)
        self.final_label = Label(root, text=self.material1)
        self.final_label.pack()
        self.final_label.place(x=225, y=330)

        self.final_label = Label(root, text="Outsole:")
        self.final_label.pack()
        self.final_label.place(x=160, y=350)
        self.final_label = Label(root, text=self.material2)
        self.final_label.pack()
        self.final_label.place(x=225, y=350)

        self.final_label = Label(root, text="Toebox:")
        self.final_label.pack()
        self.final_label.place(x=160, y=370)
        self.final_label = Label(root, text=self.material3)
        self.final_label.pack()
        self.final_label.place(x=225, y=370)

        self.final_label = Label(root, text="Upper:")
        self.final_label.pack()
        self.final_label.place(x=160, y=390)
        self.final_label = Label(root, text=self.material4)
        self.final_label.pack()
        self.final_label.place(x=225, y=390)

        self.final_label = Label(root, text="Heel:")
        self.final_label.pack()
        self.final_label.place(x=160, y=410)
        self.final_label = Label(root, text=self.material5)
        self.final_label.pack()
        self.final_label.place(x=225, y=410)

        Button(canvas, text="EXIT", command=sneaker.quit_program).place(x=315, y=270)


if __name__ == "__main__":
    # Creates the window, sets its size, makes the
    # window static so it cant be resized and add
    # a design for the widgets
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("equilux")
    root.title("Custom Sneakers")
    root.geometry("454x670")
    root.configure(bg="black")
    root.resizable(width=False, height=False)
    # Creates the the window where the turtle will
    # draw and color the sneakers.
    canvas = Canvas(root, width=400, height=300)
    canvas.pack()
    t = turtle.RawTurtle(canvas)
    t.pencolor("black")

    sneaker = Sneaker()
    design = Design()
    widget = Widget()
    root.mainloop()