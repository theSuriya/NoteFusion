from PyPDF2 import PdfReader

class PdfExtract:

    def __init__(self, pdf_file):
        self.extracted_text = self.get_pdf_text(pdf_file)

    def get_pdf_text(self, pdf_file):
        text = ""
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text