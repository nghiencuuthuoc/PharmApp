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
    
    from flask import redirect
    from dtale.app import build_app
    from dtale.views import startup

    if __name__ == '__main__':
        app = build_app(reaper_on=False)

        @app.route("/create-df")
        def create_df():
            instance = startup(data=df_iig, ignore_duplicate=True)
            return redirect(f"/dtale/main/{instance._data_id}", code=302)

        @app.route("/")
        def hello_world():
            return 'Load inactive ingredient data click <a href="/create-df">create-df</a>'

        import webbrowser
        webbrowser.open('http://localhost:8080/')
        app.run(host="0.0.0.0", port=8080)

else:
    print(f'Inactive ingredient {drug_name} not exist in ../iigdata!')



