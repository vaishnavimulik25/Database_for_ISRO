from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    
    #insertBooks = "insert into books values( '1211' ,'Artificial Intelligence: A Modern Approach' , 'Stuart Russell Peter Norvig' 'Avail' )"
  #  insert into books values( "1212" ,"Clean Code: A Handbook of Agile Software Craftsmanship" , " Robert C. Martin" , "Avail" )
  #insert into books values( "1213" , "Computer Networks" , "David J. Wetherall" , "Avail" )
  #insert into books values( "1214" , "Database System Concepts" , "Henry F. Korth" , "Avail" )
  #insert into books values( "1216" , "Moby-Dick" , "Andrew Hunt " , "Avail" )
  #insert into books values( "1217" , "The Catcher in the Rye" , "Ralph Johnson" , "Avail" )
  #insert into books values( "1218" , "Pride and Prejudice" , "John L. Hennessy" , "Avail" )
  #insert into books values( "1224" , "The Lord of the Rings" , " J.R.R. Tolkien" , "Avail" )
  #insert into books values( "1225" , "The Chronicles of Narnia" , "C.S. Lewis" , "Avail" )
  #insert into books values( "1226" , "Harry Potter and the Philosopher Stone" , "J.K. Rowling" , "Avail" )
  #insert into books values( "1227" , "Operating System Concepts" , "J.R.R. Tolkien" , "Avail" )
  #insert into books values( "1228" , "Introduction to Algorithms" , "Herman Melville" , "Avail" )
  #insert into books values( "1229" , "The Pragmatic Programmer: Your Journey to Mastery" , " J.D. Salinge" , "Avail" )
  #insert into books values( "1230" , "Design Patterns: Elements of Reusable Object-Oriented Software" , "Jane Austen" , "Avail" )
  #insert into books values( "1231" , "Computer Organization Design" , " F. Scott Fitzgerald" , "Avail" )
  #insert into books values( "1232" , "1984" , "George Orwell" , "Avail" )
  #insert into books values( "1234" , "To Kill a Mockingbird , Harper Lee" , "Avail" )
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)


    root.destroy()
    
def update_client(): 
    
    global bookInfo1,bookInfo2,bookInfo3,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=3000,height=1400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "live"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "client" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Update client", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Client Id : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Client Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Branch id : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
#    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
#   lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
#    bookInfo4 = Entry(labelFrame)
#    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
