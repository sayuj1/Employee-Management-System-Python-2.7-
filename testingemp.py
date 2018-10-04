from Tkinter import*
from tkMessageBox import *
import sqlite3
import time;







def employee_info():
        root=Tk()
        
        root.geometry("1366x768")
        root.resizable(0,0)
        
        root.configure(background='coral4')

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------
        first1=Frame(root,width=1600,height=65,bd=8,relief="raised")
        first1.pack(side=TOP)
        first1.configure(background='lime green')

        first=Frame(first1,width=1600,height=60,bg="red",bd=8,relief="raised")
        first.pack(side=TOP)
        first.configure(background='salmon1')


        f22=Frame(root,width=1590,height=95,relief="raised",bd=9,bg='lime green')
        f22.pack(side=BOTTOM)

        f2=Frame(f22,width=1600,height=90,relief="raised",bd=8,bg='DarkOrchid3')
        f2.pack(side=LEFT)

        


        f11=Frame(root,width=1270,height=620,relief="raised",bd=8,bg='lime green')
        f11.pack(side=LEFT)


        f1=Frame(f11,width=1270,height=610,relief="raised",bd=8,bg='brown')
        f1.pack(side=LEFT)

        f33=Frame(root,width=248,height=620,relief="raised",bd=8,bg='lime green')
        f33.pack(side=RIGHT)

        f3=Frame(f33,width=250,height=610,relief="raised",bd=8,bg='crimson')
        f3.pack(side=RIGHT)


        

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------


        localtime=time.asctime(time.localtime(time.time()))


        Label(first,font="times 30 bold underline",text="\t Employee record keeping system",fg="black",bg='crimson',bd=10,anchor='w',width=42).grid(row=0,column=1)
        Label(first,font="times 15 bold",text=localtime,fg="blue",bd=8,anchor='w').grid(row=1,column=1)
        Label(first,font="times 15 bold",text="\n  \n Welcomes \n You \n",fg="black",bg='crimson',bd=10,anchor='w').grid(row=0,column=0)
        Label(first,font="times 15 bold",text="\n  By \n Sayuj Sehgal \n 161B205 \n",bg='crimson',fg="black",bd=10,anchor='w').grid(row=0,column=2)



        Label(f1,text='Employee Code:',bd=4,width=15,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=0,column=0)
        e1=Entry(f1,width=14,font="times 20 bold",bd=8,bg='peach puff')
        e1.grid(row=0,column=1)
        Label(f1,text='First Name:',bd=4,width=15,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=1,column=0)
        e2=Entry(f1,width=14,font="times 20 bold",bd=8,bg='peach puff')
        e2.grid(row=1,column=1)
        Label(f1,text='Last Name:',bd=4,width=15,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=2,column=0)
        e3=Entry(f1,width=14,font="times 20 bold",bd=8,bg='peach puff')
        e3.grid(row=2,column=1)
        Label(f1,text='Mobile Number',bd=4,width=15,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=0,column=2)
        e8=Entry(f1,width=14,font="times 20 bold",bd=8,bg='peach puff')
        e8.grid(row=0,column=3)
        e8.insert(END,0)

        #-----------------------------------------------------Extra----------------------------------------------
        #Label(f1,text='',bd=4,width=2,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=0,column=4)
