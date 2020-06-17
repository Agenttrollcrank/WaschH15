from tkinter import *
import mysql.connector
from tkinter import ttk
import bcrypt

mydb = mysql.connector.connect(
    user='Yulian',
    password='FreddyIstGeil',
    host='134.130.188.10',
    database='h15')

mycursor = mydb.cursor(buffered=True)  # mysql cursor definition
PowerWindow = Tk()  # define the windown
PowerWindow.title("Register")
PowerWindow.geometry("500x500")

etagen = ["1","2","3","4","Altbau","Hinterlieger","Ehepaar_Neubau","Ehepaar_Hinterlieger","Einzel_Wohnung"]

Notebook = ttk.Notebook(PowerWindow)
Notebook.pack(pady=15)

RegisterFrame = Frame(Notebook)
PasswordResetFrame = Frame(Notebook)

RegisterFrame.pack(fill="both", expand=1)
PasswordResetFrame.pack(fill="both", expand=1)

Notebook.add(RegisterFrame, text="Register")
Notebook.add(PasswordResetFrame, text="Password Reset")


def Register():
    entrylistRegister = []
    for entries in EntryBoxesRegister:
        entrylistRegister.append(entries.get())
    hashed = bcrypt.hashpw(entrylistRegister[2].encode("utf-8"), bcrypt.gensalt())
    hashed = str(hashed).replace("b'", "")
    hashed = str(hashed).replace("'", "")
    if entrylistRegister[2] == entrylistRegister[3] and entrylistRegister[2] != "":
        if any(entrylistRegister[5] == etage for etage in etagen):
            try:
                mycursor.execute("INSERT INTO benutzer (Vorname,Nachname,Passwort,Username,Etage) VALUES ('%s', '%s', '%s', '%s', '%s')"
                                 %(entrylistRegister[0], entrylistRegister[1], hashed, entrylistRegister[4], entrylistRegister[5]))
                mydb.commit()
                message.config(text="Benutzer wurde erfolgreich \n zum System hinzugefügt")
                for entries in EntryBoxesRegister:
                    entries.delete(0, END)
            except:
                message.config(text="Falsche datan eingegeben")
        else:
            message.config(text="Bitte eine akzeptabel Etage eingeben. Versuche es nochmal")
            EntryBoxesRegister[5].delete(0, END)

    else:
        message.config(text="Passwort sind nicht gleich. Versuche es nochmal")
        EntryBoxesRegister[2].delete(0, END)
        EntryBoxesRegister[3].delete(0, END)


def ResetPassword():
    entrylistPassword = []
    for entries in EntryBoxesPassword:
        entrylistPassword.append(entries.get())
    hashed = bcrypt.hashpw(entrylistPassword[3].encode("utf-8"), bcrypt.gensalt())
    hashed = str(hashed).replace("b'", "")
    hashed = str(hashed).replace("'", "")
    if entrylistPassword[4] == entrylistPassword[3] and entrylistPassword[4] != "":
        try:
            mycursor.execute("UPDATE benutzer SET Passwort = '%s' WHERE Vorname = '%s' AND Nachname = '%s' AND Username = '%s' AND Etage = '%s'" % (hashed, entrylistPassword[0], entrylistPassword[1], entrylistPassword[4], entrylistPassword[5]))
        except:
            message.config(text="Falsche datan eingegeben")
    mydb.commit()
    message.config(text="Passwort wurde Aktualisiert")
    for entries in EntryBoxesPassword:
        entries.delete(0, END)

# things played on the screen
LabelsRegister = ["Vorname", "Nachname", "Passwort", "Passwort Wiederholen","Username", "Etage"]
EntryBoxesRegister = []
EntryBoxesPassword = []
for i, entryType in enumerate(LabelsRegister):
    label = Label(RegisterFrame, text=entryType + ": ")
    if entryType == "Passwort" or entryType == "Passwort Wiederholen":
        entryBox = Entry(RegisterFrame, show="*", width=25)
    if entryType == "Etage":
        entryBox = ttk.Combobox(RegisterFrame, value=etagen)
    else:
        entryBox = Entry(RegisterFrame, width=25)
    label.grid(row=i, column=0)
    entryBox.grid(row=i, column=1)
    label.config(font=('Arial', 18))
    entryBox.config(font=('Arial', 18))
    EntryBoxesRegister.append(entryBox)

LabelsReset = ["Vorname", "Nachname", "Alte Passwort", "Neues Password","Neues Password Wiederholen" "Username", "Etage"]
for i, entryType in enumerate(LabelsReset):
    label = Label(PasswordResetFrame, text=entryType + ": ")
    if entryType == "Passwort":
        entryBox = Entry(PasswordResetFrame, show="*", width=25)
    else:
        entryBox = Entry(PasswordResetFrame, width=25)
    label.grid(row=i, column=0)
    entryBox.grid(row=i, column=1)
    label.config(font=('Arial', 18))
    entryBox.config(font=('Arial', 18))
    EntryBoxesPassword.append(entryBox)

registerButton = Button(RegisterFrame, text="Eintragen", command=Register)
registerButton.grid(row=6, column=1)
resetButton = Button(PasswordResetFrame, text="Reset", command=ResetPassword)
resetButton.grid(row=6, column=1)
message = Label(PowerWindow, text="")
message.config(font=('Arial', 18))
message.pack()

PowerWindow.mainloop()
