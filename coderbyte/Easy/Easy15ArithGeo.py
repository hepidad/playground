#http://coderbyte.com/CodingArea/GuestEditor.php?ct=Arith%20Geo&lan=Python
'''Using the Python language, have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.
'''
global arr
arrlist = {}
def ArithGeo():
	arr = 0
	sumarr = int(raw_input("Input number of elements:"))
	for i in range (0,sumarr+1): 
		arr[i]=int(raw_input("Input element %i:"%i))
		arrlist.append(arr[i])
		print arrlist

ArithGeo()
