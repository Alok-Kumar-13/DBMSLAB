'''
Source code file of Library Management file
@author1: ashutosh 
@author2: alok   
'''
# importing  library files
from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime

# declaring all  global variables  that has been used in program
b1, b2, b3, b4, cur, con, e1, e2, e3, e4, e5, i, ps = None, None, None, None, None, None, None, None, None, None, None, None, None
window, win = None, None
com1d, com1m, com1y, com2d, com2m, com2y = None, None, None, None, None, None
logged_userid = None

# list of month for date validation
month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']

# list of year for date validation
y = list(range(2020, 2040))

# list of month for date validation
d = list(range(1, 32))

# login function for user


def loginlibr():
    global window
    connectdb()
    for i in range(cur.rowcount):
        data = cur.fetchone()
        if e1.get().strip() == str(data[1]) and e2.get().strip() == str(data[3]):
            global logged_userid
            logged_userid = str(data[1])
            closedb()
            libr()
            break
    else:
        window.withdraw()
        messagebox.showwarning("Invalid", "Invalid input")
        closedb()
        home()

# user library window gui


def libr():
    global window
    window.withdraw()
    global win, b1, b2, b3, b4, b5, b6
    win = Tk()
    win.title('Library')
    win.geometry("800x600")
    win.configure(background='#0096DC')
    win.resizable(False, False)
    text_label = Label(win, text='Select Your Choice',
                       fg='black', bg='#0096DC')
    text_label.pack(pady=(40, 40))
    text_label.config(font=('verdana', 30))
    button_frame = Frame(win, height=500, width=300, bg='#7dc5e7')
    button_frame.pack(pady=(10, 20))

    b2 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' Issue Book ', command=issuebook)
    b3 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' Return Book ', command=returnbook)
    b4 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' View Book ', command=viewbook)
    b5 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' Issued Book ', command=issuedbook)
    b6 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' LogOut ', command=logout)

    b2.grid(row=0, column=0, padx=10, pady=(20, 10))
    b3.grid(row=1, column=0, padx=10, pady=10)
    b4.grid(row=2, column=0, padx=10, pady=10)
    b5.grid(row=3, column=0, padx=10, pady=10)
    b6.grid(row=4, column=0, padx=10, pady=10)
    win.mainloop()

# when close is called it will destroy current window and open admin window


def backtoadmin():
    global win
    win.destroy()
    admin()

# when close is called it will destroy current window and open user libr window


def backtolbr():
    global win
    win.destroy()
    libr()

# issuebook gui


def issuebook():
    global win
    win.destroy()
    win = Tk()
    win.title('Issue Book')
    win.geometry("800x600")
    win.configure(background='#0096DC')
    win.resizable(False, False)
    text_label = Label(win, text='Issue Book', fg='black', bg='#0096DC')
    text_label.pack(pady=(30, 20))
    text_label.config(font=('verdana', 30))

    global e1, b, b1, e4
    global com1y, com1m, com1d, com2y, com2m, com2d
    entry_frame = Frame(win, height=700,  width=500, bg='#7dc5e7')
    entry_frame.pack(pady=(10))
    sid = Label(entry_frame, text='STUDENT ID', fg='black', bg='#7dc5e7')
    print_sid = Label(entry_frame, text=logged_userid,
                      fg='black', bg='#7dc5e7')
    e1 = logged_userid
    sid.pack(padx=(20, 20), pady=(10, 10))
    print_sid.pack(padx=(20, 20), pady=(10, 10))
    print_sid.config(font=('verdana', 30))

    no = Label(entry_frame, text='BOOK NO', fg='black', bg='#7dc5e7')
    e4 = Entry(entry_frame, width=40)
    no.pack(padx=(20, 20), pady=(10, 10))
    e4.pack(padx=(40, 40), pady=(5, 5))

    button_frame = Frame(win, bg='#0096DC')
    button_frame.pack(pady=(20, 20))
    b = Button(button_frame,
               fg='white', bg='#4166F5', width=15, height=3, text=' ISSUE BOOK ', command=issuebooks)
    b1 = Button(button_frame,
                fg='white', bg='#4166F5', width=10, height=3, text=' CLOSE ', command=backtolbr)
    b.grid(row=0, column=0, padx=20)
    b1.grid(row=0, column=1, padx=20)

    date_label = Label(entry_frame, text='Issue Date',
                       fg='black', bg='#7dc5e7')
    date_label.pack(pady=3)
    date_frame = Frame(entry_frame, height=100, width=500, bg='#0096DC')
    date_frame.pack(pady=10)
    now = datetime.datetime.now()
    com1y = Combobox(date_frame, value=y, width=5)
    com1m = Combobox(date_frame, value=month, width=5)
    com1d = Combobox(date_frame, value=d, width=5)
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)
    com1y.grid(row=0, column=0, pady=10, padx=5)
    com1m.grid(row=0, column=1, pady=10, padx=5)
    com1d.grid(row=0, column=2, pady=10, padx=5)

    expiry_label = Label(entry_frame, text='Expiry Date',
                         fg='black', bg='#7dc5e7')
    expiry_label.pack()
    e_date_frame = Frame(entry_frame, height=100, width=500, bg='#0096DC')
    e_date_frame.pack(pady=10)
    com2y = Combobox(e_date_frame, value=y, width=5)
    com2m = Combobox(e_date_frame, value=month, width=5)
    com2d = Combobox(e_date_frame, value=d, width=5)
    com2y.set(now.year)
    com2m.set(month[now.month-1])
    com2d.set(now.day)
    com2y.grid(row=0, column=0, pady=10, padx=5)
    com2m.grid(row=0, column=1, pady=10, padx=5)
    com2d.grid(row=0, column=2, pady=10, padx=5)

    win.mainloop()

