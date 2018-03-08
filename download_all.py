import os
import download_and_process

def main():
    with open('company_list.txt', 'r') as f:
        for line in f:
            companyCode = line.split(' ')[0]
            download_and_process.download_and_process(companyCode)

if __name__ == "__main__":
    main()