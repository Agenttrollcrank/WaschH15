from tkinter import *
import mysql.connector

#mysql connection
mydb = mysql.connector.connect(
    user='root',
    password='root',
    host='127.0.0.1',
    database='sys')

mycursor = mydb.cursor(buffered=True)


#define the windown
root = Tk()
root.title("WaschH15")
root.geometry("500x500")

#variable definitions
electricityOldValue = 0 #defined because it needs to be public
sl = 0

#define the function for buttons
def myClick(): #excecute button
    #credential check
    mycursor.execute("SELECT COUNT(1) FROM sys.benutzer WHERE username='%s'" % (usernameIN.get()))
    if mycursor.fetchone()[0]:
        mycursor.execute("SELECT COUNT(1) FROM sys.benutzer WHERE passwort='%s'" % (passwordIN.get()))
        if mycursor.fetchone()[0]:
            try: #checks the value inputted
                if int(electricityNewBox.get()) >= electricityOldValue:
                    mycursor.execute(
                        "UPDATE sys.strom SET Kwh = " + str(electricityNewBox.get()) + " WHERE Waschmachine = '" + str(
                            machineString.get()) + "'")
                else:
                    Label(root, text="Bitte geben Sie einen größeren Wert ein").grid(row=14, column=9)
            except:  # ValueError
                Label(root, text="Bitte geben Sie eine Zahl ein").grid(row=14, column=9)
            electricityOldBox.delete(0, END)
            electricityNewBox.delete(0, END)
            usernameIN.delete(0, END)
            passwordIN.delete(0, END)
        else:
            Label(root, text="Falsche Password").grid(row=14, column=9)
    else:
        Label(root, text="Unbekante Benutzername").grid(row=14, column=9)
    mydb.commit()
    #TODO add new entry
    #TODO take the new electricity value from the database

def newSelection(): #machine choice buttons, changes the text and previous value
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
    mycursor.execute("SELECT Kwh FROM sys.strom LIMIT " + str(sl) +",1")
    electricityOldValue = mycursor.fetchall()
    electricityOldBox.delete(0, END)
    electricityOldBox.insert(0, electricityOldValue)


titleLabel = Label(root, text="WaschH15")
machineSelection = Label(root, text="")

usernameIN = Entry(root, width=40)
passwordIN = Entry(root, width=40)
electricityOldBox = Entry(root, width=40)
electricityOldBox.insert(0,0)
electricityNewBox = Entry(root, width=40)

login = Button(root, text="Login", command=myClick, bg="#ff00ff")
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

root.mainloop()
