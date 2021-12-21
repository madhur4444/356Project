import server

emptySuffix = "(leave empty and press enter if applicable): "

def sendRequest(request):
	print("Sending request!" + request)
	return server.parseRequest(request)

def printChoices(choices):
	for i in range(len(choices)):
		print(str(i + 1) + ". " + str(choices[i]))

def addMovie():
	command = "am$$"
	command += input("Enter the movie name: ")
	command += "$$"
	command += input("Enter the date this movie was published " + emptySuffix)
	command += "$$"
	command += input("Enter the genre " + emptySuffix)
	command += "$$"
	command += input("Enter the duration " + emptySuffix)
	temp = input("Enter the country and language of your targeted audience separated by commas " + emptySuffix)
	temp = temp.split(',')
	for c in temp:
		command += "$$"
		command += c.strip()
	temp = input("Enter the director, writer, production company and actors separated by commas " + emptySuffix)
	temp = temp.split(',')
	for c in temp:
		command += "$$"
		command += c.strip()
	command += "$$"
	command += input("Enter the description " + emptySuffix)
	temp = input("Enter the average rating and number of ratings separated by commas " + emptySuffix)
	temp = temp.split(',')
	for c in temp:
		command += "$$"
		command += c.strip()
	temp = input("Enter the budget, and gross income - USA and worldwide, separated by commas " + emptySuffix)
	temp = temp.split(',')
	for c in temp:
		command += "$$"
		command += c.strip()
	command += "$$" # Empty field for metascore
	temp = input("Enter the number of user and critic reviews separated by commas " + emptySuffix)
	temp = temp.split(',')
	for c in temp:
		command += "$$"
		command += c.strip()
	response = sendRequest(command)

	if not response:
		print("ERR: Something went wrong while adding a movie, try again later!")

	return response

def deleteMovie():
	command = "bm$$"
	

def main():
	print("Hello, welcome to our movies database manager! Please enter a command")
	commandsList = ["am - Add movie", "dm - Delete movie", "r - See movie rating", "h - See commands list", "e - Exit"]
	printChoices(commandsList)
	responses = []    # List of responses for testing purposes

	while True:
		command = input()
		
		if command == "help" or command == "h":
			printChoices(commandsList)
		elif command == "e" or command == "exit":
			break
		elif command == "am":
			responses.append(addMovie())
		elif command == "dm":
			responses.append(deleteMovie())

		print("\nPlease enter a command, type help or h for the commands!")
		
	return responses                 # This is for testing purposes only, if this file is run from the CLI, nothing is returned to the command line

if __name__ == "__main__":
	main()
