import csv
from datetime import datetime

        
with open('HourPrices.csv','r') as csvin, open('HourPrices.txt', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)
        
with open('Prime-Relic Data.csv','r') as csvin, open('Prime-Relic Data.txt', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')

    for row in csvin:
        tsvout.writerow(row)
        
sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
log = 'log.txt'
with open('log.txt','r') as X:
    csvin.write(sttime)