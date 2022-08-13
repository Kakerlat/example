import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import dates as mpl_dates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd='KobusKoetsee12!'
# )


#
# c.execute("CREATE DATABASE IF NOT EXISTS bank")
#
# db.commit()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='KobusKoetsee12!',
    database="bank"
)

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS bankdetials(
             pin VARCHAR(20) PRIMARY KEY,
             first_name VARCHAR(255) NOT NULL,
             last_name VARCHAR(255) NOT NULL,
             balance int NOT NULL)""")
db.commit()

db.close()

# 3695 Is the security code for project
# This is the creation of the main screen that you see.
root = Tk()
root.title("ATM")
root.config(bg="gainsboro")
root.geometry("760x700")
mainFrame = Frame(root, bd=20, width=774, height=700, relief=RIDGE)
mainFrame.grid()

# Variables for the next one person
balance0199 = 60000

# Resizing all the images to fit buttons
# Resize your images 1
myPic = Image.open('leftAR.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
leftARNew = ImageTk.PhotoImage(resize1)

# Resize your images 2
myPic = Image.open('one.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
oneNew = ImageTk.PhotoImage(resize1)

# Resize your images 3
myPic = Image.open('two.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
twoNew = ImageTk.PhotoImage(resize1)

# Resize your images 4
myPic = Image.open('three.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
threeNew = ImageTk.PhotoImage(resize1)

# Resize your images 5
myPic = Image.open('four.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
fourNew = ImageTk.PhotoImage(resize1)

# Resize your images 6
myPic = Image.open('five.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
fiveNew = ImageTk.PhotoImage(resize1)

# Resize your images 7
myPic = Image.open('six.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
sixNew = ImageTk.PhotoImage(resize1)

# Resize your images 8
myPic = Image.open('seven.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
sevenNew = ImageTk.PhotoImage(resize1)

# Resize your images 9
myPic = Image.open('eight.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
eightNew = ImageTk.PhotoImage(resize1)

# Resize your images 10
myPic = Image.open('nine.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
nineNew = ImageTk.PhotoImage(resize1)

# Resize your images 11
myPic = Image.open('zero.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
zeroNew = ImageTk.PhotoImage(resize1)

# Resize your images 12
myPic = Image.open('rArrow.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
rightARNew = ImageTk.PhotoImage(resize1)

# Resize your images 13
myPic = Image.open('empty.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
emptyNew = ImageTk.PhotoImage(resize1)

# Resize your images 14
myPic = Image.open('cancel.png')
resize1 = myPic.resize((145, 65),Image.Resampling.LANCZOS)
cancelNew = ImageTk.PhotoImage(resize1)

# Resize your images 15
myPic = Image.open('clear.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
clearNew = ImageTk.PhotoImage(resize1)

# Resize your images 16
myPic = Image.open('enter.png')
resize1 = myPic.resize((145, 65), Image.Resampling.LANCZOS)
enterNew = ImageTk.PhotoImage(resize1)


topFrame1 = Frame(mainFrame, bd=7, width=800, height=300, relief=RIDGE)
topFrame1.grid(row=1, column=0, padx=40)
topFrame2 = Frame(mainFrame, bd=7, width=734, height=300, relief=RIDGE)
topFrame2.grid(row=0, column=0, padx=8)

topFrame2L = Frame(topFrame2, bd=4, width=190, height=300, relief=RIDGE)
topFrame2L.grid(row=0, column=0, padx=12)

topFrame2M = Frame(topFrame2, bd=5, width=300, height=300, relief=RIDGE)
topFrame2M.grid(row=0, column=1, padx=12)

topFrame2R = Frame(topFrame2, bd=5, width=190, height=300, relief=RIDGE)
topFrame2R.grid(row=0, column=2, padx=12)

# ================================Functions================================================================


def enter_Pin():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='KobusKoetsee12!',
        database="bank"
    )
    # This is the function that handels everything that happens if enter button is clicked
    c = db.cursor()

    pinNo = root.txtReciept.get("1.0", "end-1c")
    print(pinNo)

    c.execute(f"SELECT changing_balance FROM transactions WHERE pin = '{pinNo}'")
    pin = c.fetchall()
    count = c.rowcount

    if (count != 0):

        global j_balance
        j_balance = pin[-1][0]
        j_balance = str(j_balance)

        print(type(j_balance))

        c.execute(f"SELECT pin FROM bankdetials WHERE pin = '{pinNo}'")
        frog = c.fetchone()
        global j_pin
        j_pin = frog[0]
        j_pin = str(j_pin)

    db.commit()

    count = c.rowcount

    db.close()

    if (count != 0):

        root.txtReciept.delete("1.0", END)

        root.txtReciept.insert(END, "\t\t ATM" + "\n\n")
        root.txtReciept.insert(END, "Withdraw Cash\t\t\t Loan" + "\n\n\n\n\n")
        root.txtReciept.insert(END, "Cash With Reciept\t\t\t Deposit" + "\n\n\n\n\n")
        root.txtReciept.insert(END, "Balance\t\t\t Request New Pin" + "\n\n\n\n\n")
        root.txtReciept.insert(END, "Transacton graph\t\t\t Print Statement" + "\n\n\n\n\n")
        # ================================LEFT Buttons============================================================
        root.btnArL1 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=withdraw)\
        .grid(row=0, column=0, padx=2, pady=2)
        root.btnArL2 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=reciept)\
        .grid(row=1, column=0, padx=2, pady=2)
        root.btnArL3 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=balance)\
        .grid(row=2, column=0, padx=2, pady=2)
        root.btnArL4 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=graph)\
        .grid(row=3, column=0, padx=2, pady=2)
        # ================================RIGHT Buttons===========================================================
        root.btnArR1 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=Loan)\
        .grid(row=0, column=0, padx=2, pady=2)
        root.btnArR2 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=deposit)\
        .grid(row=1, column=0, padx=2, pady=2)
        root.btnArR3 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew,command=requestPin)\
        .grid(row=2, column=0, padx=2, pady=2)
        root.btnArR4 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=statement)\
        .grid(row=3, column=0, padx=2, pady=2)

    else:
        root.txtReciept.delete("1.0", END)
        root.txtReciept.insert(END, "\t\t Invalid Pin " + "\n")
        root.txtReciept.insert(END, "\t\t Try Again " + "\n\n\n\n")



def main_menu():
    for item in root.txtReciept.winfo_children():
        item.destroy()

    root.txtReciept.delete("1.0", END)

    root.txtReciept.insert(END, "\t\t ATM" + "\n\n")
    root.txtReciept.insert(END, "Withdraw Cash\t\t\t Loan" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Cash With Reciept\t\t\t Deposit" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Balance\t\t\t Request New Pin" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Transaction graph\t\t\t Print Statement" + "\n\n\n\n\n")
    # ================================LEFT Buttons============================================================
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=withdraw) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=reciept) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=graph) \
        .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=Loan) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=deposit) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=requestPin) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=NORMAL, image=rightARNew, command=statement) \
        .grid(row=3, column=0, padx=2, pady=2)

    return
def Clear():
    # This is the functions that handels everything that happens when clear button is clicked
    root.txtReciept.delete("1.0", END)
    # ================================LEFT Buttons============================================================
    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw)\
    .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept)\
    .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance)\
    .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=graph)\
    .grid(row=3, column=0, padx=2, pady=2)
    # ================================RIGHT Buttons===========================================================
    root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan)\
    .grid(row=0, column=0, padx=2, pady=2)
    root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit)\
    .grid(row=1, column=0, padx=2, pady=2)
    root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin)\
    .grid(row=2, column=0, padx=2, pady=2)
    root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=statement)\
    .grid(row=3, column=0, padx=2, pady=2)
    return


def Cancel_Transaction():
    #  This is the functions that handels everything that happens when cancel button is clicked
    cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to Leave ATM")
    if cancel > 0:
        root.destroy()
    return



def withdraw():
    # this function handels what happens if you want to withdraw
    # Destroy widgets to add new widgets
    # for item in topFrame2L.winfo_children():
    #     item.destroy()

    root.txtReciept.delete("1.0", END)

    root.txtReciept.insert(END, "\n\n main menu \n")
    root.txtReciept.insert(END, "\n\n\n\nPress -> to withdraw  \n")
    root.txtReciept.insert(END, "\n\n\nHow Much do you want to withdraw: \n$")

    def withdraw_amount():
        print(type(j_balance))

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd='KobusKoetsee12!',
            database="bank"
        )
        # This is the function that handels everything that happens if enter button is clicked
        c = db.cursor()

        c.execute(f"SELECT changing_balance FROM transactions WHERE pin = '{j_pin}'")
        dynamic_balance = c.fetchall()
        dynamic_balance = dynamic_balance[-1][0]
        print("dynamic balance", dynamic_balance)

        check = root.txtReciept.get("13.1", "13.30")
        print("check", check)
        new_balance = 0
        new_balance = int(dynamic_balance) - int(check)
        new_balance = str(new_balance)
        print("new balance", new_balance)


        currdate = datetime.today()


        # official but keep closed for now
        c.execute(f"""INSERT INTO transactions(transaction_type, amount, tdate, pin, changing_balance)
                      VALUES('withdraw', '{check}', '{currdate}', '{j_pin}', '{new_balance}')""")

        # c.execute(f"""INSERT INTO transactions(transaction_type, amount, tdate, pin, changing_balance)
        #               VALUES('withdraw', '{check}', '2022-08-10', '{j_pin}', '{new_balance}')""")

        print(balance)

        db.commit()
        db.close()

        root.txtReciept.insert(END, f"\n Your have withdrawn R{check}  \n")

    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=main_menu) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=withdraw_amount) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=graph) \
        .grid(row=3, column=0, padx=2, pady=2)

