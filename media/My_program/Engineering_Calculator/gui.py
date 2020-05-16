from tkinter import  *
import sys


class Main(Frame):


    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()


    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, bg="#000", foreground="#FFF", font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=10, y=50)


        button = [
            "x^2", "x^3", "x^4", "DEL", "C",
            "7", "8", "9", "*", "/",
            "4", "5", "6", "+", "-",
            "1", "2", "3", "%", "=",
            "(", "0", ")", "Exit"
        ]
        x = 10
        y = 90

        for b in button:
            com = lambda x = b: self.logicalc(x)
            Button(text=b, command= com, bg="#000",
                       foreground="#FFF", font=("Times New Roman", 21)).place(x=x, y=y, width=90, height=90)
            x += 92
            if x > 460:
                y += 92
                x = 10


    def logicalc(self, operation: str):
        if self.formula == "ERROR":
            self.formula = "0"
        if operation == "DEL":
            operation = ""
            self.formula = self.formula[:-1]
        if operation == "C":
            operation = ""
            self.formula = operation
        if operation == "Exit":
            sys.exit()
        elif operation == "%":
            operation = "/100"
        elif operation == "x^2":
            operation = "**2"
        elif operation == "x^3":
            operation = "**3"
        elif operation == "x^4":
            operation = "**4"
        elif operation == "=":
            operation = ""
            if self.formula[-1].isdigit() or self.formula[-2].isdigit():
                try:
                    self.formula = str(eval(self.formula))
                except ZeroDivisionError:
                    self.formula = "ERROR"
        else:
            if operation.isdigit() and self.formula == "0":
                self.formula = ""
            if not operation.isdigit():
                if self.formula != "" and not self.formula[-1].isdigit() and operation == "(" or operation == ")":
                    if operation == "(":
                        operation = "("
                    if operation == ")":
                        operation = ")"
                elif self.formula != "" and not self.formula[-1].isdigit():
                    self.formula = self.formula[:-1]
        self.formula += operation
        self.update()


    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)
        



