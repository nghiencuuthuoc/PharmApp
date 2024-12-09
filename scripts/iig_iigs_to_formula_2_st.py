"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
run this code python -m streamlit run [name_this_file.py]

"""
import sys
sys.path.append('..')
import streamlit as st
import pandas as pd
import numpy as np
import os
import xlsxwriter
# Use this function if you want to make the dashboard fit the screen width
# st.set_page_config(layout='wide')

st.set_page_config(
        page_title="PharmApp",
        layout="wide",  # Use full width of the browser
        initial_sidebar_state="auto"
    )

# # logo
# st.logo(
#     LOGO_URL_LARGE,
#     link="https://github.com/nghiencuuthuoc/NCT-LOGO/blob/main/NCT_LOGO_1000X1000_20171110%20_02.png",
#     icon_image=LOGO_URL_SMALL,
# )





st.write("""
# PharmApp - Drug Discovery and Development

🧠 This app tools for research and development pharmaceutical

Copyright 2024 | Nghiên Cứu Thuốc | RD_Pharma_Plus 👉 [github.com/nghiencuuthuoc/PharmApp](https://github.com/nghiencuuthuoc/PharmApp)
""")

# search df
def search(df: pd.DataFrame, substring: str, case: bool = False) -> pd.DataFrame: 
    mask = np.column_stack([df[col].astype(str).str.contains(substring.lower(), case=case, na=False) for col in df])
    return df.loc[mask.any(axis=1)]

# screen next
if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0


st.sidebar.subheader('Input Name')
st.sidebar.write('The Name maybe Compound chemical, Active ingredient, Brandname, Biomedicine, Cosmetic or Nutrition')
drug_input = st.sidebar.text_input("Enter name here:")


# input name
# drug_input = str(input("Enter name: "))
drug_name = drug_input.lower().replace(' ', '+').replace('-','+')



# Short name for sheet name if length than 31 character
if len(drug_name) >= 25:
    drug_name_short = drug_name.split()
    drug_name_short = drug_name_short[0]
    drug_name_short = drug_name_short + '_x_'
else:
    drug_name_short = drug_name

# Replace drug name contain ' ' to +
drug_name_replace = drug_name.replace(" ","+")

# set file inactive ingredient	
iig_txt = drug_name_replace + "_inactive_ingredient_list.txt"
iig_txt_path = os.path.join('../iigdata', iig_txt)
iigs_txt = drug_name_replace + "_iigs.txt"
iigs_txt_path = os.path.join('../iigsdata', iigs_txt)
iig_xlsx = drug_name_replace + '_iig.xlsx'
sheet_iigs = drug_name_short + '_iigs'
sheet_iig = drug_name_short + '_iig'
iig_xlsx_path =  os.path.join('../iig2excel', iig_xlsx)



# save and view iig_xlsx
def save_xlsx(df_iigs):
    # iigs_sheet = drug_name + '_iigs'
    # with pd.ExcelWriter(iig_xlsx, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    #     df_iigs.to_excel(writer, sheet_name = iigs_sheet)
    with pd.ExcelWriter(iig_xlsx_path) as writer:
        df_iigs.to_excel(writer, sheet_name = sheet_iigs)
    # iig_xlsx_open = 'D:\\PharmApp\\iig2excel' + '\\' + iig_xlsx
    # os.startfile(iig_xlsx_open)
    # print(f'{iig_xlsx} saved in iigsdata folder!')

def save_form_iig(df_iig_full):
    # save to csv form
    df_iig_full.to_csv(form_iig_txt_path)
    # export to excel
    with pd.ExcelWriter(form_iig_xlsx_path, engine='openpyxl', mode='a') as writer:
            df_iig_full.to_excel(writer, sheet_name = sheet_iig_form)


def save_form_iigs(df_iigs_full):
    # save to csv form
    df_iigs_full.to_csv(form_iigs_txt_path)
    # export to excel
    with pd.ExcelWriter(form_iigs_xlsx_path, engine='openpyxl', mode='a') as writer:
            df_iigs_full.to_excel(writer, sheet_name = sheet_iigs_form)


placeholder = st.empty()
# st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 4))
st.sidebar.button("Next 👉",on_click=nextpage,disabled=(st.session_state.page > 4))

if st.session_state.page == 0:
    st.markdown("<img src='https://raw.githubusercontent.com/nghiencuuthuoc/PharmApp/master/images/PharmApp-logo.png' style='display: block; margin: 0 auto;'>" 
            , unsafe_allow_html=True)
    st.markdown(""" #### 1. Chemical Information """)
    # st.write("Loading data of", drug_name, ". Click Next 👉")
    # st.write("Loading data of", drug_name, "...")
    # load smiles
    try:    
        import cirpy
        smiles = cirpy.resolve(drug_input, 'smiles')
        if smiles is not None:
            st.markdown(""" ##### 1.1 Smiles """)
            st.write("Smiles of", drug_input,  "is", smiles)
            # st.write(drug_input, smiles)
            st.markdown(""" ##### Structure """)
            # How show high resolution?
            from rdkit import Chem
            from rdkit.Chem import Draw
            # smiles = 'C1=CC(=C(C=C1C2=C(C(=O)C3=C(C=C(C=C3O2)O)O)O)O)O'
            m = Chem.MolFromSmiles(smiles)
            st.write(Draw.MolToImage(m))
        else:
            st.write(f'Smiles {drug_input} not show if Brandname, BioDrug . Click Next 👉')
    except:
        pass


    st.markdown(""" ##### 1.2 Molecular Properties 
        Properties Defined by the Molecular Structure
            - Molecular weight
            - Chemical stability
            - Melting point
            - Solid-state stability
            - Spectral characterization (UV, IR, NMR)
                """)
    drugs_properties_df = pd.read_csv('../physicochemical/' + "FDA_Drugs_Properties.csv", low_memory=False)
    df_prop = search(drugs_properties_df, drug_input)
    st.dataframe(df_prop)

    curated_solubility_dataset_df = pd.read_csv('../solubility/' + "curated-solubility-dataset.csv", low_memory=False)
    curated_solubility_dataset_filted = search(curated_solubility_dataset_df, drug_input)
    st.dataframe(curated_solubility_dataset_filted)

    solubility_data_df = pd.read_csv('../solubility/' + "solubility_data.csv", low_memory=False)
    solubility_data_filted = search(solubility_data_df, drug_input)
    st.dataframe(solubility_data_filted)

    solubility_delaney_processed_df = pd.read_csv('../solubility/' + "solubility_delaney_processed.csv", low_memory=False)
    solubility_delaney_processed_filted = search(solubility_delaney_processed_df, drug_input)
    st.dataframe(solubility_delaney_processed_filted)

    solubility_delaney_df = pd.read_csv('../solubility/' + "solubility_delaney.csv", low_memory=False)
    solubility_delaney_filted = search(solubility_delaney_df, drug_input)
    st.dataframe(solubility_delaney_filted)

    FDA_APPROVED_df = pd.read_csv('../Drugs@FDA/' + "FDA_APPROVED.csv", on_bad_lines='skip', low_memory=False)
    FDA_APPROVED_filted = search(FDA_APPROVED_df, drug_input)
    st.dataframe(FDA_APPROVED_filted)

    # pubchempy get solubility
    # import src.solubility as sol
    # st.write('Solubility data from PubChem')
    # st.write(sol.get_solubility(drug_input))
    st.markdown(""" ##### 1.3 Pubchempy get solubility """)
    # import src.solubility as sol
    # try:
    #     if get_solubility(drug_input) is not None:
    #         st.write('Solubility data from PubChem')
    #         st.write(sol.get_solubility(drug_input))
    # except:
    #     st.write('No data')
    #     pass
    try:
        import pubchempy as pcp 
        import re
        result = pcp.get_compounds(drug_input, 'name') # User inputs a unique chemical identifier called a CID
        cid = re.sub("[^0-9]", "", str(result))
        if cid == '':
            pass
        else:
            # print(drug_input + "'s PubChem CID is: " + cid)
            st.write(drug_input + "'s PubChem CID is: " + cid)
            import requests
            # r = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/%s/JSON' % cid)
            r = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON')
            for section in r.json()['Record']['Section']:
                if section.get('TOCHeading') == 'Chemical and Physical Properties':
                    for subsection in section['Section']:
                        if subsection['TOCHeading'] == 'Experimental Properties':
                            for subsubsection in subsection['Section']:
                                if subsubsection['TOCHeading'] == 'Solubility':
                                    for s3section in subsubsection["Information"]:
                                        solubility_info = s3section
                                        st.write(solubility_info)
    except:
        pass

    st.markdown(""" ##### 1.4 Material Properties 
        Properties Intrinsic to the Material or Particle
            - Salt form
            - Crystal form (XRPD)
            - Crystal habit
            - Particle size
            - Specific surface area
            - Hygroscopicity
                
                """)

    st.markdown(""" ##### 1.5 Material Properties
        Properties Related to Bulk Powders
            - Powder flow
            - Bulk density
            - Wettability
            - Powder
                """)
    st.markdown(""" ##### 2. Drug Approved
        Information about drug approved source:
            - Drugs@FDA Data Files
            - EMC
                """)
    st.markdown(""" ##### 2.1 Drugs@FDA Data Files""")
    Drugs_FDA_2024_df = pd.read_csv('../Drugs@FDA/' + "Drugs_FDA_2024.csv", on_bad_lines='skip', low_memory=False)
    Drugs_FDA_2024_filted = search(Drugs_FDA_2024_df, drug_input)
    st.dataframe(Drugs_FDA_2024_filted)

elif st.session_state.page == 1:
    # placeholder.text("Check inactive ingredient data")
    st.markdown(""" #### 3. Patent Information""")
    orange_book_full_df = pd.read_csv('../orange_book/orange_book_full.csv', on_bad_lines='skip', low_memory=False)
    orange_book_full_filted = search(orange_book_full_df, drug_input)
    st.dataframe(orange_book_full_filted)
    

elif st.session_state.page == 2:
    st.markdown(""" #### 4. All Dosage Form""")
    # Save file inactive_ingredient_list.txt
    if os.path.isfile(iig_txt_path) == True:
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        df_iig = pd.read_csv(iig_txt_path)
        st.markdown(""" ##### 4.1 Dosage Form: DailyMed""")
        st.dataframe(df_iig)
    else:
        import src.pharmappiig017dev as pa
        pa.get_inactive_ingredient(name_drug=drug_name)
        
        if os.path.isfile(iig_txt_path) == True:
                   pd.set_option("display.max_rows", None, "display.max_columns", None)
                   df_iig = pd.read_csv(iig_txt_path)
                   st.markdown(""" ##### 4.1 Dosage Form: DailyMed""")
                   st.dataframe(df_iig)
        else:
            st.write(f'IIG of {drug_input} not exist.')


    if os.path.isfile(iigs_txt_path) == True:
        # st.write(f'{drug_name} exist in iigsdata folder!')
        df_iigs = pd.read_csv(iigs_txt_path)
        save_xlsx(df_iigs)
        st.markdown(""" ##### 4.2 Dosage Form: SageRX""")
        st.dataframe(df_iigs)
        df_product_name = df_iigs['product_name']
        df_product_name.drop_duplicates(inplace=True)
        df_product_name.reset_index(drop=True)
        st.markdown(""" ##### 4.3 Product Name: SageRX""")
        st.dataframe(df_product_name)
    else:
        df_iigs = pd.read_csv('../sagerxdata/products_to_inactive_ingredients.csv', on_bad_lines='skip', low_memory=False)
        columns_to_drop = ['ndc9', 'product_rxcui', 'inactive_ingredient_tty', 'product_tty', 'inactive_ingredient_rxcui', 'inactive_ingredient_tty']
        df_iigs = df_iigs.drop(columns=columns_to_drop)
        df_iigs = search(df_iigs, drug_input)
        df_iigs = df_iigs.reset_index(drop=True)
        df_iigs.to_csv(iigs_txt_path, mode='a', index = False, header=True)
        save_xlsx(df_iigs)
        st.markdown(""" ##### 4.2 Dosage Form: SageRX""")
        st.dataframe(df_iigs)
        df_product_name = df_iigs['product_name']
        df_product_name.drop_duplicates(inplace=True)
        df_product_name.reset_index(drop=True)
        st.markdown(""" ##### 4.3 Product Name: SageRX""")
        st.dataframe(df_product_name)
    
    
elif st.session_state.page == 3:
    # placeholder.text("View Inactive and UNII")
    st.markdown(""" #### 5. View Inactive and UNII""")
    # st.write('---')
    # view data column inactive
    iig_txt = drug_name + "_inactive_ingredient_list.txt"
    iig_txt_path = os.path.join('../iigdata', iig_txt)

    if os.path.isfile(iig_txt_path):
        df_iig = pd.read_csv(iig_txt_path)
        df_inactive = df_iig.drop('NDC', axis=1).drop('MainDrug', axis=1).drop('Strength', axis=1).drop('Formulation', axis=1)
        df_inactive = df_inactive.drop_duplicates()
        df_inactive = df_inactive.reset_index(drop=True)
        # st.write(f'Column Inactive and UNII of {drug_name} load done, data here 👇')
        # iig_table = st.table(df_inactive)
        st.markdown(""" ##### 5.1 List Inactive and UNII: DailyMed Extract """)
        st.dataframe(df_inactive)

    else:
        st.write(f'{drug_name} not exist. Click Restart 👉')
    
    st.markdown(""" ##### 5.2 List Inactive and UNII: SageRX Extract """)
    if os.path.isfile(iigs_txt_path) == True:
        # st.write(f'{drug_name} exist in iigsdata folder!')
        df_iigs = pd.read_csv(iigs_txt_path)
        columns_to_drop = ['ndc', 'product_name', 'active', 'prescribable']
        # columns_to_drop = ['ndc', 'product_name']
        df_iigs_iu = df_iigs.drop(columns=columns_to_drop, errors='ignore')
        df_iigs_iu = df_iigs_iu.reset_index(drop=True)
        st.dataframe(df_iigs_iu)
    else:
        df_iigs = pd.read_csv('../sagerxdata/products_to_inactive_ingredients.csv', on_bad_lines='skip', low_memory=False)
        columns_to_drop = ['ndc9', 'product_rxcui', 'inactive_ingredient_tty', 'product_tty', 'inactive_ingredient_rxcui', 'inactive_ingredient_tty']
        df_iigs = df_iigs.drop(columns=columns_to_drop)
        df_iigs = search(df_iigs, drug_input)
        df_iigs = df_iigs.reset_index(drop=True)
        df_iigs.to_csv(iigs_txt_path, mode='a', index = False, header=True)
        save_xlsx(df_iigs)
        columns_to_drop = ['ndc', 'product_name', 'active', 'prescribable']
        df_iigs_iu = df_iigs.drop(columns=columns_to_drop, errors='ignore')
        df_iigs_iu = df_iigs_iu.reset_index(drop=True)
        st.dataframe(df_iigs_iu)

elif st.session_state.page == 4:
    st.markdown(""" #### 6. Build Formulation """)
    st.sidebar.header('Select Dosage Form and Route')

    # Load Inactive Ingredients Database
    df_inactive_ingredients =  pd.read_csv('../inactive_ingredients/IIR_OCOMM.csv')
    df_dosage_form = df_inactive_ingredients.drop('INGREDIENT_NAME', axis=1).drop('CAS_NUMBER', axis=1).drop('UNII', axis=1).drop('POTENCY_AMOUNT', axis=1).drop('POTENCY_UNIT', axis=1).drop('MAXIMUM_DAILY_EXPOSURE', axis=1).drop('MAXIMUM_DAILY_EXPOSURE_UNIT', axis=1).drop('RECORD_UPDATED', axis=1).drop('ROUTE', axis=1)
    df_dosage_form = df_dosage_form.drop_duplicates()
    make_choice_dosage_form = st.sidebar.selectbox('Select dosage form:', df_dosage_form)
    df_route = df_inactive_ingredients.drop('INGREDIENT_NAME', axis=1).drop('CAS_NUMBER', axis=1).drop('UNII', axis=1).drop('POTENCY_AMOUNT', axis=1).drop('POTENCY_UNIT', axis=1).drop('MAXIMUM_DAILY_EXPOSURE', axis=1).drop('MAXIMUM_DAILY_EXPOSURE_UNIT', axis=1).drop('RECORD_UPDATED', axis=1).drop('DOSAGE_FORM', axis=1)
    df_route = df_route.drop_duplicates()
    make_choice_route = st.sidebar.selectbox('Select route:', df_route)
    df_dosage_form = df_inactive_ingredients[df_inactive_ingredients["DOSAGE_FORM"] == make_choice_dosage_form]
    df_dosage_form = df_dosage_form[df_dosage_form["ROUTE"] == make_choice_route]
    df_dosage_form.set_index('UNII', inplace=True)
    st.write(f'Formulation of {drug_name} with dosage form: {make_choice_dosage_form} and route: {make_choice_route} here 👇')

    st.sidebar.header('Save Formulation')

    # set file name formulation text
    # make_choice_route = ''
    # make_choice_dosage_form = ''
    form_iig_txt = drug_name + '_[' + make_choice_route + ']_[' + make_choice_dosage_form + ']_form_iig.txt'
    form_iig_txt_path = os.path.join('../FormulaExport', form_iig_txt)
    form_iigs_txt = drug_name + '_[' + make_choice_route + ']_[' + make_choice_dosage_form + ']_form_iigs.txt'
    form_iigs_txt_path = os.path.join('../FormulaExport', form_iigs_txt)
    # set file name formulation iigs xlsx
    form_iigs_xlsx = drug_name_replace + '_[' + make_choice_route + ']_[' + make_choice_dosage_form + ']_iigs_form.xlsx'
    sheet_iigs_form = drug_name_short + '_iigs_form' # form abbreviation formulation
    form_iigs_xlsx_path =  os.path.join('../FormulaExport', form_iigs_xlsx)
    # set file name formulation iig xlsx
    form_iig_xlsx = drug_name_replace + '_[' + make_choice_route + ']_[' + make_choice_dosage_form + ']_iig_form.xlsx'
    sheet_iig_form = drug_name_short + '_iig_form' # form abbreviation formulation
    form_iig_xlsx_path =  os.path.join('../FormulaExport', form_iig_xlsx)

    if os.path.isfile(iig_txt_path) == True:
        df_iig = pd.read_csv(iig_txt_path)
        if df_iig is not None:
            # create file iig excel
            st.markdown(""" ##### 6.1 Build Formulation: IIG DailyMed """)     
            df_iig.set_index('UNII', inplace=True)
            df_iig_full = pd.merge(left=df_iig, right=df_dosage_form, left_index=True, right_index=True)
            
            df_iig_full = df_iig_full.drop(['Inactive'], axis=1)

            # vivew data streamlit
            # iig_table = st.table(df_iig_full)
            st.dataframe(df_iig_full)
            # save data
            save_form_iig_button = st.sidebar.button("Save Formulation DailyMed")
            if save_form_iig_button:
                workbook = xlsxwriter.Workbook(form_iig_xlsx_path)
                worksheet = workbook.add_worksheet(drug_name_short)
                row = 0
                col = 0
                worksheet.write(row, col, str(drug_input))
                workbook.close()
                save_form_iig(df_iig_full)
            # clicked = st.button("Click me")
            # # clip button save data
            # df_iig_full.to_csv(form_iig_txt_path)
            # # export to excel
            # with pd.ExcelWriter(form_xlsx_path, engine='openpyxl', mode='a') as writer:
            #     df_iig_full.to_excel(writer, sheet_name = sheet_iig_form)
            # with pd.ExcelWriter(form_xlsx_path) as writer:
            #     df_iig_full.to_excel(writer, sheet_name = sheet_iig_form)

            # this open file xlsx
            # form_xlsx_path_open = 'D:\\PharmApp\\FormulaExport'
            # os.startfile(form_xlsx_path_open)
    else:
        st.write(f'Data iig {drug_input} not exist. Click Next to Restart 👉')


    
    if os.path.isfile(iigs_txt_path) == True:

        st.markdown(""" ##### 6.2 Build Formulation: IIG SageRX """)
        # st.write(f'{drug_name} exist in iigsdata folder!')
        df_iigs = pd.read_csv(iigs_txt_path)
        columns_to_drop = ['active', 'prescribable']
        df_iigs = df_iigs.drop(columns=columns_to_drop, errors='ignore')
        df_iigs = df_iigs.rename(columns={'inactive_ingredient_unii': 'UNII', 'inactive_ingredient_name': 'INGREDIENT_NAME'})
        df_iigs = df_iigs.set_index('UNII')
        df_iigs_full = pd.merge(left=df_iigs, right=df_dosage_form,
                                    left_index=True, right_index=True)
        

        # vivew data streamlit
        # iig_table = st.table(df_iig_full)
        st.dataframe(df_iigs_full)
        
        # save data
        save_form_iigs_button = st.sidebar.button("Save Formulation SageRX")
        if save_form_iigs_button:
            # create file iigs excel
            workbook = xlsxwriter.Workbook(form_iigs_xlsx_path)
            worksheet = workbook.add_worksheet(drug_name_short)
            row = 0
            col = 0
            worksheet.write(row, col, str(drug_input))
            workbook.close()
            save_form_iigs(df_iigs_full)
        # clicked = st.button("Click me")
        # save csv form
        # df_iigs_full.to_csv(form_iigs_txt_path)
        # export to excel
        # with pd.ExcelWriter(form_xlsx_path, engine='openpyxl', mode='a') as writer:
        #         df_iigs_full.to_excel(writer, sheet_name = sheet_iigs_form)
        # with pd.ExcelWriter(form_xlsx_path) as writer:
        #     df_iigs_full.to_excel(writer, sheet_name = sheet_iigs_form)

        # this open file xlsx
        # form_xlsx_path_open = 'D:\\PharmApp\\FormulaExport'
        # os.startfile(form_xlsx_path_open)
        
    else:
        st.markdown(""" ##### 6.2 Build Formulation: IIG SageRX """)
        df_iigs = pd.read_csv('../sagerxdata/products_to_inactive_ingredients.csv', on_bad_lines='skip', low_memory=False)
        columns_to_drop = ['ndc9', 'product_rxcui', 'inactive_ingredient_tty', 'product_tty', 'inactive_ingredient_rxcui', 'inactive_ingredient_tty', 'active', 'prescribable']
        df_iigs = df_iigs.drop(columns=columns_to_drop)
        df_iigs = search(df_iigs, drug_input)
        df_iigs = df_iigs.reset_index(drop=True)
        df_iigs.to_csv(iigs_txt_path, mode='a', index = False, header=True)
        save_xlsx(df_iigs)
        df_iigs = df_iigs.rename(columns={'inactive_ingredient_unii': 'UNII', 'inactive_ingredient_name': 'INGREDIENT_NAME'})
        df_iigs = df_iigs.set_index('UNII')
        df_iigs_full = pd.merge(left=df_iigs, right=df_dosage_form,
                                    left_index=True, right_index=True)
        
        # vivew data streamlit
        # iig_table = st.table(df_iig_full)
        st.dataframe(df_iigs_full)
        # save data
        save_form_iigs_button = st.sidebar.button("Save Formulation SageRX")
        if save_form_iigs_button:
            # create file iigs excel
            workbook = xlsxwriter.Workbook(form_iigs_xlsx_path)
            worksheet = workbook.add_worksheet(drug_name_short)
            row = 0
            col = 0
            worksheet.write(row, col, str(drug_input))
            workbook.close()
            save_form_iigs(df_iigs_full)
        # clicked = st.button("Click me")
        # # save to csv form
        # df_iigs_full.to_csv(form_iigs_txt_path)
        # # export to excel
        # with pd.ExcelWriter(form_xlsx_path, engine='openpyxl', mode='a') as writer:
        #         df_iigs_full.to_excel(writer, sheet_name = sheet_iigs_form)

        # with pd.ExcelWriter(form_xlsx_path) as writer:
        #     df_iigs_full.to_excel(writer, sheet_name = sheet_iigs_form)

        # this open file xlsx
        # form_xlsx_path_open = 'D:\\PharmApp\\FormulaExport'
        # os.startfile(form_xlsx_path_open)

else:
    with placeholder:
        st.write(f'Finish view inactive ingredient data of {drug_input}, click Restart 😀')
        # st.button("Restart",on_click=restart)
        st.sidebar.button("Restart",on_click=restart)

# drug test
# Enbrel
