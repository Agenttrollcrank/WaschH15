from tkinter import *

root = Tk()
root.title("WaschH15")
root.geometry("500x500")

def myClick():
    pass

titleLabel = Label(root, text="WaschH15")

usernameIN = Entry(root, width=40)
passwordIN = Entry(root, width=40)

electricityValue = Entry(root, width=40)

login = Button(root, text="Login", command=myClick, bg="#ff00ff")

#frame = Choice(root,text="choice", padx=5, pady=5)

MACHINES = [
    ("Altbau", "Altbau"),
    ("Linke Maschine", "Linke Maschine"),
    ("Mitlere Maschine", "Mitlere Maschine"),
    ("Rechte Maschine", "Rechte Maschine"),
    ("Trockner Oben", "Trockner Oben"),
    ("Trockner Unten", "Trockner Unten")
]
line = 3
for text, machine in MACHINES:
    Radiobutton(root, text=text, value=machine).grid(row=line, column=10)
    line += 1




#showing it on screen
titleLabel.grid(row=0, column=10)
username = Label(root, text="Benutzername: ").grid(row=1, column=9)
usernameIN.grid(row=1, column=10)
password = Label(root, text="Passwort: ").grid(row=2, column=9)
passwordIN.grid(row=2, column=10)

#machineSelection.grid(row=4, column=10)


electricity = Label(root, text="Neuer Strom Stand: ").grid(row=10, column=9) #add previous value
electricityValue.grid(row=10, column=10)


login.grid(row=11, column=10)

root.mainloop()