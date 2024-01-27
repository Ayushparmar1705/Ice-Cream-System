from tkinter import *
from tkinter import messagebox


from tkinter import ttk
from datetime import datetime


import Home_Frame
import mysql.connector as mysql

class Billing:
    def __init__(self,height,width):
        self.height = height
        self.width = width

        


        
    def billing_func():
        billing_frame = Frame(Home_Frame.win,width=1305,height=590,bg="bisque2",bd="5",relief=GROOVE)
        billing_frame.place(x=230,y=200)

        canvas = Canvas(billing_frame,width=500,height=700,bg="whitesmoke",bd="5",relief=GROOVE)
        canvas.place(x=0,y=0)

        cus_name = Label(billing_frame,text="Customer name",font=("Calibary Bold",12),bg="white",fg="black")
        cus_name.place(x=10,y=50)


        cus_name_entry = Entry(billing_frame,width=15,bg="snow",font=("Calibari Bold",13))
        cus_name_entry.place(x=200,y=50)


        cus_phno = Label(billing_frame,text="Customer Phonenumber",font=("Calibary Bold",12),bg="white",fg="black")
        cus_phno.place(x=10,y=100)


        var1 = StringVar()

        phno_combo = ttk.Combobox(billing_frame,textvariable=var1,font=("Calibari Bold",13),width=15)
        phno_combo.place(x=200,y=100)

        conn = mysql.connect(host="localhost",user="root",password = "Ayush#2004",database="ice_cream")
        cursor = conn.cursor()


        cursor.execute("select cus_phno from customers")
        fetch_data = cursor.fetchall()


        phno_combo['values'] = (fetch_data)
        cursor.execute("commit")


        conn.close()
        def get_customer_name():
            if phno_combo.get() == "":
                messagebox.showerror("INVALID_FIELD","INVALID FIELD NAME")


            else:
                conn = mysql.connect(host="localhost",user="root",password = "Ayush#2004",database="ice_cream")
                cursor = conn.cursor()


                select_query = "select cus_name from customers where cus_phno = %s"
                select_data = [phno_combo.get()]


                cursor.execute(select_query,select_data)
                fetch_name = cursor.fetchall()


                conn.close()
                cus_name_entry.delete(0,END)
                cus_name_entry.insert(0,fetch_name)


        get_customer = Button(billing_frame,text="Get Customers",font=("Calibari Bold",10),width=15,command=get_customer_name)
        get_customer.place(x=150,y=150)



       
        var2 = StringVar()
        prod_name = Label(billing_frame,text="Products",font=("Calibari Bold",13),bg="white",fg="black")

            
        prod_name.place(x=10,y=200)
        prod_name_combo = ttk.Combobox(billing_frame,textvariable=var2,font=("Calibari Bold",13),width=15)




        prod_name_combo.place(x=200,y=200)
        conn = mysql.connect(host="localhost",user="root",password = "Ayush#2004",database="ice_cream")
        cursor = conn.cursor()




        cursor.execute("select prod_name from products")
        fetch_data = cursor.fetchall()


        prod_name_combo['values'] = (fetch_data)
        cursor.execute("commit")
        conn.close()


        qty = Label(billing_frame,text="Quntity ",font=("Calibary Bold",13),bg="white",fg="black")
        
        qty.place(x=10,y=250)
        qty_spin = Spinbox(billing_frame,font=("Calibary Bold",12),width=10,from_=1,to=50)
        qty_spin.place(x=200,y=250)


        bill_frame = Frame(billing_frame,width=1000,height=600,bg="black")
        bill_frame.place(x=500,y=0)


        canvas = Canvas(bill_frame,width=900,height=600,bg="lightgreen",bd="5",relief=SUNKEN)
        canvas.place(x=0,y=0)


        row = Label(bill_frame,text="20",state=DISABLED)
       
    

        name_list = []
        qty_list = []


        price_list = []
        total_list = []


        def insert_data():
            global ab
            ab = int(row['text'])
            date = datetime.now()


            ab = ab + 30


            row.config(text=ab)
            if prod_name_combo.get() == "":
                messagebox.showerror("INVALID_FIELD","INVALID FIELD NAME")


                
            else:
                conn = mysql.connect(host="localhost",user="root",password = "Ayush#2004",database="ice_cream")
                cursor = conn.cursor()


                select_price_query = "select prod_price from products where prod_name = %s"
                select_price_data = [prod_name_combo.get()]


                cursor.execute(select_price_query,select_price_data)
                fetch_price = cursor.fetchall()


                cursor.execute("commit")
                price = Entry(billing_frame)


                price.pack_forget()
                price.insert(0,fetch_price)
                total = int(price.get()) * int(qty_spin.get())


                select_qty_query = "select prod_qty from products where prod_name = %s"
                select_qty_data = [prod_name_combo.get()]


                cursor.execute(select_qty_query,select_qty_data)

                fetch_qty = cursor.fetchall()
                print(fetch_qty)


                if(int(qty_spin.get()) >fetch_qty[0][0]):
                    messagebox.showerror("Invalid","Quntity Has A Out of Stock")


                else:


                    other_qty = fetch_qty[0][0] - int(qty_spin.get())
                    update_query = "update products set prod_qty = %s where prod_name = %s"


                    update_data = [other_qty,prod_name_combo.get()]
                    cursor.execute(update_query,update_data)


                    cursor.execute("commit")
                    print(other_qty)


                    conn.close()





                    conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
                    cursor = conn.cursor()


                    f = "select * from products where prod_name = '"+prod_name_combo.get()+"'"
                    cursor.execute(f)
                   

                    list = cursor.fetchall()
                    cursor.execute("commit")
                    print(list)

                    utitle = "PRODUCT_NAME\t\tPRICE\t\tQUNTITY\t\tTOTAL"
                    title = Label(bill_frame,text=utitle,fg="black",bg="lightgreen")
                    title.place(x=40,y=30)
                   

                    name = list[0][1]


                    qty = int(qty_spin.get())
                    price = list[0][4]


                    total = price * qty
                    record = "" + str(id) + "     " + name + "     " + str(price) + "     " + str(
                    qty) + "     " + str(total)


                    label1 = Label(bill_frame,text=name,bg="lightgreen",fg="black",font=("Arial 10 bold"))
                    label1.place(x=50,y=ab)


                    label2 = Label(bill_frame,text=price,bg="lightgreen",fg="black",font=("Arial 10 bold"))
                    label2.place(x=200,y=ab)


                    label3 = Label(bill_frame,text=qty,bg="lightgreen",fg="black",font=("Arial 10 bold"))
                    label3.place(x=300,y=ab)


                    label4 = Label(bill_frame,text=total,bg="lightgreen",fg="black",font=("Arial 10 bold"))
                    label4.place(x=430,y=ab)



                    name_list.append(name)
                    qty_list.append(qty)


                    price_list.append(price)
                    total_list.append(total)


                    print(name)
      
        
                 
                    def check_out():
                        
                        conn = mysql.connect(host="localhost",user="root",password = "Ayush#2004",database="ice_cream")
                        cursor = conn.cursor()


                        tl = Toplevel(height=600,width=500)
                        tl.title("Billing")
                        
                        frame = Frame(tl,width=500,height=600,bg="whitesmoke")
                        frame.place(x=0,y=0)

                        canvas1 = Canvas(tl,bg="black",height=1,width=500)
                        create_line = canvas1.create_line(15,25,200,25)


                        canvas1.place(x=0,y=50)
                        date = Label(frame,text="Date :",bg="white",fg="black",font=("Calibary Bold",10 ))
                        date.place(x=0,y=70)



                        date = datetime.today()
                        dd = Label(frame,text=date,bg="white",fg="black",font=('Calibari Bold',10))
                        dd.place(x=50,y=70)


                        name = cus_name_entry.get()
                        name_query = "select cus_name from customers where cus_name = %s"
                
                        name_data = [name]
                        cursor.execute(name_query,name_data)
                        fetch_name = cursor.fetchall()


                        cursor.execute("commit")
                        d = Label(frame,text="ayushparmar1705@gmail.com",bg="white",fg="black",font=("Arial 10 bold"))
                        d.place(x=150,y=0)
                        d = Label(frame,text="CORNER HOUSE ICE-CREAM",bg="white",fg="darkgreen",font=("Arial 10 bold"))
                        d.place(x=150,y=30)
                        nl = Label(frame,text="name",bg="white",fg="black",font=("Calibari Bold",10))
                        nl.place(x=350,y=70)


                        canvas2 = Canvas(tl,bg="black",height=1,width=500)
                        create_line = canvas2.create_line(15,25,200,25)
                        canvas2.place(x=0,y=100)



                        nl2 = Label(frame,text=fetch_name,bg="white",fg="black",font=("Calibari Bold",10))
                        nl2.place(x=400,y=70)


                        display_frame = Frame(frame,width=700,height=600,bg="black")
                        display_frame.place(x=0,y=150)


                        canvas = Canvas(display_frame,width=700,height=600,bg="lightgreen",bd="5",relief=SUNKEN)
                        canvas.place(x=0,y=0)

            
                        checktitle = "PRODUCT_NAME\t\tPRICE\t\tQUNTITY\tTOTAL"


                        ct = Label(display_frame,text=checktitle,fg="black",bg="lightgreen")
                        ct.place(x=50,y=10)
                        y1 = 30
                        nlp = 50



                        for nl in range(len(name_list)):
                            
                            l1 = Label(display_frame,text=name_list[nl],bg="lightgreen",fg="black",font=("Calibary 10 bold"))
                            l1.place(x=50,y=nlp)
                            nlp+=30



                        plp = 50
                        sub_tol = 0
                        for pl in range(len(price_list)):
                            l2 = Label(display_frame,text=price_list[pl],bg="lightgreen",fg="black",font=("Calibary 10 bold"))
                            l2.place(x=200,y=plp)
                            plp+=30
                            sub_tol = sub_tol + total_list[pl]
                       


                        qlp = 50
                        qty_total = 0
                        for ql in range(len(qty_list)):

                            l3 = Label(display_frame,text=qty_list[ql],bg="lightgreen",fg="black",font=("Calibary 10 bold"))
                            l3.place(x=300,y=qlp)
                            qlp+=30

                            # Customer's buy products that sum of all quntyties
                            qty_total = qty_total + qty_list[ql]


                        tlp = 50
                        for tl in range(len(total_list)):
                            
                            l4 = Label(display_frame,text=total_list[tl],bg="lightgreen",fg="black",font=("Calibary 10 bold"))
                            l4.place(x=400,y=tlp)


                            tlp+=30


                        qt = Label(display_frame,text="Total Quntity:",font=("Arial 10 bold"),bg="lightgreen",fg="black")
                        qt.place(x=150,y=nlp+20)


                        qty_total = Label(display_frame,text=qty_total,font=("Arial 10 bold"),bg="lightgreen",fg="black")
                        qty_total.place(x=300,y=nlp+20)


                        st = Label(display_frame,text="Total:",font=("Arial 10 bold"),bg="lightgreen",fg="black")
                        st.place(x=350,y=nlp+20)



                        sub_total = Label(display_frame,text=sub_tol,font=("Arial 10 bold"),bg="lightgreen",fg="black")
                        sub_total.place(x=400,y=nlp+20)



                        def mybill():
                            conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
                            cursor = conn.cursor()


                            prod_name = ""

                            for pnl in range(len(name_list)):
                                prod_name = prod_name +","+ name_list[pnl]


                            insert_billing_query = "insert into mainbilling(date,cus_name,prod_name,sub_total) values(%s,%s,%s,%s)"
                            insert_billing_data = (date,cus_name_entry.get(),prod_name,sub_tol)


                            cursor.execute(insert_billing_query,insert_billing_data)
                            cursor.execute("commit")


                        done = Button(display_frame,text="DONE",bg="white",fg="black",font=("Calibari 10 bold"),command=mybill)
                        done.place(x=300,y=nlp+50)



                    checkout = Button(bill_frame,text="CHECK OUT",bg="black",fg="white",width=10,font=("Arial 10 bold"),command=check_out)
                    checkout.place(x=100,y=500)

                    

        add = Button(billing_frame,text="ADD",font=("Calibary Bold",10),width=15,command=insert_data)
        add.place(x=150,y=300)


        
     
    billing_func()