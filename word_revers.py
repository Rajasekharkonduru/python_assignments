def rev(inpt):
	s = inpt.split(" ")              # spilts when " " found
	s = s[::-1]                      # for reversing the words
	s = " ".join(s)                  # joins the words 
	print(inpt)
	print(s)
inpt = input("Enter a string:")
rev(inpt)                             # passing string as an argument
