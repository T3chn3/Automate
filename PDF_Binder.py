#! python3

#combinePdfs.py - combines all PDF's in the current working directory into a single PDF

import PyPDF2, os

#get all PDF filenames
pdfFiles=[]
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter=PyPDF2.PdfFileWriter()

#loop through all the files
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb') #read binary mode
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    #loop through all the pages and add them
    for pageNum in range(1,pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

#save results
pdfOutput = open('allminutes.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()


