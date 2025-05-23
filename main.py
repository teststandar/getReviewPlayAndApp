import pandas as pd
from datetime import datetime
import ios
import filter
import os
import checking
import create_folder
import android
from enum import Enum

# Enum for system choices
class SystemChoice(Enum):
    IOS = "1"
    ANDROID = "2"
    ALL = "3"

# Create folders
create_folder.create_folder("PD")
create_folder.create_folder("PDS")

# Function to get user input for system and application
def get_user_choice():
    print("1. IOS")
    print("2. ANDROID")
    print("3. ALL")
    sistem = input("Masukan Pilihan Angka : ")
    create_folder.clear_screen()
    if sistem in [SystemChoice.IOS.value, SystemChoice.ANDROID.value]:
        print("1. PD")
        print("2. PDS")
        aplikasi = input("Masukan Pilihan Angka : ")
        create_folder.clear_screen()
        if aplikasi == "1":
            name = f"PD/{'IOS_PD' if sistem == SystemChoice.IOS.value else 'ANDROID_PD'}"
        elif aplikasi == "2":
            name = f"PDS/{'IOS_PDS' if sistem == SystemChoice.IOS.value else 'ANDROID_PDS'}"
        else:
            print(f"{aplikasi} Pilihan tidak ada")
            os._exit(0)
    elif sistem == SystemChoice.ALL.value:
        name = "ALL"
    else:
        print(f"{sistem} Pilihan tidak ada")
        os._exit(0)
    return sistem, name, aplikasi if sistem in [SystemChoice.IOS.value, SystemChoice.ANDROID.value] else None

# Function to validate and get date range
def get_date_range():
    print("Contoh format tanggal 2024-01-31")
    start_date = input("Masukan tanggal awal : ")
    end_date = input("Masukan tanggal akhir : ")

    # Validate dates
    checking.check_string(start_date, "start date")
    checking.check_string(end_date, "end date")
    checking.check_date_format(start_date, "%Y-%m-%d", "start date")
    checking.check_date_format(end_date, "%Y-%m-%d", "end date")
    checking.check_date(start_date, end_date, "%Y-%m-%d")
    return start_date, end_date

# Function to create file name
def create_file_name(base_name, start_date=None, end_date=None):
    date_now = datetime.now()
    timestamp = f"{date_now.year}{date_now.month:02}{date_now.day:02}{date_now.hour:02}{date_now.minute:02}"
    if start_date and end_date:
        return f"{base_name}-{start_date}_to_{end_date}-{timestamp}.xlsx"
    return f"{base_name}-{timestamp}.xlsx"

# Function to fetch and filter reviews
def fetch_and_filter_reviews(sistem, aplikasi=None, start_date=None, end_date=None):
    if sistem == SystemChoice.IOS.value:
        all_reviews = ios.get_ios(aplikasi)
        return filter.filter_reviews_by_date_ios(all_reviews, start_date, end_date)
    elif sistem == SystemChoice.ANDROID.value:
        all_reviews = android.get_andro(aplikasi)
        return filter.filter_reviews_by_date_andro(all_reviews, start_date, end_date)
    elif sistem == SystemChoice.ALL.value:
        filtered_reviews = []
        for app_type, filter_func in [("1", filter.filter_reviews_ios_pd), ("2", filter.filter_reviews_ios_pds)]:
            data = ios.get_ios(app_type)
            filtered_reviews.extend(filter_func(data))
        for app_type, filter_func in [("1", filter.filter_reviews_andro_pd), ("2", filter.filter_reviews_andro_pds)]:
            data = android.get_andro(app_type)
            filtered_reviews.extend(filter_func(data))
        return filtered_reviews

# Main logic
sistem, name, aplikasi = get_user_choice()
if sistem != SystemChoice.ALL.value:
    start_date, end_date = get_date_range()
else:
    start_date = end_date = None

filtered_reviews = fetch_and_filter_reviews(sistem, aplikasi if sistem != SystemChoice.ALL.value else None, start_date, end_date)

# Convert to Excel
df = pd.DataFrame(filtered_reviews)
excel_name = create_file_name(name, start_date, end_date)
df.to_excel(excel_name, index=False)
print(f"Total reviews fetched: {len(filtered_reviews)}")
print(df)
print(f"All reviews have been saved to {excel_name}")

