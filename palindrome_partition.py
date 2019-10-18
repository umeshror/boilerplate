"""
Given a string, a partitioning of the string is a palindrome partitioning if every substring
of the partition is a palindrome. For example, “aba|b|bbabb|a|b|aba” 
is a palindrome partitioning of “aababbbabbababa”. 
Determine the fewest cuts needed for palindrome partitioning of a given string. 
For example, minimum 3 cuts are needed for “aababbbabbababa”. The three cuts are “aa|babbbab|b|ababa”. 
If a string is palindrome, then minimum 0 cuts are needed. If a string of length n containing all 
different characters, then minimum n-1 cuts are needed.

"""
# Dynamic Programming Solution

def minSubStrPartion(word):
    word_size = len(word)

    # cuts[i][j] = Minimum number of cuts needed for palindrome partitioning of substring str[i..j]
    cuts = [[0 for i in range(word_size)]
            for i in range(word_size)]

    """
        a  a  b  a  b  b
      a 0  0  0  0  0  0
      a 0  0  0  0  0  0
      b 0  0  0  0  0  0
      a 0  0  0  0  0  0
      b 0  0  0  0  0  0
      b 0  0  0  0  0  0
    """

    # palindromes[i][j] = true if substring str[i..j] is palindrome, else false
    palindromes = [[False for i in range(word_size)]
                   for i in range(word_size)]


    # cuts[i][j] is 0 if palindromes[i][j] is true
    for i in range(word_size):
        palindromes[i][i] = True # every letter is palindrome
        cuts[i][i] = 0 # 0 cuts if every letter is palindrome
    """
    palindromes
        a  a  b  a  b  b
      a T  F  F  F  F  F
      a F  T  F  F  F  F
      b F  F  T  F  F  F
      a F  F  F  T  F  F
      b F  F  F  F  T  F
      b F  F  F  F  F  T
    """
    for substr_size in range(2, word_size + 1):

        for i in range(word_size - substr_size + 1):
            j = i + substr_size - 1  # Set ending index
            
            if substr_size == 2:
                palindromes[i][j] = (word[i] == word[j])
            else:
                palindromes[i][j] = ((word[i] == word[j]) and
                                     palindromes[i + 1][j - 1])

            # IF word[i..j] is palindrome,
            # then cuts[i][j] is 0
            if palindromes[i][j]: # if True
                cuts[i][j] = 0
            else:

                cuts[i][j] = 100000000
                for k in range(i, j):
                    cuts[i][j] = min(cuts[i][j], cuts[i][k] +
                                     cuts[k + 1][j] + 1)

    return cuts[0][word_size - 1]



word = "aababbbabbababa"
# Min cuts needed for Palindrome Partitioning is
print(minSubStrPartion(word))
