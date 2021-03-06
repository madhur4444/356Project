import server

# Delimiter for the request
delim = "$$"

# Suffix to add in user prompt if the field can be left empty
emptySuffix = "(leave empty and press enter if applicable): "

# Helper list to map the user input to fields in the Movies table
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
	"gmd - Get Movie Details",
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

# Calls parseRequest of the server with the input request
def sendRequest(request):
	#print("Sending request!" + request)
	return server.parseRequest(request)

def printChoices(choices):
	for i in range(len(choices)):
		print(str(i + 1) + ". " + str(choices[i]))

# Prints the response it receives as input and also returns it
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

# Function used to get user input.
# This validates the input for security.
# It will be refactored in the future for additional security
# however that is not possible right now due to time contraints.
def getInput(prompt, isRequired, useDelim = True):

	if useDelim:
		inp = delim
	else:
		inp = ""
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
	command = "am" + getInput("Enter the movie name: ", True)
	command += getInput("Enter the date this movie was published ", False)
	command += getInput("Enter the duration ", False)
	command += getInput("Enter the countries where the movie was released separated by commas ", False)
	command += getInput("Enter the languages of your targeted audience separated by commas ", False)
	command += getInput("Enter the director(s), separated by commas(if more than one) ", False)
	command += getInput("Enter the writers separated by commas ", False)
	command += getInput("Enter the production companies, separated by commas(if more than one) ", False)
	command += getInput("Enter the actors and actresses separated by commas ", False)
	command += getInput("Enter the description ", False)
	command += getInput("Enter the budget ", False)
	command += getInput("Enter the gross income - USA ", False)
	command += getInput("Enter the gross income worldwide ", False)
	command += getInput("Enter the number of user reviews ", False)
	command += getInput("Enter the number of critic reviews ", False)
	response = sendRequest(command)

	if not response:
		print("ERR: Something went wrong while adding a movie, try again later!")

	return response

def deleteMovie():
	command = "dm" + getInput("Enter the movie name: ", True)
	response = sendRequest(command)

	if not response:
		print("ERR: Something went wrong while deleting a movie, try again later!")

	return response

def updateMovie():
	command = "um" + getInput("Enter the movie name: ", True)
	print("What would you like to update (enter the number from the list)?: ")

	printChoices(["Name", "Date published", "Duration", "Country", "Language", "Director", "Writer", "Production company", "Actors", "Description", "Budget", "USA Gross Income", "Worldwide Gross Income", "Number of user reviews", "Number of critic reviews"])
	fieldsIdx = int(input()) - 1
	newVal = getInput("Enter the new data ", True, False)
	for field in moviesLayman2Fields[fieldsIdx]:
		command += delim
		command += str(field) + "?=" + str(newVal)
	
	response = sendRequest(command)

	if not response:
		print("ERR: Something went wrong while updating a movie, try again later!")

	return response

# Helper function: It sends a request with an initial command + a parameter of N movies
def execCommandWithNMovies(initialCommand):

	command = initialCommand + getInput("Enter the number of movies: ", True)
	return printResponse(sendRequest(command))

def getMovieDetails():

	command = "gmd" + getInput("Enter the movie name: ", True)
	return printResponse(sendRequest(command))

# While this is a one-line function, it is kept this way for various reasons:
# 1. Readability of user: When user reads the main() function, it is much more
# 	 descriptive to read printTopNMovies() than execCommandWithNMovies() when
# 	 every other command is more readable.
# 2. Scalability: In the future, if the editor of this document
# 	 wants to improve on this and add optional/mandatory arguments from the user,
# 	 it is much easier to do it inside this wrapper function, instead of polluting the main() function.
def printTopNMovies():

	return execCommandWithNMovies("tm")

def printActorsInMovie():

	return execCommandWithNMovies("actm")

def printTopNMoviesByGenre():

	command = "tmg" + getInput("Enter the genre: ", True)
	return execCommandWithNMovies(command)

def printActorsBornToday():

	command = "abt" + getInput("Enter a different month day (mm-dd) if you like otherwise we will use today's date", False)
	return printResponse(sendRequest(command))

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

	command = "tmy" + getInput("Enter the year: ", True)
	return execCommandWithNMovies(command)

def printActedInMoviesXAndY():

	command = "abmxy" + getInput("Enter the name of the first movie: ", True)
	command += getInput("Enter the name of the second movie: ", True)
	return printResponse(sendRequest(command))

# First function for code execution
def main():
	print("Hello, welcome to our movies database manager! Please enter a command")
	printChoices(commandsList)
	responses = []    # List of responses for testing purposes

	# Program only exits when user types e or exit
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
		elif command == "gmd":
			responses.append(getMovieDetails())
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
