from tkinter import *
import mysql.connector as mysql


from tkinter import ttk
import Home_Frame


class display_product:
    def __init__(self,height,width):
        self.height = height
        self.width = width
       
    def display_prod():
        add_frame=Frame(Home_Frame.win,bg="bisque2",bd=5,relief=GROOVE)
        add_frame.place(x=230, y=200, width=1305, height=590)
    
        canvas1=Canvas(add_frame,width=600,height=500,bg="black").place(x=270, y=40)
        y_scroll = ttk.Scrollbar(add_frame,orient=VERTICAL)


        x_scroll = ttk.Scrollbar(add_frame,orient=HORIZONTAL)
        prod_table = ttk.Treeview(add_frame,columns=("id","prod_name","prod_cat","prod_qty","prod_price","prod_dis"),yscrollcommand=y_scroll,xscrollcommand=x_scroll)


        y_scroll.config(command=prod_table.yview)
        x_scroll.config(command=prod_table.xview)


        y_scroll.pack(side = RIGHT,fill=Y)
        x_scroll.pack(side = BOTTOM,fill=X)


        prod_table.heading("id",text="id")
        prod_table.heading("prod_name",text="prod_name")


        prod_table.heading("prod_cat",text="prod_catagory")
        prod_table.heading("prod_qty",text="prod_quntity")


        prod_table.heading("prod_price",text="prod_price")
        prod_table.heading("prod_dis",text="prod_discription")


        prod_table.column("id",width=100,anchor=CENTER)
        prod_table.column("prod_name",width=100,anchor=CENTER)


        prod_table.column("prod_cat",width=100,anchor=CENTER)
        prod_table.column("prod_price",width=100,anchor=CENTER)


        prod_table.column("prod_qty",width=100,anchor=CENTER)
        prod_table.column("prod_dis",width=100,anchor=CENTER)


        prod_table['show'] = 'headings'
        prod_table.pack(fill=BOTH,expand=True)


        conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
        cursor = conn.cursor()


        cursor.execute("select * from products")
        fetch_all = cursor.fetchall()


        if len(fetch_all)!=0:
            prod_table.delete(*prod_table.get_children())


            for prod in fetch_all:


                prod_table.insert('',END,values = prod)

            conn.close()

            
    display_prod()