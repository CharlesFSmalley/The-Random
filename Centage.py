import tkinter as tk
from tkinter import *
import time
from AppOpener import open
import random
from tkinter.messagebox import showerror 
from tkinter import colorchooser


class mainWindow():
    def __init__(self,master):
                self.master = master
                self.master.configure(bg='grey')
                self.master.geometry("400x400")
                self.master.title('Centage')

                



root = Tk()
root.title("master")

root.geometry("350x50")
root.resizable(False, False) 

cls = mainWindow(root)

root.mainloop()