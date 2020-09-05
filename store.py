from tkinter import *
from tkinter import Label,Tk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import sqlite3
from tkinter import messagebox
import time
from PIL import Image, ImageTk
from tkinter import filedialog

import datetime
#from datetime import datetime
from tkcalendar import DateEntry

from tkinter.ttk import Treeview, Scrollbar


#from pandas import DataFrame
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

connecter=sqlite3.connect("store.db")
c = connecter.cursor()

#df = pd.read_sql_query("SELECT * FROM order_detail", connecter)
#sa=len(df['type'])
#df1 = df[['cus_name',sa]].groupby('type')


timer = datetime.datetime.now()

try:
    #c.execute("ALTER TABLE product ADD COLUMN namees varchar(32)")
    c.execute("""CREATE TABLE `product` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	TEXT,
	`image`	TEXT
    );""")

    c.execute("""CREATE TABLE `order_detail` (
	`cus_name`	TEXT,
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`type`	TEXT,
	`phone_no`	INTEGER,
	`chest`	INTEGER,
	`sleeve`	INTEGER,
	`shoulder`	INTEGER,
	`waist`	INTEGER,
	`length`	INTEGER,
	`neck`	INTEGER,
	`price`	INTEGER,
	`center_point`	INTEGER,
	`height`	INTEGER,
	`hip`	INTEGER,
	`inseam`	INTEGER,
	`bottom`	INTEGER,
	`collar`	INTEGER,
	`inside`	INTEGER,
	`ankle`	INTEGER,
	`date`	INTEGER
    );""")

    c.execute("""CREATE TABLE `Audit` (
	`Name`	TEXT,
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`type`	TEXT,
	`amt`	INTEGER
    );""")

    c.execute("""CREATE TABLE `Transactions` (
	`name_id`	INTEGER,
	`types`	TEXT,
	`amount`	INTEGER,
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`date`	INTEGER
    );""")

    
except Exception as e:
    print(e)

    


root = Tk()





frame=Frame(root,width=10000,height=100,borderwidth=5,relief=RAISED)
frame.place(x=0,y=0)


def uploadImage_template():
    global name_e
    global original_e
    global stock_e
    global frame1
    global labelx,btn4
    global var

    try:
        let_forget()
        
    except NameError:
        print(NameError)
        
    finally:
        
    
    
        frame1=Frame(root,width=500,height=400,borderwidth=5,relief=RAISED)
        frame1.place(x=0,y=100)

            ##########label############
        name_l=Label(frame1,text="Name",font='arail 16 bold')
        name_l.place(x=0,y=100)

        or_l=Label(frame1,text="OR",font='arail 16 bold')
        or_l.place(x=0,y=70)

        Sname_l=Label(frame1,text="Select name",font='arail 16 bold')
        Sname_l.place(x=0,y=0)

        name=[]
        #####################Dropdown##############

        with connecter:
            c.execute("""SELECT * FROM product""")
            n=c.fetchall()
            if n!=[]:
                for i in n:
                    s=i[1]
                    name.append(s)
                var = StringVar(frame1)
                 # initial value
                name = list(dict.fromkeys(name))
                var.set(name[0])
                option=OptionMenu(frame1, var,*name)
                option.place(x=150,y=0)
                option.config(font=('arail 18 bold'))

                btn8=Button(frame1,text='ok',width=5,command=drop)
                btn8.place(x=150,y=50)

        ##########Entry############
            
        name_e=Entry(frame1,text='yash',font='arail 16 bold')
        name_e.place(x=130,y=100)
            
        btn4=Button(frame1,text='upload image',command=get_image)
        btn4.place(x=130,y=150)

        labelx =Label(frame1, fg="red", text="No file selected.")
        labelx.place(x=215,y=150)


        ##########Button############

        
        btn2=Button(frame1,text='submit',command=uploadImage)
        btn2.place(x=0,y=150)

        


def drop():
    name_e.insert(0,str(var.get()))

    

global status
status=0
def get_image():
    global path
    global name_e
    global status
    path=filedialog.askopenfilename(multiple=True,filetypes=[("Image File","*.png *.JPG")])
    print(name_e.get())
    #print(path)
    
    for i in path:
        if ".JPG" or ".png" or ".jpg" in i:
            btn4.configure(bg='red')
            labelx.config(text=path)
            status=1
            
        
        else:
            pass
    print(status)
    
        
            


def uploadImage():
    global status
    get_name=name_e.get()
    

    if get_name=='' or status==0:
        messagebox.showwarning("warning","fill the entry ")

    else:
        with connecter:
            c.execute("""SELECT * FROM product WHERE name='{}'""".format(get_name))
            n=c.fetchall()
        
        for i in path:
            with connecter:
                c.execute("""INSERT INTO product (name,image) VALUES ('{}','{}')""".format(get_name,i))

        
        messagebox.showinfo("congrat","You added product")
        

        name_e.delete(0,END)
        status=0
        
##################main window function##################

global tree

def search_order_template():
    global frame2,id_e,cus_n,cus_t,cus_ph,cus_c,cus_s,cus_sh,cus_w,cus_bl,cus_ne,cus_p,cus_hip,cus_price
    global cus_collar

    try:
        let_forget()
        
    except NameError:
        print(NameError)


    finally:
        
        frame2=Frame(root,width=1000,height=500,borderwidth=5,relief=RAISED)
        frame2.place(x=0,y=100)
