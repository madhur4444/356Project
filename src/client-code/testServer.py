import server

def main():
    testcases = [
        "am\nJj\n"
    ]

    expected = [
        "nice"
    ]

    for i in range(len(testcases)):
        assert server.parseRequest(testcases[i]) == expected[i]

if __name__ == "__main__":
	main()