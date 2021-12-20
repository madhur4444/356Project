import server

def main():
    testcases = [
        "am\nJj\n"
    ]

    for tc in testcases:
        server.parseRequest(tc)

if __name__ == "__main__":
	main()