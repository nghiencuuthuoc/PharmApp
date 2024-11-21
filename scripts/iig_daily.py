"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
2024-08-04: This code runs correctly
2028-08-28: move to scripts and paiig17dev

"""

# import lib
import os
import shutil
import sys
sys.path.append('..')
# input file name
# file = str(input("Enter file name with extension (csv or txt): "))
# file = 'iig_daily.txt'
file_name_loading = '../drugname/iig_daily.txt'
# file_name = 'drugname/' + file
# file_name_loading = 'drugname/' + 'loading_' + file

# create file loading
# if os.path.exists(file_name_loading):
    # os.remove(file_name_loading)
    # shutil.copyiig_daily(file_name, file_name_loading)
    # pass
# else:
    # shutil.copyiig_daily(file_name, file_name_loading)


# remove iig exist
f = open(file_name_loading,'r')
drugs_name_file = f.readlines()
for drug_name_file in drugs_name_file:
    drug = drug_name_file.replace(' ','+').replace('\n','').replace('-', '+')
    from pathlib import Path
    drug_iig_name = drug + '_inactive_ingredient_list.txt'
    folder_path = '../iigdata/'
    filepath = folder_path + drug_iig_name
    if os.path.isfile(filepath):
        with open(file_name_loading, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != drug_name_file:
                    f.write(i)
            f.truncate()
    else:
        pass

# Remove drug name len < 3 (not key name)
f = open(file_name_loading,'r')
drugs_name_file = f.readlines()
for drug_name_file in drugs_name_file:
    drug = drug_name_file.replace(' ','+').replace('\n','').replace('-', '+')
    if len(drug) <3:
        with open(file_name_loading, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != drug_name_file:
                    f.write(i)
            f.truncate()
    else:
        pass
 
# run ok
# remove drug name if number
f = open(file_name_loading,'r')
drugs_name_file = f.readlines()
for drug_name_file in drugs_name_file:
    drug = drug_name_file.replace(' ','+').replace('\n','').replace('-', '+')
    if drug.isdigit():
        with open(file_name_loading, "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != drug_name_file:
                    f.write(i)
            f.truncate()
    else:
        pass
        
        
# run ok
# get iig and remove line

f = open(file_name_loading,'r')
drugs_name_file = f.readlines()
for drug_name_file in drugs_name_file:
    drug = drug_name_file.replace(' ','+').replace('\n','').replace('-', '+')
    # get inactive ingredient
    # import src.pharmappiig013 as pa
    # import src.pharmappiig017dev as pa
    import src.pharmappiig017dev as pa
    try:
        print(f'{drug} loading!')
        pa.get_inactive_ingredient(name_drug=drug)
        print(f'{drug} done!')
        print("+---------------------------+---------------------------+")
    except:
        print(f'{drug} no found in DailyMed or run error!')
        print("+---------------------------+---------------------------+")
    with open(file_name_loading, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != drug_name_file:
                f.write(i)
        f.truncate()