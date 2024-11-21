"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
2024-08-05: This code runs correctly

"""
import os
import shutil
import pandas as pd
# from pandasgui import show
import dtale
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

comma = "+---------------------------+---------------------------+"
drugs_input = str(input("Enter names separated by comma: "))

# delete all file in iigview
iigview_folder = 'iigview'
iigview_list_file = os.listdir(iigview_folder)
for item in iigview_list_file:
    if item.endswith(".txt"):
        os.remove(os.path.join(iigview_folder, item))
# drug name
drugs_input = drugs_input.lower().replace(', ', ',')
drugs_input = drugs_input.split(",")
# get inactive ingredient
import src.pharmappiig016dev as pa
for drug in drugs_input:
    try:
        drug_name = drug.lower().replace(' ', '+').replace('-','+')
        drug_name_iig_file = drug_name + "_inactive_ingredient_list.txt"
        drug_name_iig_filepath = os.path.join('iigdata', drug_name_iig_file)
        if os.path.isfile(drug_name_iig_filepath) == True:
            print(f'{drug} exist')
            shutil.copy(drug_name_iig_filepath, 'iigview')
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
folder_path = './iigview'
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
dtale.show(dataframes)
