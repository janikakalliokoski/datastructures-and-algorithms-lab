# Implementation document

### Project structure
`CalculatorIO` class is used to read users inputs and printing the output.

`Calculator` class is the base for the calculator. This class is also in charge of defining variables and other methods concerning variables, e.g. listing defined variables.

`ShuntingYard` class is used to create the shunting-yard algorithm. 
It is in charge of parsing an expression in infix notation and returning it as a postfix notation string.

`Evaluate` class is in charge of evaluating the result from the postfix notation string.

### Time and space requirements achieved 
#### O-analysis of the pseudocode

The implementation of my shunting-yard algorithm is based on pseudocode in this [wikipedia article](https://en.wikipedia.org/wiki/Shunting_yard_algorithm) (The algorithm in detail). The running time complexity of my shunting-yard algorithm is O(n), because each token is read once, each number, operator or function is printed once, and each function, operator or parenthesis is pushed onto the stack once and also popped from the stack once. Therefore there are at most a constant number of operations executed per token. Thus the running time of the algorithm is linear in the size of the input.

### Shortcomings and improvement suggestions

I have tried to test every possible input an user may use, both valid and invalid ones. There might be errors that I have not noticed.

#### Improvement suggestions:
- switch between radians and degrees when using trigonometric funtions
- add inverse functions of sin, cos and tan
- add permutation (nPr) and combination (nCr)
- add n. root of x operations (index of root)

### Sources:
- https://en.wikipedia.org/wiki/Shunting_yard_algorithm
- https://gist.github.com/ollybritton/3ecdd2b28344b0b25c547cbfcb807ddc
- https://www.scaler.com/topics/postfix-evaluation/
