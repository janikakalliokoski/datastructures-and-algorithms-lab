# Testing document

### Coverage report:
You can run the tests with command `poetry run invoke coverage` and get the coverage report with command ` poetry run invoke coverage-report`. Finally you can open the html report with command `poetry run invoke open-html-report`.

![image](https://user-images.githubusercontent.com/96131752/216816803-840e2769-29ca-4b51-aa5b-9d91b46d4ea2.png)

### Unit testing

I have made unit tests for Calculator, ShuntingYard and Evaluate classes. I have done the tests with Python's unittest library.
The test inputs consist of various input expressions, both valid and invalid ones. I have tested various invalid inputs, so I can make sure that all possible scenarios of user inputs are tested. The tests also ensure that correct errors are raised when necessary.
I created a StubIO class for testing Calculator class so inputs can be read and result written.
