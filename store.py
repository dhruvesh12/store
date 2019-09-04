from tkinter import *
from tkinter import Label,Tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import sqlite3
from tkinter import messagebox
import time
from PIL import Image, ImageTk
from tkinter import filedialog



    #vsb = ttk.Scrollbar(frame2,orient="vertical",command=tree.yview)
    #tree.configure(yscrollcommand=vsb.set)
    #vsb.pack(side='right', fill='y')

          
    #for col in lb_header:
 #    tree.heading(col, text=col.title())
#for item in views:
#    tree.insert('', 'end', values=[item[0],item[1],item[2]])



connecter=sqlite3.connect("store.db")
c = connecter.cursor()

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
	`ankle`	INTEGER
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
    finally:
        
    
    
        frame1=Frame(root,width=500,height=400,borderwidth=5,relief=RAISED)
        frame1.place(x=0,y=100)

            ##########label############
        name_l=Label(frame1,text="Name",font='arail 16 bold')
        name_l.place(x=0,y=100)

        

        #selling_l=Label(frame1,text="selling price",font='arail 16 bold')
        #selling_l.place(x=0,y=250)

        #grams_l=Label(frame1,text="Grams",font='arail 16 bold')
        #grams_l.place(x=0,y=300)

        #id_l=Label(frame1,text="Enter id",font='arail 16 bold')
        #id_l.place(x=0,y=350)
            ##########Entry############
            
        name_e=Entry(frame1,font='arail 16 bold')
        name_e.place(x=130,y=100)
            
        btn4=Button(frame1,text='upload image',command=get_image)
        btn4.place(x=130,y=150)

        labelx =Label(frame1, fg="red", text="No file selected.")
        labelx.place(x=215,y=150)
        #selling_e=Entry(frame1,font='arail 16 bold')
        #selling_e.place(x=130,y=250)
            
        #grams_e=Entry(frame1,font='arail 16 bold')
        #grams_e.place(x=130,y=300)

        #id_e=Entry(frame1,font='arail 16 bold')
        #id_e.place(x=130,y=350)

        btn2=Button(frame1,text='submit',command=uploadImage)
        btn2.place(x=0,y=150)


def get_image():
    global path
    path=filedialog.askopenfilename(filetypes=[("Image File",'.png')])
    labelx.config(text=path)
    btn4.configure(bg='red')


def uploadImage():
    get_name=name_e.get()


    if get_name=='':
        messagebox.showwarning("warning","fill the entry ")
    else:
        
        with connecter:
            c.execute("""INSERT INTO product (name,image) VALUES ('{}','{}')""".format(get_name,path))
        messagebox.showinfo("congrat","You added product")
        

        name_e.delete(0,END)
        
##################main window function##################

global tree

def search_order_template():
    global frame2,id_e,cus_n,cus_t,cus_ph,cus_c,cus_s,cus_sh,cus_w,cus_bl,cus_ne,cus_p,cus_hip
    global cus_collar,name_e

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
        print('')

    try:
        frame2.place_forget()
    except NameError:
        print('')

    try:
        
        frame7.place_forget()
    except NameError:
        print(NameError)

    finally:
        
        frame2=Frame(root,width=1000,height=500,borderwidth=5,relief=RAISED)
        frame2.place(x=0,y=100)
#==============================Label==============================================
        lb=Label(frame2,text='Search Order',font='arail 20 bold',bg='steelblue')
        lb.place(x=250,y=0)

        lb_1=Label(frame2,text='Enter ID',font='arail 18 bold')
        lb_1.place(x=0,y=50)

        lb_n=Label(frame2,text='Enter name',font='arail 18 bold')
        lb_n.place(x=0,y=150)

        


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
#================================Entry==============================================

        id_e=Entry(frame2,font='arail 18 bold',bg='steelblue')
        id_e.place(x=100,y=50)

        Label(frame2,text='Or',font='arail 10 bold').place(x=0,y=130)

        name_e=Entry(frame2,font='arail 18 bold')
        name_e.place(x=150,y=150)

#=============================Button==================================================
        Button(frame2,text='search',bg='orange',command=search_order).place(x=0,y=100)
        


