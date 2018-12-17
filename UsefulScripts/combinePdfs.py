#!/usr/bin/python3

# Put script in directory where are all pdf files , run script it will create new pdf file called
# "CombinedPDFfiles.pdf" , all your pdf's are combined in that file

import PyPDF2,os

pdfFiles = []
for filename in os.listdir('.'):  #'.'-returns ever file in cur. dir.
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1,pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open('CombinedPDFfiles.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()