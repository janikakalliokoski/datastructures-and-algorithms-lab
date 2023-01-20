# Project Specification

**This project is done with Python. I can do peer evaluations in JavaScript projects also. The project is documented in English.**

## Bachelor's degree in Computer Science

## Scientific calculator

The program will use shunting-yard algorithm to turn an infix expression to a postfix expression (also known as Reverse Polish Notation), and then calculate the result from that expression. Operators are stored in stacks.

The program has a text UI and asks the user for a mathematical expression. The expression can contain addition, substraction, multiplication, division and exponentation operations. If the expression contains variables, they should be defined beforehand or an error will be raised. The expression can also contain basic functions. The program checks the expression for invalid characters and correct amount of left and right parentheses. If the expression is valid, it will be transformed into postfix expression by using the shunting-yard algorithm and the result is calculated.

Both time and space complexities should be O(n), where n is the length of the given expression.

I chose shunting-yard algorithm and stacks, because no other option seemed interesting. This will be challenging enough for me and I think I can actually do this one.

### Sources:
- https://medium.com/@ngpari.earth/building-a-basic-calculator-using-the-shunting-yard-algorithm-by-dijkstra-6a31b75bb4b3
- https://en.wikipedia.org/wiki/Shunting_yard_algorithm
- https://github.com/maizzuu/data-structures-lab
