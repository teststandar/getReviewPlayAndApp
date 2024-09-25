import getToken
import os
import requests

def get_all_reviews_ios(url, token):
    # Header untuk permintaan API
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    all_reviews = []  # Menyimpan semua ulasan
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            # Tambahkan ulasan dari halaman saat ini ke list
            all_reviews.extend(data.get('data', []))
            # Cek apakah ada halaman selanjutnya
            next_page = data.get('links', {}).get('next')
            url = next_page if next_page else None  # Jika ada next page, lanjutkan
        else:
            print(f"Gagal mengambil data. Status kode: {response.status_code}")
            break
    return all_reviews

def get_ios(string):
    if string == "1":
        app_id="1350501409"
    elif string == "2":
        app_id="1463026343"
    else:
        print("error jenis aplikasi")
        os._exit(0) 

    key_id ="GOWGV0F6YDLK"
    crt ="key.p8"

    # get token
    token = getToken.get_token_ios(crt, key_id)

    # URL API untuk ulasan aplikasi
    url = f"https://api.appstoreconnect.apple.com/v1/apps/{app_id}/customerReviews"

    print("waiting ....")
    all_reviews = get_all_reviews_ios(url, token)

    return all_reviews