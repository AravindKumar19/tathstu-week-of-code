Number = int(input("where you want to  print fabb series,enter the number "))
a = 0
b = 1
print("The Fibonacci series upto", Number, "th number is following:")
for i in range(Number):
    print(a, end = " ")
    c = a + b
    a = b
    b = c
