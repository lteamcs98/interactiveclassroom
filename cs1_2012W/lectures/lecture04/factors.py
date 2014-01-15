## factor.py
## A program to print the whole-number factors of a number
## Devin Balkcom
## July 2011

number = 42

possible_factor = 1
while possible_factor <= number :
	if number % possible_factor == 0:   
		print str(possible_factor) +" is a factor of " + str(number) + "."
		
	possible_factor = possible_factor + 1

print "And that's all the factors of " +str(number) + "." 