#==============================Label==============================================
        lb=Label(frame2,text='Search Order',font='arail 20 bold')
        lb.place(x=250,y=0)

        lb_1=Label(frame2,text='Enter ID',font='arail 18 bold')
        lb_1.place(x=0,y=50)

        #lb_n=Label(frame2,text='Enter name',font='arail 18 bold')
        #lb_n.place(x=0,y=150)

        


#===============================================================================

        cus_n=Label(frame2,font="arail 18 bold")
        cus_n.place(x=700,y=0)

        cus_t=Label(frame2,font="arail 18 bold")
        cus_t.place(x=700,y=40)

        cus_ph=Label(frame2,font="arail 18 bold")
        cus_ph.place(x=700,y=80)

        cus_c=Label(frame2,font="arail 18 bold")
        cus_c.place(x=700,y=120)

        cus_s=Label(frame2,font="arail 18 bold")
        cus_s.place(x=700,y=160)

        cus_sh=Label(frame2,font="arail 18 bold")
        cus_sh.place(x=700,y=200)

        cus_w=Label(frame2,font="arail 18 bold")
        cus_w.place(x=700,y=240)

        cus_bl=Label(frame2,font="arail 18 bold")
        cus_bl.place(x=700,y=280)

        #cus_ne=Label(frame2,font="arail 18 bold")
        #cus_ne.place(x=700,y=320)

        cus_p=Label(frame2,font="arail 18 bold")
        cus_p.place(x=700,y=320)

        cus_collar=Label(frame2,font="arail 18 bold")
        cus_collar.place(x=700,y=360)

        cus_hip=Label(frame2,font="arail 18 bold")
        cus_hip.place(x=700,y=400)

        cus_price=Label(frame2,font="arail 18 bold")
        cus_price.place(x=700,y=440)
#================================Entry==============================================

        id_e=Entry(frame2,font='arail 18 bold',bg='steelblue')
        id_e.place(x=100,y=50)

        #Label(frame2,text='Or',font='arail 10 bold').place(x=0,y=130)

        #name_e=Entry(frame2,font='arail 18 bold')
        #name_e.place(x=150,y=150)

#=============================Button==================================================
        Button(frame2,text='search',bg='orange',command=search_order).place(x=0,y=100)
        


def search_order():
    global cust_sl
    get_id=id_e.get()
    

    if get_id=='':
        messagebox.showwarning("Warning","sorry no input")

    else:
        
        with connecter:
                c.execute("""SELECT * FROM order_detail WHERE id='{}'""".format(get_id))
                get=c.fetchone()
                #messagebox.showinfo("congrat","You name is {}".format(get[0]))

                
                if get==None:
                    messagebox.showwarning("Warning","sorry no input")
                else:
                    if get[2]=='Shirt' or get[2]=='Safari Suit' or get[2]=='Safari Fusion':
                        
                        #print('inputs are {}'.format(get))
                        
                        cust_vender=Label(frame2,font="arail 18 bold")
                        cust_vender.place(x=500,y=0)     

                        cust_type=Label(frame2,font="arail 18 bold")
                        cust_type.place(x=500,y=40)

                        cust_pho=Label(frame2,font="arail 18 bold")
                        cust_pho.place(x=500,y=80)

                        cust_l=Label(frame2,font="arail 18 bold")
                        cust_l.place(x=500,y=120)

                        cust_s=Label(frame2,font="arail 18 bold")
                        cust_s.place(x=500,y=160)

                        cust_c=Label(frame2,font="arail 18 bold")
                        cust_c.place(x=500,y=200)

                        cust_sl=Label(frame2,font="arail 18 bold")
                        cust_sl.place(x=500,y=240)

                        cust_cp=Label(frame2,font="arail 18 bold")
                        cust_cp.place(x=500,y=280)

                        #cust_n=Label(frame2,text='seat',font="arail 18 bold")
                        #cust_n.place(x=500,y=320)

                        cust_n=Label(frame2,font="arail 18 bold")
                        cust_n.place(x=500,y=320)

                        cust_collar=Label(frame2,font="arail 18 bold")
                        cust_collar.place(x=500,y=360)

                        cust_seat=Label(frame2,font="arail 18 bold")
                        cust_seat.place(x=500,y=400)

                        cust_p=Label(frame2,font="arail 18 bold")
                        cust_p.place(x=500,y=440)

                        cus_n.configure(text=get[0])
                        cus_t.configure(text=get[2])
                        cus_ph.configure(text=get[3])
                        cus_c.configure(text=get[8])
                        cus_s.configure(text=get[6])
                        cus_sh.configure(text=get[4])
                        cus_w.configure(text=get[5])
                        cus_bl.configure(text=get[11])
                        #cus_ne.configure(text=get[9])
                        cus_p.configure(text=get[9])
                        cus_collar.configure(text=get[16])
                        cus_hip.configure(text=get[13])
                        cus_price.configure(text="Rs {}".format(get[10]))

                        ###########custamize
                        cus_price.configure(fg='green')

                        cust_vender.configure(text='Vender name')
                        cust_type.configure(text='Type')
                        cust_pho.configure(text='Phone_no')
                        cust_l.configure(text='lenght')
                        cust_s.configure(text='shoulder')
                        cust_c.configure(text='chest')
                        cust_sl.configure(text='sleeves')
                        cust_cp.configure(text='center_p')
                        cust_n.configure(text='neck')
                        cust_collar.configure(text='collar')
                        cust_seat.configure(text='seat')
                        cust_p.configure(text='Price')
                        
                        
                    elif get[2]=='Pant' or get[2]=='Kurtas':
                        try:
                            
                            cust_sl.place_forget()
                        except Exception as e:
                            print('')

                        cust_v=Label(frame2,font="arail 18 bold")
                        cust_v.place(x=500,y=0)     

                        cust_t=Label(frame2,font="arail 18 bold")
                        cust_t.place(x=500,y=40)

                        cust_p=Label(frame2,font="arail 18 bold")
                        cust_p.place(x=500,y=80)

                        cust_h=Label(frame2,font="arail 18 bold")
                        cust_h.place(x=500,y=120)

                        cust_i=Label(frame2,font="arail 18 bold")
                        cust_i.place(x=500,y=160)

                        cust_w=Label(frame2,font="arail 18 bold")
                        cust_w.place(x=500,y=200)

                        cust_hip=Label(frame2,font="arail 18 bold")
                        cust_hip.place(x=500,y=240)

                        cust_inseam=Label(frame2,font="arail 18 bold")
                        cust_inseam.place(x=500,y=280)

                        cust_a=Label(frame2,text='ankle',font="arail 18 bold")
                        cust_a.place(x=500,y=320)

                        cust_b=Label(frame2,font="arail 18 bold")
                        cust_b.place(x=500,y=360)

                        cust_price=Label(frame2,font="arail 18 bold")
                        cust_price.place(x=500,y=440)

                        

                        #cust_n=Label(frame2,text='collar',font="arail 18 bold")
                        #cust_n.place(x=500,y=400)

                        cus_n.configure(text=get[0])
                        cus_t.configure(text=get[2])
                        cus_ph.configure(text=get[3])
                        cus_c.configure(text=get[12])
                        cus_s.configure(text=get[17])
                        cus_sh.configure(text=get[7])
                        cus_w.configure(text=get[13])
                        cus_bl.configure(text=get[14])
                        #cus_ne.configure(text=get[9])
                        cus_p.configure(text=get[18])
                        cus_collar.configure(text=get[15])
                        cus_price.configure(text="Rs {}".format(get[10]))

                        ###########custamize
                        cus_price.configure(fg='green')

                        cust_v.configure(text='Vender Name')
                        cust_t.configure(text='Type')
                        cust_p.configure(text='Phone_no')
                        cust_h.configure(text='height')
                        cust_i.configure(text='inside')
                        cust_w.configure(text='waist')
                        cust_hip.configure(text='hip')
                        cust_inseam.configure(text='inseam')
                        cust_a.configure(text='ankle')
                        cust_b.configure(text='bottom')
                        cust_price.configure(text='Price')
                    
