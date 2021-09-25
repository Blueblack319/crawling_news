import os
from datetime import date

def save_to_hwp(content, site):
    outpath = os.path.join('news', f'{site}_{date.today()}.hwp')
    f = open(outpath, 'w')
    f.write(content)
    f.close()
    return