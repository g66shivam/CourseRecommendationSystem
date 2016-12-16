from user_data_testing import testing
from user_data_training import training
from user_data import user_record
from user_specific import *
import math
from inverted_index import List_of_Courses

def rmsCalculation():
	rms = 0
	g_ctr = 0

	for user_id in testing:
		g_ctr  =g_ctr + 1
		user_rec =  Course_recommendation_for_efficiency(testing[user_id],training)
		total = 0
		ctr = 0
		for c in user_record[user_id]:
			if c not in testing[user_id]:
				total = total + math.pow(user_rec[c]-user_record[user_id][c],2)
				ctr = ctr + 1
		rms = rms + math.sqrt(total/ctr)
	return rms/g_ctr

def Calculate_f1_measure():

	precision = 0
	recall = 0
	f_rate = 0
	g_ctr = 0

	for user_id in testing:
		g_ctr = g_ctr + 1
		tp = 0
		fn = 0
		fp = 0
		tn = 0

		user_rec =  Course_recommendation_for_efficiency(testing[user_id],training)
		
		rec_list = []
		not_rec_list = []
		ctr = 0
		for c in user_rec:
			rec_list.append(c)
			ctr = ctr + 1
			if(ctr>10):
				not_rec_list.append(c)

		actual_course = []
		for c in user_record[user_id]:
			if c not in testing[user_id]:
				actual_course.append(c)

		for i in range(len(rec_list)):
			if rec_list[i] in actual_course:
				tp = tp + 1
			else:
				fp = fp + 1
		
		for i in range(len(not_rec_list)):
			if not_rec_list[i] in actual_course:
				fn = fn + 1
			else:
				tn = tn + 1

		precision = precision + (float(tp)/(tp+fp))
		recall = recall + (float(tp)/(tp+fn))
		f_rate = f_rate + (float(fp)/(fp+tn))
	
	return precision/g_ctr,recall/g_ctr,f_rate/g_ctr

