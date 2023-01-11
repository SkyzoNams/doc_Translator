#!/usr/bin/env python

import os
import json
import subprocess
from packages.googletrans import Translator

def get_json(filename):
    with open(filename) as json_data:
        return json.load(json_data)

def get_relative_path(debug=True):
    if debug is False:
        return '.'
    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir)
    return parentDir.replace('\\', '/')

def create_file(file_name, data):
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)


def rename_files(pdf_folder):
    for file in os.listdir(pdf_folder):
        if file.find(' ') > -1:
            os.rename(pdf_folder + file, pdf_folder + file.strip().replace(' ', '_'))


def save_as_docx(input_filepath, output_filepath):
    if os.path.isfile(output_filepath) is True:
        return output_filepath
    elif input_filepath.endswith('.doc'):
        subprocess.run('./packages/docto.exe -f ' + input_filepath + ' -O "' + output_filepath + '" -T 16')
        return output_filepath
    elif input_filepath.endswith('.docx'):
        return input_filepath
    return 'unmanaged format'


def translate_text(text):
    if text is not None and text != '' and text.isdigit() is False and len(text) > 1:
        try:
            translator = Translator()
            transleted = translator.translate(text)
            return transleted.text
        except Exception:
            return text
    return text