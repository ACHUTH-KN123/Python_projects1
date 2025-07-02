from pypdf import PdfWriter

merger = PdfWriter()
pdfs=[]
a=int(input("Enter the number of pdf you want to merge"))
for i in range(0,a):
    name=input(f"Enter the names of pdf {i+1}")
    pdfs.append(name)
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()