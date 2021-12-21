import csv
import re

def modifyPlaceOfBirth(countryName):
    countryName = countryName.strip() # Remove front and back whitespaces
    if "[now " in countryName:
        newName = countryName.split("now ")
        newName = newName[1]
        if "]" not in newName:
            print(newName)
        countryName = newName
    if "]" in countryName:
        countryName = countryName.replace("]", "")
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
    genreMap = {}

    with open(csvtobechanged) as csvfile:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(newcsv)
        lines = list(csvreader)
        count = 0
        for line in lines:
            count += 1
            newLine = line
            doNotInclude = []
            if count == 1:
                csvwriter.writerow(newLine)
                continue
            genreMap[line[0]] = line[5]
            datePublished = line[4]
            datePublished = modifyDob(datePublished)
            newLine[4] = datePublished
            lang = line[8]
            if ", None" in lang:
                lang = lang.replace(", None", "")
            elif "None, " in lang:
                lang = lang.replace("None, ", "")
            elif "None" in lang:
                lang = lang.replace("None", "")
            line[8] = lang
            for i in doNotInclude:
                newLine.pop(i)
            csvwriter.writerow(newLine)

    return genreMap

def makeGenres(genreMap):
    fgenre = open('genres.csv', 'w')
    genrewriter = csv.writer(fgenre)
    genrewriter.writerow(['imdb_title_id', 'genre'])
    for key in genreMap:
        line = []
        line.append(key)
        line.append(genreMap[key])
        genrewriter.writerow(line)
    fgenre.close()

def sanitizeGenres():
    fgenre = open('genres.csv', 'r')
    newfgen = open('new_genres.csv', 'w')
    genrereader = csv.reader(fgenre)
    genrewriter = csv.writer(newfgen)
    lines = list(genrereader)
    for line in lines:
        newLines = []
        genre = line[1]
        if "," in genre:
            genreList = genre.split(',')
            for g in genreList:
                g = g.strip()
                newLines.append([line[0], g])
        else:
            newLines.append(line)
        genrewriter.writerows(newLines)

    fgenre.close()

def sanitizeMovieRoles():
    csvtobechanged = 'movieRoles.csv'
    newcsv = open('new_' + csvtobechanged, 'w')

    with open(csvtobechanged) as csvfile:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(newcsv)
        lines = list(csvreader)
        for line in lines:
            newLine = line
            character = line[len(line) - 1]
            if "[" in character:
                character = character.split("[")
                character = character[1]
                character = character.split("]")
                character = character[0]
            if '"' in character:
                character = character.replace('"', '')
            newLine[len(line) - 1] = character
            csvwriter.writerow(newLine)

# sanitizeNames()
# genreMap = sanitizeMovies()
# makeGenres(genreMap)
# sanitizeGenres()
# sanitizeTitlePrincipals()
# sanitizeMovieRoles()
