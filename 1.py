
#making a calculator 
from tkinter import ttk 
from tkinter import *

list1 = ["A","S","D","M"]
def addition(x,y):
    ergebnis = x+y 
    print("Das Ergebnis von x und y ist",ergebnis)


def multiplication(x,y):
    ergebnis = x*y 
    print("Das Ergebnis von x und y ist",ergebnis)


def division(x,y):
    ergebnis = x/y 
    print("Das Ergebnis von x und y ist",ergebnis)


def subtraction(x,y):
    ergebnis = x-y 
    print("Das Ergebnis von x und y ist",ergebnis)    


"""
x = int(input("Bitte Geben Sie eine Nummer ein:"))
y = int(input("Bitte Geben Sie eine Nummer ein:"))
z = input("Was Möchten Sie machen?(A/D/S/M):")
while z not in list1:
    print("Versuchen Sie es noch einmal bitte:")
    z = input("Was Möchten Sie machen?(A/D/S/M):")
if z == "M":
    multiplication(x,y)
elif z == "A":
    addition(x,y)
elif z == "S":
    subtraction(x,y)
elif z == "D":
    division(x,y)"""


f = Tk()
f.title("Calculator")
f.geometry("350x350")
e = Entry(f,width=10,borderwidth=1)
e.grid(column=0,row=0)


def callback(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear():
    return
    
    
    
a = ttk.Button(f, text="1",width=10,command = lambda: callback(1)).grid(column=0, row=2,)
ttk.Button(f, text="2",width=10,command = lambda: callback(2)).grid(column=1, row=2)
ttk.Button(f, text="3",width=10,command = lambda: callback(3)).grid(column=2, row=2)
ttk.Button(f, text="4", width=10,command = lambda: callback(4)).grid(column=0, row=3)
ttk.Button(f, text="5", width=10,command = lambda: callback(5)).grid(column=1, row=3)
ttk.Button(f, text="6", width=10,command = lambda: callback(6)).grid(column=2, row=3)
ttk.Button(f, text="7", width=10,command = lambda: callback(7)).grid(column=0, row=4)
ttk.Button(f, text="8", width=10,command = lambda: callback(8)).grid(column=1, row=4)
ttk.Button(f, text="9", width=10,command = lambda: callback(9)).grid(column=2, row=4)
ttk.Button(f, text="0",width=10,command = lambda: callback(0)).grid(column=0, row=5)
b_clear = ttk.Button(f, text="clear",width=10,command = clear).grid(column=3, row=2)
b_add = ttk.Button(f, text="add",width=10,command = addition).grid(column=1, row=5)
b_subtract = ttk.Button(f, text="subtract",width=10,command = subtraction).grid(column=2, row=5)
b_divison= ttk.Button(f, text="division",width=10,command = division).grid(column=3, row=3)
b_multiply= ttk.Button(f, text="multiply",width=10,command = multiplication).grid(column=3, row=4)



f.mainloop()


"""import tkinter
window = tkinter.Tk()
window.title("Code Violation")
def Canvas():
    Var = tkinter.StringVar()   #Making a variable which will store data
    tkinter.Label(window, text="Enter Keyword:").grid(row=0)   #Making label, no need to store it in a variable
    entry = tkinter.Entry(window, text="Enter Keyword", textvariable = Var) #making entry
    entry.grid(row=1)
    def callback(): #this function will be triggered on button press
        print(entry.get())   #get() method will give the value of the entry 
        window.destroy()     #It will destroy the tkinter window
    tester = tkinter.Button(window, text="Generate File", command = callback)
    tester.grid(columnspan=2)
Canvas()
window.mainloop()
"""





