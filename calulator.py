import math

class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.history = []
        self.last_result = None
        
    def add(self):
        result = sum(self.numbers)
        self.last_result = result
        self.history.append(('add', self.numbers, result))
        return result
    
    def subtract(self):
        result = self.numbers[0] - sum(self.numbers[1:])
        self.last_result = result
        self.history.append(('subtract', self.numbers, result))
        return result
    
    def multiply(self):
        result = 1
        for num in self.numbers:
            result *= num
        self.last_result = result
        self.history.append(('multiply', self.numbers, result))
        return result
    
    def divide(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            if num == 0:
                raise ValueError("Cannot divide by zero")
            result /= num
        self.last_result = result
        self.history.append(('divide', self.numbers, result))
        return result
    
    def sqrt(self):
        result = [math.sqrt(num) for num in self.numbers]
        self.last_result = result
        self.history.append(('sqrt', self.numbers, result))
        return result
    
    def exponent(self, power):
        result = [num ** power for num in self.numbers]
        self.last_result = result
        self.history.append(('exponent', self.numbers, result))
        return result
    
    def display_history(self):
        for operation in self.history:
            print("Operation: ", operation[0])
            print("Numbers: ", operation[1])
            print("Result: ", operation[2])
            print("-" * 20)
            
    @staticmethod
    def get_input():
        numbers = input("Enter the numbers separated by commas: ")
        numbers = [int(num) for num in numbers.split(',')]
        return numbers

#usage example
numbers = Calculator.get_input()
calc = Calculator(numbers)
print("Addition: ", calc.add())
print("Subtraction: ", calc.subtract())
print("Multiplication: ", calc.multiply())
try:
    print("Division: ", calc.divide())
except ValueError as e:
    print(e)
print("Square roots: ", calc.sqrt())
print("Exponentiation (power=2): ", calc.exponent(2))
print("Last result: ", calc.last_result)
calc.display_history()
