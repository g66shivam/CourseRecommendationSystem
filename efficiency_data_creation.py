from user_data import user_record
import random

testing = {}
training = {}

for i in range(1,6000):
	if(i%4==0):
		testing[i] = {}
		
		l = {}
		for c in user_record[i]:
			cc = random.randint(0,10)
			if(cc>6):
				l[c] = user_record[i][c]

		testing[i] = l
		#print testing,len(l),len(user_record[i])
		break
	else:
		training[i] = {}
		training[i] = user_record[i]

f = open('user_data_training.py', 'w')
print >> f,'training =',training

f = open('user_data_testing.py', 'w')
print >> f,'testing =',testing
