from tkinter import *
import mysql.connector
from tkinter import ttk
import bcrypt

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


try:
    logo = PhotoImage(file="D:/Github/WaschH15/hermann-logo-40.png")
    logolabel = Label(root, image=logo, justify=RIGHT)
    logolabel.pack()
except:
    pass
titleLabel = Label(root, text="WaschH15")
titleLabel.pack()
titleLabel.config(font=('Arial', 24))

Notebook = ttk.Notebook(root)
Notebook.pack(pady=15)

WaschGUI = Frame(Notebook)
ChangePasswordFrame = Frame(Notebook)

WaschGUI.pack(fill="both", expand=1)
ChangePasswordFrame.pack(fill="both", expand=1)

Notebook.add(WaschGUI, text="Waschen")
Notebook.add(ChangePasswordFrame, text="Passwort ändern")

Table = LabelFrame(root, padx=5, pady=5)

# variable definitions
electricityOldValue = int
electricityPosb = [0]
etagen = ["1","2","3","4","Altbau","Hinterlieger","Ehepaar_Neubau","Ehepaar_Hinterlieger","Einzel_Wohnung"]

# confirmation window
def Confirm(oldElectricity,newElectricity):
    top = Toplevel()
    top.grab_set()
    top.title("Bestätigung")
    Label(top, text="Alter Stromstand: %s" % (str(oldElectricity)), font=('Arial',14)).pack()
    Label(top, text="Neuer Stromstand: %s" % (str(newElectricity)), font=('Arial', 14)).pack()
    Button(top, text="Bestätigen", command=lambda: [top.destroy(), SendNewRecord()],font=('Arial', 14)).pack()
    Button(top, text="Exit", command=top.destroy, font=('Arial', 14)).pack()
    top.update_idletasks()
    width = 220
    height = 150
    x = (top.winfo_screenwidth() // 2) - (width // 2)
    y = (top.winfo_screenheight() // 2) - (height // 2)
    top.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def SendNewRecord():
    global lastuser
    global electricityCurrent
    try:
        if lastuser == usernameOptions and electricityCurrent == "None":
            mycursor.execute(
                "UPDATE h15.abrechnung SET Strom_bis = %s WHERE username = '%s' AND machine = '%s' ORDER BY Strom_von DESC LIMIT 1" % (
                str(electricityInBox.get()), usernameOptions, machineString.get()))
        else:
            if (electricityCurrent != electricityInBox.get()) and electricityCurrent != "None":
                mycursor.execute("INSERT INTO abrechnung VALUES('%s','%s',%s,%s)" % (
                "Kameradenschwein", str(machineString.get()), str(electricityOldValue), electricityInBox.get()))
            else:
                if electricityInBox.get() != electricityOldValue:
                    mycursor.execute(
                        "UPDATE h15.abrechnung SET Strom_bis = %s WHERE username = '%s' AND machine = '%s' ORDER BY Strom_von DESC LIMIT 1" % (
                            str(electricityInBox.get()), lastuser, machineString.get()))
            mycursor.execute("INSERT INTO abrechnung VALUES('%s','%s',%s,%s)" % (
            str(usernameOptions), str(machineString.get()), electricityInBox.get(), "NULL"))
        mycursor.execute("UPDATE h15.strom SET Kwh = " + str(electricityInBox.get()) + " WHERE Waschmachine = '" + str(
            machineString.get()) + "'")
        message.config(text="Alles Klar, Danke Dir :D Die Tabelle wird aktualisiert")
        electricityInBox.delete(0, END)
        electricityInBox.insert(0, electricityInBox.get())
        passwordIN.delete(0, END)
        electricityInBox.delete(0, END)
        mydb.commit()
        TableUpdate(str(machineString.get()))
        NewSelection()
    except:
        message.config(text="Irgendwas ist schief gelaufen, melde dich beim Netzwerkverein")
    finally:
        root.update_idletasks()
        root.after(2000, message.config(text=""))


# define the function for buttons

def Logout(): # excecute button
    global lastuser
    global electricityCurrent
    global sl
    # credential check
    mycursor.execute("SELECT username FROM h15.abrechnung WHERE machine = '%s' ORDER BY Strom_von DESC limit 0,1" % (machineString.get()))
    lastuser = str(mycursor.fetchone())
    lastuser = lastuser.replace("('","")
    lastuser = lastuser.replace("',)","")
    mycursor.execute("SELECT Strom_bis FROM h15.abrechnung WHERE machine = '%s' ORDER BY Strom_von DESC limit 0,1" % (machineString.get()))
    electricityCurrent = str(mycursor.fetchone())
    electricityCurrent = electricityCurrent.replace("(","")
    electricityCurrent = electricityCurrent.replace(",)","")
    mycursor.execute("SELECT COUNT(1) FROM h15.benutzer WHERE username='%s'" % usernameOptions) #checks that the username is in the mysql table
    if mycursor.fetchone()[0]:# my cursor returns 0 if there is such a username
        mycursor.execute("SELECT Passwort FROM h15.benutzer WHERE username='%s'" % usernameOptions) #same thing for the password
        hashed = str(mycursor.fetchone())
        hashed = hashed.replace("('", "")
        hashed = hashed.replace("',)", "")
        if bcrypt.checkpw((passwordIN.get()).encode("utf-8"), hashed.encode("utf-8")):
            if float(electricityInBox.get()) >= electricityOldValue:
                Confirm(electricityOldValue, electricityInBox.get())
            else:
                message.config(text="Bitte gib einen größeren Wert ein")
        else:
            message.config(text="Falsches Passwort")
    else:
        message.config(text="Falscher Benutzername")

def TableUpdate(mch):
    headings = ["Name","Strom Von","Strom Bis"]
    values = ["username","Strom_von","Strom_bis"]
    for row in range(6):
        if row == 0:
            for column in range(3):
                label = Label(Table, text=headings[column], bg="white", fg="black", padx=30, pady=3)
                label.grid(row=row,column=(column),sticky="nsew",padx=1,pady=1)
                label.config(font=('Arial', 16, "bold"))
                Table.grid_columnconfigure((column),weight=1)
        else:
            for column in range(3):
                mycursor.execute("SELECT %s FROM h15.abrechnung WHERE abrechnung.machine='%s' ORDER BY Strom_von DESC limit %s,1" % (str(values[column]), mch, str(row-1)))
                label = Label(Table, text=mycursor.fetchone(), bg="white", fg="black", padx=30, pady=3)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.config(font=('Arial', 16))
                Table.grid_columnconfigure(column, weight=1)


#defining the radio buttons
def NewSelection(): #machine choice buttons, changes the text and previous value
    global electricityPosb
    global electricityOldValue
    global electricityInBox
    machineSelection.config(text=machineString.get())
    if machineString.get() == "Altbau":
        sl = 0
        TableUpdate("Altbau")
    elif machineString.get() == "Linke_Maschine":
        sl = 1
        TableUpdate("Linke_Maschine")
    elif machineString.get() == "Mittlere_Maschine":
        sl = 2
        TableUpdate("Mittlere_Maschine")
    elif machineString.get() == "Rechte_Maschine":
        sl = 3
        TableUpdate("Rechte_Maschine")
    elif machineString.get() == "Trockner_Oben":
        sl = 4
        TableUpdate("Trockner_Oben")
    elif machineString.get() == "Trockner_Unten":
        sl = 5
        TableUpdate("Trockner_Unten")
    else:
        exit(1)
    mycursor.execute("SELECT Kwh FROM h15.strom LIMIT " + str(sl) +",1")
    electricityOldValue = str(mycursor.fetchone())
    electricityOldValue = electricityOldValue.replace("(", "")
    electricityOldValue = electricityOldValue.replace(",)", "")
    electricityOldValue = float(electricityOldValue)
    electricityInBox.delete(0, END)
    electricityInBox.insert(0, electricityOldValue)
    electricityPosb = []
    for pos in range(1, 15):
        pos = pos / 10
        electricityPosb.append(round(electricityOldValue + pos, 1))
    electricityInBox.config(value=electricityPosb)

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

userCount = 0

for user in usernames:
    clean = user[0]
    usernames[userCount] = clean
    userCount += 1

def on_keyrelease(event):
    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()

    # get data from test_list
    if value == '':
        data = " "
    else:
        data = []
        for item in usernames:
            if value in item.lower():
                data.append(item)

    # update data in listbox
    listbox_update(data)

def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')
    # sorting data
    data = sorted(data, key=str.lower)
    # put new data
    for item in data:
        listbox.insert('end', item)

def on_select(event):
    # display element selected on list
    global usernameOptions
    try:
        usernameOptions = event.widget.get(event.widget.curselection())
    except:
        None
    entry.delete(0, END)
    entry.insert(0, usernameOptions)

entry = Entry(WaschGUI)
entry.grid(row=1, column=1, sticky="w")
entry.config(font=('Arial', 16))
entry.bind('<KeyRelease>', on_keyrelease)

listbox = Listbox(WaschGUI, height=4)
listbox.grid(row=2, column=1,sticky="w")
listbox.config(font=('Arial', 16))
listbox.bind('<<ListboxSelect>>', on_select)
listbox_update(usernames)

passwordIN = Entry(WaschGUI, show="*", width=25)
electricityInBox = ttk.Combobox(WaschGUI, value=electricityPosb)
electricityInBox.current(0)
logout = Button(WaschGUI, text="Eintragen", command=Logout)

usernameLabel = Label(WaschGUI, text="Benutzername: ")
passwordLabel = Label(WaschGUI, text="Passwort: ")
machineSelection = Label(WaschGUI, text="")
electricityInLabel = Label(WaschGUI, text="Stromstand: ")

# drawing the radio buttons on the screen
machineString = StringVar()
line = 4
for text, machine in MACHINES:
    button = Radiobutton(WaschGUI, text=text, variable=machineString, value=machine, tristatevalue=0, command=lambda: NewSelection())
    button.grid(row=line, column=1, sticky="w")
    button.config(font=('Arial', 16))
    line += 1
# change password screen
EntryBoxesPassword = []
def ChangePassword():
    entrylistPassword = []
    for entries in EntryBoxesPassword:
        entrylistPassword.append(entries.get())
    hashed = bcrypt.hashpw(entrylistPassword[3].encode("utf-8"), bcrypt.gensalt())
    hashed = str(hashed).replace("b'", "")
    hashed = str(hashed).replace("'", "")
    if entrylistPassword[4] == entrylistPassword[3] and entrylistPassword[4] != "":
        mycursor.execute("SELECT Passwort FROM h15.benutzer WHERE username='%s'" % (
            entrylistPassword[5]))  # same thing for the password
        hashedold = str(mycursor.fetchone())
        hashedold = hashedold.replace("('", "")
        hashedold = hashedold.replace("',)", "")
        if bcrypt.checkpw(entrylistPassword[2].encode("utf-8"), hashedold.encode("utf-8")):
            try:
                mycursor.execute("UPDATE benutzer SET Passwort = '%s' WHERE Vorname = '%s' AND Nachname = '%s' AND Username = '%s' AND Etage = '%s'" % (hashed, entrylistPassword[0], entrylistPassword[1], entrylistPassword[5], entrylistPassword[6]))
                print("UPDATE benutzer SET Passwort = '%s' WHERE Vorname = '%s' AND Nachname = '%s' AND Username = '%s' AND Etage = '%s'" % (hashed, entrylistPassword[0], entrylistPassword[1], entrylistPassword[5], entrylistPassword[6]))
                message.config(text="Passwort wurde aktualisiert")
            except:
                message.config(text="Es gibt einen Fehler sorry, versuche es nochmal")
        else:
            message.config(text="Falsches altes Passwort")
    else:
        message.config(text="Passwörter stimmen nicht überein")
    mydb.commit()
    for entries in EntryBoxesPassword:
        entries.delete(0, END)

LabelsReset = ["Vorname", "Nachname", "Alte Passwort", "Neues Passwort","Neues Passwort Wiederholen", "Username", "Etage"]
for i, entryType in enumerate(LabelsReset):
    label = Label(ChangePasswordFrame, text=entryType + ": ")
    if entryType == "Passwort":
        entryBox = Entry(ChangePasswordFrame, show="*", width=25)
    else:
        entryBox = Entry(ChangePasswordFrame, width=25)
    label.grid(row=i, column=0)
    entryBox.grid(row=i, column=1)
    label.config(font=('Arial', 16))
    entryBox.config(font=('Arial', 16))
    EntryBoxesPassword.append(entryBox)

ChangePasswordButton = Button(ChangePasswordFrame, text="Zurücksetzen", command=ChangePassword)
ChangePasswordButton.grid(row=8, column=1)

Table.pack()
usernameLabel.grid(row=1, column=0)
usernameLabel.config(font=('Arial', 16))
passwordLabel.grid(row=3, column=0)
passwordLabel.config(font=('Arial', 16))
passwordIN.grid(row=3, column=1)
passwordIN.config(font=('Arial', 16))
electricityInLabel.grid(row=13, column=0)
electricityInLabel.config(font=('Arial', 16))
electricityInBox.grid(row=13, column=1)
electricityInBox.config(font=('Arial', 16))
logout.grid(row=14, column=1,sticky="w")
logout.config(font=('Arial', 16))
message = Label(root, text="")
message.config(font=('Arial', 16))
message.pack()

root.mainloop()