#http://coderbyte.com/CodingArea/GuestEditor.php?ct=Palindrome&lan=Python 

#Using the Python language, have the function Palindrome(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 
import string 

def Palindrom(thestr):
	stripstr = thestr.strip(" \t\n\r")
	if stripstr == ''.join(reversed(stripstr)):
		print 'TRUE'
	else: print 'FALSE'

	print thestr
	print stripstr


a = raw_input('Input text:')
Palindrom(a)
print a.strip(" \t\n\r")