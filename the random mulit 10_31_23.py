import tkinter as tk
from tkinter import *
import time
from time import strftime
import pyttsx3
from AppOpener import open
import random
import wikipedia
import subprocess
from tkinter.messagebox import showerror 
from wikipedia import summary 
from tkinter import colorchooser
import datetime as dt

# Background color to use :
#        #e4e4e4

class mainWindow():
        global my_time
        def __init__(self,master):
                global t_time
                #Main window config
                self.master = master
                self.master.configure(bg='grey')
                self.master.geometry("335x310")
                self.master.title('The Random')

                #Main window backgroudn image
                self.canvas = Canvas(self.master, width = 800, height = 800)
                self.canvas.pack(fill = "both", expand = True) 
                self.canvas.create_image( 0, 0, image = main_window_img,  anchor = "nw") 


                #    All the different starting buttons :
                #    each calls its own function to contruct 
                #    a new window based on the desired function
                txtrdr = tk.Button(master, command=self.textApp,
                        #text='Text \nReader', 
                        image= text_to_speech_img,
                        bg = 'green',
                        width=90,
                        height=50,
                        compound = LEFT).place(x=10, y=10)
                rndint = tk.Button(master, command=self.rndintApp,
                        font=("Calibri 10 bold"),
                        text = 'R.N.\nGenerator',
                        bg = 'blue',
                        width=12,
                        height=3).place(x=120,y=10)
                tmr = tk.Button(master, command=self.timerApp,
                        #text = 'Timer',
                        image=timer_img,
                        bg = 'purple',
                        width=90,
                        height=50).place(x=230,y=10)
                exe = tk.Button(master, command=self.exeApp,
                        #text = 'Windows Apps',
                        image=windows_control_img,
                        bg = 'green',
                        width=90,
                        height=50).place(x=10,y=90)
                cntg = tk.Button(master, command=self.CentageApp,
                        font=("Calibri 10 bold"),
                        text = 'Centage',
                        bg = 'blue',
                        width=12,
                        height=3).place(x=120,y=90)
                wik = tk.Button(master, command=self.wikiApp,
                        image= wikipedia_logo_img,
                        bg = 'purple',
                        width=90,
                        height=50,
                        compound = LEFT).place(x=230,y=90)
                snk = tk.Button(master, command=self.snakeApp,
                        image=snake_img,
                        #text = 'Snake',
                        bg = 'green',
                        width=90,
                        height=50).place(x=10,y=170)
                clr = tk.Button(master, command=self.colorApp,
                        #text= 'Color Wheel',
                        image= spinning_wheel_img,
                        bg = 'blue',
                        width=90,
                        height=50,
                        compound = LEFT).place(x= 120, y=170)
                gm = tk.Button(master, command=self.gameApp,
                        font=("Calibri 10 bold"),
                        text= 'Game \nLibrary',
                        bg = 'purple',
                        width=12,
                        height=3,
                        compound = LEFT).place(x= 230, y=170)


                # Create Label to display the Date
                date = dt.datetime.now()
                self.label = Label(master, text=f"{date:%A, %B %d, %Y}", font="Calibri, 15").place(x=10, y=235)


                ### The code below was unfinised because of errors 
                ### that were not solvable

                """
                #time_string = strftime('%H:%M:%S %p')
                #self.t_label = Label(master, text=time_string, font="Calibri, 15").place(x=10, y=270)

                screw_python = 1
                while screw_python == 1:
                        time.sleep(0.1)                
                        self.time_string = strftime('%H:%M:%S %p')
                        self.t_label.config(text =time_string)
                        self.master.update()
                """
                # End of the unfishied code



        #    Connections from the different classes to the main window

        "Timer Window Connection to the Main Class"
        def timerApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = timerWindow(self.newWindow)
        "Text Reader Connection to the Main Class"
        def textApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = textWindow(self.newWindow)
        "Random Integer Window Connection to the Main Class"
        def rndintApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = rndintWindow(self.newWindow)
        "Executable Window Connection to the Main Class"
        def exeApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = exeWindow(self.newWindow)
        "Centage Window Connection to the Main Class"
        def CentageApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = centageWindow(self.newWindow)
        "Wikipedia Window Connection to the Main Class"
        def wikiApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = wikiWindow(self.newWindow)
        "Centage Window Connection to the Main Class"
        def snakeApp(self):
                snakeWindow()
        "Color Window Connection to the Main Class"
        def colorApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = colorWindow(self.newWindow)
        "Game Window Connection to the Main Class"
        def gameApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = gameWindow(self.newWindow)

        