# function of issuebooks i.e using db


def issuebooks():
    connectdb()
    # validation
    query = """select * from book where serial not in (select serial from BookIssue) and serial = %s """
    cur.execute(query, e4.get())

    if cur.rowcount == 0:
        messagebox.showinfo("Book", "Book is not Available")
    else:
        q = 'INSERT INTO BookIssue VALUE("%s","%s","%s","%s")'
        i = datetime.datetime(int(com1y.get()), month.index(
            com1m.get())+1, int(com1d.get()))
        e = datetime.datetime(int(com2y.get()), month.index(
            com2m.get())+1, int(com2d.get()))
        i = i.isoformat()
        e = e.isoformat()
        cur.execute(q % (e1, e4.get(), i, e))
        con.commit()
        messagebox.showinfo("Book", "Book Issued")
    win.destroy()
    closedb()
    libr()

# return book gui


def returnbook():
    global win
    win.destroy()
    win = Tk()
    win.title('Return Book')
    win.geometry("800x600")
    win.configure(background='#0096DC')
    win.resizable(False, False)

    text_label = Label(win, text='Return Book', fg='black', bg='#0096DC')
    text_label.pack(pady=(30, 20))
    text_label.config(font=('verdana', 30))

    entry_frame = Frame(win, height=400,  width=500, bg='#7dc5e7')
    entry_frame.pack(pady=(30))
    global b, b1
    global e4
    book = Label(entry_frame, text='Book No', fg='black', bg='#7dc5e7')
    e4 = Entry(entry_frame, width=40)
    book.pack(padx=(20, 20), pady=(10, 10))
    e4.pack(padx=(40, 40), pady=(5, 5))

    date = Label(entry_frame, text='Date', fg='black', bg='#7dc5e7')
    date.pack(padx=(20, 20), pady=(10, 10))
    date_frame = Frame(entry_frame, height=100, width=500, bg='#0096DC')
    date_frame.pack(pady=20)

    global com1y, com1m, com1d, com2y, com2m, com2d
    com1y = Combobox(date_frame, value=y, width=5)
    com1m = Combobox(date_frame, value=month, width=5)
    com1d = Combobox(date_frame, value=d, width=5)
    '''com2y=Combobox(win,width=5)
    com2m=Combobox(win,width=5)
    com2d=Combobox(win,width=5)'''
    now = datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month-1])
    com1d.set(now.day)
    com1y.grid(row=0, column=0, pady=10, padx=5)
    com1m.grid(row=0, column=1, pady=10, padx=5)
    com1d.grid(row=0, column=2, pady=10, padx=5)

    button_frame = Frame(win, bg='#0096DC')
    button_frame.pack(pady=(20, 20))
    b = Button(button_frame,
               fg='white', bg='#4166F5', width=15, height=3, text=' RETURN BOOK ', command=returnbooks)
    b1 = Button(button_frame,
                fg='white', bg='#4166F5', width=10, height=3, text=' CLOSE ', command=backtolbr)
    b.grid(row=0, column=0, padx=20)
    b1.grid(row=0, column=1, padx=20)
    win.mainloop()