def drop_down():
    global var
    global frame9
    try:
        let_forget()
        
    except NameError:
        print(NameError)

    

    finally:
        frame9=Frame(root,width=250,height=110,borderwidth=0,bg='steelblue')
        frame9.place(x=0,y=100)
        #Label(root,text='Create Order',font="arail 18 bold").place(x=700,y=200)
        var = StringVar(frame9)
        var.set("Shirt") # initial value

        option = OptionMenu(frame9, var, "Shirt", "Pant","Safari Suit","Safari Fusion","Kurtas")
        option.place(x=0,y=0)
        option.config(font=('arail 18 bold'))
        
        button = Button(frame9, text="Select Order Type",font='arail 18 bold', command=create_order_template,bg='pink')
        button.place(x=0,y=50)

def create_order_template():
    global customer_e
    global type_e
    global pho_e
    global chest_e
    global sleeve_e
    global shoulder_e
    global waist_e
    global back_l_e
    global neck_e,collar,cus_n
    global height_e,inside_e,waist_e,seat_e,inseam_e,ankle_e,bottom_e,hip_e,price_e

    global frame3

    
    try:
        let_forget()
        
    except NameError:
        print(NameError)

    

    finally:
        frame3=Frame(root,width=500,height=550,borderwidth=5,relief=RAISED)
        frame3.place(x=240,y=100)
        
        if var.get()=='Shirt' or var.get()=='Safari Suit' or var.get()=='Safari Fusion':
            

            
    #===============================label=====================================#
            
            cus_n=Label(frame3,text='Vender Name',font="arail 18 bold")
            cus_n.place(x=0,y=0)

            cus_n=Label(frame3,text='Phone_no',font="arail 18 bold")
            cus_n.place(x=0,y=40)

            cus_n=Label(frame3,text='sleeves',font="arail 18 bold")
            cus_n.place(x=0,y=80)

            cus_n=Label(frame3,text='chest',font="arail 18 bold")
            cus_n.place(x=0,y=120)

            cus_n=Label(frame3,text='center_p',font="arail 18 bold")
            cus_n.place(x=0,y=160)

            cus_n=Label(frame3,text='shoulder',font="arail 18 bold")
            cus_n.place(x=0,y=200)

            cus_n=Label(frame3,text='waist',font="arail 18 bold")
            cus_n.place(x=0,y=240)

            cus_n=Label(frame3,text='length',font="arail 18 bold")
            cus_n.place(x=0,y=280)

            cus_n=Label(frame3,text='neck',font="arail 18 bold")
            cus_n.place(x=0,y=320)

            cus_n=Label(frame3,text='collar',font="arail 18 bold")
            cus_n.place(x=0,y=360)

            cus_n=Label(frame3,text='Hip',font="arail 18 bold")
            cus_n.place(x=0,y=400)

            cus_n=Label(frame3,text='Price',font="arail 18 bold")
            cus_n.place(x=0,y=440)
    #===================================Entry===================================#

            customer_e=Entry(frame3,font='arail 18 bold')
            customer_e.place(x=160,y=0)

            pho_e=Entry(frame3,font='arail 18 bold')
            pho_e.place(x=160,y=40)

            type_e=Entry(frame3,font='arail 18 bold')
            type_e.place(x=160,y=80)

            chest_e=Entry(frame3,font='arail 18 bold')
            chest_e.place(x=160,y=120)

            sleeve_e=Entry(frame3,font='arail 18 bold')
            sleeve_e.place(x=160,y=160)

            shoulder_e=Entry(frame3,font='arail 18 bold')
            shoulder_e.place(x=160,y=200)

            waist_e=Entry(frame3,font='arail 18 bold')
            waist_e.place(x=160,y=240)

            back_l_e=Entry(frame3,font='arail 18 bold')
            back_l_e.place(x=160,y=280)

            neck_e=Entry(frame3,font='arail 18 bold')
            neck_e.place(x=160,y=320)

            collar=Entry(frame3,font='arail 18 bold')
            collar.place(x=160,y=360)

            hip_e=Entry(frame3,font='arail 18 bold')
            hip_e.place(x=160,y=400)

            price_e=Entry(frame3,font='arail 18 bold')
            price_e.place(x=160,y=440)
    #===================================Button===================================#
            btn7=Button(frame3,text='submit',width=60,command=create_customer,bg='orange')
            btn7.place(x=0,y=480)

            customer_e.focus()

        if var.get()=='Pant' or var.get()=='Kurtas':
            

    #===============================label=====================================#
            
            cus_k=Label(frame3,text='Vender Name',font="arail 18 bold")
            cus_k.place(x=0,y=0)

            #cus_n=Label(frame3,text='sleeves',font="arail 18 bold")
            #cus_n.place(x=0,y=40)

            cus_k=Label(frame3,text='Phone_no',font="arail 18 bold")
            cus_k.place(x=0,y=40)

            cus_k=Label(frame3,text='height',font="arail 18 bold")
            cus_k.place(x=0,y=80)

            cus_k=Label(frame3,text='Inside',font="arail 18 bold")
            cus_k.place(x=0,y=120)

            cus_k=Label(frame3,text='Waist',font="arail 18 bold")
            cus_k.place(x=0,y=160)

            cus_k=Label(frame3,text='Seat',font="arail 18 bold")
            cus_k.place(x=0,y=200)

            cus_k=Label(frame3,text='Inseam',font="arail 18 bold")
            cus_k.place(x=0,y=240)

            cus_k=Label(frame3,text='Ankle',font="arail 18 bold")
            cus_k.place(x=0,y=280)

            cus_k=Label(frame3,text='Bottom',font="arail 18 bold")
            cus_k.place(x=0,y=320)

            cus_n=Label(frame3,text='Price',font="arail 18 bold")
            cus_n.place(x=0,y=360)
    #===================================Entry===================================#

            customer_e=Entry(frame3,font='arail 18 bold')
            customer_e.place(x=160,y=0)

            pho_e=Entry(frame3,font='arail 18 bold')
            pho_e.place(x=160,y=40)

            height_e=Entry(frame3,font='arail 18 bold')
            height_e.place(x=160,y=80)

            inside_e=Entry(frame3,font='arail 18 bold')
            inside_e.place(x=160,y=120)

            waist_e=Entry(frame3,font='arail 18 bold')
            waist_e.place(x=160,y=160)

            seat_e=Entry(frame3,font='arail 18 bold')
            seat_e.place(x=160,y=200)

            inseam_e=Entry(frame3,font='arail 18 bold')
            inseam_e.place(x=160,y=240)

            ankle_e=Entry(frame3,font='arail 18 bold')
            ankle_e.place(x=160,y=280)

            bottom_e=Entry(frame3,font='arail 18 bold')
            bottom_e.place(x=160,y=320)

            price_e=Entry(frame3,font='arail 18 bold')
            price_e.place(x=160,y=360)

    #===================================Button===================================#
            btn7=Button(frame3,text='submit',width=60,command=create_customer,bg='orange')
            btn7.place(x=0,y=400)

