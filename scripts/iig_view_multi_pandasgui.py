"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
2024-08-05: This code runs correctly
2028-08-28: move to scripts and paiig17dev

"""
import os
import shutil
import pandas as pd
from pandasgui import show
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import sys
sys.path.append('..')


comma = "+---------------------------+---------------------------+"
drugs_input = str(input("Enter names separated by comma: "))

# delete all file in iigview
iigview_folder = '../iigview'
iigview_list_file = os.listdir(iigview_folder)
for item in iigview_list_file:
    if item.endswith(".txt"):
        os.remove(os.path.join(iigview_folder, item))
# drug name
drugs_input = drugs_input.lower().replace(', ', ',')
drugs_input = drugs_input.split(",")
# get inactive ingredient
import src.pharmappiig017dev as pa
for drug in drugs_input:
    try:
        drug_name = drug.lower().replace(' ', '+').replace('-','+')
        iig_file = drug_name + "_inactive_ingredient_list.txt"
        iig_file_path = os.path.join('../iigdata', iig_file)
        if os.path.isfile(iig_file_path) == True:
            print(f'{drug} exist')
            shutil.copy(iig_file_path, '../iigview')
            print(comma)
        else:
            print(drug)
            pa.get_inactive_ingredient(name_drug=drug_name)
            print(f'{drug_name} done!')
            print(comma)
    except:
        print(f'{drug} run error')
        print(comma)
        pass

# view multi drug with pandasgui
folder_path = '../iigview'
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

dataframes = {}
for txt_file in txt_files:
    file_path = os.path.join(folder_path, txt_file)
    df = pd.read_csv(file_path, delimiter=',')  
    key = os.path.splitext(txt_file)[0]
    key = key.replace('_inactive_ingredient_list','').replace('+', ' ')
    dataframes[key] = df
  
for key, df in dataframes.items():
    print(f"DataFrame for {key}:")
    # print(df.head())
gui = show(**dataframes)