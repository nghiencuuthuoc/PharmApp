"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
2028-09-09: create
"""

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
    
    

    # export to excel
    if df_iig is not None:
        iig_file_xlsx = drug_name + '_iig.xlsx'
        name_sheet = drug_name + '_iig'
        iig2excel_folder = '../iig2excel'
        path_file_excel_iig = iig2excel_folder +'/' + iig_file_xlsx
        with pd.ExcelWriter(path_file_excel_iig) as writer:
            df_iig.to_excel(writer, sheet_name = name_sheet)
        # os.system('start "excel" path_file_excel_iig')
        path_file_excel_iig_open = 'D:\\PharmApp\\iig2excel'
        full_path_file_excel_iig_open = path_file_excel_iig_open + '\\' + iig_file_xlsx
        os.startfile(full_path_file_excel_iig_open)

    # view pandasgui   
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    from pandasgui import show
    if df_iig is not None:
        drug_name = drug_name.replace('+',' ')
        df_iig_name = {drug_name :df_iig}
        show(**df_iig_name) # show data with pandasgui
else:
    print(f'Inactive ingredient {drug_name} not exist in ../iigdata!')