def create_customer():
    global chest
    x = datetime.datetime.now()
    dates=x.strftime("%x")
#===================================Get Entry===================================#
    try:
        hips=hip_e.get()
        types=type_e.get()
        customer=customer_e.get() 
        phone=pho_e.get()
        chest=chest_e.get()
        sleev=sleeve_e.get()
        shoulder=shoulder_e.get()
        waist=waist_e.get()
        back_l=back_l_e.get()
        neck=neck_e.get()
        collars=collar.get()
        prices=price_e.get()
    except NameError:
        print('')
#=============================entry for pant====================================
    
#===================================Insert Entry to database===================================#
    
    if var.get()=='Shirt' or var.get()=='Safari Suit' or var.get()=='Safari Fusion':
        if customer=='' or phone=='' or chest=='' or sleev=='' or shoulder=='' or waist=='' or back_l=='' or neck=='':
            messagebox.showwarning("Entry error","Some entry are empty")
        else:
            
        
            with connecter:
                    
                c.execute("""INSERT INTO order_detail (cus_name,sleeve,phone_no,chest,center_point,shoulder,waist,length,neck,collar,type,hip,price,date) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(customer,types,phone,chest,sleev,shoulder,waist,back_l,neck,collars,var.get(),hips,prices,dates))
            with connecter:
                c.execute("""SELECT * FROM order_detail WHERE cus_name='{}' AND type='{}'""".format(customer,var.get()))
                a=c.fetchone()
            messagebox.showinfo("congrat","customer Order id is :{}".format(a[1]))
    if var.get()=='Pant' or var.get()=='Kurtas':
        
        customers=customer_e.get()
        phones=pho_e.get()
        height=height_e.get()
        inside=inside_e.get()
        waists=waist_e.get()
        seat=seat_e.get()
        inseam=inseam_e.get()
        ankle=ankle_e.get()
        bottom=bottom_e.get()
        prices=price_e.get()

        if customers=='' or phones=='' or height=='' or inside=='' or waists=='' or seat=='' or inseam=='' or ankle=='' or bottom=='' or prices=='':
            messagebox.showwarning("Entry error","Some entry are empty")

        else:
            
        
            with connecter:
                    
                c.execute("""INSERT INTO order_detail (cus_name,height,phone_no,inside,waist,hip,inseam,ankle,bottom,type,price,date) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(customers,height,phones,inside,waists,seat,inseam,ankle,bottom,var.get(),prices,dates))
            with connecter:
                c.execute("""SELECT * FROM order_detail WHERE cus_name='{}'""".format(customers))
                a=c.fetchone()
            messagebox.showinfo("congrat","customer Order id is :{}".format(a[1]))






