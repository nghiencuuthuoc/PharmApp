#epdf.pub_
from os import rename, listdir

fnames = listdir('.')
for fname in fnames:
    if fname.endswith('.lnk'):
        new_name = fname.replace(' - Shortcut', '')
        rename(fname, new_name)

