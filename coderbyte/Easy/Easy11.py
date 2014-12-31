#http://coderbyte.com/CodingArea/GuestEditor.php?ct=AB%20Check&lan=Python
'''
Using the Python language, have the function ABCheck(str) take the str parameter being passed and return the string true if the characters a and b are separated by exactly 3 places anywhere in the string at least once (ie. "lane borrowed" would result in true because there is exactly three characters between a and b). Otherwise return the string false. 

Input = "after badly"Output = "false"
Input = "Laura sobs"Output = "true"
'''
import string

def ABCheck(tex):
	
	ind = tex.find('a')
		if tex.index[ind + 3] == 'b':
			result = "True"
		
		else: 
			result = "false" 
	
	return result


texx = raw_input('Input the text: ')

ABCheck(texx)
print texx