import server

def main():
    testcases = [
        "am$$A$$2021-10-12$$45$$D$$E$$F$$G$$H$$H I$$L$$M$$N$$$$15$$30"
    ]

    expected = [
        "nice"
    ]

    for i in range(len(testcases)):
        server.parseRequest(testcases[i])
        # assert server.parseRequest(testcases[i]) == expected[i]

if __name__ == "__main__":
	main()