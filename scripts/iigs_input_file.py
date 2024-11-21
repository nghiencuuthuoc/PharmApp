import sys
sys.path.append('..')
import os
# os.getcwd()
import pandas as pd
import numpy as np
import pickle
import shutil
from pandasgui import show
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# save and load pickle
pickle_path = '../pickle/inactive_ingredients_sagerx.pickle'
inactive_ingredients_path = '../sagerxdata/products_to_inactive_ingredients.csv'

if os.path.isfile(pickle_path) == True:
    df_pickle = pd.read_pickle(pickle_path)
else:
    inactive_ingredients_sagerx = pd.read_csv(inactive_ingredients_path, low_memory=False)
    inactive_ingredients_sagerx.to_pickle(pickle_path)
    df_pickle = pd.read_pickle(pickle_path)

def search(df: pd.DataFrame, substring: str, case: bool = False) -> pd.DataFrame: 
    mask = np.column_stack([df[col].astype(str).str.contains(substring.lower(), case=case, na=False) for col in df])
    return df.loc[mask.any(axis=1)]



file = str(input("Enter file name with extension (csv or txt): "))

# create file loading
file_name = '../drugname/' + file
file_name_loading = file_name 
file_name_loading = '../drugname/' + 'loading_' + file

if os.path.exists(file_name_loading):
    os.remove(file_name_loading)
    shutil.copy(file_name, file_name_loading)
    pass
else:
    shutil.copy(file_name, file_name_loading)


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

# remove iigs exist
f = open(file_name_loading,'r')
drugs_name_file = f.readlines()
for drug_name_file in drugs_name_file:
    drug = drug_name_file.replace(' ','+').replace('\n','').replace('-', '+')
    from pathlib import Path
    drug_iig_name = drug + '_iigs.txt'
    folder_path = '../iigsdata/'
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

  
# run get iig and iigs
f = open(file_name_loading,'r')
drugs_name_file = f.readlines()
comma = "+---------------------------+---------------------------+"

for drug_name in drugs_name_file:
    drug_name = drug_name.replace(' ','+').replace('\n','').replace('-', '+')
    print(comma)
    print(f'Extracting iig and iigs {drug_name}')
    # set file
    iig_txt = drug_name + "_inactive_ingredient_list.txt"
    iig_txt_path = os.path.join('../iigdata', iig_txt)
    iigs_txt = drug_name + "_iigs.txt"
    iigs_txt_path = os.path.join('../iigsdata', iigs_txt)
    iig_xlsx = drug_name + '_iig.xlsx'
    sheet_iigs = drug_name + '_iigs'
    sheet_iig = drug_name + '_iig'
    iig_xlsx_path =  os.path.join('../iig2excel', iig_xlsx)


    # Save file iigsdata
    if os.path.isfile(iigs_txt_path) == True:
        print(f'{iigs_txt} exist in iigsdata folder!')
    else:
        df_iigs = search(df_pickle, drug_name)
        df_iigs.to_csv(iigs_txt_path, mode='a', index = False, header=True)
        print(f'{iigs_txt} saved in iigsdata folder!')

    # Save iigs to excel
    if os.path.isfile(iigs_txt_path) == True:
        df_iigs = pd.read_csv(iigs_txt_path)
        
        # export to excel
        if df_iigs is not None:
            with pd.ExcelWriter(iig_xlsx_path) as writer:
                df_iigs.to_excel(writer, sheet_name = sheet_iigs)
    else:
        print(f'The {iigs_txt_path} not exist in ../iigsdata!')

    # Save file iigdata
    if os.path.isfile(iig_txt_path) == True:
        print(f'{iig_txt} exist in iigdata folder!')
    else:
        # get iig
        # import src.pharmappiig013 as pa
        import src.pharmappiig017dev as pa
        pa.get_inactive_ingredient(name_drug=drug_name)


    # Save iig to excel 

    if os.path.isfile(iig_txt_path):
        df_iig = pd.read_csv(iig_txt_path)
        
        # export to excel
        if df_iig is not None:
            with pd.ExcelWriter(iig_xlsx_path, engine='openpyxl', mode='a') as writer:
                df_iig.to_excel(writer, sheet_name = sheet_iig)
    else:
        print(f'Inactive ingredient {drug_name} not exist in ../iigdata!')
