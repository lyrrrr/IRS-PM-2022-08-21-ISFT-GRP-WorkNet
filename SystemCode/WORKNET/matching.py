import numpy as np
import pandas as pd
# import json
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import cosine_similarity
from gensim.models.callbacks import CallbackAny2Vec
import string
from nltk.corpus import stopwords
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
from gensim.models.doc2vec import Doc2Vec
import re
import pdfplumber

#settings to show epoch progress
# for model loading
class EpochLogger(CallbackAny2Vec):
    
    def __init__(self):
        self.epoch = 0
        
    def on_epoch_begin(self, model):
        print("Epoch #{} start".format(self.epoch))

    def on_epoch_end(self, model):
        print("Epoch #{} end".format(self.epoch))
        self.epoch += 1

def preprocess(text):
    stop_words = set(stopwords.words('english'))
    # remove non-english characters, punctuation and numbers
    text.strip()
    text.replace("\n","")
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = re.sub('http\S+\s*', ' ', text)  # remove URLs
    text = re.sub('RT|cc', ' ', text)  # remove RT and cc
    text = re.sub('#\S+', '', text)  # remove hashtags
    text = re.sub('@\S+', '  ', text)  # remove mentions
    #0. split words by whitespace
    text = text.split()
    
    # 1. lower case
    text = [word.lower() for word in text]
    
    # 2. remove punctuations
    punc_table = str.maketrans('','',string.punctuation)
    text = [word.translate(punc_table) for word in text]
    
    # 3. remove stop words
    text = [word for word in text if word not in stop_words]
    
    return text

#My recommender system to find best jobs for a given resume
def jobs_recommender(r, Keywords) :

    job = pd.read_csv('./vector_data/vector_job_20.csv')

    # TODO do more on filtering related jobs!!!!!! java
    related_jobs = job.loc[job['jobtitle'].str.contains(str(Keywords))] 
    #job features need to be matched with resume
    job_m = related_jobs[['vec_1','vec_2','vec_3','vec_4','vec_5','vec_6','vec_7','vec_8','vec_9','vec_10','vec_11','vec_12',
                      'vec_13','vec_14','vec_15','vec_16','vec_17','vec_18','vec_19','vec_20']]
    #Store the results in this DF - to showcase
    matched_jobs = pd.DataFrame(columns = ["id","company","job_title","jobdescription","experience_range","industry","similarity"] )
  
    #r= r.to_numpy()
    r= r.reshape(1, -1)

    #Go through ALL the related jobs
    jd_num = job_m.shape[0]

    for jd in range(0,jd_num) :
        #print(f'jd is {jd}')        
        #Find the similarity of the jobs with resume
        jobs = job_m.iloc[jd]
        jobs = jobs.to_numpy()
        jobs = jobs.reshape(1, -1)
        # print(f'job is {jobs}')
        # print(f'r is {r}')
        # print(f'job is {job}')
        similarity = cosine_similarity(r,jobs)
        #print(f'similarity is {similarity}')
        matched_jobs.loc[len(matched_jobs)] = [jd,
                                               related_jobs['company'].iloc[jd],
                                               related_jobs['jobtitle'].iloc[jd],
                                               related_jobs['jobdescription'].iloc[jd],
                                               related_jobs['experience'].iloc[jd],
                                               related_jobs['industry'].iloc[jd],
                                               similarity[0][0]]
        

    return matched_jobs.sort_values(by=['similarity'],ascending=False)[:]

# find best resuems for a given job
def resumes_recommender(r, Keywords):

    resume = pd.read_csv('./vector_data/vector_resume_20_new.csv')

    # TODO do more on filtering related jobs!!!!!! java
    #print("keyword", str(Keywords))
    if Keywords:
        related_resumes = resume.loc[resume['Resume_str'].str.contains(str(Keywords))] 
    else:
        related_resumes = resume
    #job features need to be matched with resume
    resume_m = related_resumes[['vec_1','vec_2','vec_3','vec_4','vec_5','vec_6','vec_7','vec_8','vec_9','vec_10','vec_11','vec_12',
                      'vec_13','vec_14','vec_15','vec_16','vec_17','vec_18','vec_19','vec_20']]
    #Store the results in this DF - to showcase
    matched_resumes = pd.DataFrame(columns = ["id","name","file_name","category","similarity"] )
  
    #r= r.to_numpy()
    r= r.reshape(1, -1)
    #Go through ALL the related jobs
    ren_num = resume_m.shape[0]

    for jd in range(0,ren_num):
        #print(f'jd is {jd}')        
        #Find the similarity of the jobs with resume
        r_t = resume_m.iloc[jd]
        r_t = r_t.to_numpy()
        r_t = r_t.reshape(1, -1)
        
        similarity = cosine_similarity(r,r_t)
        #print(f'similarity is {similarity}')
        matched_resumes.loc[len(matched_resumes)] = [int(related_resumes['ID'].iloc[jd]),
                                               related_resumes['name'].iloc[jd],
                                               related_resumes['file_name'].iloc[jd],
                                               related_resumes['Category'].iloc[jd],
                                               similarity[0][0]]
        
    return matched_resumes.sort_values(by=['similarity'],ascending=False)[:]

## The whole process:
# one resume matched with many jobs
def resume_m_jobs(filename, Keywords):
    """
    read the file of uploaded resume, turn it to txt/get the string
    ,and do some preprocess to match this resume to jobs.
    """

    # TODO read pdf / change them to txt
    resume_str = ''
    with pdfplumber.open("./Resumes/"+filename) as pdf: 
        for i in range(len(pdf.pages)):
    	    # read each page
            page = pdf.pages[i] 
            # page.extract_text() get text, remove page number
            page_content = ' '.join(page.extract_text().split('\n')[:-1])
            resume_str = resume_str + page_content

    print("resume_content",resume_str[0:100])
    # f1 = open('./Resumes/test.txt')
    # resume_str = f1.read()

    # TODO preprocess: add more \n ' ' ... added stop words
    tokenized_doc = preprocess(resume_str)

    model = Doc2Vec.load("./models/my_doc2vec.model")

    # encode into feature vector 20 dim
    vector = model.infer_vector(tokenized_doc)
    vector = np.reshape(vector,(-1,20))

    matched_job = jobs_recommender(vector, Keywords).head(10)
    print("matched_job", matched_job.head(1))
    #### index 0-2 : id company title

    return matched_job

def job_m_resumes(jd_str, Keywords):
    """
    read the job str,
    ,and do some preprocess to match this job to resumes.
    """

    # TODO preprocess: add more \n ' ' ... added stop words
    tokenized_doc = preprocess(jd_str)

    model = Doc2Vec.load("./models/my_doc2vec.model")

    # encode into feature vector 20 dim
    vector = model.infer_vector(tokenized_doc)
    vector = np.reshape(vector,(-1,20))

    matched_resume = resumes_recommender(vector, Keywords).head(10)
    #print("matched_job", matched_resume.head(1))
    #### index 0-2 : id company title

    return matched_resume

# if __name__=="__main__":
#     resume_m_jobs(1)












