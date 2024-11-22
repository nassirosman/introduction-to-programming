number = int(input("Enter a non-negative integer: "))

factorial = 1

for i in range(1, number):

    factorial *= i
    print(f"(i): (factorial)")
