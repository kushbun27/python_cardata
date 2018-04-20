from tkinter import *
import tkinter
top=tkinter.Tk()
count=0

cid=StringVar()
cname=StringVar()
price=StringVar()
color=StringVar()
eng_cc=StringVar()

def Add_car():
    f=open('cardata.txt','a')
    cid=E1.get()
    cname=E2.get()
    price=E3.get()
    color=E4.get()
    eng_cc=E5.get()
    if(cid=='' or cname=='' or  price=='' or color=='' or eng_cc==''):
        print("Details can't be empty!")
        exit()
    f.writelines(cid.ljust(20)+cname.ljust(20)+price.ljust(20)+color.ljust(20)+eng_cc.ljust(3)+"\n")
    print("Record added to file!")
    f.close()

def delete_car():
    k=cid.get()
    f=open('cardata.txt','r')
    n_line=0
    for line in f:
        n_line=n_line+1
    print("No. of lines in file:")
    print(n_line)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    f.close()
    f=open('cardata.txt','w')
    for ve in lines: 
        j=ve.split()
        print(j)
        if(j[0]!=k): 
             f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n")
    f.close()
    
def search_car():
    k=cid.get()
    f=open('cardata.txt','r')
    n_line=0
    flag=0
    for line in f:
        n_line=n_line+1
    print("No. of lines in file:")
    print(n_line)
    f.seek(0)
    lines=f.readlines()
    print(lines)
    for book in lines: 
        j=book.split() 
        if(j[0]==k):   
            print(j) 
            cid.set(j[0]) 
            cname.set(j[1]) 
            price.set(j[2]) 
            color.set(j[3]) 
            eng_cc.set(j[4])
            flag=1
            break
    if(flag==0):
        print("Record not found!")
    else:
        print("Record found!")
    f.close()

def update():
    new_cid=cid.get() 
    new_cname=cname.get() 
    new_price=price.get() 
    new_color=color.get() 
    new_eng_cc=eng_cc.get() 
    f=open('cardata.txt','r')
    n_line=0
    for line in f:
        n_line=n_line+1
    print("No. of lines in file:")
    print(n_line)
    f.seek(0)
    lines=f.readlines() 
    f.close() 
    f=open('cardata.txt','w') 
    for vec in lines: 
        j=vec.split() 
        if(j[0]!=new_cid): 
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(3)+"\n")     
        else:
            f.writelines(j[0].ljust(20)+new_cname.ljust(20)+new_price.ljust(20)+new_color.ljust(20)+new_eng_cc.ljust(3)+"\n")
    print("Record updated!!")        
    f.close()        

def first_row():
    global count
    count=1
    f=open('cardata.txt','r')
    n_line=0
    flag=0
    for line in f:
        n_line=n_line+1
    print("No. of lines in file:")
    print(n_line)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print("\n")
    print(l)
    j=l[0].split()
    cid.set(j[0])
    cname.set(j[1]) 
    price.set(j[2]) 
    color.set(j[3]) 
    eng_cc.set(j[4])
    print("\n First Record of file is as:")
    print(l[0])
    f.close()
    
 
def last_row():
    f=open('cardata.txt','r')
    n_line=0
    flag=0
    for line in f:
        n_line=n_line+1
    print("No. of lines in file:")    
    print(n_line)
    f.seek(0)
    lines=f.readlines()
    l=list(lines)
    print(l)
    j=l[n_line-1].split()
    cid.set(j[0])
    cname.set(j[1]) 
    price.set(j[2]) 
    color.set(j[3]) 
    eng_cc.set(j[4])
    print("\n Last Record of file is as:")
    print(l[n_line-1])
    f.close()
    global count
    count=n_line-1


