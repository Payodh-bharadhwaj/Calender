from tkinter import *
import calendar
from _datetime import datetime
dt=datetime.now()
year=dt.year
mon=dt.month
present_month=calendar.month(year,mon)
# new_g= Label(text=f"{present_month}")
# new_g.grid(row=0, column=0)
def previous():
    global mon,year
    if mon==1:
        mon=12
        prev=calendar.month(year-1,mon)
        new_gui = Label(text=f"{prev}",font=("Ariel",18,"bold"))
        new_gui.grid(row=0, column=0)
        year=year-1
    else:
        prev=calendar.month(year,mon-1)
        new_gui = Label(text=f"{prev}",font=("Ariel",18,"bold"))
        new_gui.grid(row=0, column=0)
        mon = mon - 1

def next():
    global present_month, mon, year
    if mon == 12:
        mon = 1
        prev = calendar.month(year + 1, mon)
        new_gui = Label(text=f"{prev}",font=("Ariel",18,"bold"))
        new_gui.grid(row=0, column=0)
        year=year+1
    else:
        prev = calendar.month(year, mon + 1)
        new_gui = Label(text=f"{prev}",font=("Ariel",18,"bold"))
        new_gui.grid(row=0, column=0)
        mon = mon + 1

def month():
    global mon,year
    year=int(year_entry.get())
    mon=int(month_entry.get())
    # calendar.month(year,mon)
    new_gui = Label(text=f"{calendar.month(year,mon)}",font=("Ariel",18,"bold"))
    new_gui.grid(row=0, column=0)

window=Tk()
window.title("Calendar")
# window.config(pady=50, padx=50)
new_g= Label(text=f"{present_month}",font=("Ariel",18,"bold"))
new_g.grid(row=0, column=0)
canvas=Canvas(width=200,height=200)
canvas.grid(row=0,column=1)
#buttons
next=Button(text="Next",width=10,command=next,background="#98F5FF")
next.grid(row=6,column=3)

prev=Button(text="Prev",width=10,command=previous,background="#98F5FF")
prev.grid(row=6,column=0)
#labels
ques_lable=Label(text="Enter the year and month?")
ques_lable.grid(row=1,column=1)

show=Button(text="Show",command=month,background="#98F5FF")
show.grid(row=6,column=2,columnspan=1)
# titl_label=Label(text="Calender",font=("Ariel",20,"bold"))
# titl_label.grid(row=0,column=1)
#entry
year_entry=Entry(width=10)
year_entry.grid(row=5, column=1,columnspan=2)
month_entry=Entry(width=10)
month_entry.grid(row=6,column=1)

window.mainloop()