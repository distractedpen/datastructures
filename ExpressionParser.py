#postfix parser
from stack import Stack as Stack


operands = Stack(3)
operators = "^*/+-"

string = input("Enter an expression in postfix notation: ")



for x in string:
    a = 0
    b = 0
    c = 0
    if x not in operators:
        operands.push(x)
    else:
        b = float(operands.pop())
        a = float(operands.pop())
        if x == "^":
            c = a**b
        elif x == "*":
            c = a*b
        elif x == "/":
            c = a/b
        elif x == "+":
            c = a+b
        elif x == "-":
            c = a-b
        else:
            print("Error, cannot parse {0}.".format(x))
            break
        operands.push(c)
        
print(operands.pop())            
        
        

