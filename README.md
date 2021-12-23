# ECE 356 Project

This includes the report and all related code in src/

Inside src/, we have the code for sanitizing the csv file, the code for loading the csv file, and the code for the client and server (+ tests for each).

## Dependencies

You may need to install mysql-connector:

`pip3 install mysql-connector-python`

You may need to install datetime:

`pip3 install datetime`

You may need to install re:

`pip3 install re`

## Makefile intructions

make all/make: Starts running the client

make client: Starts running the client

make testClient: Runs the test suite for the client

make testServer: Runs the test suite for the server
