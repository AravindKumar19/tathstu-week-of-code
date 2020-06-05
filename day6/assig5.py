
max = 10023
fib = set() 
def sumoffib(): 
	global fib
	a, b = 0, 1
	fib.add(a) 
	fib.add(b) 
	while (a <= max): 
		temp = a + b 
		if temp <= max: 
			fib.add(temp) 
		a = b 
		b = temp 
def checkArray(arr, n): 
	sum = 0
	for i in range( n ): 
		if (arr[i] in fib): 
			sum += arr[i] 
	if (sum in fib): 
		return True
	return False
if __name__ == "__main__": 
	arr = [ 4,1,3,34,43,2,23,] 
	n = len(arr) 
	sumoffib() 

	if (checkArray(arr, n)): 
		print("Yes,sum of array is fibbonic number") 
	else: 
		print("No,sum of array is not fibbonic series") 
