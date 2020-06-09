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
root.geometry("1920x1080")

Wasch = LabelFrame(root, padx=5, pady=5)
Table = LabelFrame(root, padx=5, pady=5)

try:
    logo = PhotoImage(file="C:/Users/Yulian/Desktop/WaschH15-master/hermann-logo-40.png")
except:
    pass

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
                try:#checks the value inputted
                    mycursor.execute("UPDATE h15.strom SET Kwh = " + str(electricityNewBox.get()) +
                                     " WHERE Waschmachine = '" + str(machineString.get()) + "'")
                    mycursor.execute("INSERT INTO abrechnung VALUES('%s','%s',%s,%s)" % (
                    str(usernameIN.get()), str(machineString.get()), str(electricityOldValue[0]),
                    str(electricityNewBox.get())))
                    message.config(text="Alles Klar! Danke dir! :D")
                    electricityOldBox.delete(0, END)
                    electricityOldBox.insert(0, electricityNewBox.get())
                    usernameIN.delete(0, END)
                    passwordIN.delete(0, END)
                except:
                    message.config(text="Irgendein Error ist aufgetreten, sorry...")
            else:  # ValueError
                message.config(text="Bitte geben Sie einen größeren Wert ein")
            electricityNewBox.delete(0, END)
        else:
            message.config(text="Falsche Passwort")
    else:
        message.config(text="Falsche Benutzername")
    mydb.commit()
    tableUpdate(str(machineString.get()))
def tableUpdate(mch):
    headings = ["Name","Strom Von","Strom bis"]
    values = ["username","Strom_von","Strom_bis"]
    for row in range(5):
        if row == 0:
            for column in range(3):
                label = Label(Table, text=headings[column], bg="white", fg="black", padx=30, pady=3)
                label.grid(row=row,column=(column),sticky="nsew",padx=1,pady=1)
                label.config(font=('Arial', 18, "bold"))
                Table.grid_columnconfigure((column),weight=1)
        else:
            for column in range(3):
                mycursor.execute("SELECT %s FROM h15.abrechnung WHERE MATCH(machine) AGAINST('%s') LIMIT %s,1" % (str(values[column]), mch, (row-1)))
                label = Label(Table, text=mycursor.fetchone(), bg="white", fg="black", padx=30, pady=3)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.config(font=('Arial', 18))
                Table.grid_columnconfigure(column, weight=1)



titleLabel = Label(root, text="WaschH15")
try:
    logolabel = Label(root, image=logo, justify=RIGHT)
    logolabel.pack()
except:
    pass
usernameLabel = Label(Wasch, text="Benutzername: ")
passwordLabel = Label(Wasch, text="Passwort: ")
machineSelection = Label(Wasch, text="")
usernameIN = Entry(Wasch, width=25)
passwordIN = Entry(Wasch, show="*", width=25)
electricityOldBox = Entry(Wasch, width=25)
electricityOldBox.insert(0,0)
electricityNewBox = Entry(Wasch, width=25)
login = Button(Wasch, text="WASCHEN!!!", command=myClick)

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
    electricityOldValue = mycursor.fetchone()
    electricityOldBox.delete(0, END)
    electricityOldBox.insert(0, electricityOldValue)
MACHINES = [
    ("Altbau", "Altbau"),
    ("Linke Maschine", "Linke_Maschine"),
    ("Mittlere Maschine", "Mittlere_Maschine"),
    ("Rechte Maschine", "Rechte_Maschine"),
    ("Trockner Oben", "Trockner_Oben"),
    ("Trockner Unten", "Trockner_Unten")
]
#drawing the radio buttons on the screen
machineString = StringVar()
line = 3
for text, machine in MACHINES:
    button = Radiobutton(Wasch, text=text, variable=machineString, value=machine, tristatevalue=0, command=lambda: newSelection())
    button.grid(row=line, column=1, sticky="w")
    button.config(font=('Arial', 18))
    line += 1

#showing it on screen

titleLabel.pack()
titleLabel.config(font=('Arial', 24))
Wasch.pack()
Table.pack()

usernameLabel.grid(row=1, column=0)
usernameLabel.config(font=('Arial', 18))
usernameIN.grid(row=1, column=1)
usernameIN.config(font=('Arial', 18))

passwordLabel.grid(row=2, column=0)
passwordLabel.config(font=('Arial', 18))
passwordIN.grid(row=2, column=1)
passwordIN.config(font=('Arial', 18))

electricityOldLabel = Label(Wasch, text="Vorheriger Strom Stand: ")
electricityOldLabel.grid(row=11, column=0)
electricityOldLabel.config(font=('Arial', 18))

electricityOldBox.grid(row=11, column=1)
electricityOldBox.config(font=('Arial', 18))

electricityNewLabel = Label(Wasch, text="Neuer Strom Stand: ")
electricityNewLabel.grid(row=12, column=0)
electricityNewLabel.config(font=('Arial', 18))

electricityNewBox.grid(row=12, column=1)
electricityNewBox.config(font=('Arial', 18))

login.grid(row=13, column=1,sticky="w")
login.config(font=('Arial', 18))

message = Label(Wasch, text="")
message.config(font=('Arial', 18))
message.grid(row=14, column=0)


root.mainloop()