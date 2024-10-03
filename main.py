import PyPDF2

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])