#  function to returnbooks i.e db


def returnbooks():
    connectdb()
    q = 'SELECT exp FROM BookIssue WHERE serial="%s"'
    if(cur.execute(q % (e4.get())) == 0):
        messagebox.showinfo("Error", "No Book of this Serial number is Issued")
    else:
        e = cur.fetchone()
        e = str(e[0])
        i = datetime.date.today()
        e = datetime.date(int(e[:4]), int(e[5:7]), int(e[8:10]))
        if i <= e:
            a = 'DELETE FROM BookIssue WHERE serial="%s"'
            cur.execute(a % e4.get())
            messagebox.showinfo("Success", "Return SuccessFull")
            con.commit()
        else:
            t = str((i-e)*10)
            a = 'DELETE FROM BookIssue WHERE serial="%s"'
            cur.execute(a % e4.get())
            con.commit()
            messagebox.showinfo("Fine", t[:4]+' Fine ')
    win.destroy()
    closedb()
    libr()

#  funtion to view books


def viewbook():
    win = Tk()
    win.title('View Books')
    win.geometry("800x300+270+180")
    win.resizable(False, False)

    treeview = Treeview(win, columns=("Subject", "Title",
                        "Author", "Serial No"), show='headings')
    treeview.heading("Subject", text="Subject")
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Serial No", text="Serial No")

    treeview.column("Subject", anchor='center')
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Serial No", anchor='center')
    index = 0

    connectdb()
    q = 'SELECT * FROM Book'
    cur.execute(q)
    details = cur.fetchall()
    for row in details:
        treeview.insert("", index, value=row)
        index = index+1
    treeview.pack()
    win.mainloop()
    closedb()

#  funtion to view issued books


def issuedbook():
    connectdb()
    q = 'SELECT * FROM BookIssue'
    cur.execute(q)
    details = cur.fetchall()
    if len(details) != 0:
        win = Tk()
        win.title('Issued Books')
        win.geometry("800x600")
        win.configure(background='#0096DC')
        win.resizable(False, False)
        treeview = Treeview(win, columns=(
            "Student ID", "Serial No", "Issue Date", "Expiry Date"), show='headings')
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Serial No", text="Serial No")
        treeview.heading("Issue Date", text="Issue Date")
        treeview.heading("Expiry Date", text="Expiry Date")
        treeview.column("Student ID", anchor='center')
        treeview.column("Serial No", anchor='center')
        treeview.column("Issue Date", anchor='center')
        treeview.column("Expiry Date", anchor='center')
        index = 0

        for row in details:
            treeview.insert("", index, value=row)
            index = index+1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Books", "No Book Issued")
    closedb()


#  function to login as admin
def loginadmin():
    if e1.get() == 'admin' and e2.get() == 'admin':
        admin()
    else:
        messagebox.showinfo("Error", "Invalid Input")

#  functionality of admin


def admin():
    window.withdraw()
    global win, b1, b2, b3, b4, b5, b6, cur, con
    win = Tk()
    win.title('Admin')
    win.geometry("800x600")
    win.configure(background='#0096DC')
    win.resizable(False, False)
    text_label = Label(win, text='Select Your Choice',
                       fg='black', bg='#0096DC')
    text_label.pack(pady=(40, 20))
    text_label.config(font=('verdana', 30))
    button_frame = Frame(win, height=500, width=300, bg='#7dc5e7')
    button_frame.pack(pady=20)

    b1 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' Add User ', command=adduser)
    b2 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' View User ', command=viewuser)
    b3 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' Delete User ', command=deleteuser)
    b4 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' Add Book ', command=addbook)
    b5 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' Delete Book ', command=deletebook)
    b6 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' View Book ', command=viewbook)
    b7 = Button(button_frame, fg='white', bg='#4166F5', width=40,
                height=3, text=' LogOut ', command=logout)

    b1.grid(row=0, column=0, padx=10, pady=5)
    b2.grid(row=1, column=0, padx=10, pady=5)
    b3.grid(row=2, column=0, padx=10, pady=5)
    b4.grid(row=4, column=0, padx=10, pady=5)
    b5.grid(row=5, column=0, padx=10, pady=5)
    b6.grid(row=6, column=0, padx=10, pady=5)
    b7.grid(row=7, column=0, padx=10, pady=5)
    win.mainloop()

