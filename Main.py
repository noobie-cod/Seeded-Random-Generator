def check_prime(k):
	if (k>1):
		for i in range(2,k):
			if(k%i==0):
				return False
		else:
			return True
	else:
		return False

def check_even(k):
	if(k%2==0):
		return True
	else:
		return False

def seeded_random_generator(seeds):
	np.random.seed(seeds)
	k = np.random.rand(seeds).tolist()
	for i in range(0,seeds):
		temp = int((k[i]*100000)/13)
		if (check_prime(temp)):
			if(check_even(temp)):
				temp = (temp*temp)/(seeds*100)
			else:
				temp = (temp*temp)/((seeds-1)*100)
		else:
			if(check_even(temp)):
				temp = temp*(100-seeds)/(seeds**2)
			else:
				temp = temp*(temp**(0.5))/((seeds-1)**2)
		k[i] = int(temp)
	print(k)
	
import numpy as np 
seeds = int(input("Enter Seed Value: "))
seeded_random_generator(seeds)
seeds = int(input("Enter Seed Value: "))
seeded_random_generator(seeds)
seeds = int(input("Enter Seed Value: "))
seeded_random_generator(seeds)
