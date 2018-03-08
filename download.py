import sys
import time
import os
import shutil
from SECEdgar.crawler import SecCrawler 

def get_filings(companyCode, date='20200101', cik=None, count=100): 
    if cik is None:
        with open('company_list.txt', 'r') as f:
            for line in f:
                if companyCode in line:
                    line_arr = line.rstrip().split(' ')
                    cik = line_arr[-1]

    if cik is None:
        print("cik not provided and not found in list. please try again.")
        return

    # create object 
    seccrawler = SecCrawler() 
    seccrawler.filing_10K(str(companyCode), str(cik), str(date), str(count))

    dest_dir = companyCode + "/"
    src_dir = dest_dir + cik + "/10-K/"
    years_downloaded = []

    for old_filename in os.listdir(src_dir):
        parts = old_filename.split('-')
        old_year = parts[1]
        if int(old_year) > 20:
            new_year = '19' + old_year
        else:
            new_year = '20' + old_year

        years_downloaded.append(new_year)
        os.rename(src_dir + old_filename, dest_dir + companyCode + '_10K_' + new_year + '.txt')

    shutil.rmtree(dest_dir + cik + '/')
    return years_downloaded

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_filings(sys.argv[1])
    else:
        get_filings(sys.argv[1], cik=sys.argv[2])
