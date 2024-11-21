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


# input name
drug_input = str(input("Enter name: "))
# drug_name = 'nexium'
drug_name = drug_input.lower().replace(' ', '+').replace('-','+')

# set file
iig_txt = drug_name + "_inactive_ingredient_list.txt"
iig_txt_path = os.path.join('../iigdata', iig_txt)
iigs_txt = drug_name + "_iigs.txt"
iigs_txt_path = os.path.join('../iigsdata', iigs_txt)
iig_xlsx = drug_name + '_iig.xlsx'
sheet_iigs = drug_name + '_iigs'
sheet_iig = drug_name + '_iig'
iig_xlsx_path =  os.path.join('../iig2excel', iig_xlsx)


# delete all file txt in iigview
iigview_folder = '../iigview'
iigview_list_file = os.listdir(iigview_folder)
for item in iigview_list_file:
    if item.endswith(".txt"):
        os.remove(os.path.join(iigview_folder, item))



# Save file iigsdata
if os.path.isfile(iigs_txt_path) == True:
    print(f'{iigs_txt} exist in iigsdata folder!')
else:
    df_iigs = search(df_pickle, drug_name)
    df_iigs.to_csv(iigs_txt_path, mode='a', index = False, header=True)
    print(f'{iigs_txt} saved in iigsdata folder!')

# Save iigs to excel
if os.path.isfile(iigs_txt_path) == True:
    shutil.copy(iigs_txt_path, '../iigview')
    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
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
    shutil.copy(iig_txt_path, '../iigview')
    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df_iig = pd.read_csv(iig_txt_path)
    
    # export to excel
    if df_iig is not None:
        with pd.ExcelWriter(iig_xlsx_path, engine='openpyxl', mode='a') as writer:
            df_iig.to_excel(writer, sheet_name = sheet_iig)
        # os.system('start "excel" path_file_excel_iig')
        iig_xlsx_open = 'D:\\PharmApp\\iig2excel' + '\\' + iig_xlsx
        os.startfile(iig_xlsx_open)
else:
    print(f'Inactive ingredient {drug_name} not exist in ../iigdata!')

# view multi drug with pandasgui
txt_files = [f for f in os.listdir(iigview_folder) if f.endswith('.txt')]

dataframes = {}
for txt_file in txt_files:
    file_path = os.path.join(iigview_folder, txt_file)
    df = pd.read_csv(file_path, delimiter=',')  
    key = os.path.splitext(txt_file)[0]
    key = key.replace('_inactive_ingredient_list','_iig').replace('+', ' ')
    dataframes[key] = df
  
for key, df in dataframes.items():
    print(f"DataFrame for {key}:")
    # print(df.head())
gui = show(**dataframes)