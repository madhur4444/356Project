import server

def sendRequest(request):
	print("Sending request!" + request)
	return server.parseRequest(request)

def printChoices(choices):
	for i in range(len(choices)):
		print(str(i + 1) + ". " + str(choices[i]))

def main():
	print("Hello, welcome to our movies database manager! Please enter a command")
	printChoices(["am - Add movie", "dm - Delete movie from db", "r - See movie rating", "e - Exit"])
	while True:
		command = input()
		response = ""
		responses = []    # List of responses for testing purposes
		
		if command == "help" or command == "h":
			printChoices(["am - Add movie", "dm - Delete movie from db", "r - See movie rating", "e - Exit"])
		elif command == "am":
			command += " "
			command += input("Enter the movie name: ")
			response = sendRequest(command)
			print(response)
			responses.append(response)
		elif command == "e" or command == "exit":
			break

		print("\nPlease enter a command, type help or h for the commands!")
		
	return responses                 # This is for testing purposes only, if this file is run from the CLI, nothing is returned to the command line

if __name__ == "__main__":
	main()
