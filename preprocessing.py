#!/usr/bin/env python3
"""
Preprocessing of PDF files.

Converting PDF file to byte stream. Performing encoding with One Hot Encoding and n-grams.

First example below is with the "dummy.pdf" file taken from
https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf
"""

import glob
# from sklearn.feature_extraction.text import CountVectorizer

def get_file_byte_string(file):
    curr_file = open(file, "rb")
    data = curr_file.read()
    data_str = str(data)
    data_delim = ' '.join(data_str[i:i+4] for i in range(0, len(data_str), 4)) 
    data_bytes = bytes(data_delim, 'utf-8')
    curr_file.close()
    return data_bytes
