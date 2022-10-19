from faulthandler import disable
from logging import PlaceHolder
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

class crud:
    def __init__(self, root):
        self.root = root
        self.root.title("Just Crud")
        self.root.geometry("1000x520+200+50")
        self.root.resizable(False, False)
        self.root.config(bg="gray")

        # variables
        self.book_id_var = StringVar()
        self.book_name_var = StringVar()
        self.book_author_var = StringVar()
        self.book_category_var = StringVar()

        # labels & Fields
        # ---- id ----
        self.book_id = Label(self.root, 
        text="Book Id", 
        font=("comic sans serif", 15, 'bold'),
        bg="gray",
        fg="purple").place(x=10, y=60)
        self.book_id_field = Entry(self.root, 
        textvariable=self.book_id_var, 
        font=("comic sans serif", 10, 'bold'), 
        bg="white",
        fg="black")
        self.book_id_field.place(x=150, y=65)

        # ---- name ----
        self.book_name = Label(self.root,
        text="Book Name",
        font=("comic sans serif", 15, 'bold'),
        bg="gray",
        fg="purple").place(x=10, y=100)
        self.book_name_field = Entry(self.root,
        textvariable=self.book_name_var,
        font=("comic sans serif", 10, 'bold'), 
        bg="white",
        fg="black")
        self.book_name_field.place(x=150, y=105)

        self.book_author = Label(self.root,
        text="Book Author",
        font=("comic sans serif", 15, 'bold'),
        bg="gray",
        fg="purple").place(x=10, y=140)
        self.book_author_field = Entry(self.root,
        textvariable=self.book_author_var,
        font=("comic sans serif", 10, 'bold'), 
        bg="white",
        fg="black")
        self.book_author_field.place(x=150, y=145)

        self.book_category = Label(self.root,
        text="category",
        font=("comic sans serif", 15, 'bold'),
        bg="gray",
        fg="purple").place(x=10, y=180)
        self.book_category_field = ttk.Combobox(self.root,
        values =['choose category', 'Science', 'History', 'Religion'],
        textvariable=self.book_category_var,)
        self.book_category_field.place(x=150, y=185)
        self.book_category_field.current(0)


        # buttons
        # ----add----
        self.add_btn = Button(self.root,
        text="Add", 
        font=("comic sans serif", 11, 'bold'),
        bg="#3CCF4E",
        fg="white", 
        cursor="hand2", command=self.add_data).place(x=560,y=50, width=100, height=40)
        # ----Update----
        self.update_btn = Button(self.root,
        text="Update", 
        font=("comic sans serif", 11, 'bold'),
        bg="#FEB139",
        fg="white", 
        cursor="hand2", command=self.update_data).place(x=690,y=50, width=100, height=40)
        # ----Delete----
        self.delete_btn = Button(self.root,
        text="Delete", 
        font=("comic sans serif", 11, 'bold'),
        bg="#EB1D36",
        fg="white", 
        cursor="hand2", command=self.delete).place(x=560,y=100, width=100, height=40)
        # ----Clear----
        self.clear_btn = Button(self.root,
        text="Clear", 
        font=("comic sans serif", 11, 'bold'),
        bg="#607EAA",
        fg="white", 
        cursor="hand2", 
        command=self.clear_data).place(x=690,y=100, width=100, height=40)
          
       # tableau
        self.table = ttk.Treeview(self.root, columns=(1,2,3,4), height=5, show="headings")
        self.table.place(x = 100, y = 230, width=800, height=100)
        self.table.heading(1, text = "Id")
        self.table.heading(2, text = "Title")
        self.table.heading(3, text = "Author")
        self.table.heading(4, text = "Category")
        # self.table.column(1, width=70)
        # self.table.column(1, width=70)
        # self.table.column(1, width=70)
        # self.table.column(1, width=70)
        self.table.bind("<ButtonRelease-1>",self.get_data)
        self.show_data()
    def show_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="library")
        cur = con.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('', END, values=row)
        con.commit()
        con.close()
    def clear_data(self):
        self.book_id_field.delete(0,END)
        self.book_name_field.delete(0,END)
        self.book_author_field.delete(0,END)
        self.book_category_field.current(0)
    
    def add_data(self):
        con = pymysql.connect(host="localhost",user="root",password='',database="library")
        cur = con.cursor()
        cur.execute("INSERT INTO books VALUES (%s,%s,%s,%s)", (self.book_id_var.get(), self.book_name_var.get(), self.book_author_var.get(), self.book_category_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success","row inserted successfully",parent=self.root)
        self.show_data()
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database='library')
        cur = con.cursor()
        cur.execute("update books set name=%s,author=%s,category=%s where id=%s", (   
            self.book_name_var.get(),
            self.book_author_var.get(),
            self.book_category_var.get(),
            self.book_id_var.get()
        ))
        con.commit()
        con.close()
        messagebox.showinfo("data entry","row updated successfully",parent=self.root)
        # self.book_id_field.config(state="enabled")
        self.show_data()
    def get_data(self, ev):
        #self.txt_courseName.config(state="")
        #self.cne_enter
        vinfo = self.table.focus()
        content = self.table.item(vinfo)
        row = content["values"]
        print(row)
        self.book_id_var.set(row[0])
        self.book_name_var.set(row[1])
        self.book_author_var.set(row[2])
        self.book_category_var.set(row[3])
        # self.book_id_field.config(state="disabled")
    def delete(self):
        con=pymysql.connect(host="localhost",user="root",password="",database='library')
        cur = con.cursor()
        try:
            if self.book_id_var.get() == "":
                messagebox.showerror("Error","Tous les champs sont requis",parent=self.root)
            else:
                cur.execute("select * from books where id = %s",self.book_id_var.get())
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","select a book tht exists in the list ",parent=self.root)
                else:
                    op = messagebox.askyesno("confirm","are you sure ?",parent=self.root)
                    if op == True:
                        cur.execute("delete from books where id = %s",self.book_id_var.get())
                        con.commit()
                        messagebox.showinfo("delete","book deleted successfully",parent=self.root)
                        self.show_data()
        except Exception as ex:
            messagebox.showerror("Error",f"Error du to {str(ex)}")

root = Tk()
obj=crud(root)
root.mainloop()