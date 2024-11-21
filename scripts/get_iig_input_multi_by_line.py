
"""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PharmApp // Copyright 2024 // NGHIEN CUU THUOC // RnD PHARMA PLUS // WWW.NGHIENCUUTHUOC.COM
Email: nghiencuuthuoc@gmail.com // Facebook: https://facebook.com/nghiencuuthuoc
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note dev:
2024-08-01:Input multi names with (",")
2024-08-04: This code runs correctly
2028-08-28: move to scripts and paiig17dev

"""

import os
import sys
sys.path.append('..')
comma = "+---------------------------+---------------------------+"
drugs_input = str(input("Enter name: "))
# drug name
drugs_input = drugs_input.lower().replace(', ', ',')
drugs = drugs_input.split(",")
# get inactive ingredient
import src.pharmappiig017dev as pa
for drug in drugs:
    try:
        drug_name = drug.lower().replace(' ', '+').replace('-','+')
        drug_name_iig_file = drug_name + "_inactive_ingredient_list.txt"
        drug_name_iig_filepath = os.path.join('../iigdata', drug_name_iig_file)
        if os.path.isfile(drug_name_iig_filepath) == True:
            print(f'{drug} exist')
            print(comma)
        else:
            print(drug)
            pa.get_inactive_ingredient(name_drug=drug_name)
            print(f'{drug_name} done!')
            print(comma)
    except:
        print(f'{drug} run error')
        print(comma)
        pass