class timerWindow():

        def __init__(self , master):

                def timer():
                        global clock
                        clock = int(self.userin.get())
                        while clock >= 0:
                                #Delete the Old number and put in the new one
                                self.userin.delete(0, END)
                                self.userin.insert(0, clock)
                                #Pause Every Second
                                time.sleep(1)
                                clock = clock - 1
                                #Refresh The Main Window
                                self.master.update()

                
                self.master = master
                self.master.configure(bg='grey')
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("250x125+200+200")
                master.title("Timer")
                self.userin = tk.Entry(self.frame, width = 25, bg='#e4e4e4')
                self.userin.pack()
                
                self.rn = tk.Button(self.frame, 
                                        width= 11, 
                                        text = "Start Timer", 
                                        command=timer, 
                                        bg='#e4e4e4')
                self.rn.pack()

                
                self.frame.pack()

        def close_window(self):
                self.master.destroy()

class textWindow():

        def __init__(self , master):
                
                self.master = master
                self.master.title("Text Reader")
                self.master.geometry("400x195")
                self.frame = tk.Frame(master, bg='grey')
                
                string = str()
                def textReader():
                        global rd
                        rd = str(self.textBox.get("1.0",'end-1c'))
                        print(rd)
                        engine = pyttsx3.init()
                        engine.say(rd)
                        engine.runAndWait()


                self.textBox = tk.Text(self.frame,
                                        bg='#a0a0a0',  
                                        width=50, 
                                        height=10)
                self.rn = tk.Button(self.frame, 
                                        bg='#a0a0a0',  
                                        text = "Read Text", 
                                        width= 11,
                                        command=textReader)

                self.textBox.pack()
                self.rn.pack()

                #self.quitButton = tk.Button(self.frame, text = 'Quit', width = 15 , command = self.close_window)
                #self.quitButton.pack()
                 
                self.frame.pack()
                

        def close_window(self):
                self.master.destroy()

class rndintWindow():

        def __init__(self , master):
                def go():
                        global ent1, ent2
                        endInt = random.randint(-100000000, 100000000)
                        self.ent1.delete(0,"end")
                        self.ent1.insert(0,endInt)

                self.master = master
                self.master.configure(bg='grey')
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("300x175+400+400")
                master.title("Random Integer")
                #self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25 , command = self.close_window)
                #self.quitButton.pack()

                self.randomintgen = tk.Button(self.frame, 
                                        text='Generate Random Integer', 
                                        command=go, 
                                        bg='#5b5b5b')
                self.randomintgen.pack()

                self.ent1 = tk.Entry(self.frame)
                #self.ent2 = tk.Entry(self.frame)
                self.ent1.pack()
                #self.ent2.pack()

                 
                self.frame.pack()


        def close_window(self):
                self.master.destroy()