def deposit():
    # this function handels what happens if you want to deposit

    root.txtReciept.delete("1.0", END)

    root.txtReciept.insert(END, "\n\n main menu \n")
    root.txtReciept.insert(END, "\n\n\n\nPress -> to deposit  \n")
    root.txtReciept.insert(END, "\n\n\nHow Much do you want to deposit: \n$")

    def deposit_amount():
        print(type(j_balance))

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd='KobusKoetsee12!',
            database="bank"
        )
        # This is the function that handels everything that happens if enter button is clicked
        c = db.cursor()

        c.execute(f"SELECT changing_balance FROM transactions WHERE pin = '{j_pin}'")
        dynamic_balance = c.fetchall()
        dynamic_balance = dynamic_balance[-1][0]
        print("the dynamic balance", dynamic_balance)

        check = root.txtReciept.get("13.1", "13.30")
        print("check", check)
        new_balance = int(dynamic_balance) + int(check)
        new_balance = str(new_balance)

        currdate = datetime.today()
        print(currdate)

        # official but keep closed for now
        c.execute(f"""INSERT INTO transactions(transaction_type, amount, tdate, pin, changing_balance)
                             VALUES('deposit', '{check}', '{currdate}', '{j_pin}', '{new_balance}')""")

        db.commit()
        db.close()

        root.txtReciept.insert(END, f"\nYour have Deposited R{check}  \n")

    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=main_menu) \
        .grid(row=0, column=0, padx=2, pady=2)
    root.btnArL2 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=deposit_amount) \
        .grid(row=1, column=0, padx=2, pady=2)
    root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance) \
        .grid(row=2, column=0, padx=2, pady=2)
    root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=graph) \
        .grid(row=3, column=0, padx=2, pady=2)


