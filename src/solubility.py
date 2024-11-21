def get_cid(drugname):
    import pubchempy as pcp 
    import re  
    result = pcp.get_compounds(drugname, 'name') # User inputs a unique chemical identifier called a CID
    cid = re.sub("[^0-9]", "", str(result))
    print("PubChem CID of", drugname, "is", cid)
    
def get_solubility(drugname):
    #!/usr/bin/python
    #Author: Nghien Cuu Thuoc / RnD_Pharma_Plus (nghiencuuthuoc@gmail.com)
    """
    This script get solubility
    """
    import pubchempy as pcp 
    import re  
    result = pcp.get_compounds(drugname, 'name') # User inputs a unique chemical identifier called a CID
    cid = re.sub("[^0-9]", "", str(result))
    print("PubChem CID of", drugname, "is", cid)
    
    # get solubility
    
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
                                    return solubility_info