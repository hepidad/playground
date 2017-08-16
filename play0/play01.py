file = open("testWrite.txt","w")
file.write("Look Ma, no hands!") #write the content of testWrite.txt.
file.close()

file = open("testWrite.txt","r")
print file.read() #show the content of testWrite.txt.