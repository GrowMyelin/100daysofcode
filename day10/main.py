logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1 / n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def main():
    print(logo)
    num1 = int(input("What's the first number? ")) 
    num2 = int(input("What's the second number? "))
    operation_symbol = input("Pick an operation from the line above: ")
    answer = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    cont = y
    while cont == 'y':
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        n1 = answer
        n2 = int(input("What's the next number? "))
        answer = operations[operation_symbol](n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ")

if __name__ == "__main__":
    main()