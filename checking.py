import os
from datetime import datetime

def check_string(string, name):
    if string is None or string =='':
        print(name + " is null")
        os._exit(0)

def check_date_format(date_string, date_format, string):
    try:
        # Mencoba mem-parsing string sesuai format yang diberikan
        datetime.strptime(date_string, date_format)
        # return True
    except ValueError:
        # Jika terjadi kesalahan ValueError, berarti format tidak sesuai
        # return False
        print(string + " Format date tidak Sesuai (contoh : 2024-08-31)")
        os._exit(0)

def check_date(date_string, date_string2, date_format):
    start_date = datetime.strptime(date_string, date_format)
    end_date = datetime.strptime(date_string2, date_format)
    if start_date >= end_date:
        print("start date lebih besar dari end date")
        os._exit(0)
