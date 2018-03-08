import re
import sys

def parse_stock(stock_name, year):
    # input AAPL 2017, open Tickers/AAPL/AAPL10k2017
    f = open(stock_name + '/'+ stock_name + '_10K_' + year + '.txt', 'r')
    # write to Tickers/AAPL/AAPL10k1A2017
    g = open(stock_name + '/'+ stock_name + '_10K_1A_' + year + '.txt', 'w')

    # get string of 10k html
    s = f.read()
    # remove newlines
    s = re.sub('\n', ' ', s)
    # remove &nbsp; special chars
    s = re.sub(r'&nbsp;', ' ', s)
    # find all Item tags, replace with >!!!!! for easy location later
    s = re.sub(r'(?s)(?i)(?m)> +Item|>Item|^Item', '>!!!!!', s)
    # remove other special chars
    s = re.sub(r'&[#a-zA-Z0-9]*;', ' ', s)
    # remove HTML divs/tables/other elements
    s = re.sub(r'<[a-zA-Z0-9=:;\"\'-\.\s_#?%/]*>', ' ', s)
    # remove unnecessary whitespace
    s = re.sub(r'\s+', ' ', s)
    # break into sections, by !!!!!
    t = s.split('!!!!!')

    # find section 1A (risk factors), and write to new file
    for u in t:
        if (u[: 3] == ' 1A'):
            g.write(u)

def parse_stock_multiple_years(stock_name, years):
    for year in years:
        parse_stock(stock_name, year)

if __name__ == "__main__":
    parse_stock(sys.argv[1], sys.argv[2])
