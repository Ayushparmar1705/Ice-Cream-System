from tkinter import *
import mysql.connector as mysql


from tkinter import ttk
import Home_Frame


class bill_display:
    def __init__(self,height,width):
        self.height = height
        self.width = width
       
    def bill_dis():
        bill_disf=Frame(Home_Frame.win,bg="bisque2",bd=5,relief=GROOVE)
        bill_disf.place(x=230, y=200, width=1305, height=600)
    
        canvas1=Canvas(bill_disf,width=600,height=500,bg="black").place(x=270, y=40)
        y_scroll = ttk.Scrollbar(bill_disf,orient=VERTICAL)


        x_scroll = ttk.Scrollbar(bill_disf,orient=HORIZONTAL)
        bill_dis = ttk.Treeview(bill_disf,columns=("bill_id","date","cus_name","prod_name","total_qty","sub_total"),yscrollcommand=y_scroll,xscrollcommand=x_scroll)


        y_scroll.config(command=bill_dis.yview)
        x_scroll.config(command=bill_dis.xview)


        y_scroll.pack(side = RIGHT,fill=Y)
        x_scroll.pack(side = BOTTOM,fill=X)


        bill_dis.heading("bill_id",text="bill_id")
        bill_dis.heading("date",text="date")
        bill_dis.heading("total_qty",text="Quntity")

        bill_dis.heading("cus_name",text="cus_name")
        bill_dis.heading("prod_name",text="prod_name")


        bill_dis.heading("sub_total",text="sub_total")
        bill_dis.column("bill_id",width=40,anchor=CENTER)


        bill_dis.column("date",width=30,anchor=CENTER)
        bill_dis.column("cus_name",width=10,anchor=CENTER)
        
        
        bill_dis.column("prod_name",width=200,anchor=CENTER)
        bill_dis.column("sub_total",width=1,anchor=CENTER)
        bill_dis.column("total_qty",width=20,anchor=CENTER)
        bill_dis['show'] = 'headings'
        bill_dis.pack(fill=BOTH,expand=True)


        conn = mysql.connect(host="localhost",user="root",password="Ayush#2004",database="ice_cream")
        cursor = conn.cursor()


        cursor.execute("select * from mainbilling")
        fetch_all = cursor.fetchall()


        if len(fetch_all)!=0:
            bill_dis.delete(*bill_dis.get_children())


            for prod in fetch_all:


                bill_dis.insert('',END,values = prod)

            conn.close()

            
    bill_dis()
