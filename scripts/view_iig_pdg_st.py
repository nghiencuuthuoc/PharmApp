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



# st.markdown(
#         '<img src="https://raw.githubusercontent.com/nghiencuuthuoc/PharmApp/master/images/PharmApp-logo.png" height="400" style="border: 5px solid orange">',
#         unsafe_allow_html=True,
#     )


# st.markdown(
#         '<img src="https://raw.githubusercontent.com/nghiencuuthuoc/PharmApp/master/images/PharmApp-logo.png" style="border: 5px solid orange">',
#         unsafe_allow_html=True,
#     )


st.markdown("<img src='https://raw.githubusercontent.com/nghiencuuthuoc/PharmApp/master/images/PharmApp-logo.png' style='display: block; margin: 0 auto;'>" 
            , unsafe_allow_html=True)


# st.title("Extract Inactive Ingredient Drug on DailyMed")
# st.header("Extract Inactive Ingredient Drug on DailyMed")

import streamlit as st
st.markdown("<h1 style='text-align: center; color: red;'>Extract Inactive Ingredient Drug on DailyMed</h1>", unsafe_allow_html=True)

# st.subheader("Text input")

# screen next
if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def restart(): st.session_state.page = 0

placeholder = st.empty()
st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 3))


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
    placeholder.text("Check inactive ingredient data")
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
    placeholder.text("View full inactive ingredient data")
    # view data
    iig_file = drug_name + "_inactive_ingredient_list.txt"
    iig_file_path = os.path.join('../iigdata', iig_file)

    if os.path.isfile(iig_file_path):
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        df_iig = pd.read_csv(iig_file_path)
        
        if df_iig is not None:
            st.write(f'{drug_name} load done, data here 👇')
            iig_table = st.table(df_iig)
    else:
        st.write(f'{drug_name} not exist. Click Next to Restart 👉')

elif st.session_state.page == 3:
    placeholder.text("View Inactive and UNII")
    # view data column inactive
    iig_file = drug_name + "_inactive_ingredient_list.txt"
    iig_file_path = os.path.join('../iigdata', iig_file)

    if os.path.isfile(iig_file_path):
        df_iig = pd.read_csv(iig_file_path)
        df_inactive = df_iig.drop('NDC', axis=1).drop('MainDrug', axis=1).drop('Strength', axis=1).drop('Formulation', axis=1)
        df_inactive = df_inactive.drop_duplicates()
        st.write(f'Column Inactive and UNII of {drug_name} load done, data here 👇')
        iig_table = st.table(df_inactive)
    else:
        st.write(f'{drug_name} not exist. Click Restart 👉')

else:
    with placeholder:
        st.write(f'Finish view inactive ingredient data of {drug_name}, click restart 😀')
        st.button("Restart",on_click=restart)