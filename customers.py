from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector as mysql
import Home_Frame

class customers:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def customers_func():
      
        cus_frame=Frame(Home_Frame.win,bg="bisque2",bd=5,relief=GROOVE)
        cus_frame.place(x=230, y=200, width=1305, height=600)
    
      
        cus_name = Label(cus_frame,text="Customer's Name",font=("Calibari,Bold",12),bg="whitesmoke",fg="black")
        cus_name.place(x=200,y=0)

        cus_entry = Entry(cus_frame,width=20,font=("Calibari Bold",12))
        cus_entry.place(x=400,y=0)


        cus_phnum = Label(cus_frame,text="Customer's Phone_number",font=("Calibari,Bold",12),bg="whitesmoke",fg="black")
        cus_phnum.place(x=600,y=0)

        cus_phnum_entry = Entry(cus_frame,width=20,font=("Calibari Bold",12))
        cus_phnum_entry.place(x=800,y=0)

        def Addcustomers():
            name = cus_entry.get()
            phno = cus_phnum_entry.get()
            if(name == ""):
                messagebox.showerror("REQUIRED_FIELD","Invalid Field Name")
            elif(phno == ""):
                messagebox.showerror("REQUIRED_FIELD","Invalid Field Name")
            else:
                conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
                cursor = conn.cursor()
                insert_query = "insert into customers(cus_name,cus_phno) values(%s,%s)"
                insert_data = (name,phno)
                cursor.execute(insert_query,insert_data)
                cursor.execute("commit")
                conn.close()
        def Deletecustomers():
          
            phno = cus_phnum_entry.get()

            if phno == "":
                messagebox.showerror("REQUIRED_FIELD","Invalid Field Name")
            else:
                conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
                cursor = conn.cursor()
                delete_query = "delete from customers where cus_phno = %s"
                delete_data = [phno]
                cursor.execute(delete_query,delete_data)
                cursor.execute("commit")
                conn.close()  

        submit = Button(cus_frame,text="Add",bg="black",fg="white",border=2,relief=GROOVE,width=15,command=Addcustomers)
        submit.place(x=200,y=50)
        delete = Button(cus_frame,text="Delete",bg="black",fg="white",border=2,relief=GROOVE,width=15,command=Deletecustomers)
        delete.place(x=400,y=50)
        def fetch_data():
            
            display_frame=Frame(cus_frame,width=700,height=400,bg="black")
            display_frame.place(x=200, y=100)
            y_scroll = ttk.Scrollbar(display_frame,orient=VERTICAL)
            x_scroll = ttk.Scrollbar(display_frame,orient=HORIZONTAL)

            customer_table = ttk.Treeview(display_frame,columns=("id","cus_name","cus_phno"),yscrollcommand=y_scroll,xscrollcommand=x_scroll)
            y_scroll.config(command=customer_table.yview)
            x_scroll.config(command=customer_table.xview)
            y_scroll.pack(side = RIGHT,fill=Y)
            x_scroll.pack(side = BOTTOM,fill=X)

            customer_table.heading("id",text="id")
            customer_table.heading("cus_name",text="cus_name")
            customer_table.heading("cus_phno",text="cus_phno")
            customer_table.column("id",width=300,anchor=CENTER)
            customer_table.column("cus_name",width=300,anchor=CENTER)
            customer_table.column("cus_phno",width=300,anchor=CENTER)
            customer_table['show'] = 'headings'
            customer_table.pack(fill=BOTH,expand=True)
            conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
            cursor = conn.cursor()
            cursor.execute("select * from customers")
            fetch_all = cursor.fetchall()
            if len(fetch_all)!=0:
                customer_table.delete(*customer_table.get_children())
                for cus in fetch_all:
                    customer_table.insert('',END,values = cus)
                    
                conn.close()
        fetch_data()

            