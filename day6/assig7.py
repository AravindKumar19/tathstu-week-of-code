

def Akerman(m, n, s ="% s"): 
	print(s % ("A(% d, % d)" % (m, n))) 
	if m == 0: 
		return n + 1
	if n == 0: 
		return Akerman(m - 1, 1, s) 
	n2 = Akerman(m, n - 1, s % ("A(% d, %% s)" % (m - 1))) 
	return Akerman(m - 1, n2, s) 

print(Akerman(1, 2)) 

