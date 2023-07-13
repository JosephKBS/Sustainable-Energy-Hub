import pandas as pd
import numpy as np
import os
from google.colab import drive
import json
!pip install pdfminer
!pip install PyPDF2
import pdfminer
import PyPDF2
from PyPDF2 import PdfFileReader
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import PyPDF2

# setting Google drive directory
drive.mount('/content/drive')
path = 'Energy Moonshot AI/TextExtract/raw_file'
os.chdir(os.path.join('/content/drive/My Drive', path))

def clean_text(text):
  return text.replace('[^\w\s]',' ')\
  .replace('...',' ')\
  .replace('\u2026',' ')\
  .replace('\n',' ')

def text_extract(file_name,
                 detail = False,
                 page_info = False,
                 save= False,
                 save_file_name = False):
  reader = PyPDF2.PdfReader(file_name)
  empty_text=[]
  for page in reader.pages:
    content = page.extract_text()
    empty_text.append(clean_text(content))
  if detail is True:
    print("Complete!")
    print("Current path: ", os.getcwd())
  if page_info is True:
    print("Page number:",len(reader.pages))
  if save is True:
    with open(save_file_name, 'w') as txtfile:
      json.dump(empty_text, txtfile)
  return(empty_text)

all_text = {'index':[], 'file_name':[] , 'text':[] }
index = 0
step = True
save_all_file = True

if __name__ == "__main__":
  print( "Total file number: ", len(os.listdir(os.getcwd()) ) )
  for file in os.listdir(os.getcwd()):
    if file.endswith((".pdf")):
      extracted = text_extract(
        file_name = file,
        detail = False,
        page_info = False,
        save = False
      )
      all_text['index'].append(index)
      all_text['file_name'].append(file)
      all_text['text'].append(extracted)
      index += 1
    if step is True:
      print("file", index, "processed")

  if save_all_file is True:
    with open("all_text.txt", 'w') as txtfile:
      json.dump(all_text, txtfile)
      print("saving complete")
  print("ALL Completed")
