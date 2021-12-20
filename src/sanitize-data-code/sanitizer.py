import csv
import re

def modifyPlaceOfBirth(countryName):
    countryName = countryName.strip() # Remove front and back whitespaces
    if "[now " in countryName:
        newName = countryName.split("now ")
        newName = newName[1]
        if "]" not in newName:
            print(newName)
        newName = newName.split("]")
        newName = newName[0]
        countryName = newName
    countryName = "\'" + countryName + "\'"
    return countryName

def modifyDob(dob):
    dob = dob.strip()
    m = re.search('[0-9][0-9][0-9][0-9](\/|-)[0-9][0-9](\/|-)[0-9][0-9]', dob)
    if m:
        m = m.group(0)
        if "/" in m:
            print(m)
            m = m.replace("/", "-")
        dob = m
    else:
        dob = ""
    return dob

def sanitizeNames():
    csvtobechanged = 'names.csv'
    newcsv = open('new_' + csvtobechanged, 'w')

    with open(csvtobechanged) as csvfile:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(newcsv)
        lines= list(csvreader)
        count = 0
        bcountry = []
        for line in lines:
            count += 1
            newLine = line
            if count == 1:
                csvwriter.writerow(newLine)
                continue
            bcvars = line[7].split(',')
            dcvars = line[10].split(',')
            dob = line[6].split(',')
            dob = modifyDob(dob[len(dob) - 1])
            dod = line[9].split(',')
            dod = modifyDob(dod[len(dod) - 1])
            countryName = bcvars[len(bcvars)-1]
            deathCountry = dcvars[len(dcvars)-1]
            countryName = modifyPlaceOfBirth(countryName)
            deathCountry = modifyPlaceOfBirth(deathCountry)
            newLine[7] = countryName
            newLine[10] = deathCountry
            newLine[6] = dob
            newLine[9] = dod
            csvwriter.writerow(newLine)

def sanitizeMovies():
    csvtobechanged = 'movies.csv'
    newcsv = open('new_' + csvtobechanged, 'w')

    with open(csvtobechanged) as csvfile:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(newcsv)
        lines = list(csvreader)
        count = 0
        for line in lines:
            count += 1
            newLine = line
            if count == 1:
                csvwriter.writerow(newLine)
                continue
            
            csvwriter.writerow(newLine)

sanitizeMovies()
