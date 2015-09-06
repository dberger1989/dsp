#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv
data = 'football.csv'

def read_data(data):
    fin = open(data, 'rb')
    redata = csv.reader(fin)
    return redata

def get_min_score_difference(parsed_data):
    next(parsed_data)
    for item in parsed_data:
        gdiff = int(item[5]) - int(item[6])
        goal_differentials[item[0]] = (abs(gdiff))
    return min(goal_differentials.values())

def get_team(index_value, parsed_data):
    for item in goal_differentials.keys():
        if goal_differentials[item] == index_value:
            print item 


goal_differentials = {}

read_data(data)

parsed_data =  read_data(data)

get_min_score_difference(parsed_data)

get_team(1, goal_differentials)


