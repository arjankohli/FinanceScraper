import urllib

inFile = open("Tickers.txt")
outFile = open("Finished.txt", 'a')
errorFile = open("Errors.txt", 'a')

# Counter for file flushing
i = 0

for line in inFile.readlines():
    # Flush the files every 15 tickers
    i += 1
    if( i % 15 == 0):
        errorFile.flush()
        outFile.flush()

    try:
        download = "http://real-chart.finance.yahoo.com/table.csv?s=" + line.rstrip().string() + "&amp;a=08&amp;b=08&amp;c=1800&amp;d=04&amp;e=11&amp;f=2016&amp;g=w&amp;ignore=.csv"
        urllib.request.urlretrieve(download, "Stocks\\" + line + ".csv")
        print download
    except:
        errorFile.write(str(line))
    else:
        outFile.write(str(line))