##        Label(f1,text='',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=0,column=5)
##
##        Label(f1,text='\t',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=1,column=4)
##        Label(f1,text='',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=1,column=5)
##
##        Label(f1,text='\t',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=2,column=4)
##        Label(f1,text='',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=2,column=5)
##
##        Label(f1,text='\t',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=3,column=4)
##        Label(f1,text='',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=3,column=5)
##
##        Label(f1,text='\t',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=4,column=4)
##        Label(f1,text='',bd=4,width=5,height=2,font="times 24 bold",bg='brown',anchor=W).grid(row=4,column=5)
##

        #--------------------------------Date of Joining -----------------------------------------------------------
        Label(f1,text='Date of Joining',bd=4,width=19,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=3,column=0)

        spinbox1=Spinbox(f1,from_=1,to=31,state=NORMAL,width=10,font="times 14 bold")
        spinbox1.grid(row=3,column=1)

        dateList=["Jan","Feb","Mar","Apr","May","jun","July","Aug","Sep","Oct","Nov","Dec"]
        s=StringVar()
        s.set(dateList[0])
        dMenu=OptionMenu(f1,s,*dateList)
        dMenu.config(width=15,bg='peach puff')
        dMenu.grid(row=3,column=2)

        spinbox2=Spinbox(f1,from_=1990,to=2017,state=NORMAL,width=10,font="times 18 bold")
        spinbox2.grid(row=3,column=3)

        

        #--------------------------------Date of birth----------------------------------------------------------------

        Label(f1,text='Date of Birth',bd=4,width=19,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=4,column=0)

        spinbox3=Spinbox(f1,from_=1,to=31,state=NORMAL,width=10,font="times 14 bold")
        spinbox3.grid(row=4,column=1)

        dateList=["Jan","Feb","Mar","Apr","May","jun","July","Aug","Sep","Oct","Nov","Dec"]
        ss1=StringVar()
        ss1.set(dateList[0])
        dMenu=OptionMenu(f1,ss1,*dateList)
        dMenu.config(width=15,bg='peach puff')
        dMenu.grid(row=4,column=2)

        spinbox4=Spinbox(f1,from_=1990,to=2017,state=NORMAL,width=10,font="times 18 bold")
        spinbox4.grid(row=4,column=3)


        

        #--------------------------------------------------------------------------------------------------------------
        Label(f1,text='Annual Salary',bd=4,width=15,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=2,column=2)
        e5=Entry(f1,width=14,font="times 20 bold",bd=8,bg='peach puff')
        e5.grid(row=2,column=3)
        e5.insert(END,0.0)
        Label(f1,text='Department',bd=4,width=15,height=2,font="times 18 bold",bg='brown',anchor=W).grid(row=1,column=2)
        e6=Entry(f1,width=14,font="times 20 bold",bd=8,bg='peach puff')
        e6.grid(row=1,column=3)
        


        #------------------------------------------------------------------------------------------------------------------------
        #Label(f2,text="",bd=4,width=20,height=2,font="times 24 bold",bg='DarkOrchid3').grid(row=0,column=4)
        #Label(f2,text="",bd=4,width=10,height=2,font="times 12 bold",bg='DarkOrchid3').grid(row=0,column=0)
        Label(f2,text='Enter id to fetch record: \t',bd=4,width=20,height=2,font="times 18 bold",bg='DarkOrchid3',anchor=W).grid(row=0,column=0)
        Label(f2,text="",bd=4,width=20,height=2,font="times 24 bold",bg='DarkOrchid3').grid(row=0,column=3)
        e4=Entry(f2,font="times 20 bold",width=17,bg='peach puff',bd=8)
        e4.grid(row=0,column=2)

        Label(f2,text="",bd=4,width=5,height=2,font="times 24 bold",bg='DarkOrchid3').grid(row=0,column=3)
        
        #---------------------------------------------+++++++++++++++++++++++--------------------------++++++++++++++++++++++++++++++++++++++++++++++++---------------




        def quits():
                z=askyesno("","Are u sure u want to Exit")
                if z==TRUE:
                        root.destroy()
                        return

        #------------------------------------------++++++++deletion+++++++++++++++-------------------------------------
        def clear():
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                e8.delete(0,END)
                e8.insert(END,0)
                e5.insert(END,0.0)
        #-------------------------------##################-------------------------------------------------------------
        def checkmobno():
                if e8.get()!=0:
                        a=int(e8.get())
                        m=a
                        l,r=0,0
                        while a!=0:
                                r=a%10
                                l=l+1
                                a=a/10
                                #print l
                        if(l!=10):
                                showerror("oops","Incorrect mobileno.")
                                clear()
                        elif(l==10):
                                a=m
                                k=[]
                                i,r=0,0
                                while i<10:
                                    r=a%10
                                    k.append(r)
                                    a=a/10
                                    i=i+1
                                if (k[9]<7 and k[8]<=7):
                                    showerror("oops","Incorrect mobileno.")
                                    clear()
                                else:
                                        insert()
                else:
                        showerror("oops","Enter Data")

            
               
                   
        #----------------------------------------++++++++Insertion++++++++++++++----------------------------------------
        def insert():
                employee=sqlite3.Connection('emp_info')
                cur=employee.cursor()
                
                try:
                        cur.execute('create table if not exists emp1(ecode varchar(10) primary key,fname char(15),lname char(15),mobile_no number(12) unique,dob date,doj date,Annual_Salary number(13,2),department varchar(15))')
                        

                        t1=spinbox1.get()
                        t3=spinbox2.get()
                        t2=s.get()
                           
                        e7=t1+"/"+t2+"/"+t3

                        w1=spinbox3.get()
                        w3=spinbox4.get()
                        w2=ss1.get()
                           
                        e9=w1+"/"+w2+"/"+w3



                        
                        t=(e1.get(),e2.get(),e3.get(),e8.get(),e9,e7,float(e5.get()),e6.get())
        
                        cur.execute("insert into emp1 values(?,?,?,?,?,?,?,?)",t)
                        showinfo("","Insertion Successful")
                except:
                        showerror(" ","Enter valid info")
                employee.commit()
                clear()
                cur.fetchall()     

        #-----------------------------------------++++++Show++++++++++--------------------------------------------------                
        def show():
                employee=sqlite3.Connection('emp_info')
                cur=employee.cursor()
                cur.execute("select * from emp1 where ecode=?",(e4.get(),))
                if(e4.get()!=""):
                        showinfo("Retrieved Data",cur.fetchall())
                        showinfo("Retrieved Data","Data Retrieved Successfully")
                else:
                        showerror("Error","Incorrect Data")
                        
                
                e4.delete(0,END)
                #e4.insert(END,0)
        #-----------------------------------------Show all--------------------------------------------------------------
        def showall():
        ##        root1=Tk()
        ##        root1.geometry("1600x850+0+0")
        ##        root1.configure(background='sienna3')


                root1=Tk()
                root1.geometry("1600x850")
                root1.resizable(0,0)
                root1.configure(background="sienna3")

                frame11=Frame(root1,width=7900,height=65,bd=5,bg='firebrick4')
                frame11.pack()

                frame1=Frame(frame11,width=800,height=70,bd=8,bg="Crimson")
                frame1.pack()

                frame3=Frame(root1,width=1600,height=20,bg='sienna3')
                frame3.pack()

                frame2=Frame(root1,width=1600,height=740,bg="sienna3")
                frame2.pack()

                

                Label(frame1,text="All Employee Data Information",relief="raised",bg='coral1',fg='brown4',font="times 45 bold underline").grid(row=0)





                employee=sqlite3.Connection('emp_info')
                cur=employee.cursor()
                cur.execute("Select ecode from emp1",)
                a=[]
                a=cur.fetchall()
                b=[]
                cur.execute("Select fname from emp1",)
                b=cur.fetchall()
                c=[]
                cur.execute("Select lname from emp1",)
                c=cur.fetchall()
                d=[]
                cur.execute("Select mobile_no from emp1",)
                d=cur.fetchall()
                e=[]
                cur.execute("Select dob from emp1",)
                e=cur.fetchall()
                f=[]
                cur.execute("Select doj from emp1",)
                f=cur.fetchall()
                g=[]
                cur.execute("Select Annual_Salary from emp1",)
                g=cur.fetchall()
                w=[]
                cur.execute("Select department from emp1",)
                w=cur.fetchall()

                Label(frame2,text="Employee ID",fg='black',font='Arial 15 bold',relief="groove",bg='firebrick2',width=17,height=2,bd=8).grid(row=0,column=0)
                Label(frame2,text="Employee Name",fg='black',font='Arial 15 bold',relief="groove",bg='firebrick2',bd=8,width=17,height=2).grid(row=0,column=1)
                Label(frame2,text="Mobile No.",fg='black',font='Arial 15 bold',relief="groove",bg='firebrick2',bd=8,width=17,height=2).grid(row=0,column=2)
                Label(frame2,text="Date of birth",fg='black',font='Arial 15 bold',relief="groove",bg='firebrick2',bd=8,width=17,height=2).grid(row=0,column=3)
                Label(frame2,text="Date of Joining",fg='black',font='Arial 15 bold',relief="groove",bg='firebrick2',bd=8,width=17,height=2).grid(row=0,column=4)
                Label(frame2,text="Annual Salary",fg='black',font='Arial 15 bold',relief="groove",bg='firebrick2',bd=8,width=17,height=2).grid(row=0,column=5)
                Label(frame2,text="Department",fg='black',font='Arial 15 bold',relief="groove",bg='firebrick2',bd=8,width=17,height=2).grid(row=0,column=6)
                i,l,k=0,1,0
                for value in a:
                        Label(frame2,text=a[i],fg='black',font='Arial 15 bold',relief="ridge",bd=8,bg='sienna1',width=17,height=2).grid(row=l,column=k)
                        i=i+1
                        l=l+1
                i,l,k=0,1,0
                for value in b and c:
                        Label(frame2,text=b[i]+c[i],fg='black',font='Arial 15 bold',relief="ridge",bd=8,bg='sienna1',width=17,height=2).grid(row=l,column=k+1)
                        i=i+1
                        l=l+1
                i,l,k=0,1,1
                for value in d:
                        Label(frame2,text=d[i],fg='black',font='Arial 15 bold',relief="ridge",bd=8,bg='sienna1',width=17,height=2).grid(row=l,column=k+1)
                        i=i+1
                        l=l+1
                i,l,k=0,1,2
                for value in e:
                        Label(frame2,text=e[i],fg='black',font='Arial 15 bold',relief="ridge",bd=8,bg='sienna1',width=17,height=2).grid(row=l,column=k+1)
                        i=i+1
                        l=l+1
                i,l,k=0,1,3
                for value in f:
                        Label(frame2,text=f[i],fg='black',font='Arial 15 bold',relief="ridge",bd=8,bg='sienna1',width=17,height=2).grid(row=l,column=k+1)
                        i=i+1
                        l=l+1
                i,l,k=0,1,4
                for value in g:
                        Label(frame2,text=g[i],fg='black',font='Arial 15 bold',relief="ridge",bd=8,bg='sienna1',width=17,height=2).grid(row=l,column=k+1)
                        i=i+1
                        l=l+1
                i,l,k=0,1,5
                for value in w:
                        Label(frame2,text=w[i],fg='black',font='Arial 15 bold',relief="ridge",bd=8,bg='sienna1',width=17,height=2).grid(row=l,column=k+1)
                        i=i+1
                        l=l+1
                frame4=Frame(root1,width=1600,height=50,bg='sienna3')
                frame4.pack()

                frame55=Frame(root1,width=1600,height=50,bg='brown',bd=6)
                frame55.pack()
                
                frame5=Frame(frame55,width=500,height=40,bg='crimson',bd=6)
                frame5.pack()
                Button(frame5,text="Click to go back",command=root1.destroy,fg='black',font='Arial 15 bold',width=15,height=2,relief="raised",bg="lime green",bd=4,activebackground='tomato2').grid(row=0,column=3)
                root1.mainloop()
                
        ##        cur.execute("select * from emp1",)
        ##        a=[]
        ##        a=cur.fetchall()
        ##        i=0
        ##        j=7
        ##        k=1
        ##        for i in a:
        ##                Label(root,text=i).grid(row=j,column=k)
        ##                j=j+1
        ##                
                
                

        Label(f3,text="",bd=4,width=13,height=1,font="times 18 bold",bg='brown').grid(row=0)
        Label(f3,text="",bd=4,width=13,height=1,font="times 18 bold",bg='brown').grid(row=1)
        Button(f3,text='Insert',command=checkmobno,font="times 18 bold",activebackground="SpringGreen2",bg='coral2',bd=4,width=13,height=1,relief='raised').grid(row=2)
        Button(f3,text='showall',command=showall,font="times 18 bold",activebackground="SpringGreen2",bg='coral2',width=13,height=1,bd=4,relief='raised').grid(row=4)
        Button(f3,text='Reset',command=clear,font="times 18 bold",activebackground="SpringGreen2",bg='coral2',width=13,height=1,bd=4,relief='raised').grid(row=3)

        Label(f3,text="",bd=4,width=13,height=1,font="times 18 bold",bg='brown').grid(row=6)
        Label(f3,text="",bd=4,width=13,height=2,font="times 18 bold",bg='brown').grid(row=7)

        Button(f2,text='show',command=show,font="times 18 bold",activebackground="SpringGreen2",bg='coral2',width=10,bd=4,relief='raised').grid(row=0,column=3)
        Button(f2,text='Exit',command=quits,font="times 18 bold",activebackground="SpringGreen2",bg='coral2',width=10,bd=4,relief='raised').grid(row=0,column=4)


        root.mainloop()
