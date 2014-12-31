#http://coderbyte.com/CodingArea/GuestEditor.php?ct=Alphabet%20Soup&lan=Python

'''
Using the Python language, have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.  

Input = "coderbyte"Output = "bcdeeorty"
Input = "hooplah"Output = "ahhloop"

'''

print "".join(sorted(raw_input('Input the code:')))