import download
import compare
import parse
import sys
import os
import shutil

def download_and_process(companyCode, cik=None):
    print companyCode
    with open(companyCode + '_data' + '.txt', 'w') as f:
        f.write("YEAR,COSDIST,JACDIST\n")
        if cik is None:
            years = download.get_filings(companyCode)
        else:
            years = download.get_filings(companyCode, cik=cik)
        
        parse.parse_stock_multiple_years(companyCode, years)

        stockdata = []

        for year_one in years:
            try:
                print str(int(year_one)+1)
                year_two_data = compare.compare_stock(companyCode, year_one, str(int(year_one)+1))
                stockdata.append(str(int(year_one)+1) + ',' + str(year_two_data['cosDist']) + ',' + str(year_two_data['jaccard'])+'\n')
            except:
                pass

        print companyCode
        print stockdata
        f.writelines(stockdata)

    #shutil.rmtree(companyCode)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        download_and_process(sys.argv[1])
    else:
        download_and_process(sys.argv[1], cik=sys.argv[2])