from tkinter import*
from tkinter import messagebox
from functools import partial
import dbase as dbs
import datetime
import employee as emp
getemplist=emp.allemployee()
empdc={}
for val in getemplist:
    empdc.update({val[1]:val[0]})
#print(empdc)
def viewAttendence():
    dbs.cur.execute('select *from attendance')
    data=dbs.cur.fetchall()
    attendencedc={}
    def showAttendence(event):
        getdt=datelist.get(datelist.curselection())
        emplist.delete(0,END)
        getpresent=attendencedc[getdt].split(',')
        getpresent.pop()
        for val in empdc:
            nam=''
            if str(empdc[val]) in getpresent:
                nam=val+"(P)"
            else:
                nam=val+"(A)"
            emplist.insert(END,nam)
    rptview=Tk()
    rptview.geometry('366x268+500+250')
    rptview.title('Mark attendence')
    rptview.resizable(0,0)
    
    frame1=Frame(rptview,bd=1,relief=SUNKEN,width=150)
    frame1.pack(side=LEFT,fill=Y)
    lbl=Label(frame1,text='select a date',font='arial 10 bold',bg='black',fg='white')
    lbl.pack(side=TOP,fill=X)
    datelist=Listbox(frame1)
    vscroll1=Scrollbar(frame1,orient=VERTICAL,command=datelist.yview)
    vscroll1.pack(side=RIGHT,fill=Y)
    for val in data:
        datelist.insert(END,val[1])
        attendencedc.update({val[1]:val[2]})
    datelist.pack(side=LEFT,fill=Y)
    datelist.config(yscrollcommand=vscroll1.set)
    datelist.bind('<<ListboxSelect>>',showAttendence)

    frame2=Frame(rptview,bd=1,relief=SUNKEN,width=216)
    frame2.pack(side=RIGHT,fill=Y)
    emplist=Listbox(frame2)
    vscroll2=Scrollbar(frame2,orient=VERTICAL,command=datelist.yview)
    vscroll2.pack(side=RIGHT,fill=Y)
    emplist.pack(side=LEFT,fill=Y)
    emplist.config(yscrollcommand=vscroll2.set)
    rptview.mainloop()
#viewAttendence()
def createEmployeelist():
    def markAttendence():
        p=''
        for v in varlist:
            p+=str(v.get())+','
        d=datetime.datetime.today().strftime("%d-%m-%y")
        dbs.cur.execute("insert into attendance(adate,eid)values('"+str(d)+"','"+p+"')")
        dbs.db.commit()
        messagebox.showinfo('success','attendence marked')
    atnview=Tk()
    atnview.geometry('366x268+500+250')
    atnview.title('Mark attendence')
    atnview.resizable(0,0)
    
    mainframe=Frame(atnview,width=300,height=200)
    mainframe.pack(fill=BOTH)
    datacanvas=Canvas(mainframe)
    subframe=Frame(datacanvas)
    subframe.pack(fill=BOTH)
    vscrollbar=Scrollbar(mainframe,orient='vertical',command=datacanvas.yview)
    vscrollbar.pack(side=RIGHT,fill=Y)
    hscrollbar=Scrollbar(mainframe,orient='horizontal',command=datacanvas.xview)
    hscrollbar.pack(side=BOTTOM,fill=X)
    datacanvas.pack(side=LEFT)
    datacanvas.configure(yscrollcommand=vscrollbar.set)
    datacanvas.configure(xscrollcommand=hscrollbar.set)
    def myfunction(event):
        datacanvas.configure(scrollregion=datacanvas.bbox('all'),width=340,height=200)
    datacanvas.create_window((0,0),window=subframe,anchor='nw')
    subframe.bind('<Configure>',myfunction)
    
    lbl=Label(subframe,text='Sr',font='calibri 11 bold')
    lbl.grid(row=0,column=0,padx=5,pady=5)
    lbl=Label(subframe,text='Name',font='calibri 11 bold')
    lbl.grid(row=0,column=1,padx=5,pady=5)
    lbl=Label(subframe,text='Profile',font='calibri 11 bold')
    lbl.grid(row=0,column=2,padx=5,pady=5)
    r=1
    varlist=[]
    for val in empdc:
        var='sts__'+str(r)
        var=IntVar(atnview)
        varlist.append(var)
        lbl=Label(subframe,text=r)
        lbl.grid(row=r,column=0)

        lbl=Label(subframe,text=val)
        lbl.grid(row=r,column=1,sticky=W,padx=5,pady=5)

        chk=Checkbutton(subframe,onvalue=empdc[val],offvalue=0,variable=var)
        chk.grid(row=r,column=2,sticky=W,padx=5,pady=5)
        
        r+=1
    btn=Button(subframe,text='submit',font='arial 11 bold',command=markAttendence)
    btn.grid(row=3,column=2,sticky=E,padx=5,pady=5)
#createEmployeelist()
