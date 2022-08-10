from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
from PIL import ImageTk,Image
root=Tk()
def Text_to_speech():

    speech = gTTS(text = 'Welcome to library management')
    try:

        speech.save('Techarge.mp3')
        playsound('Techarge.mp3',True)
    except:
        pass

bg = ImageTk.PhotoImage(Image.open("custom-library.png"))
canvas = Canvas(root, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)
def resize_image(canvas):
   global image, resized, image2
   image = Image.open("custom-library.png")
   resized = image.resize((1400, 750), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(resized)
   canvas.create_image(0, 0, image=image2, anchor='nw')

resize_image(canvas)
Text_to_speech()
#playsound('Techarge.mp3',False)

def refresh(self,m):
    self.root.destroy()
    try:
        # root.destroy()
        win=Tk()
        canvas = Canvas(win, width=1000, height=3500)
        canvas.pack(fill=BOTH, expand=True)
        resize_image(canvas=canvas)
        # Text_to_speech()
        # playsound('Techarge.mp3')
        Multiple(win)
        m.destroy()
    except:
        win.destroy()
        #m.destroy()
        win=Tk()
        canvas = Canvas(win, width=1000, height=3500)
        canvas.pack(fill=BOTH, expand=True)
        resize_image(canvas=canvas)
        # Text_to_speech()
        # playsound('Techarge.mp3')
        Multiple(win)

class Multiple():
    # def Text_to_speech(self):
    #     # Message = entry_field.get()
    #     speech = gTTS(text='Welcome to library management')
    #     try:
    #         speech.save('Techarge.mp3')
    #         playsound('Techarge.mp3')
    #     except:
    #         pass

    def __init__(self,root):
        self.root=root
        self.root.state("zoomed")
        self.root.resizable(width=False, height=False)

        self.root.title("Library Management System ")


        headingFrame1 = Frame(self.root, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="Welcome to \n Library", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        # if (headingLabel!=""):
        #     self.Text_to_speech()
        admin_button = Button(self.root, text="ADMIN ", command=self.admin_page,font=('Helvetica',15),bg='black',fg='powder blue',bd=5)
        admin_button.place(relx=0.4, rely=0.4,relwidth=0.2,relheight=0.1)
        user_button = Button(self.root, text="STUDENT",command=self.user_page,font=('Helvetica',15),bg='black',fg='powder blue',bd=5)
        user_button.place(relx=0.4, rely=0.50,relwidth=0.2,relheight=0.1)

    def show_admin(self):
        show_ad=Tk()
        #self.show_ad=show_ad
        show_ad.title("admin page")
        show_ad.state("zoomed")
        show_ad.resizable(width=False, height=False)
        show_ad.config(bg="powder blue")
        headingFrame1 = Frame(show_ad, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="Welcome to \n ADMIN PAGE", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        add_button = Button(show_ad, text="ADD BOOKS", command=self.add_page,font=('Arial',15),bg='black',fg='white',bd=5)
        add_button.place(relx=0.4, rely=0.4,relwidth=0.25,relheight=0.1)
        view_button = Button(show_ad, text="VIEW BOOKS", command=self.view,font=('Helvetica',15),bg='black',fg='white',bd=5)
        view_button.place(relx=0.4, rely=0.5,relwidth=0.25,relheight=0.1)
        delete_button = Button(show_ad, text="DELETE BOOKS", command=self.delete,font=('Helvetica',15),bg='black',fg='white',bd=5)
        delete_button.place(relx=0.4, rely=0.6,relwidth=0.25,relheight=0.1)
        delete_button = Button(show_ad, text="BACK TO HOME SCREEN", font=('Helvetica', 15), bg='black',command=lambda m=show_ad : refresh(self,m),
                               fg='white', bd=5)
        delete_button.place(relx=0.4, rely=0.7, relwidth=0.25, relheight=0.1)
    def show_user(self):
        show_us=Tk()
        # self.root.destroy()
        show_us.state("zoomed")
        show_us.resizable(width=False, height=False)
        show_us.title("student page")
        show_us.config(bg="powder blue")
        headingFrame1 = Frame(show_us, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="Welcome to \n STUDENT PAGE", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        view_button = Button(show_us, text="STUDENT RECORD", command=self.view_stu, font=('Helvetica', 15), bg='black',
                             fg='white', bd=5)
        view_button.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.1)

        issue_button = Button(show_us, text="ISSUE BOOK", command=self.issue_book,font=('Helvetica', 15), bg='black',
                             fg='white', bd=5)
        issue_button.place(relx=0.4, rely=0.5, relwidth=0.25, relheight=0.1)
        issue_button = Button(show_us, text="RETURN BOOK", command=self.returnbook,font=('Helvetica', 15), bg='black',
                             fg='white', bd=5)

        issue_button.place(relx=0.4, rely=0.6, relwidth=0.25, relheight=0.1)
        issue_button = Button(show_us, text="BACK TO HOME SCREEN", command=lambda m=show_us : refresh(self,m),font=('Helvetica', 15), bg='black',
                              fg='white', bd=5)
        issue_button.place(relx=0.4, rely=0.7, relwidth=0.25, relheight=0.1)
    def reset(self):
        self.admin_en.delete(0,"end")
        self.admin_pa.delete(0,"end")
    def admin_page(self):
        adminn=Tk()
        #self.root.destroy()
        self.adminn = adminn
        adminn.state("zoomed")
        adminn.resizable(width=False,height=False)
        adminn.config(bg="#ff6e40")
        adminn.title("Admin page")

        headingFrame1 = Frame(adminn, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="ADMIN LOGIN", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        admin_id=Label(adminn,text="ADMIN ID:",font=('bold','17'),fg="black",bg="#ff6e40",bd=4)
        admin_id.place(relx=.35,rely=.4)
        self.admin_en=Entry(adminn,font=('Courier','15'),bd=4)
        self.admin_en.place(relx=.45,rely=.4)
        admin_pass = Label(adminn, text="Password:",
                           font=('bold', '17'),fg="black",bg="#ff6e40")
        admin_pass.place(relx=.35, rely=.5)
        self.admin_pa= Entry(adminn,show="*",font=('Courier','15'),bd=3)
        self.admin_pa.place(relx=.45, rely=.5)

        admin_bu=Button(adminn,text="LOGIN",font=('bold','17'),bg="black",fg="white",command=lambda :self.admin(self.adminn))
        admin_bu.place(relx=.38,rely=.6,relwidth=0.1,relheight=0.07)
        admin_bu = Button(adminn, text="RESET", font=('bold', '17'), bg="black", fg="white",command=self.reset)
        admin_bu.place(relx=.50, rely=.6, relwidth=0.1, relheight=0.07)
        back = Button(adminn, text="BACK", font=('bold', '17'), command = lambda m=adminn:refresh(self,m),bg="black",fg="white")
        back.place(relx=.45, rely=.7, relwidth=0.07, relheight=0.07)

    def admin(self,a):
        passw=self.admin_pa.get()
        adminn=self.admin_en.get()
        if passw=="" or adminn=="":
            messagebox.showinfo("error","all fields are required",parent=self.adminn)
        elif passw=="pass":
            messagebox.showinfo("sucess","login sucessfully",parent=self.adminn)
            self.show_admin()
            a.destroy()
        else:
            messagebox.showinfo("error","password is pass",parent=self.adminn)

    def user_page(self):
        # self.root.destroy()
        users=Tk()
        self.users=users

        users.state("zoomed")
        users.resizable(width=False,height=False)
        users.config(bg="#ff6e40")
        users.title("STUDENT login  page")
        headingFrame1 = Frame(users, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="STUDENT LOGIN", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        users_id=Label(users,text="STUDENT ID:",font=('bold','17'),fg="black",bg="#ff6e40")
        users_id.place(relx=.35,rely=.4)
        self.users_en=Entry(users,font=('Courier','15'),bd=4)
        self.users_en.place(relx=.47,rely=.4)
        users_pass = Label(users, text="PASSWORD:", font=('bold', '17'),fg="black",bg="#ff6e40")
        users_pass.place(relx=.35, rely=.5)
        self.users_pa = Entry(users,show="*",font=('Courier','15'),bd=4)
        self.users_pa.place(relx=.47, rely=.5)
        users_bu=Button(users,text="LOGIN",font=('bold','17'),bg="black",fg="white",command=self.login)
        users_bu.place(relx=.37,rely=.6,relwidth=0.1,relheight=0.07)
        reg_bu = Button(users, text="REGISTER", command=self.register_page,font=('bold', '17'),bg="black",fg="white")
        reg_bu.place(relx=.50, rely=.6,relwidth=0.1,relheight=0.07)
        back = Button(users, text="BACK", font=('bold', '17'), command = lambda m= self.users : refresh(self,m), bg="black",
                      fg="white")
        back.place(relx=.45, rely=.7, relwidth=0.07, relheight=0.07)

    def login(self):
        loginid=self.users_en.get()
        loginpass=self.users_pa.get()
        if (len(loginid)==0 or len(loginpass)==0):
            messagebox.showinfo("error","All fields are required",parent=self.users)
        else:
             try:
                import mysql.connector as d
                con = d.connect(host="localhost", user="root", password="root", database="library")
                cur = con.cursor()
                cur.execute("select * from register where stud_id='%s' and stu_passw='%s'" %(loginid,loginpass))

                row = cur.fetchone()
                if row==None:
                    messagebox.showinfo("error","invalid id/password",parent=self.users)
                else:
                    messagebox.showinfo("sucess", "login sucessfully",parent=self.users)
                    self.show_user()
             except Exception as es:
                messagebox.showinfo("error",es,parent=self.users)
                con.commit()
    def reset_register(self):
        self.stu_en.delete(0,"end")
        self.stu1_en.delete(0,"end")
        self.stu_pa.delete(0,"end")
        self.check_pa.delete(0,"end")
    def register_page(self):
        stu=Tk()
        # self.stu=stu
        stu.state("zoomed")
        stu.resizable(width=False, height=False)
        stu.config(bg="#ff6e40")
        stu.title("user register  page")
        headingFrame1 = Frame(stu, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="STUDENT REGISTER", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        stu_name = Label(stu, text="STUDENT NAME:", font=('bold', '17'),fg="black",bg="#ff6e40")
        stu_name.place(relx=.35, rely=.35)
        self.stu_en = Entry(stu,font=('Courier','15'),bd=4)
        self.stu_en.place(relx=.5, rely=.35)
        stu_id=Label(stu,text="STUDENT ID:",font=('bold','17'),fg="black",bg="#ff6e40")
        stu_id.place(relx=.35,rely=.45)
        self.stu1_en=Entry(stu,font=('Courier','15'),bd=4)
        self.stu1_en.place(relx=.5,rely=.45)
        stu_pass = Label(stu, text="PASSWORD:", font=('bold', '17'),fg="black",bg="#ff6e40")
        stu_pass.place(relx=.35, rely=.55)
        self.stu_pa = Entry(stu,show="*",font=('Courier','15'),bd=4)
        self.stu_pa.place(relx=.5, rely=.55)
        check_pass = Label(stu, text="CHECK PASS:", font=('bold', '17'),fg="black",bg="#ff6e40")
        check_pass.place(relx=.35, rely=.65)
        self.check_pa = Entry(stu,show="*",font=('Courier','15'),bd=4)
        self.check_pa.place(relx=.5, rely=.65)
        stu_bu=Button(stu,text="SUBMIT",font=('bold','17'),command=self.register,bg="black",fg="white")
        stu_bu.place(relx=.4,rely=.75,relwidth=0.1,relheight=0.07)
        reset = Button(stu, text="RESET", font=('bold', '17'), bg="black",fg="white",command=self.reset_register)
        reset.place(relx=.55, rely=.75,relwidth=0.1,relheight=0.07)
        back = Button(stu, text="BACK", font=('bold', '17'), command = lambda m=stu:refresh(self,m), bg="black",
                      fg="white")
        back.place(relx=.5, rely=.85, relwidth=0.07, relheight=0.07)
    def register(self):
        stu_name=self.stu_en.get()
        stud_id=self.stu1_en.get()
        stu_passw=self.stu_pa.get()
        stu_check=self.check_pa.get()
        if (stu_name=="" or stud_id=="" or stu_passw=="" or stu_check==""):
            messagebox.showinfo("error","All fields are required",parent=self.stu)
        elif (stu_passw != stu_check):
            messagebox.showinfo("error","password doesn't match",parent=self.stu)
        else:
            try:
                import mysql.connector as d
                con = d.connect(host="localhost", user="root", password="root", database="library")
                cur = con.cursor()
                cur.execute("insert into register values('%s','%s','%s','%s')" %(stu_name, stud_id, stu_passw, stu_check))
                messagebox.showinfo("sucess","register sucessfully",parent=self.users)
                con.commit()
            except Exception as es:
                messagebox.showinfo("error",es,parent=self.stu)

    def add_page(self):

        admin=Tk()
        self.admin=admin
        admin.state("zoomed")
        admin.resizable(width=False, height=False)
        admin.title("admin")
        admin.config(bg="red")
        headingFrame1 = Frame(admin, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="ADD BOOK", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        book_id = Label(admin, text="Book ID:", font=('bold', '17'),bg="red",fg="black")
        book_id.place(relx=.3, rely=.3)
        book_name=Label(admin,text="Book Name:",font=('bold','17'),bg="red",fg="black")
        book_name.place(relx=.3,rely=.4)
        author_name = Label(admin, text="Author Name:", font=('bold', '17'),bg="red",fg="black")
        author_name.place(relx=.3, rely=.5)
        qnty = Label(admin, text="Quantity:", font=('bold', '17'),bg="red",fg="black")
        qnty.place(relx=.3, rely=.6)
        self.bookid_entry = Entry(admin,font=('Courier','15'),bd=2)
        self.bookid_entry.place(relx=.43, rely=.3)
        self.bookname_entry=Entry(admin,font=('Courier','15'),bd=2)
        self.bookname_entry.place(relx=.43,rely=.4)
        self.authorname_entry = Entry(admin,font=('Courier','15'),bd=2)
        self.authorname_entry.place(relx=.43, rely=.5)
        self.quntyentry = ttk.Combobox(admin,font=('Courier','15'),state="readonly")
        self.quntyentry["value"]=('1','2','3','4','5','6','7','8','9','10')
        self.quntyentry.place(relx=.43, rely=.6)
        admin_submit=Button(admin,text="Submit",command=self.book_register,font=('bold', '17'),bg="black",fg="white")
        admin_submit.place(relx=.35,rely=.7,relwidth=0.1,relheight=0.07)
        quit = Button(admin, text="Quit",font=('bold', '17'),bg="black",fg="white",command=self.show_admin)
        quit.place(relx=.5, rely=.7,relwidth=0.1,relheight=0.07)
        # a.destroy()
    def issue_book(self):
        user=Tk()
        self.user=user
        user.title("User page")
        user.state("zoomed")
        user.resizable(width=False, height=False)
        user.config(bg="yellow")
        headingFrame1 = Frame(user, bg="red", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="ISSUE BOOK", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        book_id = Label(user, text="Book ID:", font=('bold', '17'),bg="yellow",fg="black")
        book_id.place(relx=.4, rely=.4)
        issued_to=Label(user,text="Issued TO:",font=('bold','17'),bg="yellow",fg="black")
        issued_to.place(relx=.4, rely=.5)
        self.book_id_entry = Entry(user,font=('Courier','15'),bd=4)
        self.book_id_entry.place(relx=.5, rely=.4)
        self.issued_entry=Entry(user,font=('Courier','15'),bd=4)
        self.issued_entry.place(relx=.5,rely=.5)
        user_submit = Button(user, text="Submit",command=self.issue,bg="black",font=('Courier','15'),fg="white")
        user_submit.place(relx=.4, rely=.6,relwidth=0.1,relheight=0.07)
        quit = Button(user, text="Quit",bg="black",font=('Courier','15'),fg="white",command=self.show_user)
        quit.place(relx=.55, rely=.6,relwidth=0.1,relheight=0.07)

    def book_register(self):
        import mysql.connector as d
        con = d.connect(host="localhost", user="root", password="root", database="library")
        cur = con.cursor()
        bid = self.bookid_entry.get()
        title = self.bookname_entry.get()
        author = self.authorname_entry.get()
        status = self.quntyentry.get()
        status = status.lower()
        if (len(bid)==0 or len(title)==0 or len(author)==0 or len(status)==0):
            messagebox.showinfo("error","All fields are required",parent=self.admin)
        else:
            try:
                cur.execute("INSERT  into books values(%s,%s,%s,%s)", (bid, title, author, status))
                con.commit()
                messagebox.showinfo("sucess", "books add sucessfully",parent=self.admin)
            except Exception as es:
                messagebox.showinfo("error", es,parent=self.admin)

    def issue(self):
        import mysql.connector as d
        con = d.connect(host="localhost", user="root", password="root", database="library")
        cur = con.cursor()
        bide=self.book_id_entry.get()
        issuedto=self.issued_entry.get()
        cur.execute("select status from books where bid='%s'"%(bide))
        q=0
        for i in cur:
           q=int(i[0])
        if q>=1:
            q=q-1
            cur.execute("update books set status='%s' where bid='%s'"%(q,bide))
            cur.execute("insert into issued values('%s','%s')"%(bide,issuedto))
            con.commit()
            messagebox.showinfo("sucess", "books issued sucessfully",parent=self.user)
        else:
            messagebox.showinfo("error","books not issued",parent=self.user)
    def view(self):
        import mysql.connector as d
        con = d.connect(host="localhost", user="root", password="root", database="library")
        cur=con.cursor()
        if con.is_connected():
            print("connected")
        else:
            print("not")
        vi=Tk()
        self.vi=vi
        vi.title("show books")
        vi.state("zoomed")
        vi.resizable(width=False,height=False)
        vi.config(bg="green")
        headingFrame1 = Frame(vi, bg="red", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="VIEW BOOK", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(vi, bg='black')
        labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
        y = 0.25
        Label(labelFrame, text="%-20s%-40s%-50s%-100s" % ('Book ID', 'Book Name', 'Author Name', 'Status'),
              bg='black', fg='white').place(relx=0.07, rely=0.1)
        Label(labelFrame, text="--------------------------------------------------------------------------------------------------"
                               "-----------------------------------------------------------------",
              bg='black', fg='white').place(relx=0.05, rely=0.2)
        getBooks="select * from books"
        quit = Button(vi, text="Quit",font=('Courier', '15'),command=self.show_admin)
        quit.place(relx=.45, rely=.85, relwidth=0.1, relheight=0.07)

        try:
            cur.execute(getBooks)
            data=cur.fetchall()
            con.commit()
            for i in data:
                Label(labelFrame, text="%-20s%-50s%-70s%-130s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white').place(
                    relx=0.07, rely=y)
                y += 0.1
        except:
            messagebox.showinfo("Failed to fetch files from database",parent=self.vi)
    def delete(self):
        de=Tk()
        self.de=de
        de.title("DELETE BOOK")
        de.state("zoomed")
        de.resizable(width=False, height=False)
        de.config(bg="orange")
        headingFrame1 = Frame(de, bg="red", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="DELETE BOOK", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        bookid = Label(de, text="Book ID:", font=('bold', '17'),fg="black",bg="orange")
        bookid.place(relx=.2, rely=.4)
        self.bookid_entry=Entry(de,font=('bold',17),bd=5)
        self.bookid_entry.place(relx=.2,rely=.5,relwidth=0.3,relheight=0.07)
        de_submit=Button(de,text="submit", command=self.delete_books,bg="black",fg="white")
        de_submit.place(relx=.2,rely=.6,relwidth=0.07,relheight=0.07)
        quit = Button(de, text="Quit", command=self.show_admin, bg="black", fg="white")
        quit.place(relx=.4, rely=.6, relwidth=0.07, relheight=0.07)

    def delete_books(self):
        import mysql.connector as d
        con = d.connect(host="localhost", user="root", password="root", database="library")
        cur = con.cursor()
        bid = self.bookid_entry.get()
        deletebooks="delete from books where bid ='"+bid+"'"
        deleteissue="delete from issued where bid = '"+bid+"'"
        try:
            if (len(bid)==0):
                messagebox.showinfo("error","Book id is necessary",parent=self.de)
            else:
                cur.execute(deletebooks)
                con.commit()
                cur.execute(deleteissue)
                con.commit()
                messagebox.showinfo("sucess","Book delete ",parent=self.de)
        except:
            messagebox.showinfo("Error","Please check book id",parent=self.de)
    def returnbook(self):
        re=Tk()
        self.re=re
        re.title("Return Book")
        re.state("zoomed")
        re.resizable(width=False, height=False)
        re.config(bg="purple")
        headingFrame1 = Frame(re, bg="red", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="RETURN BOOK", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        bookid_la = Label(re, text="BOOK ID:", font=('bold', '17'), fg="pink",bg="purple")
        bookid_la.place(relx=.3, rely=.3)
        self.BOOKID_entry = Entry(re,font=('bold',15),bd=2)
        self.BOOKID_entry.place(relx=.3, rely=.35,relwidth=0.3,relheight=0.05)
        issuedto_la=Label(re,text="ISSUED TO:",font=('bold', '17'),fg="pink",bg="purple")
        issuedto_la.place(relx=.3,rely=.45)
        self.issuedto_entry = Entry(re,font=('bold',15),bd=2)
        self.issuedto_entry.place(relx=.3, rely=.5,relwidth=0.3,relheight=0.05)
        user_submit = Button(re, text="Submit", command=self.return_book,bg="black",fg="pink",font=('bold',17))
        user_submit.place(relx=.3, rely=.6,relwidth=0.07,relheight=0.07)
        quit_submit = Button(re, text="Quit", command=self.show_user, bg="black", fg="pink",font=('bold',17))
        quit_submit.place(relx=.45, rely=.6, relwidth=0.07, relheight=0.07)
    def return_book(self):
        import mysql.connector as d
        con=d.connect(host="localhost",database="library",user="root",password="root")
        cur=con.cursor()
        BID=self.BOOKID_entry.get()
        issue = self.issuedto_entry.get()
        cur.execute("select * from issued where bid='%s'"%(BID))
        for i in cur.fetchall():
            # print(i)
            id=i[0]
            name=i[1]
            print(id,name)
            status= cur.execute("select status from books where bid ='%s'" %(id))
            status = cur.fetchall()
            print(status)
            status = status[0]
            print(status)
            q=int(status[0])
            print(q)
        if (len(BID)==0 or len(issue)==0):
            messagebox.showinfo("Error","All fields are required!",parent=self.re)
        else:
            try:
                if (name==issue):
                    print('yes')
                    q = q + 1
                    cur.execute("update books set status='%s' where bid='%s'" % (q, id))
                    cur.execute("delete from issued where (bid,issuedto)=('%s','%s')" % (BID, issue))
                    messagebox.showinfo("sucess", "Book return ", parent=self.re)
                    con.commit()
                else:
                    messagebox.showinfo("error",'name not found',parent=self.re)

            except Exception as es:
                messagebox.showinfo(es,parent=self.re)

    def view_stu(self):
        import mysql.connector as d
        con = d.connect(host="localhost", user="root", password="root", database="library")
        cur = con.cursor()
        if con.is_connected():
            print("connected")
        else:
            print("not")
        vi_su = Tk()
        self.vi_su=vi_su
        vi_su.title("show books")
        vi_su.state("zoomed")
        vi_su.resizable(height=False,width=False)
        vi_su.config(bg="green")
        headingFrame1 = Frame(vi_su, bg="red", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
        headingLabel = Label(headingFrame1, text="STUDENT RECORD", bg='black', fg='white',
                             font=('Courier', 20))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(vi_su, bg='black')
        labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
        y = 0.25
        Label(labelFrame, text="%-10s%-40s" % ('Book ID', 'ISSUED TO'),font=('Courier',14),
              bg='black', fg='white').place(relx=0.07, rely=0.1)
        Label(labelFrame, text="----------------------------------------------------------------------------",
              bg='black', fg='white').place(relx=0.05, rely=0.2)
        getBooks = "select * from issued"
        quit = Button(vi_su, text="Quit", font=('Courier', '20'), command=self.show_user,bg='black',fg='white')
        quit.place(relx=.45, rely=.85, relwidth=0.1, relheight=0.07)

        try:
            cur.execute(getBooks)
            data = cur.fetchall()
            con.commit()
            for i in data:
                Label(labelFrame, text="%-10s%-40s" % (i[0], i[1]), bg='black', fg='white',font=('Courier',14)).place(
                    relx=0.07, rely=y)
                y += 0.1
        except:
            messagebox.showinfo("error","Failed to fetch files from database",parent=self.vi_su)


obj=Multiple(root)
root.mainloop()