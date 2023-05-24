# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Parth Vyas
# Student Number:153646211
#

def wins_rock_scissors_paper(pl1,pl2):
	pl1=pl1.lower()
	pl2=pl2.lower()
	if(pl1=="rock" and pl2=="scissors"):
		return True
	elif(pl1=="paper" and pl2=="rock"):
		return True
	elif(pl1=="scissors" and pl2=="paper"):
		return True
	else:
		return False
	

def factorial(n):
	if n<2:
		return 1
	else:
		return n*factorial(n-1)


def fibonacci(n):
	if n==0 or n==1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)





def sum_to_goal(list,goals):
	for i in range(0,len(list)):
		for j in range(i+1,len(list)):
			if list[i]+list[j]==goals:
				return  list[i]*list[j]
	return 0
    

class UpCounter(object):
    stepsize=1
    num=0
    def __init__(self,stepsize) :
        self.stepsize=stepsize        
    def count(self):
        return self.num

    def update(self):
        self.num = self.num + self.stepsize
        return self.num


class DownCounter(UpCounter):
    def update(self):
        self.num = self.num - self.stepsize
        return self.num
