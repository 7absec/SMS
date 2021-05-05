from tkinter import *
from tkinter import ttk 
import pymysql
from tkinter import messagebox


class Password:

    def __init__(self,root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student Management System",bd = 10,
                relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")
        title.pack(side=TOP,fill=X)

        
        #Variables
        self.username = StringVar()
        self.old_password = StringVar()
        self.new_password = StringVar()


        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.student_btn).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        create_btn = Button(Dash_Frame,bg="#00A1E4",text="Create",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.create_btn).grid(row=1,column=0,padx=2,pady=0,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=1250,height=600)

               
        m_title = Label(Manage_Frame,text="Change Password",bg="#F0EDEE",fg="#0A090C",font=("Arial",30,"bold","italic")).grid(row = 0,columnspan=2,pady=20,padx=450)
        lbl_username = Label(Manage_Frame,text="Username -",bg="#F0EDEE",fg="#0A090C",font=("Arial",15,"bold")).grid(row = 1,column=0,pady=10,padx=500)
        txt_dept_id = Entry(Manage_Frame,textvariable=self.username,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 2,column=0,pady=10,padx=500)
        lbl_name = Label(Manage_Frame,text="Old Password -",bg="#F0EDEE",fg="#0A090C",font=("Arial",15,"bold")).grid(row = 3,column=0,pady=10,padx=500)
        txt_name = Entry(Manage_Frame,show="*",textvariable=self.old_password,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 4,column=0,pady=10,padx=500)
        lbl_name = Label(Manage_Frame,text="New Password -",bg="#F0EDEE",fg="#0A090C",font=("Arial",15,"bold")).grid(row = 5,column=0,pady=10,padx=500)
        txt_name = Entry(Manage_Frame,show="*",textvariable=self.new_password,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 6,column=0,pady=10,padx=500)
        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=400,y=420,width=410) 
        chg_btn = Button(btn_frame,text="Change Password",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=30,command=self.change_pass).grid(row=0,column=0,padx=90,pady=10,ipady=4)

       
                         

    def change_pass(self):

        if self.username.get() == "" or self.old_password.get() == "" or self.new_password.get() == "":
            messagebox.showerror("Error","Fields Missing")

        else:
            connect = pymysql.connect(host="localhost",user="root", passwd="user",database="Student")
            curr = connect.cursor()
            curr.execute("SELECT * from admin")
            rows = curr.fetchall()
            
            for row in rows:
                if row[1] == self.username.get() and row[2] == self.old_password.get():
                    connect = pymysql.connect(host="localhost",user="root", passwd="user",database="Student")  
                    curr = connect.cursor()
                    curr.execute("UPDATE ADMIN SET password=%s where username=%s", (self.new_password.get(),self.username.get()))

                    connect.commit()
                    connect.close()
                    messagebox.showinfo("Success","Password Updated Successsfully")
                else:
                    messagebox.showerror("Error","Please Make Sure That the Details are Correct")

         

    def logout(self):
        self.root.destroy() 
        st_root = Tk()
        st = Login(st_root)
        st_root.mainloop()

       
    def student_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Student(st_root)
        st_root.mainloop()

    def create_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = create(st_root)
        st_root.mainloop()



