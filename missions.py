
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from view_missions import *
from update_missions import *
from delete_missions import *

mypass = "live"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
    
def missions(): 
    
    root = Tk()
    root.title("Missions")
    root.minsize(width=3000,height=1400)
    root.geometry("600x500")
    
    #Define the PhotoImage Constructor by passing the image file
    img= PhotoImage(file='./images/missions.png', master= root)
    img = img.zoom(4)
    img_label= Label(root,image=img)

    #define the position of the image
    img_label.place(x=0, y=0)
    # Take n greater than 0.25 and less than 5
#    same=True
#    n=1.5
#    
#    # Adding a background image
#    background_image =Image.open("./images/isro.png")
#    [imageSizeWidth, imageSizeHeight] = background_image.size
#    
#    newImageSizeWidth = int(imageSizeWidth*n)
#    if same:
#        newImageSizeHeight = int(imageSizeHeight*n) 
#    else:
#        newImageSizeHeight = int(imageSizeHeight/n) 
#        
#    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
#    img = ImageTk.PhotoImage(background_image)
#    
#    Canvas1 = Canvas(root)
#    
#    Canvas1.create_image(1090,800,image = img)      
#    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
#    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#8B8378",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.15)
    headingLabel = Label(headingFrame1, text="Missions",bg="#1F1F1F", fg='white', font=('ARIAL',40,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="Update",bg='#8B8378',fg='black',font=('ARIAL',20,"bold"),            command=update_missions)
    btn1.place(relx=0.35,rely=0.35, relwidth=0.25,relheight=0.1)
        
    btn3 = Button(root,text="Delete",bg='#8B8378',fg='black',font=('ARIAl',20,"bold"),command=delete_missions)
    btn3.place(relx=0.35,rely=0.45, relwidth=0.25,relheight=0.1)
        
    btn4 = Button(root,text="View",bg='#8B8378',fg='black',font=('ARIAL',20,"bold"),command=view_missions)
    btn4.place(relx=0.35,rely=0.55, relwidth=0.25,relheight=0.1)
        
    
    root.mainloop()
