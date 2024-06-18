from fpdf import FPDF
from fpdf.html import HTMLMixin
from bs4 import BeautifulSoup
from io import BytesIO


class MyFPDF(FPDF, HTMLMixin):
    def header(self):
        # Add a border around the page
        self.rect(5.0, 5.0, self.w - 10.0, self.h - 10.0)

class Pdf:
    def __init__(self):
        self.pdf = MyFPDF()

    def replace_special_characters(self, text):
        replacements = {
            '’': "'",
            '“': '"',
            '”': '"',
            '–': '-',
            '—': '-',
            '…': '...',
        }
        for original, replacement in replacements.items():
            text = text.replace(original, replacement)
        return text

    def pdf_creator(self, html_text):
        self.pdf.add_page()
    
        # Use the built-in Arial font
        self.pdf.set_font("Times", size=12)
       
        soup = BeautifulSoup(html_text, 'html.parser')

          # Replace special characters in the text
        for element in soup.find_all(text=True):
            element.replace_with(self.replace_special_characters(element))

        # Convert entire HTML content to PDF
        self.pdf.write_html(str(soup))

        # Save PDF to bytes object
        output = BytesIO()
        self.pdf.output(output)
        pdf_bytes = output.getvalue()
        output.close()

        return pdf_bytes