def operation_manager(func):
    def wrapper(first, second, operation=None):

        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'

        return func(first, second, operation)
    return wrapper

@operation_manager
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        return "Unknown operation"


if __name__ == "__main__":
    # Ввод чисел от пользователя
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))


    result = calc(first, second)
    print(f"Result: {result}")