delta=0

def load_image():
    global Deathwing2
    global delta,frame6
    #get_img=img_e.get()
    #print(get_img)
    image_list=[]

    try:
        frame6.place_forget()
    except NameError:
        print('')
    
    if var.get()=='':
        messagebox.showwarning("Entry error","entry are empty")
    else:
        
    
        with connecter:
            c.execute("""SELECT * FROM product WHERE name='{}'""".format(var.get()))
            views=c.fetchall()
            for i in views:
                a=i[2]
                
                image_list.append(a)

            
            
               
            mylist = list(dict.fromkeys(image_list))
            

            if len(mylist)==0:
                print('no list')
                try:
                    label.configure(text='no imahge')
                except NameError:
                    messagebox.showwarning("Entry error","Some entry are empty")
            else:
                frame6=Frame(root,width=10000,height=1000,borderwidth=5,bg='steelblue')
                frame6.place(x=100,y=100)
            
                
            
                if delta == len(mylist):
                    delta=0

                if delta == -1:
                    delta=delta+1

                  
                    
                if len(mylist) != delta:
                    
                    img =Image.open(mylist[delta])
                    img = img.resize((700, 700), Image.ANTIALIAS)
                    Deathwing2=ImageTk.PhotoImage(img)
                        
                    label =Label(frame6, image = Deathwing2)
                    label.place(x=600,y=100)

                    back_button=Button(frame6, text='Previous picture', command=back)
                    back_button.place(x=600,y=810)
                    forward_button=Button(frame6, text='Next picture', command=front)
                    forward_button.place(x=700,y=810)
         
                else:
                    print('lol')
            
def show_image():
    global l
    global delta,frame7
    global current, image_list,label,img_e
    global var
    a=[]

    try:
        let_forget()
        
    except NameError:
        print(NameError)
    
    
    finally:
        frame7=Frame(root,width=500,height=500,borderwidth=5,bg='steelblue')
        frame7.place(x=0,y=100)

        with connecter:
            c.execute("""SELECT * FROM product""")
            view=c.fetchall()
            for i in view:
                a.append(i[1])
            myl = list(dict.fromkeys(a))
            
        var = StringVar(root)
        if myl==[]:
            messagebox.showwarning("Entry error","Sorry NO Image Uploaded")
        else:
            
            var.set(myl[0]) # initial value

            option = OptionMenu(frame7, var, *myl)
            option.place(x=0,y=0)
            option.config(font=('arail 18 bold'))
            
            button = Button(frame7, text="select",font='arail 18 bold', command=load_image)
            button.place(x=0,y=50)        

        
    
def back():
    global delta
    delta=delta-1
    load_image()

def front():
    global delta
    delta=delta+1
    load_image()


def tick():
    setTime = time.strftime('%I: %M %S %p')
    clock.config(text=setTime )
    clock.after(200, tick)


        
clock = Label(frame, font=('times', 50 , 'bold'), fg="green")
clock.place(x=1200,y=0)



