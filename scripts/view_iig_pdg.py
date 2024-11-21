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

# input name
drug_input = str(input("Enter name: "))
drug_name = drug_input.lower().replace(' ', '+').replace('-','+')

# Save file inactive_ingredient_list.txt
import os
print(drug_name)
iig_file = drug_name + "_inactive_ingredient_list.txt"
iig_file_path = os.path.join('../iigdata', iig_file)
if os.path.isfile(iig_file_path) == True:
    print(f'{drug_name} exist')
else:
    # get iig
    # import src.pharmappiig013 as pa
    import src.pharmappiig017dev as pa
    pa.get_inactive_ingredient(name_drug=drug_name)
    
# view data
import os
iig_file = drug_name + "_inactive_ingredient_list.txt"
iig_file_path = os.path.join('../iigdata', iig_file)

if os.path.isfile(iig_file_path):
    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df_iig = pd.read_csv(iig_file_path)
    
    
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    from pandasgui import show
    if df_iig is not None:
        drug_name = drug_name.replace('+',' ')
        df_iig_name = {drug_name :df_iig}
        show(**df_iig_name) # show data with pandasgui
else:
    print(f'The {iig_file} not exist in ../iigdata!')

