import csv

with open('names.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    lines= list(csvreader)
    count = 0
    bcountry = []
    for line in lines:
        bcvars = line[7].split(',')
        bcountry.append(bcvars[len(bcvars)-1])

    print(bcountry)