def analize():
    global frame15
    global frameTable
    try:
        let_forget()
    except NameError:
        print("")
    finally:
        #SELECT * FROM Student ORDER BY ROLL_NO DESC;
        with connecter:
                c.execute("""SELECT * FROM order_detail ORDER BY ID DESC""")
                get=c.fetchall()
        
        frame15=Frame(root,width=10000,height=10000,borderwidth=5,relief=RAISED)
        frame15.place(x=0,y=110)

        frameTable=Frame(frame15,width=10000,height=10000,borderwidth=5)
        frameTable.pack()

        

        cols = ('Customer', 'Type', 'id','Price','Date')
        listBox = ttk.Treeview(frameTable,selectmode='browse',columns=cols, show='headings')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 20))
        style.configure('Treeview', rowheight=40)
        style.configure('Treeview', font=('Helvetica', 12))
        
        
        listBox.heading("Customer", text="Customer")
        listBox.column("Customer", minwidth=0, width=200, stretch=NO)

        listBox.heading("Type", text="Type")
        listBox.column("Type", minwidth=0, width=200, stretch=NO)

        listBox.heading("id", text="id")
        listBox.column("id", minwidth=0, width=200, stretch=NO)

        listBox.heading("Price", text="Price")
        listBox.column("Price", minwidth=0, width=200, stretch=NO)

        listBox.heading("Date", text="Date")
        listBox.column("Date", minwidth=0, width=200, stretch=NO)
        
        vsb = ttk.Scrollbar(frameTable, orient="vertical", command=listBox.yview)
        vsb.place(relx=0.978, rely=0.175, relheight=0.713, relwidth=0.020)

        listBox.configure(yscrollcommand=vsb.set)

        
        
        # set column headings
        for col in cols:
            listBox.heading(col, text=col)    
        listBox.grid(row=1, column=0, columnspan=2)

        for i in get:
            rs="Rs "+str(i[10])
            listBox.insert("", "end", values=(i[0],i[2],i[1],rs,i[19]))

        #listBox.selection_set(item_iid)
        #a=listBox.focus(item_iid)

        #selected = [lstbox.get(i) for i in listBox.curselection()]

        



def auditTemplate():
    global frame16
    global name_e,var,amt_e,name_l,type_l,amt_l,option,btn22,name_eu
    let_forget()
    
    frame16=Frame(root,width=10000,height=700,borderwidth=5,relief=RAISED)
    frame16.place(x=0,y=110)


    ###########create customer###########################

    type_list=['Dena','Lena']
    ##########Label
    name_l=Label(frame16,font='arail 18 bold',text="Name")
    name_l.place(x=0,y=0)

    type_l=Label(frame16,font='arail 18 bold',text="Type")
    type_l.place(x=0,y=50)

    amt_l=Label(frame16,font='arail 18 bold',text="Amount")
    amt_l.place(x=0,y=100)

    ##########Entry
    name_e=Entry(frame16,font='arail 18 bold')
    name_e.place(x=100,y=0)

    
    var = StringVar(frame16)
    var.set(type_list[0])
    option=OptionMenu(frame16, var,*type_list)
    option.place(x=100,y=50)
    option.config(font=('arail 18 bold'))

    amt_e=Entry(frame16,font='arail 18 bold')
    amt_e.place(x=100,y=100)

    ###To save

    btn22=Button(frame16,text='Create one',font='arail 18 bold',command=createnew,bg='green')
    btn22.place(x=0,y=150)

    #btn21=Button(frame16,text='Create one',font='arail 18 bold',command=createaudit,bg='green')
    #btn21.place(x=0,y=0)

    #btn23=Button(frame16,text='Update',font='arail 18 bold',command=updateaudit,bg='yellow')
    #btn23.place(x=0,y=60)
    
    
    #name_l.destroy()


    ###################Update or Search######################
    ##########Label
    name_u=Label(frame16,font='arail 18 bold',text="Name")
    name_u.place(x=400,y=0)


    ##########Entry
    name_eu=Entry(frame16,font='arail 18 bold')
    name_eu.place(x=500,y=0)

    btn21=Button(frame16,text='Search',font='arail 18 bold',command=updateaudit,bg='green')
    btn21.place(x=400,y=49)

    btn24=Button(frame16,text='Record',font='arail 18 bold',command=record,bg='yellow')
    btn24.place(x=500,y=49)

    
    

    


def createnew():
    #let_forget()
    name=name_e.get()
    types=var.get()
    amt=amt_e.get()
    datess=timer.strftime("%x")
    with connecter:
        c.execute("""INSERT INTO Audit (Name,type,amt) VALUES ('{}','{}','{}')""".format(name,types,amt))
    with connecter:
        c.execute("""SELECT * FROM Audit WHERE Name='{}'""".format(name))
        get=c.fetchone()
        #print(get)
    with connecter:
        c.execute("""INSERT INTO Transactions (name_id,types,amount,date) VALUES ('{}','{}','{}','{}')""".format(get[1],get[2],get[3],datess))

    messagebox.showinfo("congrat","customer: {} added Sucessfully".format(get[0]))



