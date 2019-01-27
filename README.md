# NoteHub
An OCR based application to help students with disabilities  have an easier time taking notes in class 

## About the Program
This is a OCR program that converts lecture notes from an image to a pdf. It helps students with physical disabilities take notes by simply taking a picture to create an easily searchable document. 

## Process
It works by first using OpenCV to detect the rough shapes of the letters. Azure was then used to convert the image into ACSII characters. The resulting text file was converted to a pdf using python. The GUI was done through the tkinter module. 
