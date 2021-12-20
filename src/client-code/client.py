import server

def sendRequest(request):
	print("Sending request!" + request)
	return server.parseRequest(request)

def printChoices(choices):
	for i in range(len(choices)):
		print(str(i) + ". " + str(choices[i]))

def main():
	print("Hello, Please enter a choice!")
	printChoices(["am - Add movie", "dm - Delete movie from db", "r - See movie rating"])
	command = input()
	response = ""
	
	if command == "am":
		command += " "
		command += input("Enter the movie name: ")
		response = sendRequest(command)
		print(response)
		
	return response                 # This is for testing purposes only, if this file is run from the CLI, nothing is returned to the command line

if __name__ == "__main__":
	main()
