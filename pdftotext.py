# extracted_text = extract_text_from_pdf(pdf_path)
import PyPDF2

# pdf_path = '/content/drive/MyDrive/ContentFolder/StudentHandbook15.pdf'
#just give the pdf file name alog with the txt you want to store it into
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text



def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

pdf_path = '/content/drive/MyDrive/ContentFolder/AnnexIII_01022018.pdf'  # Replace with your PDF file path
output_path = '/content/drive/MyDrive/ContentFolder/VisaAdmissionAnnexIII_01022018.txt'  # Replace with the desired output text file path

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a text file
save_text_to_file(extracted_text, output_path)





