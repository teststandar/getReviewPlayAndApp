import pandas as pd
from datetime import datetime
import ios
import filter
import os
import checking
import create_folder
import android

# create folder
create_folder.create_folder("PD")
create_folder.create_folder("PDS")

# ui
print("1. IOS")
print("2. ANDROID")
print("3. ALL")
sistem = input("Masukan Pilihan Angka : ")
create_folder.clear_screen()
if sistem == "1":
    print("1. PD")
    print("2. PDS")
    aplikasi = input("Masukan Pilihan Angka : ")
    create_folder.clear_screen()
    if aplikasi == "1":
        name= "PD/IOS_PD"
    elif aplikasi == "2":
        name = "PDS/IOS_PDS"
    else:
        print(f"{aplikasi} Pilihan tidak ada")
        os._exit(0)
elif sistem == "2":
    print("1. PD")
    print("2. PDS")
    aplikasi = input("Masukan Pilihan Angka : ")
    create_folder.clear_screen()
    if aplikasi == "1":
        name= "PD/ANDROID_PD"
    elif aplikasi == "2":
        name = "PDS/ANDROID_PDS"
    else:
        print(f"{aplikasi} Pilihan tidak ada")
        os._exit(0)
elif sistem == "3":
    name = "ALL"
else:
    print(f"{sistem} Pilihan tidak ada")
    os._exit(0)

#set date
if sistem != "3":
    print("Contoh format tanggal 2024-01-31")
    start_date = input("Masukan tanggal awal : ")
    end_date = input("Masukan tanggal akhir : ")

    # cek data
    checking.check_string(start_date, "start date")
    checking.check_string(end_date, "end date")
    checking.check_string(name, "name")
    checking.check_date_format(start_date, "%Y-%m-%d", "start date")
    checking.check_date_format(end_date, "%Y-%m-%d", "end date")
    checking.check_date(start_date, end_date, "%Y-%m-%d")

# set excel name
def create_name():
    date_now = datetime.now()
    year = date_now.year
    month = date_now.month
    day = date_now.day
    hour = date_now.hour
    minute = date_now.minute
    return str(name + "-" + start_date + "_to_" + end_date + "-" + str(year) + str(month) + str(day) + str(hour) + str(minute) + ".xlsx")

def create_name_all():
    date_now = datetime.now()
    year = date_now.year
    month = date_now.month
    day = date_now.day
    hour = date_now.hour
    minute = date_now.minute
    return str(name + "-" + str(year) + str(month) + str(day) + str(hour) + str(minute) + ".xlsx")

#get data
if sistem == "1":
    all_reviews = ios.get_ios(aplikasi)
    filtered_reviews = filter.filter_reviews_by_date_ios(all_reviews, start_date, end_date)
elif sistem == "2":
    all_reviews = android.get_andro(aplikasi)
    filtered_reviews = filter.filter_reviews_by_date_andro(all_reviews, start_date, end_date)
elif sistem == "3":
    filtered_reviews = []
    data_ios_pd = ios.get_ios("1")
    filtered_review_ios_pd = filter.filter_reviews_ios_pd(data_ios_pd)
    filtered_reviews.extend(filtered_review_ios_pd)
    data_ios_pds = ios.get_ios("2")
    filtered_review_ios_pds = filter.filter_reviews_ios_pds(data_ios_pds)
    filtered_reviews.extend(filtered_review_ios_pds)
    data_andro_pd = android.get_andro("1")
    filtered_review_andro_pd = filter.filter_reviews_andro_pd(data_andro_pd)
    filtered_reviews.extend(filtered_review_andro_pd)
    data_andro_pds = android.get_andro("2")
    filtered_review_andro_pds = filter.filter_reviews_andro_pds(data_andro_pds)
    filtered_reviews.extend(filtered_review_andro_pds)


# conver to Excel
df = pd.DataFrame(filtered_reviews)
if sistem == "3":
    print("Total reviews fetched: ", len(filtered_reviews))
    print(df)
    excel_name = create_name_all()
    df.to_excel(excel_name, index=False)
    print("All reviews have been saved to " + excel_name)
else:
    print("Total reviews fetched: ", len(all_reviews))
    print(df)
    excel_name = create_name()
    df.to_excel(excel_name, index=False)
    print("All reviews have been saved to " + excel_name)