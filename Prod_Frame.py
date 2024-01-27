from tkinter import *
from tkinter import ttk


import mysql.connector as mysql
import display_products
from tkinter import messagebox

import customers
import Billing


import update_frame
import Home_Frame


import delete_frame
import bill_data


import pyttsx3
f1 = Frame(Home_Frame.win,height=200,width=Home_Frame.width,bg="lightgreen",border=5,relief=GROOVE)
f1.place(x=0,y=0)


ice = Label(f1,text="CORNER HOUSE ICE-CREAM",font=("Arial 10 bold"),bg="whitesmoke",fg="black",padx=10,pady=10)
ice.place(x=600,y=20)


f2 = Frame(Home_Frame.win,height=Home_Frame.height,width=230,bg="whitesmoke",border=5,relief=GROOVE)
f2.place(x=0,y=200)

prod = Label(f2,text="PRODUCTS",font=("Arial 10 bold"),bg="whitesmoke",fg="black",padx=10,pady=10)
prod.place(x=60,y=0)

class prod_add:
    def __init__(self,height,width):
        self.height = height
        self.width = width


    def Add():
    
        add_frame=Frame(Home_Frame.win,bg="bisque2",bd=5,relief=GROOVE)
        add_frame.place(x=230, y=200, width=1305, height=590)
    
        canvas1=Canvas(add_frame,width=600,height=500,bg="black").place(x=270, y=40)
        name = Label(add_frame,fg="white",bg="black", text="Product Name: ", font=("calibri Bold",15)).place(x=350, y=100)


        name_entry = Entry(add_frame,width=20,font=("calibri Bold",10),bg="snow")
        name_entry.place(x=500,y=105)

        combo = Label(add_frame,text="Catagory: ",bg="black",fg="white",font=("Calibri Bold",15))
        combo.place(x=350,y=150)


        var1 = StringVar()
        combo_ttk = ttk.Combobox(add_frame,textvariable=var1,values="CHOCKOLATES")
        

        list = ["CHOCKOLATES","ICE_CREAM","MILK_SHACK","SANDWITCHES","SUNDAE","CONES "]
        combo_ttk['values'] = (list)

        

        combo_ttk.place(x=500,y=150)

        qty = Label(add_frame,fg="white",bg="black", text="Quntity: ", font=("calibri Bold",15)).place(x=350, y=200)
        qty_entry = Entry(add_frame,width=20,font=("calibri Bold",10),bg="snow")


        qty_entry.place(x=500,y=200)
        qty_entry.insert(0,0)

        price = Label(add_frame,fg="white",bg="black", text="Price: ", font=("calibri Bold",15)).place(x=350, y=250)
        price_entry = Entry(add_frame,width=20,font=("calibri Bold",10),bg="snow")


        price_entry.place(x=500,y=250)
        price_entry.insert(0,0)

        dis = Label(add_frame,fg="white",bg="black", text="Discription: ", font=("calibri Bold",15)).place(x=350, y=300)
        dis_entry = Entry(add_frame,width=20,font=("calibri Bold",10),bg="snow")


        dis_entry.place(x=500,y=300)
        combo_ttk.insert(0,"FORZEN_SWEETS")


        def submit_data():
            name = name_entry.get()
            price = int(price_entry.get())


            qty = int(qty_entry.get())
            dis = dis_entry.get()


            cat = combo_ttk.get()
            
            if name == "":
                messagebox.showerror("REQUIRED_FIELD","Please Fillup Field")


            elif cat == "":
                messagebox.showerror("REQUIRED_FIELD","Please Fillup Field")


            elif price == 0:
                messagebox.showerror("REQUIRED_FIELD","Please Fillup Field")


            elif qty == 0:
                messagebox.showerror("REQUIRED_FIELD","Please Fillup Field")


            elif dis == "":
                messagebox.showerror("REQUIRED_FIELD","Please Fillup Field")


            else:
                conn = mysql.connect(host="localhost",user="root",database="ice_cream",password="Ayush#2004")
                cursor = conn.cursor()


                insert_query = "insert into products(prod_name,prod_cat,prod_qty,prod_price,prod_dis) values(%s,%s,%s,%s,%s)"
                insert_data = (name,cat,qty,price,dis)


                cursor.execute(insert_query,insert_data)

                sa = pyttsx3.init()
                sa.say("Product Has Been Added")
                sa.runAndWait()
                messagebox.showinfo("ADDED","Product Added Succesfully")


                cursor.execute("commit")
                conn.close()


        submit = Button(add_frame,text="submit",width=15,height=1,command=submit_data)
        submit.place(x=400,y=350)


        def reset_entrie():
            name_entry.delete(0,END)
            price_entry.delete(0,END)


            qty_entry.delete(0,END)
            dis_entry.delete(0,END)

        reset = Button(add_frame,text="reset",width=15,height=1,command=reset_entrie)
        reset.place(x=550,y=350)


    Add()
    add_btn = Button(f2,text="Add",font=("Calibari ,bold",10),command=Add,height=2,width=20,activebackground="black",activeforeground="white")
    add_btn.place(x=20,y=50)


    delete_btn = Button(f2,text="delete",font=("Calibari ,bold",10),command=delete_frame.delete_frame_class.delete_func,height=2,width=20,activebackground="black",activeforeground="white")
    delete_btn.place(x=20,y=150)


    update_btn = Button(f2,text="update",font=("Calibari , bold ",10),height=2,width=20,activebackground="black",activeforeground="white",command=update_frame.prod_update.update)
    update_btn.place(x=20,y=250)


    display_btn = Button(f2,text="display",font=("Calibari ,bold",10),command=display_products.display_product.display_prod,height=2,width=20,activebackground="black",activeforeground="white")
    display_btn.place(x=20,y=350)


    cus_btn = Button(f1,text="Customers",font=("Calibari ,bold",10),command=customers.customers.customers_func,height=2,width=20,activebackground="black",activeforeground="white")
    cus_btn.place(x=400,y=100)


    bill_main = Button(f1,text="Bill Records",font=("Calibari ,bold",10),width=20,height=2,activebackground="black",activeforeground="white",command=bill_data.bill_display.bill_dis)
    bill_main.place(x=600,y=100)


    billing = Button(f1,text="Customer Billing",font=("Calibari ,bold",10),width=20,height=2,activebackground="black",activeforeground="white",command=Billing.Billing.billing_func)
    billing.place(x=800,y=100)

    exit = Button(f1,text="Close",font=("Calibari ,bold",10),activebackground="black",activeforeground="white",command=quit)
    exit.place(x=1000,y=100)


Home_Frame.win.mainloop()