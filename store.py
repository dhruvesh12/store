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






connecter=sqlite3.connect("store.db")
c = connecter.cursor()


root = Tk()
frame=Frame(root,width=10000,height=100,borderwidth=5,relief=RAISED)
frame.place(x=0,y=0)


def uploadImage_template():
    global name_e
    global original_e
    global stock_e
    global frame1
    global labelx

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

def update():
    global frame2

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

    finally:
        
        frame2=Frame(root,width=500,height=500,borderwidth=5,relief=RAISED)
        frame2.place(x=0,y=100)
        lb_header = ['product name', 'Original price','Stock']
        
        with connecter:
            c.execute("""SELECT * FROM product""")
            views=c.fetchall()

        tree = ttk.Treeview(frame2,columns=lb_header, show="headings",selectmode='browse')
        tree.pack(side='left')
        


        
        vsb = ttk.Scrollbar(frame2,orient="vertical",command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side='right', fill='y')

          
        for col in lb_header:
            tree.heading(col, text=col.title())
        for item in views:
            tree.insert('', 'end', values=[item[0],item[1],item[2]])


def create_order_template():
    global customer_e
    global type_e
    global pho_e
    global chest_e
    global sleeve_e
    global shoulder_e
    global waist_e
    global back_l_e
    global neck_e

    global frame3
    
    try:
        l.place_forget()
        
    except NameError:
        print(NameError)

    try:
        frame3.place_forget()
        
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

    finally:

        frame3=Frame(root,width=500,height=500,borderwidth=5,relief=RAISED)
        frame3.place(x=0,y=100)
#===============================label=====================================#
        
        cus_n=Label(frame3,text='Vender Name',font="arail 18 bold")
        cus_n.place(x=0,y=0)

        cus_n=Label(frame3,text='Type',font="arail 18 bold")
        cus_n.place(x=0,y=40)

        cus_n=Label(frame3,text='Phone_no',font="arail 18 bold")
        cus_n.place(x=0,y=80)

        cus_n=Label(frame3,text='chest',font="arail 18 bold")
        cus_n.place(x=0,y=120)

        cus_n=Label(frame3,text='sleeves',font="arail 18 bold")
        cus_n.place(x=0,y=160)

        cus_n=Label(frame3,text='shoulder',font="arail 18 bold")
        cus_n.place(x=0,y=200)

        cus_n=Label(frame3,text='waist',font="arail 18 bold")
        cus_n.place(x=0,y=240)

        cus_n=Label(frame3,text='back length',font="arail 18 bold")
        cus_n.place(x=0,y=280)

        cus_n=Label(frame3,text='neck',font="arail 18 bold")
        cus_n.place(x=0,y=320)
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
#===================================Button===================================#
        btn7=Button(frame3,text='submit',command=create_customer)
        btn7.place(x=0,y=360)

def create_customer():
#===================================Get Entry===================================#    
    customer=customer_e.get()
    typs=type_e.get()
    phone=pho_e.get()
    chest=chest_e.get()
    sleev=sleeve_e.get()
    shoulder=shoulder_e.get()
    waist=waist_e.get()
    back_l=back_l_e.get()
    neck=neck_e.get()
#===================================Insert Entry to database===================================#
    if customer=='' or typs=='' or phone=='' or chest=='' or sleev=='' or shoulder=='' or waist=='' or back_l=='' or neck=='':
        messagebox.showwarning("Entry error","Some entry are empty")
    else:
        
        with connecter:
            
            c.execute("""INSERT INTO order_detail (cus_name,type,phone_no,chest,sleeve,shoulder,waist,back_length,neck) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(customer,typs,phone,chest,sleev,shoulder,waist,back_l,neck))
        messagebox.showinfo("congrat","You added customer")


image_list=[]
delta=0

def load_image():
    global Deathwing2
    global delta
    
    with connecter:
        c.execute("""SELECT * FROM product""")
        views=c.fetchall()
        for i in views:
            a=i[2]
            image_list.append(a)
        mylist = list(dict.fromkeys(image_list))
        
        if len(image_list) != delta:
            img =Image.open(image_list[delta])
            img = img.resize((500, 500), Image.ANTIALIAS)
            Deathwing2=ImageTk.PhotoImage(img)
            #label(image=Deathwing2)
            label =Label(root, image = Deathwing2)
            label.place(x=100,y=200)
            
        else:
            print('lol')

def show_image():
    global l
    global delta
    global current, image_list,label
    
    try:
        l.place_forget()
        
    except NameError:
        print(NameError)

    try:
        
        frame1.place_forget()
    except NameError:
        print(NameError)

        
    try:
        frame2.place_forget()
    except NameError:
        print(NameError)
    finally:
       
        
       
        load_image()

        back_button=Button(root, text='Previous picture', command=back)
        back_button.place(x=100,y=710)
        forward_button=Button(root, text='Next picture', command=front)
        forward_button.place(x=200,y=710)
    
def back():
    global delta
    delta=delta-1
    load_image()

def front():
    global delta
    delta=delta+1
    load_image()


        

        

    

###############main window ######################


btn2=Button(frame,text='Upload Image',font='arail 18 bold',command=uploadImage_template,bg='orange')
btn2.place(x=0,y=0)

btn3=Button(frame,text='view product',font='arail 18 bold',command=update,bg='orange')
btn3.place(x=200,y=0)

btn5=Button(frame,text='view image',font='arail 18 bold',command=show_image,bg='orange')
btn5.place(x=400,y=0)

btn6=Button(frame,text='Create order',font='arail 18 bold',command=create_order_template,bg='orange')
btn6.place(x=600,y=0)


######################################################################
#root.overrideredirect(True)
root.title('store')
root.configure(background='steelblue')
root.state('zoomed')
root.mainloop()
