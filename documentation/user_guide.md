# User guide

Clone the project to your computer. Then move into the repository.

Install dependencies
```bash
poetry install
```
Start the calculator
```bash
poetry run invoke start
```
Run tests
```bash
poetry run invoke coverage
```
Get coverage report
```bash
poetry run invoke coverage-report
```
Open the coverage report
```bash
poetry run invoke open-html-report
```
