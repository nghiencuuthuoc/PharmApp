"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:

"""
import sys
sys.path.append('..')
# input name
drug_input = str(input("Enter name: "))
# drug_input = 'nexium'
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

drug_name_csv = drug_name + "_inactive_ingredient_list.txt"
drug_name_csv_path = os.path.join('../iigdata', drug_name_csv)

if os.path.isfile(drug_name_csv_path):
    import pandas as pd
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    # df_iig = pd.read_csv(drug_name_csv_path, header=0, delim_whitespace=True)
    df_iig = pd.read_csv(drug_name_csv_path)
    
    
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    from pandasgui import show
    if df_iig is not None:
        drug_name = drug_name.replace('+',' ')
        df_iig_name = {drug_name :df_iig}
        show(**df_iig_name) # show data with pandasgui
        # load Inactive Ingredients Database
        df_inactive_ingredients =  pd.read_csv('../inactive_ingredients/IIR_OCOMM.csv')
        dosage_form = str(input("ENTER DOSAGE FORM: ")) # CAPSULE, DELAYED RELEASE
        # dosage_form = dosage_form.upper()
        df_dosage_form = df_inactive_ingredients[df_inactive_ingredients["DOSAGE_FORM"] == dosage_form]
        route = str(input("ENTER ROUTE: ")) # ORAL
        # route = route.upper()
        df_dosage_form = df_dosage_form[df_dosage_form["ROUTE"] == route]
        df_dosage_form.set_index('UNII', inplace=True)
        df_iig.set_index('UNII', inplace=True)
        df_iig_full = pd.merge(left=df_iig, right=df_dosage_form,
                                      left_index=True, right_index=True)
        
        df_iig_full = df_iig_full.drop(['Inactive'], axis=1)

        # export formulation to excel
        drug_name_replace = drug_name.replace(" ","+")
        file_excel_drug_name = drug_name_replace + '_[' + route + ']_[' + dosage_form + ']_formula.xlsx'
        # name_sheet = drug_name + '_formula_full_export'
        drug_name_short = []
        if len(drug_input) >= 25:
            drug_name_short = drug_input.split()
            drug_name_short = drug_name_short[0]
            drug_name_short = drug_name_short + '_x_'
        else:
            drug_name_short = drug_name
        
        name_sheet = drug_name_short + '_iigf'
        formula_folder = '../FormulaExport'
        path_file_excel_formula = formula_folder +'/' + file_excel_drug_name
        with pd.ExcelWriter(path_file_excel_formula) as writer:
            df_iig_full.to_excel(writer, sheet_name = name_sheet)
        path_file_excel_formula_open = 'D:\\PharmApp\\FormulaExport'
        full_path_file_excel_formula_open = path_file_excel_formula_open + '\\' + file_excel_drug_name
        os.startfile(full_path_file_excel_formula_open)
        # # view dict dataframe
        # df_iig_full = {drug_name :df_iig_full}
        # show(**df_iig_full) # show data with pandasgui
else:
    print(f'Inactive ingredient {drug_name} not exist in iigdata!')





