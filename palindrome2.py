def pal(line):
	s = line.lower()                           # for ignoring case(upper,lower)
	l = []
	for i in s:
		if i.isalnum():                        # isalnum for taking only alphanumaric charecters
			l.append(i)
	rev = l[::-1]                              # reversing the sting
	if l == rev:
		print("palindrome")
	else:
		print("not a palindrome")
r = ""
f = open("file.txt","r")                       # Open the file with read only permit.
line = f.readline()                            # use the read line to read further.
lop = line.split(".")                          # used "." as a delimiter.
for i in range(len(lop)):
	print(i)
	r = lop[i]
	pal(r)	                                   # passing the string as a arg for checking
