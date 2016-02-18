# Contains analysis of the nycjobs and find insights



import sys
import os
from collections import Counter
import csv
from datetime import datetime
import numpy as np

# parameter: tuple or list
# returns: the last elementt of a list or a tuple
def last_key(item):
    return item[-1]

# parameter: reads the nyc jobs input file
# returns: The Department with the minimum and the maximum salary
def get_maxMinSalary(file):
    csvfile = csv.DictReader(open(file))
    depsalary = [(row['Agency'], row['Salary Range To']) for row in csvfile]
    depsalary = sorted(depsalary, key = last_key)
    print "The Department with the Minimum salary is : ", depsalary[0]
    print "The Department with the Maximum salary is : ", depsalary[-1]

    return depsalary[0], depsalary[-1]


# parameter : reads the nyc jobs input file
# returns: The department name with maximum number of jobs.
def get_maxJobCount(file):
    csvfile = csv.DictReader(open(file))
    maxjobcount = Counter()
    for row in csvfile:
        if row['Agency'] not in maxjobcount.keys():
            maxjobcount[row['Agency']] = int(row['# Of Positions'])
        else:
            maxjobcount[row['Agency']] = maxjobcount[row['Agency']] + int(row['# Of Positions'])
    jobcount = []
    for k,v in maxjobcount.items():
        jobcount.append((k,v))
    maxjobcount = sorted(jobcount, key = last_key)
    print "The Department with the most Job Openings is : ", maxjobcount[-1]
    return maxjobcount

def find_driving_variable(file, column, field):
    csvfile = csv.DictReader(open(file))
    date_difference = [datetime.strptime(row['Posting Updated'], '%m/%d/%Y %H:%M:%S') - 
        datetime.strptime(row['Posting Date'],'%m/%d/%Y %H:%M:%S') 
        for row in csvfile if row[column] == field]
    difference_list = [row.days for row in date_difference]
    mean_difference = np.mean(difference_list)
    print "The average difference in days between the posting updated and posting created is : ", mean_difference

    return difference_list, mean_difference


# Call the functions to get the respective functions
def main():
    file = sys.argv[1]
    get_maxJobCount(file)
    get_maxMinSalary(file)
    find_driving_variable(file, 'Posting Type', 'Internal')


# Boiler plate code to call main
if __name__ == '__main__':
    main()