class create:

    def __init__(self,root):

        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student Management System",bd = 10,relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9")
        title.pack(side=TOP,fill=X)

        
        #Variables
        self.admin = StringVar()
        self.username = StringVar()
        self.password = StringVar()


        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)

        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.student_btn).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        create_btn = Button(Dash_Frame,bg="#00A1E4",text="Create",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20).grid(row=1,column=0,padx=2,pady=0,sticky="w")

        password_btn = Button(Dash_Frame,text="Password",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20, command=self.password_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE",font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=1250,height=600)

               
                
        m_title = Label(Manage_Frame,text="Create user",bg="#F0EDEE",fg="#0A090C",font=("Arial",30,"bold","italic")).grid(row = 0,columnspan=2,pady=20,padx=450)
        lbl_id = Label(Manage_Frame,text="Admin Id -",bg="#F0EDEE",fg="#0A090C",font=("Arial",15,"bold")).grid(row = 1,column=0,pady=10,padx=500)
        txt_admin = Entry(Manage_Frame,textvariable=self.admin,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 2,column=0,pady=10,padx=500)
        lbl_username = Label(Manage_Frame,text="Username -",bg="#F0EDEE",fg="#0A090C",font=("Arial",15,"bold")).grid(row = 3,column=0,pady=10,padx=500)
        txt_usr = Entry(Manage_Frame,textvariable=self.username,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 4,column=0,pady=10,padx=500)
        lbl_name = Label(Manage_Frame,text="Password -",bg="#F0EDEE",fg="#0A090C",font=("Arial",15,"bold")).grid(row = 5,column=0,pady=10,padx=500)
        txt_pass = Entry(Manage_Frame,textvariable=self.password,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 6,column=0,pady=10,padx=500)
        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=400,y=420,width=410) 
        crt_btn = Button(btn_frame,text="Create User",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=30,command=self.create_user).grid(row=0,column=0,padx=90,pady=10,ipady=4)

       
                         

    def create_user(self):

        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error","Fields Missing")

        else:
            connect = pymysql.connect(host="localhost",user="root", passwd="user",database="Student")
            curr = connect.cursor()
            curr.execute("insert into Admin values(%s,%s,%s)" ,(self.admin.get(),self.username.get(),self.password.get()))
            connect.commit()
            connect.close()
            messagebox.showinfo("Success","Password Updated Successsfully")


    def logout(self):
        self.root.destroy() 
        st_root = Tk()
        st = Login(st_root)
        st_root.mainloop()

       
    def student_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Student(st_root)
        st_root.mainloop()

    def password_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Password(st_root)
        st_root.mainloop()




