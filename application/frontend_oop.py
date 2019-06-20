import tkinter
from backend_oop import Connector

database = Connector("books.db")

class Button_funcs:
    
    def get_selected_row(self,event):
        global selected_tuple
        index=list1.curselection()
        selected_tuple = list1.get(index)
        e1.delete(0,tkinter.END)
        e1.insert(tkinter.END,selected_tuple[1])
        e2.delete(0,tkinter.END)
        e2.insert(tkinter.END,selected_tuple[2])
        e3.delete(0,tkinter.END)
        e3.insert(tkinter.END,selected_tuple[3])
        e4.delete(0,tkinter.END)
        e4.insert(tkinter.END,selected_tuple[4])

    def view_command(self):
        list1.delete(0,tkinter.END)
        for row in database.view():
            list1.insert(tkinter.END,row) 

    def search_command(self):
        list1.delete(0,tkinter.END)
        for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
            list1.insert(tkinter.END,row)

    def add_command(self):
        database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list1.delete(0,tkinter.END)
        list1.insert(tkinter.END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

    def update_command(self):
        database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        self.view_command()

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.view_command()

button_funcs = Button_funcs()

window=tkinter.Tk()
window.wm_title("Book Store")

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

# Get the values for a selected row in the UI
list1.bind('<<ListboxSelect>>',button_funcs.get_selected_row)

button_1=tkinter.Button(window,text="View all",width=12,command=button_funcs.view_command)
button_1.grid(row=2,column=3)

button_2=tkinter.Button(window,text="Search entry",width=12,command=button_funcs.search_command)
button_2.grid(row=3,column=3)

button_3=tkinter.Button(window,text="Add entry",width=12,command=button_funcs.add_command)
button_3.grid(row=4,column=3)

button_4=tkinter.Button(window,text="Update selected",width=12,command=button_funcs.update_command)
button_4.grid(row=5,column=3)

button_5=tkinter.Button(window,text="Delete selected",width=12,command=button_funcs.delete_command)
button_5.grid(row=6,column=3)

button_6=tkinter.Button(window,text="Close",width=12,command=window.destroy)
button_6.grid(row=7,column=3)

window.mainloop()