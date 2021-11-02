import os
from datetime import date


def save_to_hwp(content, site, start, end):
    outpath = os.path.join("news", f"{site}_{date.today()}({start}~{end}).hwp")
    f = open(outpath, "w")
    f.write(content)
    f.close()
    return
