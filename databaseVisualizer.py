import mysql.connector
import tkinter  as tk 
from tkinter import ttk
from tkinter import * 
from tkinter.messagebox import showinfo 
root = Tk()
root.geometry("550x650") 
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="",
  database="classData"
)

ID = StringVar()
Name = StringVar()
Class = StringVar()
Grade = StringVar()
Gender = StringVar()
delete_id = StringVar()
update_id = StringVar()
update_val = StringVar()
dropdown_str = StringVar()
style = ttk.Style()
style.theme_use("default")
frame = Frame(root)
scroll = Scrollbar(frame)
def show():
    frame.forget()
    scroll.forget()
    frame.pack(side = 'left')
   
    scroll.pack(side = RIGHT, fill = Y)
    tree = ttk.Treeview(frame, show = 'headings',height = 400, 
                        yscrollcommand = scroll.set)
    tree.pack()
    scroll.config(command = tree.yview)
    my_conn = my_connect.cursor()
    ####### end of connection ####
    my_conn.execute("SELECT * FROM student")
    column_names = [i[0] for i in my_conn.description]
    tree['columns'] = column_names
    tree.tag_configure('oddrow', foreground = "green")
    tree.tag_configure('oddrow' , background='orange')
    tree.tag_configure('evenrow', background='purple')
    for k in range(len(column_names)):
        tree.column(column_names[k], width = 55)
        tree.heading(column_names[k], text = column_names[k])
        # e = Entry(root,width = 10, fg = 'blue')
        # e.grid(row = i, column = k)
        # e.insert(END,column_names[k])
    for student in my_conn: 
        grade = ""
        if student[3] >= 60: grade = 'pass'
        else: grade = 'fail'
        current_row = []
        for j in range(len(student)):
            current_row.append(student[j])
            # label = tk.Label(text_area, text=student[j], 
            #              borderwidth=0, width=10)
            # label.grid(row=i+1, column=j, sticky="nsew", padx=1, pady=1)
            # current_row.append(label)
            # e = Entry(root, width=10, fg='blue',background = color) 
            # e.grid(row=i+1, column=j) 
            # e.insert(END, student[j])
            
        tree.insert("",'end', values = current_row, tags = ('oddrow',))
def insert(): 
    try:
        cursor = my_connect.cursor()
        i_id = int(ID.get())
        i_name = Name.get()
        i_class = Class.get()
        i_grade = int( Grade.get())
        i_gender = Gender.get()
        sql = "INSERT into student(id,name,class,mark,gender) values (%s,%s,%s,%s,%s)"
        val = (i_id,i_name,i_class,i_grade,i_gender)
        cursor.execute(sql,val)
        my_connect.commit()
    except:
        showinfo(
            title = 'Input Alert',
            message="Please provide inputs or type a number for ID and grade" 
            )

def delete():
    d_id = int(delete_id.get())
    cursor = my_connect.cursor()
    sql = "DELETE FROM student WHERE id = %s"
    val = (d_id,)
    cursor.execute(sql,val)
    my_connect.commit()
    

def update():
    try:
        u_id = int(update_id.get())
        if dropdown_str in ["Grade", "UD"]:
            u_val = int(update_val.get())
        else:
            u_val = update_val.get()
        cursor = my_connect.cursor()
        
        sql = "UPDATE student SET " + dropdown_str.get() + " = %s WHERE id = %s"
        
        val = ( u_val,u_id)
        cursor.execute(sql,val)
        my_connect.commit()
    except:
         showinfo(
            title = 'Input Alert',
            message="Please provide inputs or type a number for ID and grade" 
            )
    
button = Button(root, text='show', command=show)
button.place(x=350, y = 20, width=50)

e1 = Entry(root, textvar=ID, justify=RIGHT)
l1 = Label(root, text = "ID")
l1.place(x = 350, y = 60)
e1.place(x = 350, y = 80, width = 20)
e2 = Entry(root, textvar=Name, justify=RIGHT)
l1 = Label(root, text = "Name")
l1.place(x = 400, y = 60)
e2.place(x = 400, y = 80,width = 80)
l1 = Label(root, text = "Class")
l1.place(x = 350, y = 100)
e3 = Entry(root, textvar=Class, justify=RIGHT)
e3.place(x = 350, y = 120,width = 40)
l1 = Label(root, text = "Grade")
l1.place(x = 400, y = 100)
e4 = Entry(root, textvar=Grade, justify=RIGHT)
e4.place(x = 400, y = 120, width = 30)
l1 = Label(root, text = "Gender")
l1.place(x = 440, y = 100)
e5 = Entry(root, textvar=Gender, justify=RIGHT)
e5.place(x = 440, y = 120, width = 30)
insert_button = Button(root,text = 'insert',command = insert)
insert_button.place(x = 350, y = 140)

l6 = Label(root, text = "ID")
l6.place(x = 350, y = 180)
e6 = Entry(root, textvar= delete_id, justify=RIGHT)
e6.place(x = 350, y = 200)
delete_button = Button(root, text = 'delete', command = delete)
delete_button.place(x = 350, y = 240)

l7 = Label(root, text = "ID")
l7.place(x = 350, y = 270)
e7 = Entry(root, textvar= update_id, justify=RIGHT)
e7.place(x = 350, y = 290)

options = ["id", "name", "class", "mark", "gender"]
dropdown_str.set("id")
l8 = Label(root, text = "Column to update:")
l8.place(x = 350, y = 320)
dropdown = OptionMenu(root,dropdown_str,*options)
dropdown.place(x = 460, y= 320)
e7 = Entry(root, textvar= update_val, justify=RIGHT)
e7.place(x = 350, y = 350)
update_button = Button(root, text = 'update', command = update)
update_button.place(x = 350, y = 370)


root.mainloop()