def search_order():
    get_id=id_e.get()
    get_name=name_e.get()

    if get_id=='' and get_name=='':
        messagebox.showwarning("Warning","sorry no input")

    else:
        with connecter:
                c.execute("""SELECT * FROM order_detail WHERE id='{}' OR cus_name='{}'""".format(get_id,get_name))
                get=c.fetchone()
                #messagebox.showinfo("congrat","You name is {}".format(get[0]))

                
                if get==None:
                    messagebox.showwarning("Warning","sorry no input")
                else:
                    if get[2]=='Shirt':
                        print('inputs are {}'.format(get))
                        
                        cust_n=Label(frame2,text='Vender Name',font="arail 18 bold")
                        cust_n.place(x=500,y=0)     

                        cust_n=Label(frame2,text='Type',font="arail 18 bold")
                        cust_n.place(x=500,y=40)

                        cust_n=Label(frame2,text='Phone_no',font="arail 18 bold")
                        cust_n.place(x=500,y=80)

                        cust_n=Label(frame2,text='lenght',font="arail 18 bold")
                        cust_n.place(x=500,y=120)

                        cust_n=Label(frame2,text='shoulder',font="arail 18 bold")
                        cust_n.place(x=500,y=160)

                        cust_n=Label(frame2,text='chest',font="arail 18 bold")
                        cust_n.place(x=500,y=200)

                        cust_n=Label(frame2,text='sleeves',font="arail 18 bold")
                        cust_n.place(x=500,y=240)

                        cust_n=Label(frame2,text='center_p',font="arail 18 bold")
                        cust_n.place(x=500,y=280)

                        #cust_n=Label(frame2,text='seat',font="arail 18 bold")
                        #cust_n.place(x=500,y=320)

                        cust_n=Label(frame2,text='neck',font="arail 18 bold")
                        cust_n.place(x=500,y=320)

                        cust_n=Label(frame2,text='collar',font="arail 18 bold")
                        cust_n.place(x=500,y=360)

                        cust_n=Label(frame2,text='seat',font="arail 18 bold")
                        cust_n.place(x=500,y=400)

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
                        
                    elif get[2]=='Pant':

                        cust_n=Label(frame2,text='Vender Name',font="arail 18 bold")
                        cust_n.place(x=500,y=0)     

                        cust_n=Label(frame2,text='Type',font="arail 18 bold")
                        cust_n.place(x=500,y=40)

                        cust_n=Label(frame2,text='Phone_no',font="arail 18 bold")
                        cust_n.place(x=500,y=80)

                        cust_n=Label(frame2,text='height',font="arail 18 bold")
                        cust_n.place(x=500,y=120)

                        cust_n=Label(frame2,text='inside',font="arail 18 bold")
                        cust_n.place(x=500,y=160)

                        cust_n=Label(frame2,text='waist',font="arail 18 bold")
                        cust_n.place(x=500,y=200)

                        cust_n=Label(frame2,text='hip',font="arail 18 bold")
                        cust_n.place(x=500,y=240)

                        cust_n=Label(frame2,text='inseam',font="arail 18 bold")
                        cust_n.place(x=500,y=280)

                        cust_n=Label(frame2,text='ankle',font="arail 18 bold")
                        cust_n.place(x=500,y=320)

                        cust_n=Label(frame2,text='bottom',font="arail 18 bold")
                        cust_n.place(x=500,y=360)

                        

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
                        
                    
def drop_down():
    global var
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

    finally:
        var = StringVar(root)
        var.set("Shirt") # initial value

        option = OptionMenu(root, var, "Shirt", "Pant")
        option.place(x=0,y=100)
        option.config(font=('arail 18 bold'))
        
        button = Button(root, text="select",font='arail 18 bold', command=create_order_template)
        button.place(x=0,y=150)

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
    global height_e,inside_e,waist_e,seat_e,inseam_e,ankle_e,bottom_e,hip_e

    global frame3
    
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

    finally:
        frame3=Frame(root,width=500,height=500,borderwidth=5,relief=RAISED)
        frame3.place(x=120,y=100)
        if var.get()=='Shirt':
            

            
    #===============================label=====================================#
            
            cus_n=Label(frame3,text='Vender Name',font="arail 18 bold")
            cus_n.place(x=0,y=0)

            cus_n=Label(frame3,text='sleeves',font="arail 18 bold")
            cus_n.place(x=0,y=40)

            cus_n=Label(frame3,text='Phone_no',font="arail 18 bold")
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
    #===================================Entry===================================#

            customer_e=Entry(frame3,font='arail 18 bold')
            customer_e.place(x=160,y=0)

            type_e=Entry(frame3,font='arail 18 bold')
            type_e.place(x=160,y=40)

            pho_e=Entry(frame3,font='arail 18 bold')
            pho_e.place(x=160,y=80)

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
    #===================================Button===================================#
            btn7=Button(frame3,text='submit',command=create_customer)
            btn7.place(x=0,y=440)

            customer_e.focus()

        if var.get()=='Pant':
            

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

    #===================================Button===================================#
            btn7=Button(frame3,text='submit',command=create_customer)
            btn7.place(x=0,y=400)

