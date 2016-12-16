from inverted_index import List_of_Courses
import random
user_record = {}

for i in range(1,6001):
	user_record[i] = {}
	c = random.randint(30,100)
	for j in range(c):
		ctr = random.randint(0,149)
		if List_of_Courses[ctr] in user_record[i]:
			continue
		else:
			user_record[i][List_of_Courses[ctr]] = random.randint(1,5) 
#print user_record
f = open('user_data1.py', 'w')
print >> f,'user_record =',user_record
print len(user_record)