import requests
from os.path import basename

url = 'http://www2.illinoisworknet.com/DownloadPrint/December%202015%20Monthly%20WARN%20Report.pdf'


pdf_fname = 'ILWARN-' + basename(url)
print("Downloading", url, 'into', pdf_fname)
resp = requests.get(url)
with open(pdf_fname, 'wb') as f:
    f.write(resp.content)

from glob import glob
pdf_filename = glob('ILWARN-*.pdf')
for pdf_fname in pdf_filename:
    print("This is a filename of a pdf:", pdf_fname)

import csv
import pdfplumber

outfile = open('ILWARN.csv', 'w')
outcsv = csv.writer(outfile)

pdf_fnameDEC = 'ILWARN-December%202015%20Monthly%20WARN%20Report.pdf'

pdf = pdfplumber.open(pdf_fnameDEC)
page = pdf.pages

for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  
        outcsv.writerow(row)
outfile.close