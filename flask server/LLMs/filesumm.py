import PyPDF2
from flask import request
def extract_text_from_pdf(mypdf):
    #with open('pdf_file_path', 'rb') as pdf_file:
    
    pdf_reader = PyPDF2.PdfReader(mypdf)# Create a PDF reader object

        # Initialize an empty string to store text
    full_text = ''

        # Loop through each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]# Get a specific page

            # Extract text from the page 
        text = page.extract_text()

            # Append the text of each page to the full_text
        full_text += text

    return full_text

def save_text_to_file(text, output_file_path):
   with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text) # Save the extracted text to a text file

if __name__=="__main__":
    save_text_to_file(extract_text_from_pdf("fetamplifier.pdf"),"out.txt")