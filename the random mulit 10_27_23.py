import tkinter as tk
from tkinter import *
import time
import pyttsx3
from AppOpener import open
import random
import wikipedia
import subprocess
from tkinter.messagebox import showerror 
from wikipedia import summary 
from tkinter import colorchooser


# Background color to use :
#        #e4e4e4



class mainWindow():

        def __init__(self,master):
                self.master = master
                self.master.configure(bg='grey')
                self.master.geometry("315x165+400+400")
                self.master.title('The Random')
                txtrdr = tk.Button(master, command=self.textApp,
                        text='Text \nReader', 
                        image= text_to_speech_img,
                        bg = 'green',
                        width=87.25,
                        height=33.25,
                        compound = LEFT).place(x=10, y=10)
                rndint = tk.Button(master, command=self.rndintApp,
                        text = 'R.N.\nGenerator',
                        bg = 'blue',
                        width=12,
                        height=2).place(x=110,y=10)
                tmr = tk.Button(master, command=self.timerApp,
                        text = 'Timer',
                        bg = 'purple',
                        width=12,
                        height=2).place(x=210,y=10)
                exe = tk.Button(master, command=self.exeApp,
                        text = 'Windows Apps',
                        bg = 'green',
                        width=12,
                        height=2).place(x=10,y=60)
                hlpr = tk.Button(master, command=self.helperApp,
                        text = 'Helper',
                        bg = 'blue',
                        width=12,
                        height=2).place(x=110,y=60)
                wik = tk.Button(master, command=self.wikiApp,
                        image= wikipedia_logo_img,
                        text = 'Wikipedia \nSearch',
                        bg = 'purple',
                        width=87.25,
                        height=33.25,
                        compound = LEFT).place(x=210,y=60)
                snk = tk.Button(master, command=self.snakeApp,
                        text = 'Snake',
                        bg = 'green',
                        width=12,
                        height=2).place(x=10,y=110)
                clr = tk.Button(master, command=self.colorApp,
                        text= 'Color Wheel',
                        image= spinning_wheel_img,
                        bg = 'blue',
                        width=87.25,
                        height=33.25,
                        compound = LEFT).place(x= 110, y=110)
                gm = tk.Button(master, command=self.gameApp,
                        text= 'Game Library',
                        bg = 'purple',
                        width=12,
                        height=2,
                        compound = LEFT).place(x= 210, y=110)

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
        "Helper Window Connection to the Main Class"
        def helperApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = helperWindow(self.newWindow)
        def wikiApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = wikiWindow(self.newWindow)
        def snakeApp(self):
                snakeWindow()
        def colorApp(self):
                self.newWindow = tk.Toplevel(self.master)
                self.app = colorWindow(self.newWindow)
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
                self.userin = tk.Entry(self.frame, width = 25)
                self.userin.pack()
                
                self.rn = tk.Button(self.frame, width= 11, text = "Start Timer", command=timer)
                self.rn.pack()

                
                self.frame.pack()

        def close_window(self):
                self.master.destroy()

class textWindow():

        def __init__(self , master):
                
                self.master = master
                self.master.configure(bg='grey')
                self.frame = tk.Frame(master)
                self.master.geometry("250x125+200+200")

                string = str()
                self.textBox = tk.Text(self.frame, width=50, height=10)
                self.textBox.pack()
                def textReader():
                        global rd
                        rd = str(self.textBox.get("1.0",'end-1c'))
                        print(rd)
                        engine = pyttsx3.init()
                        engine.say(rd)
                        engine.runAndWait()
                self.rn = tk.Button(self.frame, width= 11, text = "Read Text", command=textReader)
                self.rn.pack()
                self.master.geometry("400x250")
                master.title("Text Reader")
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
                self.frame = tk.Frame(master)
                self.master.geometry("300x175+400+400")
                master.title("Random Integer")
                #self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25 , command = self.close_window)
                #self.quitButton.pack()

                self.randomintgen = tk.Button(self.frame, text='Generate Random Integer', command=go)
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

class helperWindow():

        def __init__(self , master):
                self.master = master
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("400x400+400+400")
                master.title("Helper Window")
                self.frame.pack()

        def close_window(self):
                self.master.destroy()

