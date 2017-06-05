
##########################################################################################################################################
#------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------- Shanks Transform for accelerated convergence V.1.0 -------------------------------------#
#-------------------------------------------- By Keerthi Vasan.G.C, Student Researcher, JNCASR, Bangalore ---------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------#
#########################################################################################################################################


## Reads the coefficients as input from input_seq file -- > Stores them in an array.
with open('input_seq') as f:
    c = []
    for line in f:
    	c.append(line.rstrip('\n'))
coef =  map(float,c)

## Take these coefficients and add them up term by term
Shanks = [] ## Lets call this summation : Shanks 0 
print "Shanks Transform 0"
for i in range(len(coef)):
	Shanks.append(sum(coef[:i+1]))
	print sum(coef[:i+1])

print "************************"
## Now to do this recursively for n - Shanks transforms 

n = 5 # Number of shank transforms to be done..
dummy = [] 
for i in range(n):
	print "Shanks Transform " + str(i+1)
	for i in range(1, len(Shanks)-1):
		num = Shanks[i]**2 -Shanks[i+1]*Shanks[i-1]
		den = 2*Shanks[i] - Shanks[i+1] -Shanks[i-1]
		print float(num/den)
		dummy.append(float(num/den))
	print "************************"
	Shanks[:] = dummy[:] ## Copying the dummpy list to this one.. 
	dummy = [] 
