from tkinter import *
import mysql.connector

#mysql connection
mydb = mysql.connector.connect(
    user='Yulian',
    password='FreddyIstGeil',
    host='134.130.188.10',
    database='h15')

mycursor = mydb.cursor(buffered=True)

#define the windown
root = Tk()
root.title("WaschH15")
root.geometry("500x500")

#variable definitions
sl = 0
electricityOldValue = int

#define the function for buttons
def myClick(): #excecute button
    #credential check
    mycursor.execute("SELECT COUNT(1) FROM h15.benutzer WHERE username='%s'" % (usernameIN.get()))
    if mycursor.fetchone()[0]:
        mycursor.execute("SELECT COUNT(1) FROM h15.benutzer WHERE passwort='%s' AND username='%s'" % (passwordIN.get(),usernameIN.get()))
        if mycursor.fetchone()[0]:
            if int(electricityNewBox.get()) >= electricityOldValue[0]:
                try: #checks the value inputted
                    mycursor.execute("UPDATE h15.strom SET Kwh = " + str(electricityNewBox.get()) +
                                     " WHERE Waschmachine = '" + str(machineString.get()) + "'")
                    message.config(text="Alles Klar! Danke dir! Vergesse nicht deine Wäsche :D")
                    electricityOldBox.delete(0, END)
                    electricityOldBox.insert(0, electricityNewBox.get())
                    usernameIN.delete(0, END)
                    passwordIN.delete(0, END)
                except:
                    message.config(text="Bitte geben Sie einen zahl an")
            else:  # ValueError
                message.config(text="Bitte geben Sie einen größeren Wert ein")
            electricityNewBox.delete(0, END)
        else:
            message.config(text="Falsche Passwort")
    else:
        message.config(text="Falsche Benutzername")
    mydb.commit()
    #TODO add new entry

def newSelection(): #machine choice buttons, changes the text and previous value
    global electricityOldValue
    machineSelection.config(text=machineString.get())
    if machineString.get() == "Altbau":
        sl = 0
    elif machineString.get() == "Linke_Maschine":
        sl = 1
    elif machineString.get() == "Mittlere_Maschine":
        sl = 2
    elif machineString.get() == "Rechte_Maschine":
        sl = 3
    elif machineString.get() == "Trockner_Oben":
        sl = 4
    elif machineString.get() == "Trockner_Unten":
        sl = 5
    else:
        exit(1)
    mycursor.execute("SELECT Kwh FROM h15.strom LIMIT " + str(sl) +",1")
    electricityOldValue = mycursor.fetchone()
    electricityOldBox.delete(0, END)
    electricityOldBox.insert(0, electricityOldValue)

titleLabel = Label(root, text="WaschH15")
machineSelection = Label(root, text="")

usernameIN = Entry(root, width=40)
passwordIN = Entry(root, show="*", width=40)
electricityOldBox = Entry(root, width=40)
electricityOldBox.insert(0,0)
electricityNewBox = Entry(root, width=40)

login = Button(root, text="WASCHEN!!!", command=myClick)
#defining the radio buttons
MACHINES = [
    ("Altbau", "Altbau"),
    ("Linke_Maschine", "Linke_Maschine"),
    ("Mittlere_Maschine", "Mittlere_Maschine"),
    ("Rechte_Maschine", "Rechte_Maschine"),
    ("Trockner_Oben", "Trockner_Oben"),
    ("Trockner_Unten", "Trockner_Unten")
]
#drawing the radio buttons on the screen
machineString = StringVar()
line = 3
for text, machine in MACHINES:
    Radiobutton(root, text=text, variable=machineString, value=machine, tristatevalue=0, command=lambda: newSelection()).grid(row=line, column=10)
    line += 1

#showing it on screen
titleLabel.grid(row=0, column=10)
usernameLabel = Label(root, text="Benutzername: ").grid(row=1, column=9)
usernameIN.grid(row=1, column=10)
passwordLabel = Label(root, text="Passwort: ").grid(row=2, column=9)
passwordIN.grid(row=2, column=10)

#machineSelection.grid(row=10, column=10)
electricityOldLabel = Label(root, text="Vorheriger Strom Stand: ").grid(row=11, column=9)
electricityOldBox.grid(row=11, column=10)
electricityNewLabel = Label(root, text="Neuer Strom Stand: ").grid(row=12, column=9)
electricityNewBox.grid(row=12, column=10)
login.grid(row=13, column=10)
message = Label(root, text="")
message.grid(row=14, column=10)

#TODO display last user behind the machine
#TODO radio button from left to right
#TODO graphical shit, Logo, Big label,
#TODO Table for feedback

root.mainloop()
