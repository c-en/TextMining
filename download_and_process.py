import download
import compare
import parse
import sys
import os
import shutil

def download_and_process(companyCode, cik=None):
    print companyCode

    if cik is None:
        years = download.get_filings(companyCode)
    else:
        years = download.get_filings(companyCode, cik=cik)

    parse.parse_stock_multiple_years(companyCode, years)

    folder = 'Data/'
    try:
        os.makedirs(os.path.dirname(folder))
    except:
        pass

    print sorted(years)

    for year_one in set(years):
        try:
            print year_one
            print str(int(year_one)+1)
            year_two_data = compare.compare_stock(companyCode, year_one, str(int(year_one)+1))
            stockdata = companyCode + ',' + str(year_two_data['cosDist']) + ',' + str(year_two_data['jaccard'])+'\n'

            print "Writing"
            filepath = folder + year_one + '_data.txt'
            if not os.path.isfile(filepath):
                with open(filepath, 'w') as f:
                    f.write("TICKER,COSDIST,JACDIST\n")
            with open(filepath, 'a') as f:
                f.write(stockdata)
        except Exception as err:
            print (err)
            pass

    try:
        shutil.rmtree(companyCode + '/')
    except Exception as err:
        print (err)
        pass


if __name__ == "__main__":
    if len(sys.argv) == 2:
        download_and_process(sys.argv[1])
    else:
        download_and_process(sys.argv[1], cik=sys.argv[2])