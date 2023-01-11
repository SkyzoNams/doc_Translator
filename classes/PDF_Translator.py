from packages.docx import Document 
from packages.googletrans import Translator
from packages.oodocx import oodocx
from utils.utils import *

class   PDF_Translator:
    def __init__(self, filename, input_folder, output_folder):
        self.filename = filename
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.doc_obj = oodocx.Docx(self.input_folder)
        p = self.doc_obj.search('F2MB')

        # self.headers = self.doc_obj.sections[0].header
        # self.footers = self.doc_obj.sections[0].footer
        # self.run()
        self.doc_obj.save(self.output_folder + 'trans-' + self.filename)


    def run(self):
        try:
            self.translate_sections()
            self.translate_paragraphs()
            self.translate_tables()
        except Exception as e:
            raise e

    def translate_sections(self):
        for section in self.doc_obj.sections:
            section = self.translate_header(section)
            section = self.translate_footer(section)

    def translate_header(self, section):
        for table in section.header.tables:
            if table._cells:
                for cell in table._cells:
                    for para in cell.paragraphs:
                        para.text = self.translate_text(para.text)
        for para in section.header.paragraphs:
            para.text = self.translate_text(para.text)
        return section

    def translate_footer(self, section):
        for table in section.footer.tables:
            if table._cells:
                for cell in table._cells:
                    for para in cell.paragraphs:
                        para.text = self.translate_text(para.text)
        for para in section.footer.paragraphs:
            para.text = self.translate_text(para.text)
        return section
    

    def translate_tables(self):
        for table in self.doc_obj.tables:
            if table._cells:
                for cell in table._cells:
                    for para in cell.paragraphs:
                        para.text = self.translate_text(para.text)


    def translate_paragraphs(self):
        try:
            for para in self.doc_obj.paragraphs:
                para.text = self.translate_text(para.text)
        except Exception as e:
            raise e


    def translate_text(self, text):
        if text is not None and text != '' and text.isdigit() is False and len(text) > 1:
            try:
                translator = Translator()
                transleted = translator.translate(text)
                return transleted.text
            except Exception:
                return text
        return text