from tkinter import *
import mysql.connector as mysql


from tkinter import ttk
from tkinter import messagebox

import Home_Frame
import Prod_Frame


import pyttsx3


class delete_frame_class:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    
    def delete_func():
        add_frame=Frame(Home_Frame.win,bg="bisque2",bd=5,relief=GROOVE)
        add_frame.place(x=230, y=200, width=1305, height=590)
    
        canvas1=Canvas(add_frame,width=600,height=500,bg="black").place(x=270, y=40)
        delete = Label(add_frame,text="Products: ",font=("Calibri Bold",15),bg="black",fg="white")


        delete.place(x=400,y=100)
        delete_combobox = ttk.Combobox(add_frame,width=20,font=("Calibri Bold",10))


        delete_combobox.place(x=500,y=105)
        conn = mysql.connect(host="localhost",user="root",password = "Ayush#2004",database="ice_cream")

        
        cursor = conn.cursor()
        cursor.execute("select prod_name from products")
        fetch_data = cursor.fetchall()
        delete_combobox['values'] = (fetch_data)
        cursor.execute("commit")
        conn.close()


       
        def delete_prod():
            conn = mysql.connect(host="localhost",user="root",password = "Ayush#2004",database="ice_cream")
            cursor = conn.cursor()



            delete_query = "delete from products where prod_name = %s"
            delete_data = [delete_combobox.get()]


            cursor.execute(delete_query,delete_data)
            cursor.execute("commit")

            sd = pyttsx3.init()
            sd.say("Product Has Been Deleted")
            sd.runAndWait()
            messagebox.showinfo("DELETED","product Deleted succesfully...")
            conn.close()
         
        delete = Button(add_frame,text="Delete",bg="white",fg="black",width=20,command=delete_prod)
        delete.place(x=400,y=200)


    delete_func()
