import tkinter
import backend

link = backend.Connector("books.db")

def view_command():
    list1.delete(0,tkinter.END)
    for row in link.view():
        list1.insert(tkinter.END,row) 

def search_command():
    list1.delete(0,tkinter.END)
    for row in link.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(tkinter.END,row)

def add_command():
    link.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,tkinter.END)
    list1.insert(tkinter.END,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def update_command():
    pass

def delete_command():
    pass

def close_command():
    pass


window=tkinter.Tk()

l1=tkinter.Label(window,text="Title")
l1.grid(row=0,column=0)

l2=tkinter.Label(window,text="Author")
l2.grid(row=0,column=2)

l3=tkinter.Label(window,text="Year")
l3.grid(row=1,column=0)

l4=tkinter.Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text = tkinter.StringVar()
e1=tkinter.Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = tkinter.StringVar()
e2=tkinter.Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = tkinter.StringVar()
e3=tkinter.Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = tkinter.StringVar()
e4=tkinter.Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1 = tkinter.Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll_bar_1 = tkinter.Scrollbar(window)
scroll_bar_1.grid(row=2,column=2)
list1.configure(yscrollcommand=scroll_bar_1.set)
scroll_bar_1.configure(command=list1.yview)

button_1=tkinter.Button(window,text="View all",width=12,command=view_command)
button_1.grid(row=2,column=3)

button_2=tkinter.Button(window,text="Search entry",width=12,command=search_command)
button_2.grid(row=3,column=3)

button_3=tkinter.Button(window,text="Add entry",width=12,command=add_command)
button_3.grid(row=4,column=3)

button_4=tkinter.Button(window,text="Update",width=12,command=update_command)
button_4.grid(row=5,column=3)

button_5=tkinter.Button(window,text="Delete",width=12,command=delete_command)
button_5.grid(row=6,column=3)

button_6=tkinter.Button(window,text="Close",width=12,command=close_command)
button_6.grid(row=7,column=3)




window.mainloop()

