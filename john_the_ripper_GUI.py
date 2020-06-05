#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
import os, subprocess as sub, platform



class JohnTheRipper:
    class GUI:
        def goodAsNew():
            os.remove('variables.sh')
            f = open("variables.sh","w+")
        goodAsNew

        top = Tk()
        top.geometry("350x350") 
        #title

        #menu
        top.title('Hacking GUI')
        top
        #os.system('sudo yum -y -q install john')
        tab_parent = ttk.Notebook(top)

        tab1 = ttk.Frame(tab_parent) 
        tab2 = ttk.Frame(tab_parent) 

        tab_parent.add (tab1, text="John The Ripper")
        tab_parent.add(tab2, text="goBuster")

        tab_parent.pack(expan=1, fill='both')
    GUI
    mb = Menubutton(GUI.tab1, text="decryption method")
    mb.menu = Menu(mb)
    mb["menu"] = mb.menu

    #entry for hash location
    label1 = Label(GUI.tab1, text="Hash file location:")
    entry1 = StringVar()
    entry0 = Entry(GUI.tab1, textvariable=entry1, justify="center", width=13)
    def echoEntry(self, echoEntry: ("echo entry1=" + entry1.get() + ">> variables.sh")):
        self.echoEntry = echoEntry
    entrybutton=Button(GUI.tab1, text="Commit", command=lambda: os.system(echoEntry))


    #menu for decryption method
    class dec:
        def md5():
            for i in range(1):
                os.system('echo "dec = "raw-md5"" >> variables.sh')
        def des():
            for i in range(1):
                os.system('echo "dec = "des"" >> variables.sh')            
        def mysql():
            for i in range(1):
                os.system('echo "dec = "mysql"" >> variables.sh')
        def sha1():
            for i in range(1):
                os.system('echo "dec = "raw-sha1"" >> variables.sh')
        def sha256():
            for i in range(1):
                os.system('echo "dec = "raw-sha256"" >> variables.sh')
        def sha224():
            for i in range(1):
                os.system('echo "dec = "raw-sha224"" >> variables.sh')
        def sha384():
            for i in range(1):
                os.system('echo "dec = "raw-384"" >> variables.sh')
        def sha512():
            for i in range(1):
                os.system('echo "dec = "raw-sha512"" >> variables.sh')
    def johnCmd():
        for t in range(1):
            os.system('echo "john --format=$dec $entry1 " >> ./variables.sh')

    mb.menu.add_command(label="md5", command=dec.md5)
    mb.menu.add_command(label="DES", command=dec.des)
    mb.menu.add_command(label="MySQL", command=dec.mysql)
    mb.menu.add_command(label="sha1", command=dec.sha1)
    mb.menu.add_command(label="sha-224", command=dec.sha224)
    mb.menu.add_command(label="sha-256", command=dec.sha256)
    mb.menu.add_command(label="sha-384", command=dec.sha384)
    mb.menu.add_command(label="sha-512", command=dec.sha512)

    clear = Button(GUI.tab1, text="clear" , command=GUI.goodAsNew)
    ready = Button(GUI.tab1, text="Ready", command=johnCmd)
    submit1 = Button(GUI.tab1, text="Submit" , command=lambda: exec(open("./variables.sh").read()))
    #os.system('./variables.sh'))

    label1.place(relx=0.020, rely=0.020, anchor=NW)
    entry0.place(relx=0.55, rely=0.040, anchor=CENTER)
    entrybutton.place(relx=0.95, rely=0.010, anchor=NE)
    mb.place(relx=0.55, rely=0.150, anchor=CENTER)
    clear.pack(side=LEFT)
    ready.place(relx=0.5, rely=0.50, anchor=CENTER)
    submit1.pack(side=RIGHT)

    GUI.top.mainloop()

    