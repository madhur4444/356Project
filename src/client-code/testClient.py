from io import StringIO
import sys
import client

def main():
    testcases = [
        "am\nJj\n"
    ]

    for tc in testcases:
        sys.stdin = StringIO(tc)
        client.main()

if __name__ == "__main__":
	main()