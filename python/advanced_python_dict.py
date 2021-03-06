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


###########
#paart 3 question 7
# prints dictionary with firt name and last name as strings:
import csv
import re

fpath = '/Users/David/ds/metis/prework/dsp/python/faculty.csv'

fin = open(fpath, 'rb')

dictfin = csv.DictReader(fin)
dlist= []
for item in dictfin:
    dlist.append(item)

for item in dlist:
    item['name'] = tuple(item['name'].split())
    

p = re.compile(r'of\s\S+')
su = []
for item in dlist:
    item[' title'] = p.sub('', item[' title'])


lid = {}
for item in dlist:
    nu = {item['name']:[[item[' title'], item[' email']]]}
    if item['name'] not in lid.keys():
        lid[item['name']] = [item[' title'], item[' email']]
    else:lid[item['name']].append([item[' title'], item[' email']])
                

count = 0
for item in lid.keys():
    if count < 3:
        print item
        print lid[item]
        count += 1
        
############
# Part 3 Question 8
# Prints the first 3 entries sorted by last name. 

import csv
import re

fpath = '/Users/David/ds/metis/prework/dsp/python/faculty.csv'

fin = open(fpath, 'rb')

dictfin = csv.DictReader(fin)
dlist= []
for item in dictfin:
    dlist.append(item)

for item in dlist:
    item['name'] = tuple(item['name'].split())
    
p = re.compile(r'of\s\S+')
su = []
for item in dlist:
    item[' title'] = p.sub('', item[' title'])

lid = {}
for item in dlist:
    nu = {item['name']:[[item[' title'], item[' email']]]}
    if item['name'] not in lid.keys():
        lid[item['name']] = [item[' title'], item[' email']]
    else:lid[item['name']].append([item[' title'], item[' email']])

slid = sorted(lid, key=lambda x:x[-1])

ndic = {}
for item in slid[:3]:
    ndic[item] = lid[item]
    print item, ndic[item]