#  logout function


def logout():
    win.destroy()
    try:
        closedb()
    except:
        print("Logged Out")
    home()

# function to close connection and  DB


def closedb():
    global con, cur
    cur.close()
    con.close()

# function to add user using gui


def adduser():
    global win
    win.destroy()
    win = Tk()
    win.title('ADD USER')
    win.geometry("800x600")
    win.configure(background='#0096DC')
    text_label = Label(
        win, text='Add User', fg='white', bg='#0096DC')
    text_label.pack(pady=(30, 20))
    text_label.config(font=('verdana', 30))

    entry_frame = Frame(win, height=400, width=500, bg='#7dc5e7')
    entry_frame.pack(pady=30)

    button_frame = Frame(win, bg='#0096DC')
    button_frame.pack(pady=(20, 20))

    global e1, b, e2, e3, e4
    b = Button(button_frame, text="ADD USER",
               fg='white', bg='#4166F5', width=10, height=3, command=addusers)
    b1 = Button(button_frame, text="CLOSE",
                fg='white', bg='#4166F5', width=10, height=3, command=backtoadmin)
    b.grid(row=0, column=0, padx=20)
    b1.grid(row=0, column=1, padx=20)

    name = Label(entry_frame, text='Name', fg='black', bg='#7dc5e7')
    e1 = Entry(entry_frame, width=40)
    name.pack(padx=(20, 20), pady=(10, 10))
    e1.pack(padx=(40, 40), pady=(5, 5))

    usid = Label(entry_frame, text='USER ID', fg='black', bg='#7dc5e7')
    usid.pack(padx=(20, 20), pady=(10, 10))
    e2 = Entry(entry_frame, width=40)
    e2.pack(padx=(40, 40), pady=(5, 5))

    branch = Label(entry_frame, text='BRANCH', fg='black', bg='#7dc5e7')
    branch.pack(padx=(20, 20), pady=(10, 10))
    e3 = Entry(entry_frame, width=40)
    e3.pack(padx=(40, 40), pady=(5, 5))

    mob = Label(entry_frame, text='MOBILE NO', fg='black', bg='#7dc5e7')
    mob.pack(padx=(20, 20), pady=(10, 10))
    e4 = Entry(entry_frame, width=40)
    e4.pack(padx=(40, 40), pady=(5, 20))

    win.mainloop()

# function to  add user in db via gui


def addusers():
    connectdb()
    q = 'INSERT INTO Login VALUE("%s","%i","%s","%i")'
    global con, cur
    cur.execute(q % (e1.get(), int(e2.get()), e3.get(), int(e4.get())))
    messagebox.showinfo("User", "User Added")
    con.commit()
    win.destroy()
    closedb()
    admin()

# function to view user from login table


def viewuser():
    win = Tk()
    win.geometry("800x600")
    win.title('View User')
    win.resizable(False, False)
    treeview = Treeview(win, columns=("Name", "User ID",
                        "Branch", "Mobile No"), show='headings')
    treeview.heading("Name", text="Name")
    treeview.heading("User ID", text="User ID")
    treeview.heading("Branch", text="Branch")
    treeview.heading("Mobile No", text="Mobile No")
    treeview.column("Name", anchor='center')
    treeview.column("User ID", anchor='center')
    treeview.column("Branch", anchor='center')
    treeview.column("Mobile No", anchor='center')
    index = 0

    connectdb()
    details = cur.fetchall()
    for row in details:
        treeview.insert("", index, value=row)
        index = index+1
    treeview.pack()
    win.mainloop()
    closedb()

# function to delete user ui


