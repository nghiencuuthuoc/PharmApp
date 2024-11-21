#!/usr/bin/python
#Author: Nghien Cuu Thuoc / RnD_Pharma_Plus (nghiencuuthuoc@gmail.com)
"""
This script get solubility
"""

import pubchempy as pcp 
import re

# get_cid.py
drugname = input("Enter molecule name (ex: Miconazole nitrate): ")

result = pcp.get_compounds(drugname, 'name') # User inputs a unique chemical identifier called a CID
cid = re.sub("[^0-9]", "", str(result))
print(drugname + "'s PubChem CID is: " + cid)

# get solubility

import requests
r = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/%s/JSON' % cid)
for section in r.json()['Record']['Section']:
    if section.get('TOCHeading') == 'Chemical and Physical Properties':
        for subsection in section['Section']:
            if subsection['TOCHeading'] == 'Experimental Properties':
                for subsubsection in subsection['Section']:
                    if subsubsection['TOCHeading'] == 'Solubility':
                        for s3section in subsubsection["Information"]:
                                print(s3section)
  