class wikiWindow():
        def __init__(self , master):
                def get_summary():                
                        try: 
                                self.answer.delete(1.0, END) 
                                self.answer.insert(INSERT, summary(self.keyword_entry.get())) 

                        except Exception as error: 
                                showerror("Error", error) 

                self.master = master
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("500x375")
                self.master.configure(bg='grey')
                self.master.title("Wikipedia Search")

                self.top_frame = Frame(master, bg='grey') 
                self.top_frame.pack(side="top", fill="x", padx=50, pady=10) 
                self.bottom_frame = Frame(master, bg='grey') 
                self.bottom_frame.pack(side="top", fill="x", padx=10, pady=10) 


                self.keyword_entry = Entry(self.top_frame, font=("Arial", 10, "bold"), width=25, bd=4) 
                self.keyword_entry.pack(side="left", ipady=6,) 
                self.search_button = Button(self.top_frame, text="SEARCH",font=( 
                        "Arial", 10, "bold"), width=10, bd=4, command=get_summary) 
                self.search_button.pack(side="right") 


                self.scroll = Scrollbar(self.bottom_frame) 
                self.answer = Text(self.bottom_frame, font=("Arial", 10), fg="black", 
                                        width=55, height=15, bd=5, yscrollcommand=self.scroll.set) 
                self.answer.pack(side="left", fill="y") 
                self.scroll.pack(side="left", fill="y") 
                 
                self.frame.pack()
                 


        def close_window(self):
                self.master.destroy()

class colorWindow():

        def __init__(self , master):
                def choose_color():
                        # variable to store hexadecimal code of color
                        color_code = colorchooser.askcolor(title ="Choose color") 
                        #print(color_code)
                        self.out.insert(0, ('RGB',color_code))


                self.master = master
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("250x75")
                self.master.configure(bg='grey')
                master.title("Color Window")
                self.frame.pack()
                self.clrbut = tk.Button(self.frame, text='Select Color', command= choose_color)
                self.clrbut.pack()

                self.out = tk.Entry(self.frame,width=25 )
                self.clrbut.pack()
                self.out.pack()

        
        def close_window(self):
                self.master.destroy()

class gameWindow():
        def __init__(self , master):
                global game_libraryback
                global game_libraryback_img
                self.master = master
                self.frame = tk.Frame(master, bg='grey')
                self.master.geometry("300x200")
                self.master.configure(bg='grey')
                master.title("Game Library")
                self.frame.pack()

                canvas1 = Canvas(self.master, width = 400, height = 400)
                canvas1.pack(fill = "both", expand = True) 
                canvas1.create_image( 0, 0, image = game_libraryback_img,  anchor = "nw") 
  


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



                self.frame_1 = tk.Frame(master, bg='grey')
                self.frame_2 = tk.Frame(master, bg='grey')
                self.frame_3 = tk.Frame(master, bg='grey')
                
                self.haloI = tk.Button(self, text='Halo Infinite', command=launchHaloI, width=10, height=2)
                self.haloI.pack(side=tk.LEFT, padx="2")
                self.halo = tk.Button(self.frame_1, text='Halo \nComabt Evolved', command=launchHalo, width=10, height=2)
                self.halo.pack(side=tk.LEFT, padx="2")
                self.mine = tk.Button(self.frame_1, text='Minecraft', command=launchMinecraft, width=10, height=2)
                self.mine.pack(side=tk.LEFT, padx="2")
                self.val = tk.Button(self.frame_2, text='Valorant', command=launchVal, width=10, height=2)
                self.val.pack(side=tk.LEFT, padx="2")
                self.apex = tk.Button(self.frame_2, text='Apex Legends', command=launchApex, width=10, height=2)
                self.apex.pack(side=tk.LEFT, padx="2")

                self.haloI_canvas = canvas1.create_window(window = self.haloI)



                self.frame_1.pack(fill="x", padx="3", pady="3")
                self.frame_2.pack(fill="x", padx="3", pady="3")
                self.frame_3.pack(fill="x", padx="3", pady="3")



        
        def close_window(self):
                self.master.destroy()




def snakeWindow():
        subprocess.run(["python", "F:\Projects and Printers\The Random\Working Folder\Centage.py"])









root = Tk()


spinning_wheel = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\spinning_wheel.png") 
spinning_wheel_img = spinning_wheel.subsample(25, 25)

txt_to_spch = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\text_to_speech.png")
text_to_speech_img = txt_to_spch.subsample(22, 15)

wikipedia_logo = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\wikipedia_logo.png")
wikipedia_logo_img = wikipedia_logo.subsample(35, 35)


game_libraryback = PhotoImage(file = r"F:\Projects and Printers\The Random\Working Folder\gamelibrary.png")
game_libraryback_img = game_libraryback.subsample(10,10)



root.title("master")

root.geometry("350x50")
root.resizable(False, False) 

cls = mainWindow(root)

root.mainloop()