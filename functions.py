#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
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

def JohnTheRipper():
    def goodAsNew():
        os.remove('variables.sh')
        f = open("variables.sh","w+")
    goodAsNew

    mb = Menubutton(tab1, text="decryption method")
    mb.menu = Menu(mb)
    mb["menu"] = mb.menu

    #entry for hash location
    label1 = Label(tab1, text="Hash file location:")
    entry1 = StringVar()
    def echoEntry():
        inputValue = entry0.get("1.0", "end-lo")
        print(inputValue)
    entry0 = Entry(tab1, textvariable=entry1, justify="center", width=13)
    #def echoEntry(self, echoEntry: ("echo entry1=" + entry1.get() + ">> variables.sh")):
    #    self.echoEntry = echoEntry
    entrybutton=Button(tab1, text="Commit", command=lambda: echoEntry )

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

    clear = Button(tab1, text="clear" , command=goodAsNew)
    ready = Button(tab1, text="Ready", command=johnCmd)
    submit1 = Button(tab1, text="Submit" , command=lambda: exec(open("./variables.sh").read()))
    #os.system('./variables.sh'))

    label1.place(relx=0.020, rely=0.020, anchor=NW)
    entry0.place(relx=0.55, rely=0.040, anchor=CENTER)
    entrybutton.place(relx=0.95, rely=0.010, anchor=NE)
    mb.place(relx=0.55, rely=0.150, anchor=CENTER)
    clear.pack(side=LEFT)
    ready.place(relx=0.5, rely=0.50, anchor=CENTER)
    submit1.pack(side=RIGHT)
def goBuster():
    def goodAsNew1():
        os.remove('goBustvar.sh')
        f = open("goBustvar.sh","w+")
    goodAsNew1

    mb1 = Menubutton(tab2, text="wordlists")
    mb1.menu = Menu(mb1)
    mb1["menu"] = mb1.menu

    # entry for URL
    label2 = Label(tab2, text="Website URL:")
    entry3 = StringVar()
    entry2 = Entry(tab2, textvariable=entry3, justify="center", width=13)
    echoEntry = ("echo entry1=" + entry2.get() + ">> variables.sh")
    eb1=Button(tab2, text="Commit", command=lambda: os.system(echoEntry))

    class wl:
        def rockYou():
            for i in range(1):
                os.system('echo "wl = "/usr/share/wordlists/rockyou.txt"" >> goBustvar.sh')
        def big():
            for i in range(1):
                os.system('echo "wl = "/usr/share/wordlists/dirb/big.txt"" >> goBustvar.sh')            
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
    def goBusterCmd():
        for t in range(1):
            os.system('echo "gobuster -u $entry3 -w $wl " >> ./goBustvar.sh')

    mb1.menu.add_command(label="rockYou", command=wl.rockYou)
    mb1.menu.add_command(label="big", command=wl.big)
    #mb1.menu.add_command(label="MySQL", command=wl.mysql)
    #mb1.menu.add_command(label="sha1", command=wl.sha1)
    #mb1.menu.add_command(label="sha-224", command=wl.sha224)
    #mb1.menu.add_command(label="sha-256", command=wl.sha256)
    #mb1.menu.add_command(label="sha-384", command=wl.sha384)
    #mb1.menu.add_command(label="sha-512", command=wl.sha512)

    label2.place(relx=0.020, rely=0.020, anchor=NW)
    entry2.place(relx=0.55, rely=0.040, anchor=CENTER)
    eb1.place(relx=0.95, rely=0.010, anchor=NE)
    mb1.place(relx=0.55, rely=0.150, anchor=CENTER)