def Loan():
    # this function handles what happens if you want to take out a loan

    root.txtReciept.delete("1.0", END)

    root.txtReciept.focus_set()
    root.txtReciept.insert(END, "\n\nWithdraw Cash\t\t\t Loan" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Cash With Reciept\t\t\t Deposit" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Balance\t\t\t Request New Pin" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Mini Statement\t\t\t Print Statement" + "\n")
    root.txtReciept.insert(END, "Enter Loan Amount: $")

def balance():
    # this function handles what happens if you want to check your balance
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='KobusKoetsee12!',
        database="bank"
    )
    # This is the function that handels everything that happens if enter button is clicked
    c = db.cursor()

    c.execute(f"SELECT changing_balance FROM transactions WHERE pin = '{j_pin}'")
    updated_balance = c.fetchall()
    updated_balance = updated_balance[-1][0]
    print(updated_balance)


    db.commit()
    db.close()


    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, f"Your Balance: \n${updated_balance}  \n")
    # root.txtReciept.insert(END, "Withdraw Cash\t\t\t Loan" + "\n\n\n\n\n")
    # root.txtReciept.insert(END, "Cash With Reciept\t\t\t Deposit" + "\n\n\n\n\n")
    # root.txtReciept.insert(END, "Balance\t\t\t Request New Pin" + "\n\n\n\n\n")
    # root.txtReciept.insert(END, "Transaction graph\t\t\t Print Statement" + "\n\n\n\n\n")

