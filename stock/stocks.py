import csv
import os
from urllib.request import urlopen

current_dir = os.getcwd()
raw_path = current_dir + '/Raw/'

urls = [
    'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1607792592&period2=1639328592&interval=1d&events=history&includeAdjustedClose=true',
    'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1607792604&period2=1639328604&interval=1d&events=history&includeAdjustedClose=true',
    'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1607792692&period2=1639328692&interval=1d&events=history&includeAdjustedClose=true'
]
raw_file_name = dict(GOOG='GOOG.csv', IBM='IBM.csv', MSFT='MSFT.csv')
GOOG = 'GOOG'
IBM = 'IBM'
MSFT = 'MSFT'


def raw_writer(url, filename):
    local_path = os.path.join(raw_path, filename)
    with urlopen(url) as file, open(local_path, 'wb') as f:
        f.write(file.read())


for url in urls:
    if GOOG in url:
        raw_writer(url, raw_file_name[GOOG])
    if IBM in url:
        raw_writer(url, raw_file_name[IBM])
    if MSFT in url:
        raw_writer(url, raw_file_name[MSFT])

files = [os.path.join(raw_path, file)
         for file in os.listdir(raw_path)
         if file.endswith('.csv')]

for file in files:
    output = os.path.join(current_dir + '/Results/', file.rpartition('/')[-1].partition('.')[0] + '_out.csv')
    with open(file, 'r', encoding='utf-8') as f_in, open(output, 'w', newline='', encoding='utf-8') as f_out:
        dict_reader = csv.DictReader(f_in, delimiter=',')
        headers = dict_reader.fieldnames
        headers.append('Change')
        dict_writer = csv.DictWriter(f_out, delimiter=',', fieldnames=headers)
        dict_writer.writeheader()
        for row in dict_reader:
            change = '{:.6f}'.format((float(row['Close']) - float(row['Open'])) / float(row['Open']))
            row['Change'] = change
            dict_writer.writerow(row)
