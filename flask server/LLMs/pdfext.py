import PyPDF2
#pdfpath="C:\Users\niran\Desktop\Projects\6.Introduction_to_555_TIMER_AND_FEATURES_1698430878347.pdf"
def savefil(data):
    with open("volatilefile.txt","w") as f:
        f.write(data)
def pdftotext(pdfpath):
    pdfread=PyPDF2.PdfReader(pdfpath)
    full_text=""
    for i in range(0,len(pdfread.pages)):
       page=pdfread.pages[i]
       text=page.extract_text()
       full_text+=text
    savefil(full_text)


if __name__=="__main__":
    pdfpath="C:\\Users\\niran\\Desktop\\Projects\\6.Introduction_to_555_TIMER_AND_FEATURES_1698430878347.pdf"
    pdftotext(pdfpath)