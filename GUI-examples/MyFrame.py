#from Tkinter import *
import Tkinter as _tk
import tkMessageBox as mbox
import tkSimpleDialog as tkDialog

#_tk = Tkinter
#mbox = tkMessageBox
#tkDialog = tkSimpleDialog

class MyApp:
    
    def __init__(self, master):
        #frame = _tk.Frame( width=768, height=576 )
        frame = _tk.Frame( master )
        frame.pack()
        
        self.btn_quit = _tk.Button(frame, text="Quit", fg="red", command=frame.quit)
        self.btn_quit.pack(side=_tk.LEFT)
        
        self.btn_hi = _tk.Button(frame, text="Hello", fg="blue", command=self.sayHello)
        self.btn_hi.pack(side=_tk.RIGHT)
        
    def sayHello(self):
        theName = tkDialog.askstring("Your Name", "What is your name?")
        if theName != None :
            mbox.showinfo("Greeting", "Hello "+theName)
        else :
            mbox.showinfo("Greeting", "jum ")
    

root = _tk.Tk()
app = MyApp( root )
root.mainloop()