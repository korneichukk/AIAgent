import sys
sys.path.append('pkg')
from calculator import Calculator

calculator = Calculator()
expression = "3 + 7 * 2"
result = calculator.evaluate(expression)
print(result)