def updateaudit():
    type_lists=['Dena','Lena']
    global result,varss,amt_es,amt_ll,btn23
    #listBox1.destroy()
    try:
        amt_ll.destroy()
        amt_es.destroy()
        btn23.destroy()
        
    except NameError:
        print(NameError)
        
    try:
        listBox1.place_forget()
        
    except NameError:
        print(NameError)
    
    with connecter:
        c.execute("""SELECT * FROM Audit WHERE Name='{}'""".format(name_eu.get()))
        result=c.fetchone()

    if result==None:
        messagebox.showwarning("Warning","No User Found")
    else:
        

        #type_l=Label(frame16,font='arail 18 bold',text="Type")
        #type_l.place(x=400,y=100)

        amt_ll=Label(frame16,font='arail 18 bold',text="Amount")
        amt_ll.place(x=400,y=150)

        """varss = StringVar(frame16)
        varss.set(type_lists[0])
        options=OptionMenu(frame16, varss,*type_lists)
        options.place(x=500,y=100)
        options.config(font=('arail 18 bold'))"""

        amt_es=Entry(frame16,font='arail 18 bold')
        amt_es.place(x=500,y=150)


        ############record

        

        def update():
            updatess=timer.strftime("%x")
            updatedamt=int(result[3])-int(amt_es.get())

            if result[3]==0 or result[3]<0:
                messagebox.showinfo("Info","This Customer Has Done Payment")
                amt_ll.destroy()
                amt_es.destroy()
                btn23.destroy()
            else:
                

                mes=response=messagebox.askquestion("Title of message box ","Want To Update ?", icon='question')
                print(mes)
                if mes=="yes":
                    
                    with connecter:
                        c.execute("""INSERT INTO Transactions (name_id,types,amount,date) VALUES ('{}','{}','{}','{}')""".format(result[1],result[2],amt_es.get(),updatess))
                        c.execute("""Update Audit set amt = '{}' where id ='{}' """.format(updatedamt,result[1]))
                    amt_ll.destroy()
                    amt_es.destroy()
                    btn23.destroy()

                else:
                    print('yash')

            
            
            

            #for i in get:
            #    rs="Rs "+str(i[10])
            #    listBox1.insert("", "end", values=(i[0],i[2],i[1],rs,i[19]))

        
    
        btn23=Button(frame16,text='Update',font='arail 18 bold',command=update,bg='yellow')
        btn23.place(x=400,y=200)

        

global listBox1
def record():
    #type_lists=['Dena','Lena']
    global result,varss,amt_es,amt_l
    global listBox1
    
    try:
        listBox1.destroy()
        
    except NameError:
        print(NameError)
        
    try:
        amt_ll.destroy()
        amt_es.destroy()
        btn23.destroy()
        
    except NameError:
        print(NameError)
    
    with connecter:
        c.execute("""SELECT * FROM Audit WHERE Name='{}'""".format(name_eu.get()))
        result=c.fetchone()

    if result==None:
        messagebox.showwarning("Warning","No User Found")
    else:
        cols1s = ('Name', 'Type', 'Amt','Date')
        listBox1 = ttk.Treeview(frame16,selectmode='extended',columns=cols1s, show='headings')

        style1 = ttk.Style()
        style1.configure("Treeview.Heading", font=(None, 20))
        style1.configure('Treeview', rowheight=40)
        style1.configure('Treeview', font=('Helvetica', 12))
                
                
        listBox1.heading("Name", text="Name")
        listBox1.column("Name", minwidth=0, width=200, stretch=NO)

        listBox1.heading("Type", text="Type")
        listBox1.column("Type", minwidth=0, width=200, stretch=NO)

        listBox1.heading("Amt", text="Amt")
        listBox1.column("Amt", minwidth=0, width=200, stretch=NO)

        listBox1.heading("Date", text="Date")
        listBox1.column("Date", minwidth=0, width=200, stretch=NO)

        #listBox1.heading("Date", text="Date")
        #listBox1.column("Date", minwidth=0, width=200, stretch=NO)
                
        vsb1 = ttk.Scrollbar(listBox1, orient="vertical", command=listBox1.yview)
        vsb1.place(relx=0.978, rely=0.175, relheight=0.713, relwidth=0.020)
        

        listBox1.configure(yscrollcommand=vsb1.set)
        
        style1 = ttk.Style()

        #listBox1.tag_configure("red_fg", foreground="blue")

        
        

        # set column headings
        for col in cols1s:
            listBox1.heading(col, text=col)    
        listBox1.place(x=0,y=210)
        #listBox1.tag_configure('fg', foreground="#fff")
            
        with connecter:
            c.execute("""SELECT Name,type,amount,date,amt FROM Audit INNER JOIN Transactions ON Audit.id = Transactions.name_id""")
            new_result=c.fetchall()
            
          
            for i in new_result:
                if i[0]==name_eu.get():
                    print(i)
                    #for i in get:
                    #rs="Rs "+str(i[10])
                    listBox1.insert("", "end", values=(i[0],i[1],i[2],i[3]),tags=['blue_fg'])

            listBox1.insert("", "end", values=("-","-","-","-"),tags=['red_fg'])
                    
            for i in new_result:
                if i[0]==name_eu.get():
                    listBox1.insert("", "end", values=("Total Remaining","-",i[4],"-"),tags=['red_fg'])
                    break
            
        

