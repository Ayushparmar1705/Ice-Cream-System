from tkinter import *
from tkinter import ttk


import mysql.connector as mysql
import display_products



from tkinter import messagebox
import Home_Frame


import pyttsx3



class prod_update:
    def __init__(self,height,width):
        self.height = height
        self.width = width


    def update():
    
        add_frame=Frame(Home_Frame.win,bg="bisque2",bd=5,relief=GROOVE)
        add_frame.place(x=230, y=200, width=1305, height=590)
    
        canvas1=Canvas(add_frame,width=800,height=500,bg="black").place(x=250, y=40)


        search = Label(add_frame,text="search product",font=("Calibari Bold",15),bg="black",fg="white")
        search.place(x=300,y=50)



        sv = StringVar()
        conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
        cursor = conn.cursor()
      
        cursor.execute("select prod_name from products")
        
        search_cb = ttk.Combobox(add_frame,textvariable=sv)
        search_cb.place(x=500,y=50)

        

        pn = cursor.fetchall()
        cursor.execute("commit")


        search_cb['values'] = (pn)
        conn.close()
        


        def search():
            conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
            cursor = conn.cursor()


            spnq = "select prod_name from products where prod_name = '"+search_cb.get()+"';"
            cursor.execute(spnq)

        
            fpn = cursor.fetchall()
            cursor.execute("commit")


            spcq = "select prod_cat from products where prod_name = '"+search_cb.get()+"';"
            cursor.execute(spcq)

        
            fpc = cursor.fetchall()
            cursor.execute("commit")



            spqq = "select prod_qty from products where prod_name = '"+search_cb.get()+"';"
            cursor.execute(spqq)



        
            fpq = cursor.fetchall()
            cursor.execute("commit")



            sppq = "select prod_price from products where prod_name = '"+search_cb.get()+"';"
            cursor.execute(sppq)


            fpp = cursor.fetchall()
            spcd = "select prod_dis from products where prod_name = '"+search_cb.get()+"';"
        
            cursor.execute(spcd)
            fpd = cursor.fetchall()


            cursor.execute("commit")

            cursor.execute("commit")



            conn.close()


           


            search_btn =  Button(add_frame,text="search",bg="white",fg="black",font=("Arial 10 bold"),command=search)
            search_btn.place(x=700,y=50)


            name = Label(add_frame,fg="white",bg="black", text="Product Name: ", font=("calibri Bold",15)).place(x=350, y=100)
            name_entry = Entry(add_frame,width=20,font=("calibri Bold",10),bg="snow")


            name_entry.place(x=500,y=100)
            name_entry.insert(0,fpn)
            

            combo = Label(add_frame,text="Catagory: ",bg="black",fg="white",font=("Calibri Bold",15))
            combo.place(x=350,y=150)


            var1 = StringVar()
            combo_ttk = ttk.Combobox(add_frame,textvariable=var1)

            combo_ttk.place(x=500,y=150)
            combo_ttk['values'] = (fpc)



            qty = Label(add_frame,fg="white",bg="black", text="Quntity: ", font=("calibri Bold",15)).place(x=350, y=200)
            qty_entry = Entry(add_frame,width=20,font=("calibri Bold",10),bg="snow")


            qty_entry.place(x=500,y=200)
            qty_entry.insert(0,fpq)

            price = Label(add_frame,fg="white",bg="black", text="Price: ", font=("calibri Bold",15)).place(x=350, y=250)
            price_entry = Entry(add_frame,width=20,font=("calibri Bold",10),bg="snow")


            price_entry.place(x=500,y=250)
           
          
            price_entry.insert(0,fpp)

            dis = Label(add_frame,fg="white",bg="black", text="Discription: ", font=("calibri Bold",15)).place(x=350, y=300)
            dis_entry = Entry(add_frame,width=20,font=("calibri Bold",10),bg="snow")

            dis_entry.place(x=500,y=300)
         

            dis_entry.insert(0,fpd)


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


                    update_query = "update products set prod_name = %s,prod_cat = %s,prod_qty = %s,prod_price = %s,prod_dis = %s where prod_name = %s"
                    update_data = (name,cat,qty,price,dis,search_cb.get())


                    cursor.execute(update_query,update_data)

                    sa = pyttsx3.init()
                    sa.say("Product Has Been Updated")


                    sa.runAndWait()
                    messagebox.showinfo("ADDED","Product Updated Succesfully")


                    cursor.execute("commit")
                    conn.close()


            submit = Button(add_frame,text="update",width=15,height=1,command=submit_data)
            submit.place(x=400,y=350)


            def reset_entrie():
                name_entry.delete(0,END)
                price_entry.delete(0,END)


                qty_entry.delete(0,END)
                dis_entry.delete(0,END)

            reset = Button(add_frame,text="reset",width=15,height=1,command=reset_entrie)
            reset.place(x=550,y=350)


        search()



    update()

