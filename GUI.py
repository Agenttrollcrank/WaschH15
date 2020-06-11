from tkinter import *
import mysql.connector
from tkinter import ttk
import bcrypt
import time

# mysql connection all the login data
mydb = mysql.connector.connect(
    user='Yulian',
    password='FreddyIstGeil',
    host='134.130.188.10',
    database='h15')

mycursor = mydb.cursor(buffered=True)  # mysql cursor definition

# define the windown
root = Tk()
root.title("WaschH15")
root.geometry("1080x850")

Wasch = LabelFrame(root, padx=5, pady=5)
Table = LabelFrame(root, padx=5, pady=5)

try:
    logo = PhotoImage(file="D:/Github/WaschH15/hermann-logo-40.png")
except:
    pass
# variable definitions

electricityOldValue = int
# define the function for buttons
def logout(): # excecute button
    # credential checkg
    mycursor.execute("SELECT username FROM h15.abrechnung WHERE MATCH(machine) AGAINST('%s') ORDER BY Strom_von DESC limit 0,1" % (machineString.get()))
    lastuser = str(mycursor.fetchone())
    lastuser = lastuser.replace("('","")
    lastuser = lastuser.replace("',)","")
    mycursor.execute("SELECT Strom_bist FROM h15.abrechnung WHERE MATCH(machine) AGAINST('%s') ORDER BY Strom_von DESC limit 0,1" % (machineString.get()))
    electricityCurrent = str(mycursor.fetchone())
    electricityCurrent = electricityCurrent.replace("(","")
    electricityCurrent = electricityCurrent.replace(",)","")
    mycursor.execute("SELECT COUNT(1) FROM h15.benutzer WHERE username='%s'" % (usernameOptions.get())) #checks that the username is in the mysql table
    if mycursor.fetchone()[0]:# my cursor returns 0 if there is such a username
        mycursor.execute("SELECT Passwort FROM h15.benutzer WHERE username='%s'" % (usernameOptions.get())) #same thing for the password
        hashed = str(mycursor.fetchone())
        hashed = hashed.replace("('", "")
        hashed = hashed.replace("',)", "")
        if bcrypt.checkpw((passwordIN.get()).encode("utf-8"), hashed.encode("utf-8")):
            try:
                if float(electricityInBox.get()) >= electricityOldValue:
                    try:
                        if lastuser == usernameOptions.get() and electricityCurrent == "None":
                            mycursor.execute("UPDATE h15.abrechnung SET Strom_bist = %s WHERE username = '%s' AND machine = '%s' ORDER BY Strom_von DESC LIMIT 1" % (str(electricityInBox.get()), usernameOptions.get(), machineString.get()))
                        else:
                            if float(electricityCurrent) != float(electricityInBox.get()):
                                mycursor.execute("INSERT INTO abrechnung VALUES('%s','%s',%s,%s)" % ("Kameradenschwein", str(machineString.get()), str(electricityOldValue), electricityInBox.get()))
                            mycursor.execute("INSERT INTO abrechnung VALUES('%s','%s',%s,%s)" % (str(usernameOptions.get()), str(machineString.get()), electricityInBox.get(), "NULL"))
                        mycursor.execute("UPDATE h15.strom SET Kwh = " + str(electricityInBox.get()) + " WHERE Waschmachine = '" + str(machineString.get()) + "'")
                        message.config(text="Alles Klar! Danke dir! :D")
                        electricityInBox.delete(0, END)
                        electricityInBox.insert(0, electricityInBox.get())
                        passwordIN.delete(0, END)
                    except:
                        message.config(text="Irgendein Error ist aufgetreten, sorry... ")
                else:  # ValueError
                    message.config(text="Bitte geben Sie einen größeren Wert ein")
                electricityInBox.delete(0, END)
            except ValueError:
                message.config(text="Bitte eine Zahl Eingeben")
            except:
                message.config(text="Irgendein Error ist aufgetreten, sorry... ")
        else:
            message.config(text="Falsche Passwort")
    else:
        message.config(text="Falsche Benutzername")
    mydb.commit()
    tableUpdate(str(machineString.get()))

