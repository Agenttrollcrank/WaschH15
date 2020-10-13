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

AbbrechnungFrame = Frame(Notebook)

AbbrechnungFrame.pack(fill="both", expand=1)

Notebook.add(AbbrechnungFrame, text="AbbrechnungFrame")

Table = LabelFrame(root, padx=5, pady=5)


# variable definitions
electricityOldValue = int
electricityPosb = [0]
etagen = ["1","2","3","4","Altbau","Hinterlieger","Ehepaar_Neubau","Ehepaar_Hinterlieger","Einzel_Wohnung"]


def Abbrechnung():
    # Open and read the file as a single buffer
    fd = open('D:\Github\WaschH15\SQL Skripts and Tables\Abrechnungsskript.sql', 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            print(command)
            mycursor.execute(command)
        except():
            print("Command skipped: ", command)
    mydb.commit()

MACHINES = [
    ("Altbau", "Altbau"),
    ("Linke Maschine", "Linke_Maschine"),
    ("Mittlere Maschine", "Mittlere_Maschine"),
    ("Rechte Maschine", "Rechte_Maschine"),
    ("Trockner Oben", "Trockner_Oben"),
    ("Trockner Unten", "Trockner_Unten")
]
#abrechnung
def AbrechnungTable():
    Abbrechnung()
    headings = ["Nachname","Kosten","Verbrauch","etage"]
    for row in range(20):
        if row == 0:
            for column in range(4):
                label = Label(Table, text=headings[column], bg="white", fg="black", padx=30, pady=3)
                label.grid(row=row,column=(column),sticky="nsew",padx=1,pady=1)
                label.config(font=('Arial', 10, "bold"))
                Table.grid_columnconfigure((column),weight=1)
        else:
            for column in range(4):
                mycursor.execute("SELECT %s FROM h15.Zusammenfassung ORDER BY Nachname DESC limit %s,1" % (str(headings[column]), str(row-1)))
                label = Label(Table, text=mycursor.fetchone(), bg="white", fg="black", padx=30, pady=3)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.config(font=('Arial', 10))
                Table.grid_columnconfigure(column, weight=1)

abrechnenButton = Button(AbbrechnungFrame, text="Registrieren", command=AbrechnungTable)
abrechnenButton.grid(row=1, column=1)
#all the config and displaying items in the window
Table.pack()
message = Label(root, text="")
message.config(font=('Arial', 18))
message.pack()

root.mainloop()