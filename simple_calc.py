value_one = int(input("Введите первое число: "))
value_two = int(input("Введите второе число: "))

operation = input("Выберите операцию + - * /: ")

if operation == "+":
    print(f"Результат сложения: {value_one + value_two}")
elif operation == "-":
    print(f"Результат вычитания: {value_one - value_two}")
elif operation == "*":
    print(f"Результат умножения: {value_one * value_two}")
elif operation == "/":
    if value_two == 0:
        print("На ноль делить нельзя")
        quit()
    print(f"Результат деления: {value_one / value_two}")
else:
    print("Выбрана неверная операция")
