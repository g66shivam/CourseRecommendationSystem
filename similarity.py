import math
import operator
from inverted_index import index

tfreq = {}
similarity_index = index
sim_matrix = {}

def Calculate_termFrequency():
	for course in index:
		for term in index[course][1]:
			if term in tfreq:
				tfreq[term] = tfreq[term] + 1
			else:
				tfreq[term] = 1

def Calculate_score():
	#calculating tf-idf score
	for course in similarity_index:
		for term in similarity_index[course][1]:
			similarity_index[course][1][term] = math.log10(1+index[course][1][term])*math.log10(len(similarity_index)/tfreq[term])

	#normalization

	for course in similarity_index:
		nf = 0
		for term in similarity_index[course][1]:
			nf = nf + math.pow(similarity_index[course][1][term],2)
		nf = math.sqrt(nf)
		
		if(nf!=0):
			for term in similarity_index[course][1]:
				similarity_index[course][1][term] = similarity_index[course][1][term]/nf

def Calculate_similarity():
	for course in similarity_index:
		sim_matrix[course] = {}
		for c2 in similarity_index:
			
			if(c2==course):
				continue
			
			vector_product = 0
			
			for term in similarity_index[course][1]:
				if(term in similarity_index[c2][1]):
					vector_product = vector_product + similarity_index[course][1][term]*similarity_index[c2][1][term]
			sim_matrix[course][c2] = vector_product

def print_order():
	f = open('out1.txt', 'w')
	for course in sim_matrix:
		print >> f,course,similarity_index[course][0]['level']
		sorted_x = reversed(sorted(sim_matrix[course].items(), key=operator.itemgetter(1)))

		for c_name in sorted_x:
			print >> f,c_name[1],c_name[0],similarity_index[c_name[0]][0]['level']
		print >> f,'\n\n'


Calculate_termFrequency()
Calculate_score()
Calculate_similarity()
print_order()


