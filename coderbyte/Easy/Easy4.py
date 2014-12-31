





import string; tr = string.maketrans('abcdefghijklmnopqrstuvwxyz1234567890!#$%&+* ', 'bcdEfghIjklmnOpqrstUvwxyzA1234567890!#$%&+* '); print raw_input('Input the messages:').translate(tr)


#attempt
#print "".join((chr((ord(letter)+1)) for letter in raw_input('Input the messages:'))).translate(tr) 
#vowel ='aiueo'; let = raw_input('Input the messages:'); print "".join((chr((ord(letter)+1)) for letter in let ))
#print "".join((chr(97+(ord(letter)-97+1) % 26) for letter in raw_input('Input the messages:') if letter in vowel: letter.upper))
#import string; tr = string.maketrans('aBCDeFGHiJKLMNoPQRSTuVWXYZ', 'AbcdEfghIjklmnOpqrstUvwxyz'); print "".join((chr((ord(letter)+1)) for letter in raw_input('Input the messages:'))).translate(tr) 