def deleteuser():
    global win
    win.destroy()
    win = Tk()
    win.title('Delete User')
    win.geometry("800x600")
    win.resizable(False, False)
    win.configure(background='#0096DC')
    text_label = Label(win, text='Delete User', fg='white', bg='#0096DC')
    text_label.pack(pady=(30, 20))
    text_label.config(font=('verdana', 30))
    entry_frame = Frame(win, height=400, width=500, bg='#7dc5e7')
    entry_frame.pack(pady=30)

    button_frame = Frame(win, bg='#0096DC')
    button_frame.pack(pady=(20, 20))
    global e1, e2, b2
    usid = Label(entry_frame, text='USER to be Deleted',
                 fg='black', bg='#7dc5e7')
    e1 = Entry(entry_frame, width=40)
    usid.pack(padx=(20, 20), pady=(20, 10))
    e1.pack(padx=(40, 40), pady=(10, 10))

    paswrd = Label(entry_frame, text='ADMIN_PASSWORD',
                   fg='black', bg='#7dc5e7')
    paswrd.pack(padx=(20, 20), pady=(20, 10))
    e2 = Entry(entry_frame, width=40)
    e2.pack(padx=(40, 40), pady=(10, 50))
    admin_button = Button(button_frame, text="Delete",
                          fg='white', bg='#4166F5', width=10, height=3, command=deleteusers)
    user_button = Button(button_frame, text="Close",
                         fg='white', bg='#4166F5', width=10, height=3, command=backtoadmin)
    admin_button.grid(row=0, column=0, padx=20)
    user_button.grid(row=0, column=1, padx=20)

    win.mainloop()

# function to delete user fron login table


def deleteusers():
    connectdb()
    print(e1, e2)
    if e2.get() == 'admin':
        q = 'DELETE FROM Login WHERE userid="%i"'
        cur.execute(q % (int(e1.get())))
        con.commit()
        win.destroy()
        if (cur.rowcount == 0):
            messagebox.showinfo("ERROR", "User NOT Exist")
        else:
            messagebox.showinfo("Delete", "User Deleted")
        closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        closedb()

# function to add book gui


def addbook():
    global win
    win.destroy()
    win = Tk()
    win.title('Add Book')
    win.geometry("800x600")
    win.configure(background='#0096DC')
    win.resizable(False, False)
    global e1, b, b1, e1, e2, e3, e4
    entry_frame = Frame(win, height=400, width=500, bg='#7dc5e7')
    entry_frame.pack(pady=30)
    sub = Label(entry_frame, text='SUBJECT', fg='black', bg='#7dc5e7')
    e1 = Entry(entry_frame, width=40)
    sub.pack(padx=(20, 20), pady=(10, 10))
    e1.pack(padx=(40, 40), pady=(5, 5))

    tit = Label(entry_frame, text='TITLE', fg='black', bg='#7dc5e7')
    tit.pack(padx=(20, 20), pady=(10, 10))
    e2 = Entry(entry_frame, width=40)
    e2.pack(padx=(40, 40), pady=(5, 5))

    auth = Label(entry_frame, text='AUTHOR', fg='black', bg='#7dc5e7')
    auth.pack(padx=(20, 20), pady=(10, 10))
    e3 = Entry(entry_frame, width=40)
    e3.pack(padx=(40, 40), pady=(5, 5))

    ser = Label(entry_frame, text='SERIAL NO', fg='black', bg='#7dc5e7')
    ser.pack(padx=(20, 20), pady=(10, 10))
    e4 = Entry(entry_frame, width=40)
    e4.pack(padx=(40, 40), pady=(5, 20))
    button_frame = Frame(win, bg='#0096DC')
    button_frame.pack(pady=(20, 20))
    b = Button(button_frame, fg='white', bg='#4166F5', width=10, height=3,
               text=' ADD BOOK', command=addbooks)
    b1 = Button(button_frame, fg='white', bg='#4166F5', width=10,
                height=3, text=' CLOSE ', command=backtoadmin)
    b.grid(row=0, column=0, padx=20)
    b1.grid(row=0, column=1, padx=20)
    win.mainloop()

# function to add book in book table


def addbooks():
    connectdb()
    q = 'INSERT INTO Book VALUE("%s","%s","%s","%i")'
    global cur, con
    cur.execute(q % (e1.get(), e2.get(), e3.get(), int(e4.get())))
    con.commit()
    win.destroy()
    messagebox.showinfo("Book", "Book Added Successfully")
    closedb()
    admin()

# function to delete book gui


