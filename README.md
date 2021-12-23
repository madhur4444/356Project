# ECE 356 Project

This includes the report and all related code in src/

Inside src/, we have the code for sanitizing the csv file, the code for loading the csv file, and the code for the client and server (+ tests for each).

## [**Click for link to ECE 356 Video Demo**](https://drive.google.com/drive/folders/14APdPcb03vSUuKKOA5jyZMM9ycsS5ddD)

## Dependencies

You may need to install mysql-connector:

`pip3 install mysql-connector-python`

You may need to install datetime:

`pip3 install datetime`

You may need to install re:

`pip3 install re`

## Instructions (How to use the client)

`$ make` or `$ make all`: Starts running the client

`$ make client`: Starts running the client

`$ make test`: Runs the test suite for the client and the server

`$ make testClient`: Runs the test suite for the client

`$ make testServer`: Runs the test suite for the server
