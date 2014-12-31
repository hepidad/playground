#http://coderbyte.com/CodingArea/GuestEditor.php?ct=Time%20Convert&lan=Python 
'''
Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon. 

Input = 126Output = "2:6"
Input = 45Output = "0:45"

'''
import datetime

print str(datetime.timedelta(seconds=int(raw_input('Input seconds:'))))
