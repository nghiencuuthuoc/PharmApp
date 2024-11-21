"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
2024-08-04: This code runs correctly
2028-08-28: move to scripts and paiig17dev

"""
import sys
sys.path.append('..')
# get_iig_enter_name_pandagui_view_ndcw
# input name
drug_input = str(input("Enter name: "))
drug_name = drug_input.lower().replace(' ', '+').replace('-','+')

# Save file inactive_ingredient_list.txt
import os
print(drug_name)
drug_name_iig_file = drug_name + "_inactive_ingredient_list.txt"
drug_name_iig_filepath = os.path.join('../iigdata', drug_name_iig_file)
if os.path.isfile(drug_name_iig_filepath) == True:
    print(f'{drug_name} exist')
else:
    # get iig
    # import src.pharmappiig013 as pa
    import src.pharmappiig017dev as pa
    pa.get_inactive_ingredient(name_drug=drug_name)
    
# view data column inactive
import os
drug_name_csv = drug_name + "_inactive_ingredient_list.txt"
drug_name_csv_path = os.path.join('../iigdata', drug_name_csv)

if os.path.isfile(drug_name_csv_path):
    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df_iig = pd.read_csv(drug_name_csv_path)
    df_inactive = df_iig.drop('NDC', axis=1).drop('MainDrug', axis=1).drop('Strength', axis=1).drop('Formulation', axis=1)
    df_inactive = df_inactive.drop_duplicates()
    # view pandasgui
    from pandasgui import show
    import warnings
    drug_name_inactive = drug_name + '_inactive'
    warnings.simplefilter(action='ignore', category=FutureWarning)
    if df_inactive is not None:
        df_inactive_name = {drug_name_inactive:df_inactive}
        show(**df_inactive_name) # show data with pandasgui
else:
    print(f'Inactive ingredient {drug_name} not exist in ../iigdata!')