"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
view_iig_pdg.py

"""
import sys
sys.path.append('..')
import streamlit as st
import pandas as pd
import os
# Use this function if you want to make the dashboard fit the screen width
# st.set_page_config(layout='wide')

st.set_page_config(
        page_title="view_iig_pdg_st",
        layout="wide",  # Use full width of the browser
        initial_sidebar_state="auto"
    )

# # logo
# st.logo(
#     LOGO_URL_LARGE,
#     link="https://github.com/nghiencuuthuoc/NCT-LOGO/blob/main/NCT_LOGO_1000X1000_20171110%20_02.png",
#     icon_image=LOGO_URL_SMALL,
# )


# st.markdown("<img src='https://raw.githubusercontent.com/nghiencuuthuoc/PharmApp/master/images/PharmApp-logo.png' style='display: block; margin: 0 auto;'>" 
#             , unsafe_allow_html=True)


st.write("""
# PharmApp - Drug Discovery and Development

This app tools for research and development pharmaceutical

See more 👉 [github.com/nghiencuuthuoc/PharmApp](https://github.com/nghiencuuthuoc/PharmApp)
""")

st.write('---')
# st.markdown("<h1 style='text-align: center; color: red;'>Extract Inactive Ingredient Drug on DailyMed</h1>", unsafe_allow_html=True)
st.subheader('Extract Inactive Ingredient Drug on DailyMed')

# st.subheader("Text input")
st.write('---')
# screen next
if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0

placeholder = st.empty()
st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 4))


# drug_input = st.text_input("Enter Drug Name Here")
drug_input = st.text_input("Your enter name:")


# input name
# drug_input = str(input("Enter name: "))
drug_name = drug_input.lower().replace(' ', '+').replace('-','+')


if st.session_state.page == 0:
    # Replace the placeholder with some text:
    # st.write("You enter name: ", drug_input , "!")
    st.write("Loading data of", drug_name, ". Click Next 👉")

elif st.session_state.page == 1:
    # placeholder.text("Check inactive ingredient data")
    st.markdown(""" #### Check inactive ingredient data""")
    # Save file inactive_ingredient_list.txt
    iig_file = drug_name + "_inactive_ingredient_list.txt"
    iig_file_path = os.path.join('../iigdata', iig_file)
    if os.path.isfile(iig_file_path) == True:
        # print(f'{drug_name} exist')
        st.write(f'Data of {drug_name} exist. Click Next 👉')
    else:
        # get iig
        # import src.pharmappiig013 as pa
        # st.write(f'{drug_name} not exist, please wait loading... ')
        import src.pharmappiig017dev as pa
        pa.get_inactive_ingredient(name_drug=drug_name)
        
        if os.path.isfile(iig_file_path) == True:
            st.write(f'{drug_name} load done 😀')
        else:
            st.write(f'{drug_name} not exist. Click Next to Restart 👉')


elif st.session_state.page == 2:
    # Replace the chart with several elements:
    # placeholder.text("View Full Inactive Ingredient Data")
    st.markdown(""" #### View Full Inactive Ingredient Data""")
    # view data
    iig_file = drug_name + "_inactive_ingredient_list.txt"
    iig_file_path = os.path.join('../iigdata', iig_file)

    if os.path.isfile(iig_file_path):
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        df_iig = pd.read_csv(iig_file_path)
        
        if df_iig is not None:
            st.write(f'{drug_name} load done, data here 👇')
            # iig_table = st.table(df_iig)
            st.dataframe(df_iig)
    else:
        st.write(f'{drug_name} not exist. Click Next to Restart 👉')

elif st.session_state.page == 3:
    # placeholder.text("View Inactive and UNII")
    st.markdown(""" #### View Inactive and UNII""")
    # view data column inactive
    iig_file = drug_name + "_inactive_ingredient_list.txt"
    iig_file_path = os.path.join('../iigdata', iig_file)

    if os.path.isfile(iig_file_path):
        df_iig = pd.read_csv(iig_file_path)
        df_inactive = df_iig.drop('NDC', axis=1).drop('MainDrug', axis=1).drop('Strength', axis=1).drop('Formulation', axis=1)
        df_inactive = df_inactive.drop_duplicates()
        st.write(f'Column Inactive and UNII of {drug_name} load done, data here 👇')
        # iig_table = st.table(df_inactive)
        st.dataframe(df_inactive)

    else:
        st.write(f'{drug_name} not exist. Click Restart 👉')

elif st.session_state.page == 4:
    # placeholder.text("From Inactive Ingredient Data Build Formulation")
    st.sidebar.header('Select Dosage Form and Route')
    st.markdown(""" #### From Inactive Ingredient Data Build Formulation""")
    iig_file = drug_name + "_inactive_ingredient_list.txt"
    iig_file_path = os.path.join('../iigdata', iig_file)
    df_iig = pd.read_csv(iig_file_path)

    if df_iig is not None:
        # Load Inactive Ingredients Database
        df_inactive_ingredients =  pd.read_csv('../inactive_ingredients/IIR_OCOMM.csv')


        df_dosage_form = df_inactive_ingredients.drop('INGREDIENT_NAME', axis=1).drop('CAS_NUMBER', axis=1).drop('UNII', axis=1).drop('POTENCY_AMOUNT', axis=1).drop('POTENCY_UNIT', axis=1).drop('MAXIMUM_DAILY_EXPOSURE', axis=1).drop('MAXIMUM_DAILY_EXPOSURE_UNIT', axis=1).drop('RECORD_UPDATED', axis=1).drop('ROUTE', axis=1)
        df_dosage_form = df_dosage_form.drop_duplicates()
        make_choice_dosage_form = st.sidebar.selectbox('Select dosage form:', df_dosage_form)

        df_route = df_inactive_ingredients.drop('INGREDIENT_NAME', axis=1).drop('CAS_NUMBER', axis=1).drop('UNII', axis=1).drop('POTENCY_AMOUNT', axis=1).drop('POTENCY_UNIT', axis=1).drop('MAXIMUM_DAILY_EXPOSURE', axis=1).drop('MAXIMUM_DAILY_EXPOSURE_UNIT', axis=1).drop('RECORD_UPDATED', axis=1).drop('DOSAGE_FORM', axis=1)
        df_route = df_route.drop_duplicates()
        make_choice_route = st.sidebar.selectbox('Select route:', df_route)

        # st.write(f'You choose dosage form: {make_choice_dosage_form} and route: {make_choice_route}')

        # dosage_form = str(input("ENTER DOSAGE FORM: ")) # CAPSULE, DELAYED RELEASE
        # dosage_form = dosage_form.upper()
        df_dosage_form = df_inactive_ingredients[df_inactive_ingredients["DOSAGE_FORM"] == make_choice_dosage_form]
        # route = str(input("ENTER ROUTE: ")) # ORAL
        # route = route.upper()
        df_dosage_form = df_dosage_form[df_dosage_form["ROUTE"] == make_choice_route]

        df_dosage_form.set_index('UNII', inplace=True)
        df_iig.set_index('UNII', inplace=True)
        df_iig_full = pd.merge(left=df_iig, right=df_dosage_form,
                                      left_index=True, right_index=True)
        
        df_iig_full = df_iig_full.drop(['Inactive'], axis=1) 
        # export to excel
        file_excel_drug_name = drug_name + '_formula_full_export.xlsx'
        drug_name_short = []
        if len(drug_input) >= 25:
            drug_name_short = drug_input.split()
            drug_name_short = drug_name_short[0]
            drug_name_short = drug_name_short + '_x_'
        else:
            drug_name_short = drug_name
        # st.write(f'Short name is {drug_name_short}')
        name_sheet = drug_name_short + '_iigf'
        formula_folder = '../FormulaExport'
        path_file_excel_formula = formula_folder +'/' + file_excel_drug_name
        with pd.ExcelWriter(path_file_excel_formula) as writer:
            df_iig_full.to_excel(writer, sheet_name = name_sheet)
        path_file_excel_formula_open = 'D:\\PharmApp\\FormulaExport'
        full_path_file_excel_formula_open = path_file_excel_formula_open + '\\' + file_excel_drug_name
        # os.startfile(full_path_file_excel_formula_open)

        # vivew data streamlit
        st.write(f'Formulation of {drug_name} with dosage form: {make_choice_dosage_form} and route: {make_choice_route} here 👇')
        # iig_table = st.table(df_iig_full)
        st.dataframe(df_iig_full)
else:
    with placeholder:
        st.write(f'Finish view inactive ingredient data of {drug_name}, click restart 😀')
        st.button("Restart",on_click=restart)