import json
import os
import math
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps= PorterStemmer()

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

import urllib.request
def create_data_files(project_name,base_url,filename):
            queue =project_name+'/'+filename+'.txt'
	
            if os.path.isfile(queue):
                append_to_file(queue,base_url)
            
            if not os.path.isfile(queue):
            	write_file(queue,base_url)
		
def write_file(path, data):
    f=open(path,'w')
    f.write(data)
    f.close()

def append_to_file(path,data):
	with open (path,'a') as file:
		file.write(data+'\n')
i=0
final_ans_total="{"
with open('IRDATA.json') as json_data:
    json_response = json.load(json_data)
    for course in json_response['courses']:
        #course=json_response['courses'][0]
        i=i+1
        course_title=course['title']
        course_level=course['level']
        course_summary=course['summary'].lower()

        stop_words=set(stopwords.words("english"))
        #words=word_tokenize(course_summary)
        words=tokenizer.tokenize(course_summary)
        words.sort()
        filtered_sentence=[]
        new_str=""
        final_str="'"+course_title+"':[{'level':'"+course_level+"'},{"
        for w in words:
            if w not in stop_words:
                filtered_sentence.append(w)
        #print(filtered_sentence)
        freq=1
        prev=ps.stem(filtered_sentence[0])
        for itr in range (1,len(filtered_sentence)):
        #for w in filtered_sentence:
            #print(ps.stem(w))
            w=ps.stem(filtered_sentence[itr])
            curr=w
            if(curr==prev):
                freq=freq+1
            else:
                final_str+="'"+prev+"': "+str(1)+","
                new_str+=prev+"\n"
                freq=1
            prev=curr                
        final_str+="}]"
        #print(final_str)
        final_ans_total+=final_str+","
        create_data_files('final_IR',new_str,'myfile_27_oct_pl')

final_ans_total+="}"
#print(final_ans_total)
create_data_files('final_IR',final_ans_total,'myfile_27_oct')

         
