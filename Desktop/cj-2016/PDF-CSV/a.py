import requests
from os.path import basename
urls = [
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn12.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn13.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn14.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/WARN_Interim_041614_to_063014.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/WARNReportfor7-1-2014to06-30-2015.pdf',
    'http://www.edd.ca.gov/jobs_and_training/warn/WARN-Report-for-7-1-2015-to-03-25-2016.pdf'
]

for url in urls:
    pdf_fname = 'CAWARN-' + basename(url)
    print("Downloading", url, 'into', pdf_fname)
    resp = requests.get(url)
    with open(pdf_fname, 'wb') as f:
        f.write(resp.content)

from glob import glob
pdf_filenames = glob('CAWARN-*.pdf')
for pdf_fname in pdf_filenames:
    print("This is a filename of a pdf:", pdf_fname)

import csv
import pdfplumber

outfile = open('CAWARN12.csv', 'w')
outcsv = csv.writer(outfile)

pdf_fname12 = 'CAWARN-eddwarncn12.pdf'

pdf = pdfplumber.open(pdf_fname12)
page = pdf.pages

for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  
        outcsv.writerow(row)
outfile.close

outfile = open('CAWARN13.csv', 'w')
outcsv = csv.writer(outfile)

pdf_fname13 = 'CAWARN-eddwarncn13.pdf'

pdf = pdfplumber.open(pdf_fname13)
page = pdf.pages

for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  
        outcsv.writerow(row)
outfile.close

outfile = open('CAWARN14.csv', 'w')
outcsv = csv.writer(outfile)

pdf_fname14 = 'CAWARN-eddwarncn14.pdf'

pdf = pdfplumber.open(pdf_fname14)
page = pdf.pages

for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  
        outcsv.writerow(row)
outfile.close

outfile = open('CAWARN1415.csv', 'w')
outcsv = csv.writer(outfile)

pdf_fname1415 = 'CAWARN-WARNReportfor7-1-2014to06-30-2015.pdf'

pdf = pdfplumber.open(pdf_fname1415)
page = pdf.pages

for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  
        outcsv.writerow(row)
outfile.close

outfile = open('CAWARN1516.csv', 'w')
outcsv = csv.writer(outfile)

pdf_fname1516 = 'CAWARN-WARN-Report-for-7-1-2015-to-03-25-2016.pdf'

pdf = pdfplumber.open(pdf_fname1516)
page = pdf.pages

for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  
        outcsv.writerow(row)
outfile.close