class exeWindow():

        def __init__(self , master):

                def chrome():
                        open('google chrome')
                def spot():
                        open('spotify')
                def vscode():
                        open('visual studio code')
                def xbox():
                        open('xbox', match_closest=True)
                def model():
                        open('autodesk fusion 360', match_closest=True)
                def phone():
                        open('phone link', match_closest=True)
                def premire20():
                        open('adobe premire elements 2020', match_closest=True)
                def photoshop20():
                        open('adobe photoshop 2020', match_closest=True)
                def entryprogram():
                        open(self.user.get(), match_closest=True)
                        
                self.master = master
                self.master.configure(bg='grey')
                self.frame_1 = tk.Frame(master, bg='grey')
                self.frame_2 = tk.Frame(master, bg='grey')
                self.frame_3 = tk.Frame(master, bg='grey')
                self.frame_4 = tk.Frame(master, bg='grey')
                self.frame_5 = tk.Frame(master, bg='grey')
                self.frame_6 = tk.Frame(master, bg='grey')

                self.master.geometry("275x225")
                master.title("Executable Opener")

                self.chrome = tk.Button(self.frame_1, text='Chrome', command=chrome)
                self.chrome.pack(side=tk.LEFT, padx="2")
                #self.chrome.pack(padx="2")

                self.spot = tk.Button(self.frame_1, text='Spotify', command=spot)
                self.spot.pack(side=tk.LEFT, padx="2")
                #self.spot.pack(padx="2")

                self.chrome = tk.Button(self.frame_1, text='VS Code', command=vscode)
                self.chrome.pack(side=tk.LEFT, padx="2")
                #self.chrome.pack(padx="2")

                self.xbox = tk.Button(self.frame_2, text='Xbox', command=xbox)
                self.xbox.pack(side=tk.LEFT, padx="2")
                #self.xbox.pack(padx="2")

                self.modl = tk.Button(self.frame_2, text='Fusion', command=model)
                self.modl.pack(side=tk.LEFT, padx="2")
                #self.modl.pack(padx="2")

                self.fone = tk.Button(self.frame_2, text='Phone Link', command=phone)
                self.fone.pack(side=tk.LEFT, padx="2")
                #self.fone.pack(padx="2")
                
                self.premire = tk.Button(self.frame_3, text='Adobe Premire Elements 2022', command=premire20)
                self.premire.pack(side=tk.LEFT, padx="2")
                #self.premire.pack(padx="2")

                self.phot = tk.Button(self.frame_4, text='Adobe Photoshop 2020', command=photoshop20)
                self.phot.pack(side=tk.LEFT, padx="2")
                #self.phot.pack(padx="2")

                self.user = tk.Entry(self.frame_5, width=15)
                self.user.pack(side=tk.LEFT, padx="4")

                self.ent = tk.Button(self.frame_6, text='Run Program', command=entryprogram)
                self.ent.pack(side=tk.LEFT, padx="4")


                #self.quitButton = tk.Button(self.frame_6, text = 'Quit', width = 20 , command = self.close_window)
                #self.quitButton.pack(side=tk.LEFT)

                 
                self.frame_1.pack(fill="x", padx="3", pady="3")
                self.frame_2.pack(fill="x", padx="3", pady="3")
                self.frame_3.pack(fill="x", padx="3", pady="3")
                self.frame_4.pack(fill="x", padx="3", pady="3")
                self.frame_5.pack(fill="x", padx="3", pady="3")
                self.frame_6.pack(fill="x", padx="3", pady="3")


        def close_window(self):
                self.master.destroy()

class centageWindow():

        def __init__(self , master):
                self.master = master
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("400x400+400+400")
                self.master.title("Centage")
                self.master.config(bg='grey')
                self.frame.pack()

        def close_window(self):
                self.master.destroy()

class wikiWindow():
        def __init__(self , master):
                # Defining the search command
                def get_summary():                
                        try: 
                                self.answer.delete(1.0, END) 
                                self.answer.insert(INSERT, summary(self.keyword_entry.get())) 

                        except Exception as error: 
                                showerror("Error", error) 


                #Creating the main window
                self.master = master
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("500x375")
                self.master.configure(bg='#5b5b5b')
                self.master.title("Wikipedia Search")

                self.top_frame = Frame(master, bg='#5b5b5b') 
                self.top_frame.pack(side="top", fill="x", padx=50, pady=10) 
                self.bottom_frame = Frame(master, bg='#5b5b5b') 
                self.bottom_frame.pack(side="top", fill="x", padx=10, pady=10) 


                self.keyword_entry = Entry(self.top_frame, 
                                                font=("Arial", 10, "bold"), 
                                                bg='#838383',
                                                width=25, 
                                                bd=4) 
                self.keyword_entry.pack(side="left", ipady=6,) 
                self.search_button = Button(self.top_frame, 
                                                text="SEARCH",font=("Arial", 10, "bold"), 
                                                bg='#838383',
                                                width=10, 
                                                bd=4, 
                                                command=get_summary) 
                self.search_button.pack(side="right") 
                self.scroll = Scrollbar(self.bottom_frame) 
                self.answer = Text(self.bottom_frame, font=("Arial", 10), 
                                                fg="black", 
                                                bg='#838383',
                                                width=55, 
                                                height=15, 
                                                bd=5, 
                                                yscrollcommand=self.scroll.set) 
                self.answer.pack(side="left", fill="y") 
                self.scroll.pack(side="left", fill="y") 
                 
                self.frame.pack()
                 


        def close_window(self):
                self.master.destroy()

class colorWindow():

        def __init__(self , master):
                def choose_color():
                        # Variable to store hexadecimal code of color
                        color_code = colorchooser.askcolor(title ="Choose color") 
                        #print(color_code)
                        self.out.insert(0, ('RGB',color_code))


                self.master = master
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("275x200")
                self.master.configure(bg='grey')
                master.title("Color Window")
                
                self.clrbut = tk.Button(self.frame, 
                                        text='Select Color', 
                                        command= choose_color, 
                                        width=10, 
                                        height=3)
                self.clrbut.pack()

                self.out = tk.Entry(self.frame, 
                                        width=25)

                self.out.pack()
                self.frame.pack()

        
        def close_window(self):
                self.master.destroy()

