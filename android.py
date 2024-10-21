import os
from google_play_scraper import reviews_all
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import requests

def get_token():
    SCOPES = ['https://www.googleapis.com/auth/androidpublisher']
    CLIENT_SECRET_FILE = 'key.json'
    
    credentials = service_account.Credentials.from_service_account_file(CLIENT_SECRET_FILE, scopes=SCOPES)

    # Refresh token jika perlu
    credentials.refresh(Request())

    return credentials.token

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

def get_andro_2(string):
    if string == "1":
        app_id="com.pegadaiandigital"
    elif string == "2":
        app_id="co.pegadaian.syariah.nasabah"
    else:
        print("error jenis aplikasi")
        os._exit(0)
    access_token = get_token()
    url = f'https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{app_id}/reviews'
    # url = f'https://mybusiness.googleapis.com/v4/{app_id}/reviews'
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    all_reviews = []
    token = None

    while True:
        params = {
            'maxResults': 100
        }
        
        if token:
            params['token'] = token
        
        # Kirim permintaan HTTP GET untuk mengambil ulasan
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            reviews_data = response.json()
            all_reviews.extend(reviews_data.get('reviews', []))
            
            # Periksa apakah ada token untuk halaman selanjutnya (pagination)
            token = reviews_data.get('tokenPagination', {}).get('nextPageToken')
            
            # Jika tidak ada token untuk halaman selanjutnya, berhenti mengambil ulasan
            if not token:
                break
        else:
            print(f"Error: {response.status_code}")
            break
    
    return all_reviews