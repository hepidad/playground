#http://coderbyte.com/CodingArea/GuestEditor.php?ct=Ex%20Oh&lan=Python

#Using the Python language, have the function ExOh(str) 
#take the str parameter being passed and return the string true 
#if there is an equal number of x's and o's, otherwise return the string false. 
#Only these two letters will be entered in the string, no punctuation or numbers.
#For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

def ExOh(str):
	if a.count('x') == a.count('o'):
		print 'TRUE'

	else: print 'FALSE'
	
	print 'Sum of x', a.count('x') 
	print 'Sum of o', a.count('o')

a=raw_input('input the ExOh:')
ExOh(a)