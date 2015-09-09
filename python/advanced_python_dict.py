##########
#Part 3 Question 6
#Creates a dictionary in the appropriate format
import csv
import re

fpath = '/Users/David/ds/metis/prework/dsp/python/faculty.csv'

fin = open(fpath, 'rb')

dictfin = csv.DictReader(fin)
dlist= []
for item in dictfin:
    dlist.append(item)

p = re.compile(r'of\s\S+')
su = []
for item in dlist:
    item[' title'] = p.sub('', item[' title'])

na = re.compile(r'\S\w+$')
for item in dlist:
    item['name'] = na.search(item['name']).group()

lid = {}
for item in dlist:
    nu = {item['name']:[[item[' title'], item[' email']]]}
    if item['name'] not in lid.keys():
        lid[item['name']] = [[item[' title'], item[' email']]]
    else:lid[item['name']].append([item[' title'], item[' email']])
        

print lid

#print first 3 entries:
count = 0
for item in lid.keys():
    if count < 3:
        print item
        print lid[item]
        count += 1


##################
