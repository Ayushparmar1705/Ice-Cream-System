from tkinter import *
import Prod_Frame




win = Tk()



height = win.winfo_screenheight()
width = win.winfo_screenwidth()

win.geometry("{}x{}".format(width,height))
win.state("zoomed")
win.title("Logged-In")



class Home_frame:
    def __init__(self,height,width):
        self.height = height
        self.width = width