from pdf2docx import Converter
from docx2pdf import convert

n=int(input("1. PDF to DOCX\n2. DOCX to PDF\nEnter your option : "))
if(n==1):
    print("\nEnter full path and pdf file name without file type(.pdf)\n")
    old_pdf=input("Enter the path of PDF file : ")
    new_doc=input("Enter the DOC file name : ")
    p2d=Converter(old_pdf+".pdf")
    p2d.convert(new_doc+".docx")
    p2d.close()
elif(n==2):
    print("\nEnter full path and docx file name without file type(.docx)\n")
    old_doc=input("Enter the path of DOCX file : ")
    new_pdf=input("Enter the PDF file name : ")
    convert(old_doc+".docx",new_pdf+".pdf")
else:
    print("Invalid Input...")