def deletebook():
    global win
    win.destroy()
    win = Tk()
    win.title('Delete Book')
    win.geometry("800x600")
    win.configure(background='#0096DC')
    win.resizable(False, False)
    text_label = Label(win, text="Delete User", fg='black', bg='#0096DC')
    text_label.pack(pady=(30, 20))
    text_label.config(font=('verdana', '30'))
    global e2, b2, e1
    entry_frame = Frame(win, height=400, width=500, bg='#7dc5e7')
    entry_frame.pack(pady=30)
    button_frame = Frame(win, bg='#0096DC')
    button_frame.pack(pady=(20, 20))

    usid = Label(entry_frame, text='Serial NO', fg='black', bg='#7dc5e7')
    e1 = Entry(entry_frame, width=40)
    usid.pack(padx=(20, 20), pady=(10, 10))
    e1.pack(padx=(40, 40), pady=(5, 5))

    paswrd = Label(entry_frame, text='PASSWORD', fg='black', bg='#7dc5e7')
    paswrd.pack(padx=(20, 20), pady=(10, 10))
    e2 = Entry(entry_frame, width=40)
    e2.pack(padx=(40, 40), pady=(5, 20))

    b1 = Button(button_frame, text="DELETE",
                fg='white', bg='#4166F5', width=10, height=3, command=deletebooks)
    b2 = Button(button_frame, text="CLOSE",
                fg='white', bg='#4166F5', width=10, height=3, command=backtoadmin)
    b1.grid(row=0, column=0, padx=10)
    b2.grid(row=0, column=1, padx=10)

    win.mainloop()

# function to delete book from book table


def deletebooks():
    connectdb()
    if e2.get() == 'admin':
        q = 'DELETE FROM Book WHERE serial="%i"'
        if(cur.execute(q % (int(e1.get()))) == 0):
            messagebox.showinfo("Error", "Enter Valid Serial number")
        else:
            messagebox.showinfo("Delete", "Book Deleted")
        con.commit()
        win.destroy()
        closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        closedb()


'''
function to  connect mysql database,
create library database and use that 
create table login, Book ,BookIssue 
'''


def connectdb():
    global con, cur
    con = p.connect(host="localhost", user="ak")
    cur = con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS Library')
    cur.execute('USE Library')
    global enter
    if enter == 1:
        l = 'CREATE TABLE IF NOT EXISTS Login(name varchar(20),userid varchar(10) primary key,branch varchar(20),mobile int(10))'
        b = 'CREATE TABLE IF NOT EXISTS Book(subject varchar(20),title varchar(20),author varchar(20),serial int primary key)'
        i = 'CREATE TABLE IF NOT EXISTS BookIssue(stdid varchar(20),serial int ,issue date,exp date)'
        cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        enter = enter+1
    query = 'SELECT * FROM Login'
    cur.execute(query)

# home page and driver function


def home():
    try:
        global window, b1, b2, e1, e2, con, cur, win
        window = Tk()
        window.title('Welcome')
        window.resizable(False, False)
        window.geometry("800x600")
        window.configure(background='#0096DC')
        text_label = Label(
            window, text='Library Management System', fg='white', bg='#0096DC')
        text_label.pack(pady=(30, 20))
        text_label.config(font=('verdana', 30))

        entry_frame = Frame(window, height=400, width=500, bg='#7dc5e7')
        entry_frame.pack(pady=30)

        button_frame = Frame(window, bg='#0096DC')
        button_frame.pack(pady=(20, 20))
        admin_button = Button(button_frame, text="User Login",
                              fg='white', bg='#4166F5', width=10, height=3, command=loginlibr)
        user_button = Button(button_frame, text="Admin Login",
                             fg='white', bg='#4166F5', width=10, height=3, command=loginadmin)
        admin_button.grid(row=0, column=0, padx=20)
        user_button.grid(row=0, column=1, padx=20)
        usid = Label(entry_frame, text='USER ID', fg='black', bg='#7dc5e7')
        e1 = Entry(entry_frame, width=40)
        usid.pack(padx=(20, 20), pady=(20, 10))
        e1.pack(padx=(40, 40), pady=(10, 10))

        paswrd = Label(entry_frame, text='PASSWORD', fg='black', bg='#7dc5e7')
        paswrd.pack(padx=(20, 20), pady=(20, 10))
        e2 = Entry(entry_frame, width=40)
        e2.pack(padx=(40, 40), pady=(10, 50))
        window.mainloop()
    except Exception:
        window.destroy()


# calling driver function
enter = 1
home()
