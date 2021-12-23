import server

delim = "$$"

emptySuffix = "(leave empty and press enter if applicable): "

moviesLayman2Fields = [
	["title", "original_title"],
	["year_of_release", "date_published"],
	["duration"],
	["country"],
	["language"],
	["director"],
	["writer"],
	["production_company"],
	["actors"],
	["description"],
	["budget"],
	["usa_gross_income"],
	["worldwide_gross_income"],
	["reviews_from_users"],
	["reviews_from_critics"]
]

commandsList = [
	"am - Add movie",
	"dm - Delete movie",
	"um - Update movie data",
	"tm - Top N Movies",
	"actm - Actors in a movie",
	"tmg - Top N movies By genre",
	"abt - Actors born today (day and month)",
	"mvus - N highest voted movies in the US",
	"mvo - N highest voted movies in the world",
	"tmxc - Top movies released in a country",
	"lrm - N lowest rated movies",
	"awaxy - Actors who were active in a timeframe (years)",
	"mba - Movies acted by some actor",
	"mdd - Movies directed by some director",
	"tmy - Top N movies of a year",
	"abmxy - Actors who acted in two specific movies",
	"h - See commands list",
	"e - Exit"
]

def sendRequest(request):
	print("Sending request!" + request)
	return server.parseRequest(request)

def printChoices(choices):
	for i in range(len(choices)):
		print(str(i + 1) + ". " + str(choices[i]))

def printResponse(response: dict):

	print("Here is your response!")
	print("*********************")

	# Get number of rows
	for key in response:
		numRows = len(response[key])
		break
	
	for i in range(numRows):
		# Print each column name and value
		for key in response:
			print(str(key) + ": " + str(response[key][i]))
		print("*********************")
	
	return response

def getInput(prompt, isRequired):

	inp = delim
	if isRequired:
		while True:
			temp = input(prompt)
			if temp != "\n":
				inp += temp
				break
	else:
		inp += input(prompt + emptySuffix)
	
	return inp

def addMovie():
	command = "am" + delim + getInput("Enter the movie name: ", True)
	command += delim
	command += input("Enter the date this movie was published " + emptySuffix)
	command += delim
	command += input("Enter the duration " + emptySuffix)
	command += delim
	temp = input("Enter the countries where the movie was released separated by commas " + emptySuffix)
	command += delim
	temp = input("Enter the languages of your targeted audience separated by commas " + emptySuffix)
	command += delim
	temp = input("Enter the director(s), separated by commas(if more than one) " + emptySuffix)
	command += delim
	temp = input("Enter the writers separated by commas " + emptySuffix)
	command += delim
	temp = input("Enter the production companies, separated by commas(if more than one) " + emptySuffix)
	command += delim
	temp = input("Enter the actors and actresses separated by commas " + emptySuffix)
	command += delim
	command += input("Enter the description " + emptySuffix)
	command += delim
	temp = input("Enter the budget " + emptySuffix)
	command += delim
	temp = input("Enter the gross income - USA " + emptySuffix)
	command += delim
	temp = input("Enter the gross income worldwide " + emptySuffix)
	command += delim # Empty field for metascore
	temp = input("Enter the number of user and critic reviews separated by commas " + emptySuffix)
	temp = temp.split(',')
	for c in temp:
		command += delim
		command += c.strip()
	response = sendRequest(command)

	if not response:
		print("ERR: Something went wrong while adding a movie, try again later!")

	return response

def deleteMovie():
	command = "bm" + delim + input("Enter the movie name: ")
	response = sendRequest(command)

	if not response:
		print("ERR: Something went wrong while deleting a movie, try again later!")

	return response

