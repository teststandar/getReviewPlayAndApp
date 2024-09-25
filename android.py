import os
from google_play_scraper import reviews_all


def get_andro(string):
    if string == "1":
        app_id="com.pegadaiandigital"
    elif string == "2":
        app_id="co.pegadaian.syariah.nasabah"
    else:
        print("error jenis aplikasi")
        os._exit(0) 

    print("waiting ....")
    all_reviews = reviews_all(
        app_id,
        lang='id',
        country='id',
    )

    return all_reviews