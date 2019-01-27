from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def generate(pdfname):

    inp = open("textmodel.txt",'r')
    pd = str(pdfname+".pdf")
    output = canvas.Canvas(pd)
    output.setFont("Times-Roman",12)
    i = 0.5*inch
    j = 11*inch
    for line in inp:
        sting = line[:-1]
        words = sting.split(' ')
        linecount = int(len(sting)/90) + 1
        charcount = 0
        outstring = ""
        l = 0
        for k in range(0,linecount):
            while(charcount<=90 and l!=len(words)):
                outstring+=(words[l])
                outstring+=(" ")
                charcount+=len(words[l]) +1
                l+=1
            output.drawString(i,j,outstring)
            j -= 0.25*inch
            if j == 1*inch:
                output.showPage()
                output.setFont("Times-Roman",12)
                j = 11*inch
            outstring = ""
            charcount = 0
    output.showPage()
    output.save()