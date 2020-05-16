from gui import *

if __name__ == "__main__":
    root = Tk()
    root["bg"] = "#000"
    root.geometry("480x550+100+100")
    root.title("Engineering Calculator.")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