"""
def graph():
    global sort_graph
    
    
    try:
        frameTable.destroy()
        let_forgot()
    except NameError:
        print(NameError)
    finally:
        db={}
        frameTabl=Frame(frame15,width=10000,height=10000,borderwidth=5)
        frameTabl.place(x=0,y=110)
       
        with connecter:
            
            c.execute(""SELECT * FROM order_detail"")
            get=c.fetchall()
            p=[]
            d=[]
            for i in get:
                
                p.append(i[10])
                #d.append(i[19])
                kc_d=datetime.datetime.strptime(i[19], '%m/%d/%y')
                d.append(datetime.date.strftime(kc_d, "%d/%m/%y"))
            
        db['price']=p
        db['date']=d
        #print(db)
        df2 = DataFrame(db,columns=['date','price'])
        
        figure2 = plt.Figure(figsize=(20,6), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, frameTabl)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[['date','price']].groupby('date').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        ax2.set_title('LifeTime Sale Report')

        ################sort######################
        global calf
        global calt
        From_l=Label(frame15,text='From',font='arail 18 bold')
        From_l.place(x=110,y=0)
        dates=datetime.datetime.now()
        calf = DateEntry(frame15, width=12,height=12, year=dates.year, month=dates.month, day=int('1'), 
        background='darkblue', foreground='white', borderwidth=2)
        calf.place(x=200,y=10)

        To_l=Label(frame15,text='To',font='arail 18 bold')
        To_l.place(x=310,y=0)
        #dates=datetime.datetime.now()
        calt = DateEntry(frame15, width=12,height=12, year=dates.year, month=dates.month, day=dates.day, 
        background='darkblue', foreground='white', borderwidth=2)
        calt.place(x=380,y=10)

        

        def sort_graph():
            global sort_graph
            try:
                frameTabll.place_forget()
            except Exception as e:
                print('')
            

            
            frameTabl.place_forget()

            frameTabll=Frame(frame15,width=10000,height=10000,borderwidth=5)
            frameTabll.place(x=0,y=110)
            
            df={}
            fromcalf=calf.get_date()
            tocalf=calt.get_date()
            f="{}/{}/{}".format(fromcalf.month,fromcalf.day,fromcalf.year)
            t="{}/{}/{}".format(tocalf.month,tocalf.day,tocalf.year)

            date_str = '09-19-2018'

            d = datetime.datetime.strptime(f, '%m/%d/%Y')
            ff=datetime.date.strftime(d, "%m/%d/%y")

            new_d=datetime.datetime.strptime(t, '%m/%d/%Y')
            tt=datetime.date.strftime(new_d, "%m/%d/%y")
            pp=[]
            dd=[]
            with connecter:
            
                c.execute(""SELECT * FROM order_detail WHERE date BETWEEN '{}' AND '{}'"".format(ff,tt))
                get=c.fetchall()
                if get==[]:
                    messagebox.showwarning("Entry error","Sorry No Data Available")
                else:
                    
                    for i in get:
                        pp.append(i[10])
                        kk_d=datetime.datetime.strptime(i[19], '%m/%d/%y')
                        dd.append(datetime.date.strftime(kk_d, "%d/%m/%y"))
                        
                    df['price']=pp
                    df['date']=dd

                    ##############Graph##################
                    df3 = DataFrame(df,columns=['date','price'])
                
                    figure2 = plt.Figure(figsize=(10,4), dpi=100)
                    ax2 = figure2.add_subplot(111)
                    line2 = FigureCanvasTkAgg(figure2, frameTabll)
                    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
                    df3 = df3[['date','price']].groupby('date').sum()
                    df3.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
                    ax2.set_title('Sale Report')

        
        btn11=Button(frame15,text='Filter',font='arail 18 bold',command=sort_graph,bg='orange')
        btn11.place(x=500,y=0)"""
     


def let_forget():

    
    try:
        listBoxl.place_forget()
        
    except NameError:
        print(NameError)
        
    try:
        frameTabll.place_forget()
        
    except NameError:
        print(NameError)

    try:
        frameTabl.place_forget()
        
    except NameError:
        print(NameError)
        
    try:
        frame15.place_forget()
        
    except NameError:
        print(NameError)
        
    try:
        frame9.place_forget()
        
    except NameError:
        print(NameError)
        
    try:
        frame3.place_forget()
        
    except NameError:
        print(NameError)

    try:
        l.place_forget()
        
    except NameError:
        print(NameError)

    try:
        
        frame1.place_forget()
    except NameError:
        print(NameError)

    try:
        
        frame6.place_forget()
    except NameError:
        print(NameError)

    try:
        
        frame7.place_forget()
    except NameError:
        print(NameError)

        
    try:
        frame2.place_forget()
    except NameError:
        print(NameError)

    try:
        frame16.place_forget()
    except NameError:
        print(NameError)

    
    
###############main window ######################
btn8=Button(frame, text=u'\u26A0',font='arail 18 bold',bg='red',command=root.destroy)
btn8.place(x=1800,y=0)



btn2=Button(frame,text='Upload Image',font='arail 18 bold',command=uploadImage_template,bg='orange')
btn2.place(x=0,y=0)

btn3=Button(frame,text='Search Order',font='arail 18 bold',command=search_order_template,bg='orange')
btn3.place(x=200,y=0)

btn5=Button(frame,text='view image',font='arail 18 bold',command=show_image,bg='orange')
btn5.place(x=400,y=0)

btn6=Button(frame,text='Create order',font='arail 18 bold',command=drop_down,bg='orange')
btn6.place(x=600,y=0)

btn6=Button(frame,text='Analize',font='arail 18 bold',command=analize,bg='orange')
btn6.place(x=800,y=0)

btn20=Button(frame,text='Audit',font='arail 18 bold',command=auditTemplate,bg='orange')
btn20.place(x=1000,y=0)


######################################################################
root.overrideredirect(False)
root.title('store')

root.configure(background='steelblue')
root.state('zoomed')
if __name__ == '__main__':
    tick()
    root.mainloop()

