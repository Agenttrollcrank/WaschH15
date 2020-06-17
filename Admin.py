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
    mycursor.execute("INSERT INTO benutzer (Vorname,Nachname,Passwort,Username,Etage) VALUES ('%s', '%s', '%s', '%s', '%s')"
                     %(entrylistRegister[0], entrylistRegister[1], hashed, entrylistRegister[3], entrylistRegister[4]))
    mydb.commit()
    message.config(text="Benutzer wurde erfolgreich \n zum System hinzugefügt")
    for entries in EntryBoxesRegister:
        entries.delete(0, END)


def ResetPassword():
    entrylistPassword = []
    for entries in EntryBoxesPassword:
        entrylistPassword.append(entries.get())
    hashed = bcrypt.hashpw(entrylistPassword[3].encode("utf-8"), bcrypt.gensalt())
    hashed = str(hashed).replace("b'", "")
    hashed = str(hashed).replace("'", "")
    print("UPDATE benutzer SET Passwort = '%s' WHERE Vorname = '%s' AND Nachname = '%s' AND Username = '%s' AND Etage = '%s'"
                     % (hashed, entrylistPassword[0], entrylistPassword[1], entrylistPassword[4], entrylistPassword[5]))
    mycursor.execute("UPDATE benutzer SET Passwort = '%s' WHERE Vorname = '%s' AND Nachname = '%s' AND Username = '%s' AND Etage = '%s'"
                     % (hashed, entrylistPassword[0], entrylistPassword[1], entrylistPassword[4], entrylistPassword[5]))
    mydb.commit()
    message.config(text="Passwort wurde Aktualisiert")
    for entries in EntryBoxesPassword:
        entries.delete(0, END)

# things played on the screen
LabelsRegister = ["Vorname", "Nachname", "Passwort", "Username", "Etage"]
EntryBoxesRegister = []
EntryBoxesPassword = []
for i, entryType in enumerate(LabelsRegister):
    label = Label(RegisterFrame, text=entryType + ": ")
    if entryType == "Passwort":
        entryBox = Entry(RegisterFrame, show="*", width=25)
    else:
        entryBox = Entry(RegisterFrame, width=25)
    label.grid(row=i, column=0)
    entryBox.grid(row=i, column=1)
    label.config(font=('Arial', 18))
    entryBox.config(font=('Arial', 18))
    EntryBoxesRegister.append(entryBox)

LabelsReset = ["Vorname", "Nachname", "Alte_Passwort", "Neue_Password", "Username", "Etage"]
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
