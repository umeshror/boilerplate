"""
Given a string, a partitioning of the string is a palindrome partitioning if every substring
of the partition is a palindrome. For example, “aba|b|bbabb|a|b|aba” 
is a palindrome partitioning of “ababbbabbababa”. 
Determine the fewest cuts needed for palindrome partitioning of a given string. 
For example, minimum 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”. 
If a string is palindrome, then minimum 0 cuts are needed. If a string of length n containing all 
different characters, then minimum n-1 cuts are needed.

"""

# Dynamic Programming Solution

def minSubStrPartion(str): 
	
  n = len(str) 
	
	# C[i][j] = Minimum number of cuts needed for palindrome partitioning of substring str[i..j] 
	C = [[0 for i in range(n)] 
			for i in range(n)] 
      
	# P[i][j] = true if substring str[i..j] is palindrome, else false
	P = [[False for i in range(n)] 
				for i in range(n)] 

	j = 0
	k = 0
	L = 0
	
	# C[i][j] is 0 if P[i][j] is true 
	for i in range(n): 
		P[i][i] = True; 
		C[i][i] = 0; 
    
	for L in range(2, n + 1): 
		
		for i in range(n - L + 1): 
			j = i + L - 1 # Set ending index 
			
			if L == 2: 
				P[i][j] = (str[i] == str[j]) 
			else: 
				P[i][j] = ((str[i] == str[j]) and
							P[i + 1][j - 1]) 
							
			# IF str[i..j] is palindrome, 
			# then C[i][j] is 0 
			if P[i][j] == True: 
				C[i][j] = 0
			else: 
      
				C[i][j] = 100000000
				for k in range(i, j): 
					C[i][j] = min (C[i][j], C[i][k] +
								C[k + 1][j] + 1) 
                
	return C[0][n - 1] 

str = "ababbbabbababa"
print ('Min cuts needed for Palindrome Partitioning is', 
									minSubStrPartion(str)) 
				
