import sys
sys.path.append('..')

# input name
# drug_input = str(input("Enter name: "))
drug_input = 'nexium'
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
    # import src.pharmappiig016dev as pa
    import src.pharmappiig017dev as pa
    pa.get_inactive_ingredient(name_drug=drug_name)