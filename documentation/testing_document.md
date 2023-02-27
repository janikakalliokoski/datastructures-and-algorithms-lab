# Testing document

### Coverage report:

Run tests
```bash
poetry run invoke coverage
```
Get the coverage report
```bash
poetry run invoke coverage-report
```
Open the html report
```bash
poetry run invoke open-html-report
```

![image](https://user-images.githubusercontent.com/96131752/221557557-9554b6a8-9e9c-4197-beed-21a711b7bf5a.png)

[![codecov](https://codecov.io/gh/janikakalliokoski/datastructures-and-algorithms-lab/branch/main/graph/badge.svg?token=I9TZKLLES7)](https://codecov.io/gh/janikakalliokoski/datastructures-and-algorithms-lab)
See how the unit testing is divided by clicking the codecov badge.

### Unit testing and correctness testing

I have made unit tests for Calculator, ShuntingYard and Evaluate classes. I have done the tests with Python's unittest library.
The test inputs consist of various input expressions, both valid and invalid ones. I have tested various invalid inputs, so I can make sure that all possible scenarios of user inputs are tested. The tests also ensure that correct errors are raised when necessary.
I created a StubIO class for testing Calculator class so inputs can be read and result written.