def tableUpdate(mch):
    headings = ["Name","Strom Von","Strom Bist"]
    values = ["username","Strom_von","Strom_bist"]
    for row in range(5):
        if row == 0:
            for column in range(3):
                label = Label(Table, text=headings[column], bg="white", fg="black", padx=30, pady=3)
                label.grid(row=row,column=(column),sticky="nsew",padx=1,pady=1)
                label.config(font=('Arial', 18, "bold"))
                Table.grid_columnconfigure((column),weight=1)
        else:
            for column in range(3):
                mycursor.execute("SELECT %s FROM h15.abrechnung WHERE MATCH(machine) AGAINST('%s') ORDER BY Strom_von DESC limit %s,1" % (str(values[column]), mch, str(row-1)))
                label = Label(Table, text=mycursor.fetchone(), bg="white", fg="black", padx=30, pady=3)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.config(font=('Arial', 18))
                Table.grid_columnconfigure(column, weight=1)

#defining the radio buttons
def newSelection(): #machine choice buttons, changes the text and previous value
    global electricityOldValue
    machineSelection.config(text=machineString.get())
    if machineString.get() == "Altbau":
        sl = 0
        tableUpdate("Altbau")
    elif machineString.get() == "Linke_Maschine":
        sl = 1
        tableUpdate("Linke_Maschine")
    elif machineString.get() == "Mittlere_Maschine":
        sl = 2
        tableUpdate("Mittlere_Maschine")
    elif machineString.get() == "Rechte_Maschine":
        sl = 3
        tableUpdate("Rechte_Maschine")
    elif machineString.get() == "Trockner_Oben":
        sl = 4
        tableUpdate("Trockner_Oben")
    elif machineString.get() == "Trockner_Unten":
        sl = 5
        tableUpdate("Trockner_Unten")
    else:
        exit(1)
    mycursor.execute("SELECT Kwh FROM h15.strom LIMIT " + str(sl) +",1")
    electricityOldValue = str(mycursor.fetchone())
    electricityOldValue = electricityOldValue.replace("(", "")
    electricityOldValue = electricityOldValue.replace(",)", "")
    electricityOldValue = float(electricityOldValue)
    electricityInBox.delete(0, END)
    electricityInBox.insert(0, electricityOldValue)

MACHINES = [
    ("Altbau", "Altbau"),
    ("Linke Maschine", "Linke_Maschine"),
    ("Mittlere Maschine", "Mittlere_Maschine"),
    ("Rechte Maschine", "Rechte_Maschine"),
    ("Trockner Oben", "Trockner_Oben"),
    ("Trockner Unten", "Trockner_Unten")
]

# username combobox
mycursor.execute("SELECT username FROM h15.benutzer")
usernames = mycursor.fetchall()
usercount = 0

for user in usernames:
    clean = str(user).replace("('","")
    clean = clean.replace("',)","")
    usernames[usercount] = clean
    usercount += 1

usernameOptions = ttk.Combobox(Wasch, value=usernames)
usernameOptions.current(0)
passwordIN = Entry(Wasch, show="*", width=25)
electricityInBox = Entry(Wasch, width=25)
logout = Button(Wasch, text="Eintragen", command=logout)
titleLabel = Label(root, text="WaschH15")
usernameLabel = Label(Wasch, text="Benutzername: ")
passwordLabel = Label(Wasch, text="Passwort: ")
machineSelection = Label(Wasch, text="")
electricityInLabel = Label(Wasch, text="Strom Stand: ")

# drawing the radio buttons on the screen
machineString = StringVar()
line = 3
for text, machine in MACHINES:
    button = Radiobutton(Wasch, text=text, variable=machineString, value=machine, tristatevalue=0, command=lambda: newSelection())
    button.grid(row=line, column=1, sticky="w")
    button.config(font=('Arial', 18))
    line += 1

# showing it on screen
try:
    logolabel = Label(root, image=logo, justify=RIGHT)
    logolabel.pack()
except:
    pass
# all the config and displaying items in the window
titleLabel.pack()
titleLabel.config(font=('Arial', 24))
Wasch.pack()
Table.pack()
usernameLabel.grid(row=1, column=0)
usernameLabel.config(font=('Arial', 18))
usernameOptions.grid(row=1, column=1)
usernameOptions.config(font=('Arial', 18))
passwordLabel.grid(row=2, column=0)
passwordLabel.config(font=('Arial', 18))
passwordIN.grid(row=2, column=1)
passwordIN.config(font=('Arial', 18))
electricityInLabel.grid(row=12, column=0)
electricityInLabel.config(font=('Arial', 18))
electricityInBox.grid(row=12, column=1)
electricityInBox.config(font=('Arial', 18))
logout.grid(row=13, column=1,sticky="w")
logout.config(font=('Arial', 18))
message = Label(Wasch, text="")
message.config(font=('Arial', 18))
message.grid(row=14, column=0)

root.mainloop()