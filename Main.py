#import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import font
from PIL import ImageTk,Image
import webcamimage
from handwrittenconversion import conversion 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from pdfgen import generate

global directory
global text
global pdfname
	
def getFile():
	root.filename =  filedialog.askopenfilename(initialdir = "Desktop",title = "Select file",filetypes = (("jpeg files","*.jpg"),("pdf files","*.pdf"),("all files","*.*")))
	print ((root.filename))
	directory = root.filename
	text = conversion(directory) 

def convertpdf():
	pdfname = e1_value.get()
	generate(pdfname)
	#print(pdfname)




root = Tk()
root.attributes("-fullscreen",True)
#root.geometry("1920x1080")
root.configure(background='black')

canvas = Canvas(root, width = 710, height = 228,bd=0, highlightthickness=0)
#canvas.grid(row =0, column =1)
canvas.pack(pady=75)
img = ImageTk.PhotoImage(Image.open("Logo.png"))  
canvas.create_image(355, 114, anchor="center", image=img)

e1_value = StringVar()
e1=Entry(root, textvariable=e1_value)
e1.pack()
e1.focus_set()

b1font = font.Font(family = "Georgia", size = 16)
b1 = Button(root, text = "File Select", command=getFile, font = b1font,fg='white', bg='red')
#b1.grid(row =2, column =0)
b1.pack(side=LEFT,padx=250) 

b2 = Button(root, text = "Capture Image", command=webcamimage.webCam, font = b1font,fg='white', bg='red')
#b2.grid(row =2, column =2)
b2.pack(side=RIGHT,padx=250)

Button(root, text="Quit", command=root.destroy,fg='red', bg='black').pack(side=BOTTOM)

b3font = font.Font(family = "Georgia", size = 20)
b3 = Button(root, text="Note It!", width=15,fg='white', bg='red',font = b3font, command=convertpdf)
#b3.grid(row =4, column =1,columnspan=2)
b3.pack(side=BOTTOM,pady=150)

root.mainloop()

