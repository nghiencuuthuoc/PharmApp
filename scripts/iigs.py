import sys
sys.path.append('..')
import os
# os.getcwd()
import pandas as pd
import numpy as np
import pickle

# save and load pickle
pickle_path = '../pickle/inactive_ingredients_sagerx.pickle'
inactive_ingredients_path = '../sagerxdata/products_to_inactive_ingredients.csv'

if os.path.isfile(pickle_path) == True:
    df_pickle = pd.read_pickle(pickle_path)
else:
    inactive_ingredients_sagerx = pd.read_csv(inactive_ingredients_path, low_memory=False)
    inactive_ingredients_sagerx.to_pickle(pickle_path)
    df_pickle = pd.read_pickle(pickle_path)

columns_to_drop = ['ndc9', 'product_rxcui', 'inactive_ingredient_tty', 'product_tty', 'inactive_ingredient_rxcui', 'inactive_ingredient_tty']
df_pickle = df_pickle.drop(columns=columns_to_drop)

def search(df: pd.DataFrame, substring: str, case: bool = False) -> pd.DataFrame: 
    mask = np.column_stack([df[col].astype(str).str.contains(substring.lower(), case=case, na=False) for col in df])
    return df.loc[mask.any(axis=1)]

drug_name = str(input("Enter drug name: "))
# drug_name = 'nexium'

# Short name for sheet name if length than 31 character
if len(drug_name) >= 25:
    drug_name_short = drug_name.split()
    drug_name_short = drug_name_short[0]
    drug_name_short = drug_name_short + '_x_'
else:
    drug_name_short = drug_name

# Replace drug name contain ' ' to +
drug_name_replace = drug_name.replace(" ","+")

# set file
iig_txt = drug_name_replace + "_inactive_ingredient_list.txt"
iig_txt_path = os.path.join('../iigdata', iig_txt)
iigs_txt = drug_name_replace + "_iigs.txt"
iigs_txt_path = os.path.join('../iigsdata', iigs_txt)
iig_xlsx = drug_name_replace + '_iig.xlsx'
sheet_iigs = drug_name_short + '_iigs'
sheet_iig = drug_name_short + '_iig'
iig_xlsx_path =  os.path.join('../iig2excel', iig_xlsx)



# view df_iigs
def view(df_iigs):
    from pandasgui import show
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    if df_iigs is not None:
        df_iigs = {sheet_iigs :df_iigs}
        show(**df_iigs) # show data with pandasgui

# save and view iig_xlsx
def save_xlsx(df_iigs):
    # iigs_sheet = drug_name + '_iigs'
    # with pd.ExcelWriter(iig_xlsx, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    #     df_iigs.to_excel(writer, sheet_name = iigs_sheet)
    with pd.ExcelWriter(iig_xlsx_path) as writer:
        df_iigs.to_excel(writer, sheet_name = sheet_iigs)
    iig_xlsx_open = 'D:\\PharmApp\\iig2excel' + '\\' + iig_xlsx
    os.startfile(iig_xlsx_open)
    print(f'{iig_xlsx} saved in iigsdata folder!')

if os.path.isfile(iigs_txt_path) == True:
    print(f'{iigs_txt} exist in iigsdata folder!')
    df_iigs = pd.read_csv(iigs_txt_path)
    save_xlsx(df_iigs)
    view(df_iigs)
else:
    df_iigs = search(df_pickle, drug_name)
    df_iigs.to_csv(iigs_txt_path, mode='a', index = False, header=True)
    save_xlsx(df_iigs)
    view(df_iigs)
