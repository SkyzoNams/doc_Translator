from utils.utils import *
from classes.PDF_Translator import PDF_Translator

import os

DOC_INPUT_FOLDER = get_relative_path() + '/files/input/doc/'
DOCX_INPUT_FOLDER = get_relative_path() + '/files/input/docx/'
DOCX_OUTPUT_FOLDER = get_relative_path() + '/files/output/docx/'


def handler():

    translate_text('bonjour')
    return 
    try:
        for doc in os.listdir(DOC_INPUT_FOLDER):
            if doc.find('~') == -1:
                filepath = save_as_docx(DOC_INPUT_FOLDER + doc, DOCX_INPUT_FOLDER + doc + "x")
                if filepath != "unmanaged format":
                    PDF_Translator(doc + "x", filepath, DOCX_OUTPUT_FOLDER)
        print ('DOCX Translation Done.\n')
    except Exception as e:
        print ('[ERROR] ' + str(e))




handler()