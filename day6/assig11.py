
def maxProduct(arr, n):  
	if n < 3: 
		return -1 
	arr.sort() 
	return max(arr[0] * arr[1] * arr[n - 1], 
			arr[n - 1] * arr[n - 2] * arr[n - 3]) 
if __name__ == "__main__": 

	arr = [-10, -3, 5, 6, -20] 
	n = len(arr) 

	_max = maxProduct(arr, n) 

	if _max == -1: 
		print("No Triplet Exists") 
	else: 
		print("Maximum product is", _max) 

