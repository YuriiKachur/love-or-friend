while True:
    # Read two numbers from the user
    a = float(input("Введіть перше число (a): "))
    b = float(input("Введіть друге число (b): "))

    # Loop to ensure a valid operation symbol is entered
    while True:
        operation = input("Введіть операцію (+, -, *, /, **, //, %) або 'exit' для виходу: ")
        
        if operation == 'exit':
            print("Програма завершена.")
            exit()

        # Check for valid operation
        if operation == '+':
            print(f"{a} + {b} = {a + b}")
            break
        elif operation == '-':
            print(f"{a} - {b} = {a - b}")
            break
        elif operation == '*':
            print(f"{a} * {b} = {a * b}")
            break
        elif operation == '/':
            if b != 0:
                print(f"{a} / {b} = {a / b}")
            else:
                print("Ділення на нуль неможливе.")
            break
        elif operation == '**':
            print(f"{a} ** {b} = {a ** b}")
            break
        elif operation == '//':
            if b != 0:
                print(f"{a} // {b} = {a // b}")
            else:
                print("Цілочисельне ділення на нуль неможливе.")
            break
        elif operation == '%':
            if b != 0:
                print(f"{a} % {b} = {a % b}")
            else:
                print("Обчислення залишку від ділення на нуль неможливе.")
            break
        else:
            print("Невірний символ. Будь ласка, виберіть одну з операцій: +, -, *, /, **, //, % або 'exit' для виходу.")
