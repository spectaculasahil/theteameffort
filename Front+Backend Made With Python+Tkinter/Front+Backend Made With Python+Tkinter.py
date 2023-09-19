def legalinfo():
    messagebox.showinfo('Caution','''This is a an End user license agreement acknowledging that this software is made by  all the factors written afterwards would result in a strict legal action
    :  1. Using this product for any sort of criminal activity 2.Tampering or plagiarising this product 3. Use of the software outside the
    company policy . Refer to  for more information   ''')

def help():
    messagebox.showinfo('Hello','Login if you have an account or Sign UP if you don\'t')



def tablecheck():
    import mysql.connector as sqltor
    connect=sqltor.connect(host='localhost',user='root',passwd='1234')
    cursor=connect.cursor()
    cursor.execute('use customer_database;')
    cursor.execute('show tables;')
    if ('login_info',) in cursor:
        messagebox.showinfo('Table Integrity','Table found no need to be created')
    else:
        cursor.execute(' create table login_info(cust_id int(9) auto_increment primary key,cust_name char(40),cust_email varchar(60),cust_Phno varchar(13),cust_address varchar(100),cust_password varchar(100),cust_balance int(9));')
        messagebox.showinfo('Table Integrity','Table was not found but now is created')

                                                                                  


def newaccountsignup():
    def register():
        x1=Name.get()
        messagebox.showinfo('Success','Thanks for creating the account')
        x2=Email.get()
        x3=Phno.get()
        x4=Add.get()
        x5=Passwd.get()
        import mysql.connector as sqltor
        connect=sqltor.connect(host='localhost',user='root',passwd='1234')
        cursor=connect.cursor()
        cursor.execute('use customer_database;')
        sql="insert into login_info(cust_name,cust_email,cust_Phno,cust_address,cust_password,cust_balance) values(%s,%s,%s,%s,%s,%s)"
        data=(x1,x2,int(x3),x4,x5,85000)
        cursor.execute(sql,data)
        connect.commit()
        
        

    signup=Toplevel()
    signup.configure(bg='black')
    signup.geometry('300x320')
    signup.title('Enter your details')
    btnconfirm=Button(signup,text='Confirm',command=register)
    btnconfirm.place(x=135,y=280)
    Name=Entry(signup,width=30)
    Name.place(x=72,y=82)
    lName=Label(signup,text='Name')
    lName.place(x=30,y=82)
    Email=Entry(signup,width=30)
    Email.place(x=72,y=122)
    lEmail=Label(signup,text='Email')
    lEmail.place(x=30,y=122)
    Phno=Entry(signup,width=30)
    Phno.place(x=72,y=162)
    lPhno=Label(signup,text='Phone')
    lPhno.place(x=30,y=162)
    Add=Entry(signup,width=30)
    Add.place(x=72,y=202)
    lAdd=Label(signup,text='Address')
    lAdd.place(x=15,y=202)
    Passwd=Entry(signup,width=30)
    Passwd.place(x=72,y=242)
    lPasswd=Label(signup,text='Password')
    lPasswd.place(x=10,y=242)
    
    

def connectioncheck():
    import mysql.connector as sqltor
    connect=sqltor.connect(host='localhost',user='root',passwd='1234')
    if connect.is_connected:
        messagebox.showinfo('Database Check','Connection to database established')
        cursor=connect.cursor()
        cursor.execute('show databases;')
        if ('customer_database',) in cursor:
            messagebox.showinfo('Database Check','Master Database present')
        else:
            cursor.execute('create database customer_database;')
            messagebox.showinfo('Database Check','Master Database was not present but now it is Created')
            
    else:
        messagebox.showinfo('Database Check','No Connection established')