def next():

    global count 
    i=0
    n_line=0
    f=open('cardata.txt','r')
    for line in f:
        n_line=n_line+1
    print("No. of lines in file:")    
    print(n_line)
    f.seek(0)
    try: 
        while(i<=count): 
            l=f.readline() 
            i=i+1 
        m=l.split() 
        cid.set(m[0]) 
        cname.set(m[1]) 
        price.set(m[2]) 
        color.set(m[3]) 
        eng_cc.set(m[4]) 
        print(m)
    except:
        cid.set("") 
        cname.set("") 
        price.set("") 
        color.set("") 
        eng_cc.set("")
        print("Sorry, no more records!")
    count=count+1 
    f.close()

def previous():
    global count 
    i=0
    n_line=0
    f=open('cardata.txt','r')
    for line in f:
        n_line=n_line+1
    print("No. of lines in file:")    
    print(n_line)
    f.seek(0)
    try: 
        while(i<=count-1): 
            l=f.readline() 
            i=i+1 
        m=l.split() 
        cid.set(m[0]) 
        cname.set(m[1]) 
        price.set(m[2]) 
        color.set(m[3]) 
        eng_cc.set(m[4]) 
        print(m)
    except:
        cid.set("") 
        cname.set("") 
        price.set("") 
        color.set("") 
        eng_cc.set("")
        print("Sorry, no more records!")
    count=count-1 
    f.close()
    
tkinter.Label(top, text="CAR ID",font=('monotype corsiva',15,'bold'),bg="aqua").grid(row=0)
tkinter.Label(top, text="CAR NAME:",font=('monotype corsiva',15,'bold'),bg="aqua").grid(row=1)
tkinter.Label(top, text="Price:",font=('monotype corsiva',15,'bold'),bg="aqua").grid(row=2)
tkinter.Label(top, text="CAR COLOR:",font=('monotype corsiva',15,'bold'),bg="aqua").grid(row=3)
tkinter.Label(top, text="CAR eng_cc:",font=('monotype corsiva',15,'bold'),bg="aqua").grid(row=4)
E1 = tkinter.Entry(top,textvariable=cid)
E2 = tkinter.Entry(top,textvariable=cname)
E3 = tkinter.Entry(top,textvariable=price)
E4 = tkinter.Entry(top,textvariable=color)
E5 = tkinter.Entry(top,textvariable=eng_cc)
E1.grid(row=0, column=1)
E2.grid(row=1, column=1)
E3.grid(row=2, column=1)
E4.grid(row=3, column=1)
E5.grid(row=4, column=1)

fr=tkinter.Button(top,text="First entry",width=20,bg="green",font=('monotype corsiva',15,'bold'),command=first_row).grid(row=6, column=0)
pr=tkinter.Button(top,text="Previous",width=20,bg="greenyellow",font=('monotype corsiva',15,'bold'),command=previous).grid(row=7, column=0)
nr=tkinter.Button(top,text="Next",width=20,bg="greenyellow",font=('monotype corsiva',15,'bold'),command=next).grid(row=8, column=0)
lr=tkinter.Button(top,text="Last entry",width=20,bg="green",font=('monotype corsiva',15,'bold'),command=last_row).grid(row=9, column=0)

rb=tkinter.Button(top,text="ADD",width=20,bg="green",font=('monotype corsiva',15,'bold'),command=Add_car).grid(row=6, column=3)
db=tkinter.Button(top,text="DELETE",width=20,bg="greenyellow",font=('monotype corsiva',15,'bold'),command=delete_car).grid(row=7, column=3)
sb=tkinter.Button(top,text="SEARCH",width=20,bg="greenyellow",font=('monotype corsiva',15,'bold'),command=search_car).grid(row=8, column=3)
ub=tkinter.Button(top,text="UPDATE",width=20,bg="green",font=('monotype corsiva',15,'bold'),command=update).grid(row=9, column=3)
ub=tkinter.Button(top,text="CLOSE WINDOW",width=20,bg="red",font=('monotype corsiva',15,'bold'),command=top.destroy).grid(row=10, column=1,columnspan = 1)

top.configure(bg="aqua")
top.mainloop()