def statement():
        # this function handles what happens if you want to check your statement

        root.txtReciept.delete("1.0", END)
        root.txtReciept.insert(END, "Your Balance: \n$60000  \n")
        root.txtReciept.insert(END, "09/02\t KFC........................$5.00" + "\n")
        root.txtReciept.insert(END, "10/02\t Tickets GNR........$67.00" + "\n")
        root.txtReciept.insert(END, "23/02\t Machinery...........$5333.00" + "\n")
        root.txtReciept.insert(END, "05/03\t PC Upgrades......$7565.00" + "\n")
        root.txtReciept.insert(END, "13/03\t Signs....................$799.00" + "\n")
        root.txtReciept.insert(END, "13/03\t LogoCreate.........$234.00" + "\n")
        root.txtReciept.insert(END, "25/03\t CASH....................$23.00" + "\n")
        root.txtReciept.insert(END, "12/06\t ATMS....................$6767.00" + "\n")
        root.txtReciept.insert(END, "12/06\t ATM Paper..........$780.00" + "\n")
        root.txtReciept.insert(END, "13/06\t CASH....................$49.00" + "\n")
        root.txtReciept.insert(END, "14/06\t ATM Program.....$1000000.00" + "\n")
        root.txtReciept.insert(END, " + \n")
        root.txtReciept.insert(END, "---------------------------------------------------------------------""\n")
        root.txtReciept.insert(END, " TOTAL......................................$1021622" + "\n")

def graph():
    # this function handles what happens if you want to check your mini statement

    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "Press to show transaction graph:")


    def show_graph():

        plt.style.use('grayscale')
        # plt.gcf().autofmt_xdate()
        # plt.grid(True)


        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd='KobusKoetsee12!',
            database="bank"
        )

        c = db.cursor()

        c.execute("SELECT tdate FROM transactions")
        dates = c.fetchall()

        c.execute("SELECT changing_balance FROM transactions")
        amounts = c.fetchall()
        date_x = []
        amount_y = []

        for date in dates:
            tr = date[0]
            date_x.append(tr)

        for amount in amounts:
            amt = int(amount[0])
            amount_y.append(amt)

        print(date_x)
        print(amount_y)
        print(datetime)

        fig = plt.Figure(figsize=(5,6),dpi=60)

        grid = plt.grid()


        fig.add_subplot(111).plot_date(date_x, amount_y,'o-')

        chart = FigureCanvasTkAgg(fig,root.txtReciept)

        chart.get_tk_widget().grid(row=0, column=0)




        # plt.plot_date(date_x, amount_y, marker='o', linestyle='-')
        # plt.gcf().autofmt_xdate()
        # plt.show()

    root.btnArL1 = Button(topFrame2L, width=145, height=65, state=NORMAL, image=leftARNew, command=show_graph) \
        .grid(row=0, column=0, padx=2, pady=2)


def reciept():
    # this function handels what happens if you want to have cash and it gives you a reciept

    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "       Thank you for using Goliath National Bank" + "\n\n")
    root.txtReciept.insert(END, "Withdraw Cash\t\t\t Loan" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Cash With Reciept\t\t\t Deposit" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Balance\t\t\t Request New Pin" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Mini Statement\t\t\t Print Statement" + "\n\n")
    root.txtReciept.insert(END, " Cash withdraw: $")


def requestPin():

    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "\t             Welcome to GNB\n")
    root.txtReciept.insert(END, "\t         Enter Home Address at the end\n")
    root.txtReciept.focus_set()
    root.txtReciept.insert(END, "      New Pin will be sent to your Home Address\n")

def back():
    root.txtReciept.delete("1.0", END)
    root.txtReciept.insert(END, "\t\t ATM" + "\n\n")
    root.txtReciept.insert(END, "Withdraw Cash\t\t\t Loan" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Cash With Reciept\t\t\t Deposit" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Balance\t\t\t Request New Pin" + "\n\n\n\n\n")
    root.txtReciept.insert(END, "Transaction graph\t\t\t Print Statement" + "\n\n\n\n\n")

# This gives value 0 to button 0 and it also puts value at the end of txtreciept
def btn0():
    value0 = 0
    root.txtReciept.insert(END, value0)
    return

# This gives value 1 to button 1 and it also puts value at the end of txtreciept
def btn1():
    value1 = 1
    root.txtReciept.insert(END, value1)


# This gives value 2 to button 2 and it also puts value at the end of txtreciept
def btn2():
    value2 = 2
    root.txtReciept.insert(END, value2)


# This gives value 3 to button 3 and it also puts value at the end of txtreciept
def btn3():
    value3 = 3
    root.txtReciept.insert(END, value3)


# This gives value 4 to button 4 and it also puts value at the end of txtreciept
def btn4():
    value4 = 4
    root.txtReciept.insert(END, value4)


# This gives value 5 to button 5 and it also puts value at the end of txtreciept
def btn5():
    value5 = 5
    root.txtReciept.insert(END, value5)


# This gives value 6 to button 6 and it also puts value at the end of txtreciept
def btn6():
    value6 = 6
    root.txtReciept.insert(END, value6)


# This gives value 7 to button 7 and it also puts value at the end of txtreciept
def btn7():
    value7 = 7
    root.txtReciept.insert(END, value7)


