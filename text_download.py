import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime
import seaborn as sns
import os
from google.colab import drive
!pip install pdfminer
!pip install PyPDF2
import pdfminer
import PyPDF2
from PyPDF2 import PdfFileReader
#from pdfminer.high_level import extract_text
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import PyPDF2
import requests
import urllib
import urllib.request
import os
import os.path
import time
from urllib.parse import urljoin
import urllib.request
!pip install validators
import validators


drive.mount('/content/drive')
path_base = 'Energy Moonshot AI/TextExtract'
path_rawfile = '/raw_file'
path_cleanfile = '/cleaned_file'
os.chdir(os.path.join('/content/drive/My Drive', path_base + path_rawfile))

# URL list
url_list = [
    "https://un-energy.org/wp-content/uploads/2017/01/2015-Activities-of-Member-Organizations-and-Partners-of-UN-Energy_29-March-2016.pdf",
    "https://sustainabledevelopment.un.org/content/documents/1324Activities%20UN-Energy%20Members%20for%20the%20Decade%20Draft%20Report.pdf",
    "https://www.fao.org/publications/card/en/c/b1e6ca6a-9cc5-4538-8a97-e713037f7898/",
    "https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1754web-26894285.pdf",
    "https://www-pub.iaea.org/MTCD/Publications/PDF/CCANP16web-86692468.pdf"
]

def url_check(url):
  if validators.url(url) == True: 
    return True
  else: 
    print("url is not valid")
  if url.endswith(".pdf")==False:
    print("url is not pdf file")

def file_download(url, name):
  urllib.request.urlretrieve(url, file_name)

if __name__ == "__main__":
  index = 0
  success_index = 0
  print("Total URLs: ", len(url_list))
  for url_item in url_list:
    index += 1
    file_name = "FILE_" + str(index) + ".pdf"
    time.sleep(0.3)
    # check url
    url_check(url_item)
    try:
      file_download(url_item, file_name)
      success_index += 1
    except:
      print("   file", index, "failed to download")
      pass
  print("ALL COMPLETED")
  print("Success rate:",  round(success_index/index,1)*100 , "%" )

