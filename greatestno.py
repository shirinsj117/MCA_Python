pi=3.1416
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the thrid number:"))
if num1 >= num2 and num1 >= num3:
    n = num1
elif num2 >= num1 and num1 >= num3:
    n = num2
else:
    n = num3
    print(f"The greatest number is:{n}")
    nn = n**2
    nnn = n**3
    result = n + nn + nnn
    print(f"n + nn + nnn = {n} + {nn} + {nnn} = {result}")
    radius = n
    area = pi * radius ** 2
    perimeter = 2 * pi * radius
    print (f"\n For a circle with radius {radius}:")
    print (f"Area = {area: .2f}")
    print (f"Perimeter (circumference) = {perimeter: .2f}")