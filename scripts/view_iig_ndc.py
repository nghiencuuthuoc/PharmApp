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
    
# view data
import os
drug_name_csv = drug_name + "_inactive_ingredient_list.txt"
drug_name_csv_path = os.path.join('../iigdata', drug_name_csv)

if os.path.isfile(drug_name_csv_path):
    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df_iig = pd.read_csv(drug_name_csv_path)
    
    # Browser NDC
    import numpy as np
    import webbrowser  
    ndc_arr = pd.DataFrame(df_iig,columns=['NDC']).to_numpy()
    unique_ndc_arr = np.unique(ndc_arr)
    ndcs = unique_ndc_arr.tolist()
    for ndc in ndcs:
        # url = "https://ndclist.com/ndc/" + ndc
        url = "https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query=" + ndc
        print(url)
        webbrowser.open_new_tab(url)
    
    # view pandasgui
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    from pandasgui import show
    if df_iig is not None:
        df_iig_name = {drug_name :df_iig}
        show(**df_iig_name) # show data with pandasgui
else:
    print(f'Inactive ingredient {drug_name} not exist in ../iigdata!')