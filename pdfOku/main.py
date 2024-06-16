import PyPDF2 as pdf
import re


"""dosya=open("US_Declaration.pdf",mode="rb")
pdfRead=pdf.PdfFileReader(dosya)
print(pdfRead.numPages)
print(pdfRead.getPage(0).extractText())
dosya.close()"""

"""
dosya=open("US_Declaration.pdf","rb")
pdfRead=pdf.PdfFileReader(dosya)
firstPage=pdfRead.getPage(1)
pdfWrite=pdf.PdfFileWriter()

pdfWrite.addPage(firstPage)
pdfOutput=open("MyPdf","wb+")
pdfWrite.write(pdfOutput)
pdfOutput.close()

dosya2=open("MyPdf","rb")
pdfRead2=pdf.PdfFileReader(dosya2)
print(pdfRead2.getPage(0).extractText())"""

dosya=open("Business_Proposal.pdf","rb")
pdfReader=pdf.PdfFileReader(dosya)
page_two=pdfReader.getPage(1).extractText()
with open("contacts.txt","w+") as contacts:
    contacts.write(page_two)
    contacts.seek(0)

with open("contacts.txt","r") as contacts:
    print(contacts.read())

pattern=r"[\w]+@[\w]+.\w{3}"
email=re.findall(pattern,page_two)
print(email)