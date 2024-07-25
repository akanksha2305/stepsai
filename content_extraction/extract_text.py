import PyPDF2
import pdfplumber

def extract_text_from_pdf_pypdf2(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

def extract_text_from_pdf_pdfplumber(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    pdf_paths = [
        'Introduction-to-Data-Science-AAgah-20240620-1.pdf',
        'Dynamicsl.pdf',
        'Research-Data-Management-in-the-Canadian-Context-1712778191.pdf'
    ]
    
    for pdf_path in pdf_paths:
        text = extract_text_from_pdf_pdfplumber(pdf_path)
        output_path = pdf_path.replace('.pdf', '.txt')
        save_text_to_file(text, output_path)
        print(f"Extracted text saved to {output_path}")
