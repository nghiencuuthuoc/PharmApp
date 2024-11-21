"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
2024-08-04: This code runs correctly

"""

# get_iig_enter_name_pandagui_view_ndcw
# input name
drug_input = str(input("Enter name: "))
drug_name = drug_input.lower().replace(' ', '+').replace('-','+')

# Save file inactive_ingredient_list.txt
import os
print(drug_name)
drug_name_iig_file = drug_name + "_inactive_ingredient_list.txt"
drug_name_iig_filepath = os.path.join('iigdata', drug_name_iig_file)
if os.path.isfile(drug_name_iig_filepath) == True:
    print(f'{drug_name} exist')
else:
    # get iig
    # import src.pharmappiig013 as pa
    import src.pharmappiig016dev as pa
    pa.get_inactive_ingredient(name_drug=drug_name)
    
# view data
import os
drug_name_csv = drug_name + "_inactive_ingredient_list.txt"
drug_name_csv_path = os.path.join('iigdata', drug_name_csv)

if os.path.isfile(drug_name_csv_path):
    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df_iig = pd.read_csv(drug_name_csv_path)
    # full df_iig
    drug_name = drug_name.replace('+',' ')
    df_iig_drug_name = {drug_name :df_iig}
    # Inactive
    df_inactive = df_iig.drop(['NDC','MainDrug','Strength','Formulation','UNII'], axis=1 ,errors = 'ignore')
    df_inactive = df_inactive.drop_duplicates()
    drug_name_inactive = drug_name + "_inactive"
    df_iig_inactive = {drug_name_inactive :df_inactive}
	# MainDrug
    df_maindrug = df_iig.drop(['NDC','Inactive','Strength','Formulation','UNII'], axis=1 ,errors = 'ignore')
    df_maindrug = df_maindrug.drop_duplicates()
    drug_name_maindrug = drug_name + "_maindrug"
    df_iig_maindrug = {drug_name_maindrug :df_maindrug}
	# NDC
    df_ndc = df_iig.drop(['MainDrug','Inactive','Strength','Formulation','UNII'], axis=1 ,errors = 'ignore')
    df_ndc = df_ndc.drop_duplicates()
    drug_name_ndc = drug_name + "_ndc"
    df_iig_ndc = {drug_name_ndc :df_ndc}
	# Strength
    df_strength = df_iig.drop(['NDC','Inactive','MainDrug','Formulation','UNII'], axis=1 ,errors = 'ignore')
    df_strength = df_strength.drop_duplicates()
    drug_name_strength = drug_name + "_strength"
    df_iig_strength = {drug_name_strength :df_strength}
	# UNII
    df_unii = df_iig.drop(['NDC','Inactive','Strength','Formulation','MainDrug'], axis=1 ,errors = 'ignore')
    df_unii = df_unii.drop_duplicates()
    drug_name_unii = drug_name + "_unii"
    df_iig_unii = {drug_name_unii :df_unii}
	# Formulation
    df_formulation = df_iig.drop(['NDC','Inactive','Strength','MainDrug','UNII'], axis=1 ,errors = 'ignore')
    df_formulation = df_formulation.drop_duplicates()
    drug_name_formulation = drug_name + "_formulation"
    df_iig_formulation = {drug_name_formulation :df_formulation}

    # show data with pandasgui
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    from pandasgui import show
    if df_iig is not None:
        show(df_iig_drug_name, df_formulation, df_iig_inactive,df_iig_maindrug,df_iig_ndc,df_iig_strength,
             df_iig_unii)
else:
    print(f'Inactive ingredient {drug_name} not exist in iigdata!')