class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        
        title = Label(self.root,text="Student Management System",bd = 10,relief=GROOVE,font=("Arial",43,"bold"),bg="#00A1E4",fg="#FFFCF9").pack(side=TOP,fill=X)        

        #Variables
        self.roll_no = StringVar()
        self.name = StringVar()
        self.email_id = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.address = StringVar()
        self.search_combo = StringVar()
        self.search_field = StringVar()

        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Dash_Frame.place(x=2,y=95,width=98,height=600)        

        manage_student_btn = Button(Dash_Frame,bg="#00A1E4",text="Student",fg="#F0EDEE", font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20).grid(row=0,column=0,padx=2,pady=0,sticky="w")
        password_btn = Button(Dash_Frame,text="create",bg="#00A1E4",fg="#F0EDEE", font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")
        exit_btn = Button(Dash_Frame,text="Exit",bg="#00A1E4",fg="#F0EDEE", font=("Arial",9,"bold"),relief=GROOVE,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Manage_Frame.place(x=100,y=95,width=450,height=600)
        m_title = Label(Manage_Frame,text="Manage Student",bg="#F0EDEE",fg="#0A090C",font=("Arial",30,"bold","italic")).grid(row = 0,columnspan=2,pady=20)
        lbl_roll = Label(Manage_Frame,text="Roll No.",bg="#F0EDEE",fg="black",font=("Arial",15,"bold")).grid(row = 1,column=0,pady=10,padx=20,sticky="w")
        txt_Roll = Entry(Manage_Frame,textvariable=self.roll_no,font=("Arial",15,"bold"), bd=5,relief=GROOVE).grid(row = 1,column=1,pady=10,padx=20,sticky="w")
        lbl_name = Label(Manage_Frame,text="Name.",bg="#F0EDEE",fg="black",font=("Arial",15,"bold")).grid(row = 2,column=0,pady=10,padx=20,sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name,font=("Arial",15,"bold"), bd=5,relief=GROOVE).grid(row = 2,column=1,pady=10,padx=20,sticky="w")
        lbl_email = Label(Manage_Frame,text="Email-ID.",bg="#F0EDEE",fg="black", font=("Arial",15,"bold")).grid(row = 3,column=0,pady=10,padx=20,sticky="w")
        txt_email = Entry(Manage_Frame,textvariable=self.email_id, font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_contact = Label(Manage_Frame,text="Contact",bg="#F0EDEE",fg="black", font=("Arial",15,"bold")).grid(row = 5,column=0,pady=10,padx=20,sticky="w")
        txt_contact = Entry(Manage_Frame,textvariable=self.contact, font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 5,column=1,pady=10,padx=20,sticky="w")
        
        bl_gender = Label(Manage_Frame,text="Gender",bg="#F0EDEE",fg="black", font=("Arial",15,"bold")).grid(row = 4,column=0,pady=10,padx=20,sticky="w")
        gender_box = ttk.Combobox(Manage_Frame,textvariable=self.gender,font=("Arial",13,"bold"),state="readonly")
        gender_box['values'] =("Male","Female","Other")
        gender_box.grid(row=4,column=1,pady=10,padx=20,sticky="w")    

        lbl_DOB = Label(Manage_Frame,text="D.O.B",bg="#F0EDEE",fg="black", font=("Arial",15,"bold")).grid(row = 6,column=0,pady=10,padx=20,sticky="w")
        self.txt_DOB = Entry(Manage_Frame,textvariable=self.dob,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 6,column=1,pady=10,padx=20,sticky="w")
        
        lbl_address = Label(Manage_Frame,text="Address",bg="#F0EDEE",fg="black",font=("Arial",15,"bold")).grid(row = 7,column=0,pady=10,padx=20,sticky="w")
        self.txt_address = Text(Manage_Frame,bd=2,relief=RIDGE,width =30,height=4).grid(row = 7,column=1,pady=10,padx=20,sticky="w")
        
        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=12,y=520,width=410) 
        add_btn = Button(btn_frame,text="Add",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.add_student).grid(row=0,column=0,padx=5,pady=10)
        update_btn = Button(btn_frame,text="Update",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)
        delete_btn = Button(btn_frame,text="Delete",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)
        clear_btn = Button(btn_frame,text="Clear",width=10,bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        #Detail Frame
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=550,y=95,width=800,height=600)
        lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",font=("Arial",18,"bold")).grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,font=("Arial",13,"bold"),state="readonly")
        search_box['values'] = ("Roll_No","Name","Contact_No")
        search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,font=("Arial",10,"bold"),bd=5,relief=GROOVE).grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")        
        search_btn = Button(Detail_Frame,text="Search",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.search_data).grid(row=0,column=5,padx=10,pady=10)
        show_all_btn = Button(Detail_Frame,text="Show All",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.show_data).grid(row=0,column=6,padx=10,pady=10)
        logout_btn = Button(Detail_Frame,text="Log Out",bg="#00A1E4",fg="#FFFCF9",font=("Arial",10,"bold"),relief=GROOVE,width=10,pady=5,command=self.logout).grid(row=0,column=7,padx=10,pady=10)


 #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=10,y=60,width=760,height=505)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Roll-No","Name","Gender","Contact No","Email-ID","D.O.B","Address",),xscrollcommand=X_scroll.set,
        yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("Roll-No",text="Roll-No")
        self.Table.heading("Name",text="Name")
        self.Table.heading("Gender",text="Gender")
        self.Table.heading("Contact No",text="Contact No")
        self.Table.heading("Email-ID",text="Email-ID")
        self.Table.heading("D.O.B",text="D.O.B")
        self.Table.heading("Address",text="Address")

        

        self.Table['show']="headings"
        self.Table.column("Roll-No",width=100)
        self.Table.column("Name",width=100)
        self.Table.column("Gender",width=100)
        self.Table.column("Contact No",width=100)
        self.Table.column("Email-ID",width=100)
        self.Table.column("D.O.B",width=100)
        self.Table.column("Address",width=150)

        

        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        self.txt_DOB.bind("<FocusIn>", self.foc_in)
        self.txt_DOB.bind("<FocusOut>", self.foc_out)


        self.put_placeholder()
        self.show_data()

       
        


    def add_student(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.gender.get()== "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect(host="localhost",user="root",passwd="user",database="Student")
            curr = connect.cursor()
            curr.execute("INSERT INTO STUDENT VALUES(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no.get(), self.name.get(), self.gender.get(), self.contact.get(), self.email_id.get(), self.dob.get(), self.address.get() ))
            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Added")

    def show_data(self):

        connect = pymysql.connect(host="localhost",user="root", passwd="user",database="Student")
        curr = connect.cursor()
        
        curr.execute("SELECT * from student")
        rows = curr.fetchall()

        if(len(rows)!=0):

            self.Table.delete(*self.Table.get_children())
            for row in rows:
                self.Table.insert('',END,values=row)
            connect.commit()
        connect.close()        

    def clear_field(self):
        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == ""  or self.contact.get() == "" :
            messagebox.showerror("Error","Fields Empty")

        else:
            self.roll_no.set("")
            self.name.set("")
            self.gender.set("")
            self.contact.set("")
            self.email_id.set("")           
            self.dob.set("")
            self.address.set("")

    def get_fields(self,event):
        cursor_row = self.Table.focus()
        content = self.Table.item(cursor_row)
        row = content['values']
        self.roll_no.set(row[0])
        self.name.set(row[1])
        self.gender.set(row[2])
        self.contact.set(row[3])
        self.email_id.set(row[4])
        self.dob.set(row[5])
        self.address.delete()

    def update(self):
        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.contact.get() == "":
            messagebox.showerror("Error","Fields are Empty")

        else:
            connect = pymysql.connect(host="localhost",user="root", passwd="user",database="Student")
            curr = connect.cursor()
            curr.execute("UPDATE STUDENT SET name=%s,gender=%s,contact_no=%s,email_id=%s,dob=%s, address=%s where roll_no=%s",(self.name.get(),self.gender.get(),self.contact.get(),self.email_id.get(),  self.dob.get(), self.address.get(),  self.roll_no.get() ))
            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Updated")

    def delete(self):
        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.contact.get() == "":
            messagebox.showerror("Error","Fields are Empty")

        else:
            connect = pymysql.connect(host="localhost",user="root", passwd="user",database="Student")
            curr = connect.cursor()
            curr.execute("DELETE from STUDENT where roll_no=%s",(self.roll_no.get()))
            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Deleted")

    def search_data(self):
        if self.search_combo.get() == "" or self.search_field.get() == "":
            messagebox.showerror("Error","Some Fields might be Empty")

        else:
            connect = pymysql.connect(host="localhost",user="root", passwd="user",database="Student")
            curr = connect.cursor()
            curr.execute("SELECT * from student where "+str(self.search_combo.get())+ " LIKE '%"+str(self.search_field.get())+"%'")
            rows = curr.fetchall()

            if(len(rows)!=0):
                self.Table.delete(*self.Table.get_children())
                for row in rows:
                    self.Table.insert('',END,values=row)
                connect.commit()
            connect.close()

    def put_placeholder(self):
        self.txt_DOB.insert(0,"DD-MM-YYYY")
        self.txt_DOB['fg'] = "grey"

    def foc_in(self,event):
        if self.txt_DOB['fg'] == "grey":
            self.txt_DOB.delete('0', 'end')
            self['fg'] = "grey"

    def foc_out(self, event):
        if not self.get():
            self.txt_DOB.put_placeholder()

    def logout(self):
        self.root.destroy() 
        st_root = Tk()
        st = Login(st_root)
        st_root.mainloop()        

    def pass_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = create(st_root)
        st_root.mainloop()


class Login:

    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("350x350+450+200")
        self.root.resizable(0,0)
        self.username = StringVar()
        self.password = StringVar()

        title = Label(self.root,text="Login",bd = 5,relief=GROOVE,font=("Arial",30,"bold"),bg="#FFFCF9",fg="#0A090C").pack(side=TOP,fill=X)
        Main_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame.place(x=0,y=60,width=350,height=290)
        lbl_username = Label(Main_Frame,text="Username :-",bg="#F0EDEE",fg="#0A090C",font=("Arial",10,"bold")).grid(row = 1,column=0,pady=45,padx=30,sticky="w")
        txt_username = Entry(Main_Frame,textvariable=self.username,width = 12,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 1,column=1,pady=45,padx=5,sticky="w")
        lbl_password = Label(Main_Frame,text="Password :-",bg="#F0EDEE",fg="#0A090C",font=("Arial",10,"bold")).grid(row = 2,column=0,pady=5,padx=30,sticky="w")
        txt_password = Entry(Main_Frame,show="*",textvariable=self.password,width = 12,font=("Arial",15,"bold"),bd=5,relief=GROOVE).grid(row = 2,column=1,pady=5,padx=5,sticky="w")
        btn_frame = Frame(Main_Frame,bg="#F0EDEE")
        btn_frame.place(x=100,y=200,width=170)
        login_btn = Button(btn_frame,text="Login",width=20,relief=GROOVE,bg="#00A1E4",font=("Arial",10,"bold"),command=self.validate_user).grid(row=0,column=0,padx=0,pady=10)        

    def validate_user(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error","Fields Missing")

        else:
            connect = pymysql.connect(host="localhost",user="root", passwd="user",database="Student")
            curr = connect.cursor()
            curr.execute("SELECT * from admin")
            rows = curr.fetchall()

            for row in rows:
                if row[1] == self.username.get() and row[2]== self.password.get():
                    self.root.destroy() 
                    st_root = Tk()
                    st = Student(st_root)
                    st_root.mainloop()  

                else:
                    messagebox.showerror("Error","Please Make Sure That the Details are Correct")
            

root = Tk()
st = Login(root)
root.mainloop()