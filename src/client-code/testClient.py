from io import StringIO
import sys
import client

def main():
    testcases = [
        "am\nJj\n"
    ]

    expected = [
        "nice"
    ]

    for i in range(len(testcases)):
        sys.stdin = StringIO(testcases[i])
        assert client.main() == expected[i]

if __name__ == "__main__":
	main()