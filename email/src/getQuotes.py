"""Julia Foote
    This program prompts the user for a stock symbol and outputs the string of all
    the data based on the flags at the end of the URL. Next the program parses those
    data values into their separate flags values using the match function using regular
    expressions. Then it outputs the stripped data into an XML style format."""


import urllib.request
import re

def print_stock_info(str_syms):
    str_url = 'http://finance.yahoo.com/d/quotes.csv?f=sd1t1l1bawmc1vj2&e=.csv'
    str_url = str_url + str_syms

    try:
        f = urllib.request.urlopen(str_url)
    except:
        print("URL access failed:\n" + str_url + "\n")
        return
    for line in f.readlines():
        line = line.decode().strip()
        print(line)

def process_quotes(str_syms):
    """This function takes the users input symbol data which is passed through
    the parameter as the variable 'str_syms' and adds it to the end of the url.
    The data is then parsed through using regular expressions and is then outputted
    in XML format. This function also checks for data that is 'N/A' and ignores
    them when outputting."""
    str_url = 'http://finance.yahoo.com/d/quotes.csv?f=sd1t1l1bawmc1vj2&e=.csv'
    str_url = str_url + str_syms

    try:
        f = urllib.request.urlopen(str_url)
    except:
        print("URL access failed:\n" + str_url + "\n")
        return
    for line in f.readlines():
        line = line.decode().strip()
       # print(line + '\n')

        # matching, manipulations and output of stock data in XML format
        print("<stockQuote>")

        # Matches and outputs qSymbol if not N/A
        m = re.match('.*?([A-Za-z]+).*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qSymbol>" + m.group(1) + "</qSymbol>")

        # Matches and outputs qDate if not N/A
        m = re.match('.*?(\d+[/|-]\d+[/|-]\d+).*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qDate>" + m.group(1) + "</qDate>")

        # Matches and outputs qTime if not N/A
        m = re.match('.*?(\d+[:]\d+[a-z]+).*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qTime>" + m.group(1) + "</qTime>")

        # Matches and outputs qLastSalePrice if not N/A
        m = re.match('.*?(\d+[.]\d+).*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qLastSalePrice>" + m.group(1) + "</qLastSalePrice>")

        # Matches and outputs qBidPrice if not N/A
        m = re.match('.*?\d+[,](\d+[.]\d+)', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qBidPrice>" + m.group(1) + "</qBidPrice>")

        # Matches and outputs qAskPrice if not N/A
        m = re.match('.*?(\d+[.]\d+),"', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qAskPrice>" + m.group(1) + "</qAskPrice>")

        # Matches and outputs q52WeekLow if not N/A
        m = re.match('.*?(\d+[.]\d+)\s[-]', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<q52WeekLow>" + m.group(1) + "</q52WeekLow>")

        # Matches and outputs q52WeekHigh if not N/A
        m = re.match('.*?[-]\s(\d+[.]\d+).*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<q52WeekHigh>" + m.group(1) + "</q52WeekHigh>")

        # Matches and outputs qTodaysLow if not N/A
        m = re.match('.*?","(\d+[.]\d+)\s[-].*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qTodaysLow>" + m.group(1) + "</qTodaysLow>")

        # Matches and outputs qTodaysHigh if not N/A
        m = re.match('.*?[-]\s(\d+[.]\d+)",[+|-].*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qTodaysHigh>" + m.group(1) + "</qTodaysHigh>")

        # Matches and outputs qNetChangePrice if not N/A
        m = re.match('.*?([+|-]\d+[.]\d+).*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qNetChangePrice>" + m.group(1) + "</qNetChangePrice>")

        # Matches and outputs qShareVolumeQty if not N/A
        m = re.match('.*?(\d{5,20}).*?', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qShareVolumeQty>" + (m.group(1)).replace(" ", '').replace(",", '') + "</qShareVolumeQty>")

        # Matches and outputs qTotalOutstandingSharesQty if not N/A
        m = re.match('.*?(\d{5,20}$)', line)
        if m is None:
            print('', end="")
        else:
            print("\t\t<qTotalOutstandingSharesQty>" + (m.group(1)).replace(" ", '').replace(",", '')
                  + "</qTotalOutstandingSharesQty>")

        print("</stockQuote>")


if __name__ == '__main__':
    print("Quotes Processor, Written by Julia Foote")
    print()
    while True:
        sym = input("Enter a Stock Symbol: ")
        if not sym:
            break
        if len(sym) == 0:
            pass
        str_syms = '&s=' + sym
        process_quotes(str_syms)