def updateMovie():
	command = "um" + delim + input("Enter the movie name: ")
	print("What would you like to update (enter the number from the list)?: ")

	printChoices(["Name", "Date published", "Duration", "Country", "Language", "Director", "Writer", "Production company", "Actors", "Description", "Budget", "USA Gross Income", "Worldwide Gross Income", "Number of user reviews", "Number of critic reviews"])
	fieldsIdx = int(input()) - 1
	newVal = input("Enter the new data " + emptySuffix)
	for field in moviesLayman2Fields[fieldsIdx]:
		command += delim
		command += str(field) + "?=" + str(newVal)
	
	response = sendRequest(command)

	if not response:
		print("ERR: Something went wrong while updating a movie, try again later!")

	return response

def execCommandWithNMovies(initialCommand):

	command = initialCommand + getInput("Enter the number of movies: ", True)
	return printResponse(sendRequest(command))

def printTopNMovies():

	return execCommandWithNMovies("tm")

def printActorsInMovie():

	return execCommandWithNMovies("actm")

def printTopNMoviesByGenre():

	command = "tmg" + getInput("Enter the genre: ", True)
	return execCommandWithNMovies(command)

def printActorsBornToday():

	return printResponse(sendRequest("abt"))

def printNMostVotedMoviesUS():

	return execCommandWithNMovies("mvus")

def printNMostVotedMoviesOverall():

	return execCommandWithNMovies("mvo")

def printTopNMoviesFromX():

	command = "tmxc" + getInput("Enter the country name: ", True)
	return execCommandWithNMovies(command)

def printNLowestRatedMovies():

	return execCommandWithNMovies("lrm")

def printActedBetweenYearsXAndY():

	command = "awaxy" + getInput("Enter the lowerbound of the years range: ", True)
	command += getInput("Enter the upperbound of the years range: ", True)
	return printResponse(sendRequest(command))

def printMoviesByActor():

	command = "mba" + getInput("Enter the actor's full name: ", True)
	return printResponse(sendRequest(command))

def printMoviesByDirector():

	command = "mdd" + getInput("Enter the director's full name: ", True)
	return printResponse(sendRequest(command))

def printTopNMoviesOfYear():

	command = "tmy" + delim + input("Enter the year: ")
	return execCommandWithNMovies(command)

def printActedInMoviesXAndY():

	command = "abmxy" + delim + input("Enter the name of the first movie: ") + delim
	command += input("Enter the name of the second movie: ")
	return printResponse(sendRequest(command))

def main():
	print("Hello, welcome to our movies database manager! Please enter a command")
	printChoices(commandsList)
	responses = []    # List of responses for testing purposes

	while True:
		command = input()
		
		if command == "help" or command == "h":
			printChoices(commandsList)
		elif command == "e" or command == "exit":
			print("Thank you for using this application!")
			break
		elif command == "am":
			responses.append(addMovie())
		elif command == "dm":
			responses.append(deleteMovie())
		elif command == "um":
			responses.append(updateMovie())
		elif command == "tm":
			responses.append(printTopNMovies())
		elif command == "actm":
			responses.append(printActorsInMovie())
		elif command == "tmg":
			responses.append(printTopNMoviesByGenre())
		elif command == "abt":
			responses.append(printActorsBornToday())
		elif command == "mvus":
			responses.append(printNMostVotedMoviesUS())
		elif command == "mvo":
			responses.append(printNMostVotedMoviesOverall())
		elif command == "tmxc":
			responses.append(printTopNMoviesFromX())
		elif command == "lrm":
			responses.append(printNLowestRatedMovies())
		elif command == "awaxy":
			responses.append(printActedBetweenYearsXAndY())
		elif command == "mba":
			responses.append(printMoviesByActor())
		elif command == "mdd":
			responses.append(printMoviesByDirector())
		elif command == "tmy":
			responses.append(printTopNMoviesOfYear())
		elif command == "abmxy":
			responses.append(printActedInMoviesXAndY())

		print("\nPlease enter a command, type help or h for the commands!")
		
	return responses                 # This is for testing purposes only, if this file is run from the CLI, nothing is returned to the command line

if __name__ == "__main__":
	main()
