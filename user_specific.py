from similarity_matrix import sim_matrix
from user_data import user_record
from inverted_index import List_of_Courses
import operator,math

def CourseScore_ItemSim(course_list):
	Course_score = {}

	for course in List_of_Courses:
		if course in course_list:
			continue

		total = 0
		sim_sum = 0

		for c in course_list:
			sim_sum = sim_sum + sim_matrix[course][c]
			total = total + sim_matrix[course][c]*course_list[c]
		if(sim_sum!=0):
			Course_score[course] = total/sim_sum
	#c1 =  list(reversed(sorted(Course_score.items(), key=operator.itemgetter(1))))
	#print c1
	#print '\n\n'
	return Course_score


def User_Similarity(user_sim,course_list,user_record):
	#using pearson correlation coefficient
	for uid in user_record:
		si = {}
		for course in course_list:
			if course in user_record[uid]:
				si[course] = 1

		n = len(si)

		if(n==0):
			user_sim[uid] = 0
			continue

		sum1=sum([course_list[it] for it in si])
		sum1 = sum1/n
		sum2=sum([user_record[uid][it] for it in si])
		sum2 = sum2/n

		numerator = sum([(course_list[it]-sum1)*(user_record[uid][it]-sum2) for it in si])
		
		sum1Sq = math.sqrt(sum([math.pow(course_list[it]-sum1,2) for it in si]))
		sum2Sq = math.sqrt(sum([math.pow(user_record[uid][it]-sum2,2) for it in si]))
	
		den = sum1Sq*sum2Sq
		
		if(den==0):
			user_sim[uid] = 0
			continue
		r  = numerator/den
		user_sim[uid] = r


def CourseScore_UserSim(course_list,user_record):
	Course_score = {}
	user_sim = {}
	User_Similarity(user_sim,course_list,user_record)

	for course in List_of_Courses:
		#only score courses i haven't seen yet
		if course in course_list:
			continue

		total = 0
		sim_sum = 0
		for person in user_record:
			if(user_sim[person]<=0):
				continue
			if course in user_record[person]:
				sim_sum = sim_sum + user_sim[person]
				total = total + user_record[person][course]*user_sim[person]

		if(sim_sum!=0):
			Course_score[course] = total/sim_sum

	#c1 =  list(reversed(sorted(Course_score.items(), key=operator.itemgetter(1))))
	#print c1
	#print '\n\n'
	return Course_score


def Hybrid_Recommender(course_list,user_record):
	Course_Item_sim = CourseScore_ItemSim(course_list)
	Course_User_sim = CourseScore_UserSim(course_list,user_record)
	
	user_recom = {}

	#70% weightage to item based results and 30% to user based results

	for c1 in Course_Item_sim:
		user_recom[c1] = 0.8*Course_Item_sim[c1]
		if c1 in Course_User_sim:
			user_recom[c1] = user_recom[c1] + (0*Course_User_sim[c1])

	for c1 in Course_User_sim:
		if c1 in user_recom:
			continue
		else:
			user_recom[c1] = 0*Course_User_sim[c1]
	return list(reversed(sorted(user_recom.items(), key=operator.itemgetter(1))))

def Course_recommendation(course_list,user_record):
	user_recom = []
	l = Hybrid_Recommender(course_list,user_record)

	for i in range(10):
		user_recom.append(l[i][0])
	return user_recom

def Course_recommendation_for_efficiency(course_list,user_record):
	user_recom = []
	l = Hybrid_Recommender(course_list,user_record)
	val = {}
	for i in range(len(l)):
		val[l[i][0]] = l[i][1]
	
	return val