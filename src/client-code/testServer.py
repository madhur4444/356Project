import server

def main():
    testcases = [
        "am$$A$$2021-10-12$$B$$C$$D$$E$$F$$G$$H$$H, I$$J$$K$$L$$M$$N$$$$O$$P"
    ]

    expected = [
        "nice"
    ]

    for i in range(len(testcases)):
        server.parseRequest(testcases[i])
        # assert server.parseRequest(testcases[i]) == expected[i]

if __name__ == "__main__":
	main()