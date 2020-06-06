#!/usr/bin/python3
#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from functions import JohnTheRipper, goBuster
import os, subprocess as sub, platform  

top = Tk()
top.geometry("350x350") 
#title

#menu
top.title('Hacking GUI')
top

tab_parent = ttk.Notebook(top)

tab1 = ttk.Frame(tab_parent) 
tab2 = ttk.Frame(tab_parent) 

tab_parent.add (tab1, text="John The Ripper")
tab_parent.add(tab2, text="goBuster")

tab_parent.pack(expan=1, fill='both')


JohnTheRipper() 
goBuster()

top.mainloop()