#employee_info()



#-----------------------------------------------First Screen -------------------------------------------------------------------------------------------------------------------------------
root11=Tk()#main root window for details
root11.geometry("1366x768+0+0")
root11.configure(background='DarkOrange4')
root11.resizable(0,0)


def quity(Motion):
     root11.destroy()
     employee_info()
   


    
f=Frame(root11,width=1200,height=150,bg="black",relief="sunken",bd=10)#bottom frame on first page for image
f.pack(side=TOP)
f.configure(background='black')

f4=Frame(root11,height=25,width=1600,bg='DarkOrange4')
f4.pack(side=TOP)

ff=Frame(root11,width=1200,height=750,bg="black",relief="sunken",bd=10)#top frame on bottom frame for image
ff.pack()
ff.configure(background='red4')

f3=Frame(root11,width=1380,height=30,bg='darkorange4')
f3.pack()

f2=Frame(root11,width=1200,height=100,bg="black",relief="sunken",bd=10) #bottom frame for details  
f2.pack()
f2.configure(background='red4')



ff1=Frame(ff,width=1200,height=500,bg="black",relief="sunken",bd=10)#top frame for details
ff1.pack()
ff1.configure(background='red4')



Label(ff1,text="NAME     ",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=23,height=2).grid(row=1,column=0)
Label(ff1,text="SAYUJ SEHGAL",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=25,height=2).grid(row=1,column=3)
Label(ff1,text="Enrollmentno.",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=23,height=2).grid(row=2,column=0)
Label(ff1,text="161B205",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=25,height=2).grid(row=2,column=3)
Label(ff1,text="COURSE",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=23,height=2).grid(row=3,column=0)
Label(ff1,text="B.TECH.",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=25,height=2).grid(row=3,column=3)
Label(ff1,text="BRANCH ",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=23,height=2).grid(row=4,column=0)
Label(ff1,text="CSE  ",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=25,height=2).grid(row=4,column=3)
Label(ff1,text="BATCH  ",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=23,height=2).grid(row=5,column=0)
Label(ff1,text="B7 (BZ) ",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=25,height=2).grid(row=5,column=3)
Label(ff1,text="email-id ",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=23,height=2).grid(row=6,column=0)
Label(ff1,text="sayujsehgal@iprakash.com",fg='black',font='Arial 20 bold',relief="raised",bg='brown3',anchor=W,borderwidth=4,width=25,height=2).grid(row=6,column=3)



l1=Label(f2,text="         Move cursor over here to proceed to mainpage",fg='black',font='Arial 15 bold',relief="raised",bg='darkkhaki',anchor=W,borderwidth=4,width=50,height=2)
l1.grid(row=0)



a=PhotoImage(file='Header.gif')#to get header image on first page
l=Label(f,image=a)
l1.bind('<Motion>',quity)# splash screen to distroy the first page when mouse is moved over the image
l.grid()
root11.mainloop()

