import csv
fpath = '/Users/David/ds/metis/prework/dsp/python/faculty.csv'
import re

fin = open(fpath, 'rb')
dfile = csv.DictReader(fin)


emlist = []
for item in dfile:
    emlist.append(item[' email'])

emsublists = [[item] for item in emlist]


tfile = open('email_list.csv', 'wb') 

csv_writer = csv.writer(tfile)

csv_writer.writerows(emsublists)

tfile.close()
