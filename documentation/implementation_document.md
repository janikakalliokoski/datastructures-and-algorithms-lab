# Implementation document

### Project structure
`CalculatorIO` class is used to read users inputs and printing the output.

`Calculator` class is the base for the calculator.

`ShuntingYard` class is used to create the shunting-yard algorithm. 
It is in charge of parsing an expression in infix notation and returning it as a postfix notation string.

`Evaluate` class is in charge of evaluating the result from the postfix notation string.

### Sources:
- https://en.wikipedia.org/wiki/Shunting_yard_algorithm
- https://gist.github.com/ollybritton/3ecdd2b28344b0b25c547cbfcb807ddc
- https://www.scaler.com/topics/postfix-evaluation/
