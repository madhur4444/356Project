import server

def sendRequest(request):
	print("Sending request!" + request)
	server.parseRequest(request)

def printChoices(choices):
	for i in range(len(choices)):
		print(str(i) + ". " + str(choices[i]))

def main():
	print("Hello, Please enter a choice!")
	printChoices(["am - Add movie", "dm - Delete movie from db", "r - See movie rating"])
	command = input()
	
	if command == "am":
		command += " "
		command += input("Enter the movie name: ")
		sendRequest(command)

if __name__ == "__main__":
	main()
