size = int(input("Enter the size of tuple: "))#
print("Enter the elements in tuple one by one")
arrary = []
for i in range(size):
    arrary.append(input())
arrary= tuple(arrary)
element = input("Enter the element whose occurrences you want to know: ")
print("Tuple contains the element", arrary.count(element), "times")
