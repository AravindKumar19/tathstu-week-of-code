Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@aravind222148 
vibrantachintya
/
twowaits-twoc
1
18
 Code
 Issues 0
 Pull requests 0 Actions
 Projects 0
 Wiki
 Security 0
 Insights
twowaits-twoc/Day 3/program6.py /
 Achintya Gaumat changes
7eddd47 18 days ago
31 lines (28 sloc)  932 Bytes
  
def Sum(List, size,sum):
    sumList = []
    if size == 1:
        for x in List:
            sumList.append(sum + x)
        return sumList
    L2 = list(List)
    for x in List:
        L2.remove(x)
        sumList.extend(Sum(L2,size-1,sum + x))
    return sumList

def summation(List,size):
    sumList = list(List)
    for i in range (2, size + 1):
        sumList.extend(Sum(List,i,0))
    number = 1
    while True:
        if number not in sumList:
            print("The least integer which is not present in the list and also cannot be represented as the summation of sub-elements is",number)
            break
        number += 1

size = int(input("Enter the no of elements you want to add in the list: "))
List = []
print("Enter the elements in list one by one.")
for i in range(size):
    List.append(int(input()))
summation(List, size)