def create_customer():
    global chest
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
    except NameError:
        print('')
#=============================entry for pant====================================
    
#===================================Insert Entry to database===================================#
    
    if var.get()=='Shirt':
        if customer=='' or phone=='' or chest=='' or sleev=='' or shoulder=='' or waist=='' or back_l=='' or neck=='':
            messagebox.showwarning("Entry error","Some entry are empty")
        else:
            
        
            with connecter:
                    
                c.execute("""INSERT INTO order_detail (cus_name,sleeve,phone_no,chest,center_point,shoulder,waist,length,neck,collar,type,hip) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(customer,types,phone,chest,sleev,shoulder,waist,back_l,neck,collars,var.get(),hips))
            with connecter:
                c.execute("""SELECT * FROM order_detail WHERE cus_name='{}'""".format(customer))
                a=c.fetchone()
            messagebox.showinfo("congrat","customer Order id is :{}".format(a[1]))
    if var.get()=='Pant':
        customers=customer_e.get()
        phones=pho_e.get()
        height=height_e.get()
        inside=inside_e.get()
        waists=waist_e.get()
        seat=seat_e.get()
        inseam=inseam_e.get()
        ankle=ankle_e.get()
        bottom=bottom_e.get()
        with connecter:
                
            c.execute("""INSERT INTO order_detail (cus_name,height,phone_no,inside,waist,hip,inseam,ankle,bottom,type) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(customers,height,phones,inside,waists,seat,inseam,ankle,bottom,var.get()))
        with connecter:
            c.execute("""SELECT * FROM order_detail WHERE cus_name='{}'""".format(customers))
            a=c.fetchone()
        messagebox.showinfo("congrat","customer Order id is :{}".format(a[1]))


delta=0

def load_image():
    global Deathwing2
    global delta,frame6
    get_img=img_e.get()
    #print(get_img)
    image_list=[]

    try:
        frame6.place_forget()
    except NameError:
        print('')
    
    if get_img=='':
        messagebox.showwarning("Entry error","entry are empty")
    else:
        
    
        with connecter:
            c.execute("""SELECT * FROM product WHERE name='{}'""".format(get_img))
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
                frame6.place(x=400,y=100)
            
                
            
                if delta == len(mylist):
                    delta=0

                if delta == -1:
                    delta=delta+1
                    #print(len(mylist))
                    #print(delta)
                    
                    
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
    finally:
        frame7=Frame(root,width=500,height=500,borderwidth=5,bg='steelblue')
        frame7.place(x=0,y=100)

        img_e=Entry(frame7,font='arail 18 bold')
        img_e.place(x=0,y=0)

        img_e.focus()
        
        back_button=Button(frame7, text='show picture', command=load_image)
        back_button.place(x=0,y=50)
       
        
       
        


    
def back():
    global delta
    delta=delta-1
    load_image()

def front():
    global delta
    delta=delta+1
    load_image()


        

        
symbol = {'alpha':945, 'beta':946, 'gamma': 947, 'delta': 948, 'epsilon':949}
    
###############main window ######################
btn8=Button(frame, text=u'\u26A0',font='arail 18 bold',bg='red',command=root.destroy)
btn8.place(x=1800,y=0)
#btn8.configure(image=photo1)


btn2=Button(frame,text='Upload Image',font='arail 18 bold',command=uploadImage_template,bg='orange')
btn2.place(x=0,y=0)

btn3=Button(frame,text='Search Order',font='arail 18 bold',command=search_order_template,bg='orange')
btn3.place(x=200,y=0)

btn5=Button(frame,text='view image',font='arail 18 bold',command=show_image,bg='orange')
btn5.place(x=400,y=0)

btn6=Button(frame,text='Create order',font='arail 18 bold',command=drop_down,bg='orange')
btn6.place(x=600,y=0)


######################################################################
root.overrideredirect(True)
root.title('store')

root.configure(background='steelblue')
root.state('zoomed')
root.mainloop()
