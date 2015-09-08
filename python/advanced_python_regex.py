#Part 1, Question 1:
#to count how many types of degrees there are:
import csv
import re
fpath = '/Users/David/Desktop/faculty.csv'

fin = open(fpath, 'rb')
firead = csv.reader(fin)
print x[1].replace('.', '') for x[1] in firead

degrees = []
for item in firead:
    subdot = item[1].replace('.', '')
    degrees.append(subdot)

degsp = []
for item in degrees[1:]:
    degsp.append(item.split())

deglist = []
for item in degsp:
    deglist += item

countdict = {x:deglist.count(x)  for x in deglist}
print countdict

###########################

#part 1 q2
#To determine how many types of titles there are:
import csv
fpath = '/Users/David/Desktop/faculty.csv'

fin = open(fpath, 'rb')
dfile = csv.DictReader(fin)

newlist = [item for item in dfile]
titlist = []
for item in newlist[1:]:
    titlist.append(item[' title'])

dictlist = {item: titlist.count(item) for item in titlist}
print dictlist

###########################

#part 1 question q3:
#print emails
import csv
fpath = '/Users/David/Desktop/faculty.csv'

fin = open(fpath, 'rb')
dfile = csv.DictReader(fin)
for item in dfile:
    print item[' email']
    
###########################

#Part 1 Question 4
#Prints the frequencies of the domains
import csv
fpath = '/Users/David/ds/metis/prework/dsp/python/faculty.csv'
import re

fin = open(fpath, 'rb')
dfile = csv.DictReader(fin)


emlist = []
for item in dfile:
    emlist.append(item[' email'])


domains = []
p = re.compile(r'@\S+')
for item in emlist:
    dm = p.findall(item)
    domains.append(dm)

domlist = []
for item in domains:
    domlist += item

domcount = {x: domlist.count(x) for x in domlist}
print domcount


fin = open(fpath, 'rb')
dfile = csv.DictReader(fin)

newlist = [item for item in dfile]
titlist = []
for item in newlist[1:]:
    titlist.append(item[' title'])

dictlist = {item: titlist.count(item) for item in titlist}
print dictlist

#part 1 question q3:
#print emails
import csv
fpath = '/Users/David/Desktop/faculty.csv'

fin = open(fpath, 'rb')
dfile = csv.DictReader(fin)
for item in dfile:
    print item[' email']
>>>>>>> 6bf902591e8dc8a5887bfdbc2c8dd9701701e425

