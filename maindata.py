import csvdata
import urldata
import symbols
import sys


# This function will take symbol go to the URl and downloads data
# and prints the required computated data
def main():
    try:
        symbol=symbols.symbol_name()                                        #getting symbols from the excel sheet
    except UnboundLocalError:
        print "symbol not found"
        sys.exit(0)
    company_url="https://in.finance.yahoo.com/q/hp?s="+symbol+"&ql=0"
    urldata.get_csvfile(company_url)                                    #downloading csvfile


    high=csvdata.high_price("test.csv")                                 #getting highest and lowest in the file
    date_of_high=csvdata.date_of_value(high)
    print "The highest price for the stock %s is %f on %s"%(symbol,high,date_of_high)
    low=csvdata.low_price("test.csv")
    date_of_low=csvdata.date_of_value(low)
    print "The lowest price for the stock %s is %f on %s"%(symbol,low,date_of_low)
    

if __name__ == '__main__':
    main()
