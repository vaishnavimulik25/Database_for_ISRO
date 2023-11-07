from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from branch import *
from employee import *
from branch_supplier import *
from client import *
from missions import *
# Add your own database name and password here to reflect in the code
mypass = "live"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Company")
root.minsize(width=3000,height=1400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=1.5

# Adding a background image
background_image =Image.open("./images/isro.png")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(1090,800,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

#headingFrame1 = Frame(root,bg="#191970",bd=5)

#headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

headingFrame1 = Frame(root,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.15)

headingLabel = Label(headingFrame1, text="Database for ISRO",bg='#191970',fg='white', font=('Courier',50))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Missions",bg='black',fg='white',font=('ARIAL',20,"bold"), command=missions)
btn1.place(relx=0.35,rely=0.35, relwidth=0.25,relheight=0.1)
    
btn2 = Button(root,text="Employees",bg='black',fg='white',font=('ARIAL',20,"bold"),command=employees)
btn2.place(relx=0.35,rely=0.45, relwidth=0.25,relheight=0.1)
    
btn3 = Button(root,text="Clients",bg='black',fg='white',font=('ARIAl',20,"bold"), command=clients)
btn3.place(relx=0.35,rely=0.55, relwidth=0.25,relheight=0.1)
    
btn4 =Button(root,text="Branch",bg='black',fg='white',font=('ARIAL',20,"bold"),command =branch)
btn4.place(relx=0.35,rely=0.65, relwidth=0.25,relheight=0.1)
    
btn5 = Button(root,text="Branch_supplier",bg='black',fg='white',font=('ARIAL',20,"bold"), command =branch_supplier)
btn5.place(relx=0.35,rely=0.75, relwidth=0.25,relheight=0.1)

root.mainloop()
