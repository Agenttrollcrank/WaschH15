from tkinter import *

#define the windown
root = Tk()
root.title("WaschH15")
root.geometry("500x500")

#variable definitions
electricityOldValue = 0

#define the function for buttons
def myClick(): #excecute button
    selection = r.get()
    if selection == "Altbau":
        print(selection)
    elif selection == "Linke Maschine":
        print(selection)
    elif selection == "Mitlere Maschine":
        print(selection)
    elif selection == "Rechte Maschine":
        print(selection)
    elif selection == "Trockner Oben":
        print(selection)
    elif selection == "Trockner Unten":
        print(selection)
    else:
        exit(1)

def newSelection(t): #machine choice buttons, changes the text and previous value TODO: change the values to the ones from the database
    machineSelection.config(text=t)
    if t == "Altbau":
        electricityOldValue = 1
    elif t == "Linke Maschine":
        electricityOldValue = 2
    elif t == "Mitlere Maschine":
        electricityOldValue = 3
    elif t == "Rechte Maschine":
        electricityOldValue = 4
    elif t == "Trockner Oben":
        electricityOldValue = 5
    elif t == "Trockner Unten":
        electricityOldValue = 6
    else:
        exit(1)
    electricityOldBox.delete(0, END)
    electricityOldBox.insert(0, str(electricityOldValue))


titleLabel = Label(root, text="WaschH15")
machineSelection = Label(root, text="")

usernameIN = Entry(root, width=40)
passwordIN = Entry(root, width=40)
electricityOldBox = Entry(root, width=40)
electricityOldBox.insert(0,str(electricityOldValue))
electricityNewBox = Entry(root, width=40)

login = Button(root, text="Login", command=myClick, bg="#ff00ff")

MACHINES = [
    ("Altbau", "Altbau"),
    ("Linke Maschine", "Linke Maschine"),
    ("Mitlere Maschine", "Mitlere Maschine"),
    ("Rechte Maschine", "Rechte Maschine"),
    ("Trockner Oben", "Trockner Oben"),
    ("Trockner Unten", "Trockner Unten")
]

r = StringVar()
line = 3
for text, machine in MACHINES:
    Radiobutton(root, text=text, variable=r, value=machine, tristatevalue=0, command=lambda: newSelection(r.get())).grid(row=line, column=10)
    line += 1




#showing it on screen
titleLabel.grid(row=0, column=10)
username = Label(root, text="Benutzername: ").grid(row=1, column=9)
usernameIN.grid(row=1, column=10)
password = Label(root, text="Passwort: ").grid(row=2, column=9)
passwordIN.grid(row=2, column=10)

#machineSelection.grid(row=10, column=10)
electricityOldLabel = Label(root, text="Vorheriger Strom Stand: ").grid(row=11, column=9)
electricityOldBox.grid(row=11, column=10)
electricityNewLabel = Label(root, text="Neuer Strom Stand: ").grid(row=12, column=9)
electricityNewBox.grid(row=12, column=10)
login.grid(row=13, column=10)


root.mainloop()