# This gives value 8 to button 8 and it also puts value at the end of txtreciept
def btn8():
    value8 = 8
    root.txtReciept.insert(END, value8)


# This gives value 9 to button 9 and it also puts value at the end of txtreciept
def btn9():
    value9 = 9
    root.txtReciept.insert(END, value9)


# ===============================Adding where TEXT comes:Screen===========================================
root.txtReciept = Text(topFrame2M, height=20, width=40, bd=12, font=("arial", 9, "bold"))
root.txtReciept.grid(row=0, column=0)

# ================================LEFT Buttons============================================================
root.btnArL1 = Button(topFrame2L,  width=145, height=65, state=DISABLED, image=leftARNew, command=withdraw)\
.grid(row=0, column=0, padx=2, pady=2)
root.btnArL2 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=reciept)\
.grid(row=1, column=0, padx=2, pady=2)
root.btnArL3 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew, command=balance)\
.grid(row=2, column=0, padx=2, pady=2)
root.btnArL4 = Button(topFrame2L, width=145, height=65, state=DISABLED, image=leftARNew)\
.grid(row=3, column=0, padx=2, pady=2)
# ================================RIGHT Buttons===========================================================
root.btnArR1 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=Loan)\
.grid(row=0, column=0, padx=2, pady=2)
root.btnArR2 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=deposit)\
.grid(row=1, column=0, padx=2, pady=2)
root.btnArR3 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew, command=requestPin)\
.grid(row=2, column=0, padx=2, pady=2)
root.btnArR4 = Button(topFrame2R, width=145, height=65, state=DISABLED, image=rightARNew)\
.grid(row=3, column=0, padx=2, pady=2)
# ==============================PIN PAD===================================================================

root.btn1 = Button(topFrame1, width=145, height=65, state=NORMAL, image=oneNew, command=btn1)\
.grid(row=0, column=0, padx=2, pady=2)
root.btn2 = Button(topFrame1, width=145, height=65, state=NORMAL, image=twoNew, command=btn2)\
.grid(row=1, column=0, padx=2, pady=2)
root.btn3 = Button(topFrame1, width=145, height=65, state=NORMAL, image=threeNew, command=btn3)\
.grid(row=2, column=0, padx=2, pady=2)
root.btnPlain1 = Button(topFrame1, width=145, height=65, state=NORMAL, image=emptyNew)\
.grid(row=3, column=0, padx=2, pady=2)

root.btn4 = Button(topFrame1, width=145, height=65, state=NORMAL, image=fourNew, command=btn4)\
.grid(row=0, column=1, padx=2, pady=2)
root.btn5 = Button(topFrame1, width=145, height=65, state=NORMAL, image=fiveNew, command=btn5)\
.grid(row=1, column=1, padx=2, pady=2)
root.btn6 = Button(topFrame1, width=145, height=65, state=NORMAL, image=sixNew, command=btn6)\
.grid(row=2, column=1, padx=2, pady=2)
root.btnZero = Button(topFrame1, width=145, height=65, state=NORMAL, image=zeroNew, command=btn0)\
.grid(row=3, column=1, padx=2, pady=2)

root.btn7 = Button(topFrame1, width=145, height=65, state=NORMAL, image=sevenNew, command=btn7)\
.grid(row=0, column=2, padx=2, pady=2)
root.btn8 = Button(topFrame1, width=145, height=65, state=NORMAL, image=eightNew, command=btn8)\
.grid(row=1, column=2, padx=2, pady=2)
root.btn9 = Button(topFrame1, width=145, height=65, state=NORMAL, image=nineNew, command=btn9)\
.grid(row=2, column=2, padx=2, pady=2)
root.btnPlain2 = Button(topFrame1, width=145, height=65, state=NORMAL, image=emptyNew)\
.grid(row=3, column=2, padx=2, pady=2)
root.btnClear = Button(topFrame1, width=145, height=65, state=NORMAL, image=clearNew, command=Clear)\
.grid(row=0, column=3, padx=2, pady=2)
root.btnCancel = Button(topFrame1, width=145, height=65, state=NORMAL, image=cancelNew, command=Cancel_Transaction)\
.grid(row=1, column=3, padx=2, pady=2)
root.btnEnter = Button(topFrame1, width=145, height=65, state=NORMAL, image=enterNew, command=enter_Pin)\
.grid(row=2, column=3, padx=2, pady=2)
root.btnPlain3 = Button(topFrame1, width=145, height=65, state=NORMAL, image=rightARNew, command=main_menu)\
.grid(row=3, column=3, padx=2, pady=2)


'''Here is where you call the main loop and to run the project.'''
root.mainloop()



