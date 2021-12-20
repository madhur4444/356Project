import csv

newcsv = open('new_names.csv')

with open('names.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    csvwriter = csv.writer(newcsv)
    lines= list(csvreader)
    count = 0
    bcountry = []
    for line in lines:
        count += 1
        newLine = line
        bcvars = line[7].split(',')
        countryName = bcvars[len(bcvars)-1]
        countryName = countryName.strip() # Remove front and back whitespaces
        if "[now " in countryName:
            newName = countryName.split("now ")
            newName = newName[1]
            if "]" not in newName:
                print(newName)
            newName = newName.split("]")
            newName = newName[0]
            countryName = newName
        newLine[7] = countryName
        if (count < 3):
            print(newLine)