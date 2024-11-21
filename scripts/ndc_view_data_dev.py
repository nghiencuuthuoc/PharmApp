# view multi drug with pandasgui
import os
import shutil
import pandas as pd
from pandasgui import show
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

folder_path = '../ndcdata'
txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

dataframes = {}
for txt_file in txt_files:
    file_path = os.path.join(folder_path, txt_file)
    df = pd.read_csv(file_path, delimiter=','rb')  
    key = os.path.splitext(txt_file)[0]
    dataframes[key] = df
  
for key, df in dataframes.items():
    print(f"DataFrame for {key}")
    # print(df.head())
gui = show(**dataframes)