def loginaccount():
    a=()
    e1=Emailidlogin.get()
    p1=Passwordlogin.get()
    import mysql.connector as sqltor
    connect=sqltor.connect(host='localhost',user='root',passwd='1234')
    cursor=connect.cursor()
    cursor.execute('use customer_database;')
    cursor.execute('select * from login_info;')
    rows=cursor.fetchall()
    for x in rows:
        a=a+x
    if e1 not in a and p1 in a:
        messagebox.showinfo('Login','Account not present Sign up first !')
    elif e1 and p1 in a:
        messagebox.showinfo('Login','Account found redirecting you to diferent window')
        s=a.index(e1)
        global v
        v=a[s-1]
        u=a[s+4]

        def afterlogin():
            def laptops():
                from tkinter import ttk
                def prod1():
                    cart=Toplevel()
                    cart.configure(bg='black')
                    cart.geometry('350x200')
                    cart.title('Enter Quantity')
                    cartet=Entry(cart,width=30)
                    cartet.place(x=100,y=82)
                    lName=Label(cart,text='Enter Quantity')
                    lName.place(x=0,y=80)
                    prodidb=Entry(cart,width=30)
                    prodidb.place(x=100,y=120)
                    lNameprodidb=Label(cart,text='Enter Product_ID')
                    lNameprodidb.place(x=0,y=120)


                    
                    
                    

                stuff=Toplevel()
                tv=ttk.Treeview(stuff,columns=(1,2,3,4,5),show='headings',height='50')
                tv.pack()
                tv.heading(1,text='Product_ID')
                tv.heading(2,text='Product_Name')
                tv.heading(3,text='Product_Price')
                tv.heading(4,text='Product_Quantity')
                tv.heading(5,text='Product_Type')
                
                
                stuff.title('Watches Section')
                stuff.geometry('1600x900')
                import mysql.connector as sqltor
                connect=sqltor.connect(host='localhost',user='root',passwd='1234')
                cursor=connect.cursor()
                cursor.execute('use customer_database;')
                cursor.execute('select * from stock where prod_type="Laptop";')
                for x in cursor:
                    tv.insert('','end',values=x)
                btcart=Button(stuff,text='Add to cart',command=prod1)
                btcart.place(x=25,y=150)
            def watches():
                from tkinter import ttk
                def prod1():
                    cart=Toplevel()
                    cart.configure(bg='black')
                    cart.geometry('350x200')
                    cart.title('Enter Quantity')
                    cartet=Entry(cart,width=30)
                    cartet.place(x=100,y=82)
                    lName=Label(cart,text='Enter Quantity')
                    lName.place(x=0,y=80)
                    prodidb=Entry(cart,width=30)
                    prodidb.place(x=100,y=120)
                    lNameprodidb=Label(cart,text='Enter Product_ID')
                    lNameprodidb.place(x=0,y=120)

            globalscreen2=Toplevel()
            globalscreen2.title('Category Selection')
            globalscreen2.geometry('1600x900')
            photo3=PhotoImage(file='Categoryselection.gif')
            lbphoto3=Label(globalscreen2,image=photo3,bg='black')
            lbphoto3.photo=photo3
            lbphoto3.place(x=0,y=0)
            btnwatch= Button(globalscreen2, text="",command=watches)
            btnwatch.place(x=750,y=750)

            

            lusername=Label(globalscreen2,text=('USER : ',v))
            lusername.place(x=1432,y=148)
            
            lbalance=Label(globalscreen2,text=('Your Bank Balance (Rs):',u))
            lbalance.place(x=1390,y=170)

            
            btnclcart = Button(stuff, text="Clear Cart",command=clearcart)
            btnclcart.place(x=25,y=100)
            btnbuynow=Button(stuff,text='Buy And Pay Now',command=buynow)
            btnbuynow.place(x=0,y=200) 
            lusername=Label(stuff,text=('Total Price Rs: ',h))
            lusername.place(x=1300,y=800)


        afterlogin()    
    else:
        messagebox.showinfo('Login','Account not present Sign up first !')
        
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
window=Tk()
window.title('Welcome to Curiosity!!')
window.configure(bg='black')
photo=PhotoImage(file='1.gif')
lblogo=Label(window,image=photo,bg='black')
lblogo.place(x=650,y=150)
window.geometry('1600x900')
btnlog = Button(window, text="Login",command=loginaccount)
btnsign = Button(window, text="Sign Up",command=newaccountsignup)
btnlog.place(x=740,y=597)
btnlegalinfo=Button(window, text="Legal Info",command=legalinfo)
btnlegalinfo.grid(row=20,column=1)
btnhelp = Button(window, text="Help!!!",command=help)
btnhelp.grid(row=4,column=1)
btnsign.place(x=825,y=597)
btnconnectioncheck=Button(window,text='Click here to make sure master database is available',command=connectioncheck)
btnconnectioncheck.place(x=1221,y=780)
btntableintegrity=Button(window,text='Click here to test table integity',command=tablecheck)
btntableintegrity.place(x=1000,y=780)
Emailidlogin=Entry(window,width=30)
Emailidlogin.place(x=736,y=478)
lEmailidlogin=Label(window,text='EmailID')
lEmailidlogin.place(x=670,y=478)
Passwordlogin=Entry(window,width=30)
Passwordlogin.place(x=736,y=525)
lPasswordlogin=Label(window,text='Password')
lPasswordlogin.place(x=670,y=525)
window.mainloop()











    





    
