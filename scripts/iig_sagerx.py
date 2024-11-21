import sys
sys.path.append('..')
# import os
# os.getcwd()
import pandas as pd
import numpy as np
import pickle

# inactive_ingredients_sagerx = pd.read_csv("../sagerxdata/products_to_inactive_ingredients.csv", low_memory=False)
# # inactive_ingredients_sagerx.head()
# # Save
# inactive_ingredients_sagerx.to_pickle('../pickle/inactive_ingredients_sagerx.pickle')

inactive_ingredients_sagerx = pd.read_pickle('../pickle/inactive_ingredients_sagerx.pickle')

columns_to_drop = ['ndc9', 'product_rxcui', 'inactive_ingredient_tty', 'product_tty', 'inactive_ingredient_rxcui', 'inactive_ingredient_tty']
inactive_ingredients_sagerx = inactive_ingredients_sagerx.drop(columns=columns_to_drop)

def search(df: pd.DataFrame, substring: str, case: bool = False) -> pd.DataFrame: 
    mask = np.column_stack([df[col].astype(str).str.contains(substring.lower(), case=case, na=False) for col in df])
    return df.loc[mask.any(axis=1)]

df = inactive_ingredients_sagerx
drug_name = str(input("Enter drug name: "))
# drug_name = 'nexium'
df_iigs = search(df, drug_name)
from pandasgui import show
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
if df_iigs is not None:
    df_iigs = {drug_name :df_iigs}
    show(**df_iigs) # show data with pandasgui