class gameWindow():
        def __init__(self , master):
                global game_libraryback
                global game_libraryback_img
                global haloIn
                global haloI_img
                self.master = master
                #self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("405x300")
                self.master.configure(bg='grey')
                self.master.resizable(False, False) 

                master.title("Game Library")
                #self.frame.pack()

                self.canvas = Canvas(self.master, width = 400, height = 400)
                self.canvas.pack(fill = "both", expand = True) 
                self.canvas.create_image( 0, 0, image = game_libraryback_img,  anchor = "nw") 
  

                
                def launchHaloI():
                        open('Halo Infinite', match_closest=True)
                def launchHalo():
                        open('Halo', match_closest=True)
                def launchMinecraft():
                        open('Minecraft', match_closest=True)
                def launchVal():
                        open('Valorant', match_closest=True)
                def launchApex():
                        open('Apex Legends', match_closest=True)
                def launchDiscord():
                        open('Discord', match_closest=True)



                self.frame_1 = tk.Frame(master, bg='grey')
                self.frame_2 = tk.Frame(master, bg='grey')
                self.frame_3 = tk.Frame(master, bg='grey')
                
                # Game Launch
                self.haloI = tk.Button(self.canvas, 
                                        #text='Halo \nInfinite', 
                                        command=launchHaloI, 
                                        image=haloI_img,
                                        width=90, height=75).place(x=20,y=20)
                self.halo = tk.Button(self.canvas, 
                                        #text='Halo \nComabt \nEvolved', 
                                        command=launchHaloI, 
                                        image=halo_CE_img,
                                        width=90, height=75).place(x=140, y=20)
                self.mine = tk.Button(self.canvas, 
                                        #text='Minecraft', 
                                        image=minecraft_img,
                                        command=launchMinecraft, 
                                        width=90, height=75).place(x=260, y=20)
                self.val = tk.Button(self.canvas, 
                                        #text='Valorant', 
                                        image=valorant_img,
                                        command=launchVal, 
                                        width=90, height=75).place(x=20, y=110)
                self.apex = tk.Button(self.canvas, 
                                        image=apex_Legends_img,
                                        #text='Apex \nLegends', 
                                        command=launchApex, 
                                        width=90, height=75).place(x=140, y=110)
                self.disc = tk.Button(self.canvas, 
                                        image=discord_img,
                                        #text='Discord', 
                                        command=launchDiscord, 
                                        width=90, height=75).place(x=260, y=110)
                


        
        def close_window(self):
                self.master.destroy()

#   Calls geeks for geek's snake demonstration in python
def snakeWindow():
        subprocess.run(["python", "F:\Projects and Printers\The Random\Working Folder\Snake.py"])



root = Tk()



#   Below are all the images used in any of the app widgets
#   MAIN WINDOW IMAGES

main_window = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\main_window.png")
main_window_img= main_window.subsample(8,8)

spinning_wheel = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\spinning_wheel.png") 
spinning_wheel_img = spinning_wheel.subsample(15, 15)

txt_to_spch = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\text_to_speech.png")
text_to_speech_img = txt_to_spch.subsample(13, 13)

wikipedia_logo = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\wikipedia_logo.png")
wikipedia_logo_img = wikipedia_logo.subsample(22, 22)

timer = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\timer.png")
timer_img = timer.subsample(25, 25)

snake = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\snake.png")
snake_img = snake.subsample(8, 8)

windows_control = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\windows_control.png")
windows_control_img = windows_control.subsample(15, 15)


#   GAME LIBRARY IMAGES 
game_libraryback = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\gamelibrary.png")
game_libraryback_img = game_libraryback.subsample(10, 10)

haloIn = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\halo_infinite.png")
haloI_img = haloIn.subsample(15, 20)

halo_CE = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\halo_ce.png")
halo_CE_img = halo_CE.subsample(10, 7)

minecraft = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\minecraft.png")
minecraft_img = minecraft.subsample(5, 6)

valorant = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\valorant.png")
valorant_img = valorant.subsample(3, 3)

apex_Legends= PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\apex_legends.png")
apex_Legends_img = apex_Legends.subsample(3, 3)

discord= PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\discord.png")
discord_img = discord.subsample(7, 7)

root.title("master")

root.geometry("350x50")
root.resizable(False, False) 

cls = mainWindow(root)


root.mainloop()