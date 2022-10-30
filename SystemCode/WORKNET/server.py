import os
import urllib.request
from flask import (Flask, render_template, request,
                   send_from_directory, jsonify)
from werkzeug.utils import secure_filename
import viewing
import pandas as pd
import matching
from gensim.models.callbacks import CallbackAny2Vec

app = Flask(__name__)
#app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = './Resumes/'
app.config['JD_Folder'] = './JobDesc/'


ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def uploadFile(file):
    Filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], Filename))
    return Filename

class EpochLogger(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 0
        
    def on_epoch_begin(self, model):
        print("Epoch #{} start".format(self.epoch))

    def on_epoch_end(self, model):
        print("Epoch #{} end".format(self.epoch))
        self.epoch += 1


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources/<path:path>')
def send_resources(path):
    return send_from_directory('resources', path)

@app.route('/uploadResumePage')
def uploadResumePage():
    return render_template('uploadResumePage.html')

@app.route('/updateJDPage')
def classifierPage():
    return render_template('updateJDpage.html')

@app.route('/QuickCandidates')
def QuickSearchCandidatesPage():
    return render_template('QuickSearchCandidates.html')

@app.route('/QuickJobs')
def QuickJobs():
    return render_template('QuickSearchJobs.html')


@app.route('/uploadResumeAction', methods=['POST'])
def uploadResumeAction():
    name = request.form['name']
    Keywords = request.form['keyword']
    # Following code is to upload resume file to server
    try:
        uploadfile = request.files['uploadfile']
    except:
        uploadfile = None

    if uploadfile:
        uploadfilename = uploadFile(uploadfile)
        
        resume_data = matching.resume_m_jobs(uploadfilename, Keywords)
        #resume_data = pd.read_csv('./jobs_db.csv', index_col=0)

        result = viewing.dataframe(resume_data)
    else:
        result = "No Profile to upload"

    return render_template('ResumePageResult.html', results = result)


@app.route('/updateJDAction', methods=['POST'])
def updateJDAction():
    name = request.form['name']
    Keywords = request.form['keyword']
    Description = request.form['Description']
    # Following code is to job description file to server
    if Description:
        # with open(f"{app.config['JD_Folder']}{name}.txt", "w", encoding = 'utf-8') as file:
        #     file.write(Description)

        job_title = str(name).split("-")[1]    # get title from name
        # print("jd title", job_title)
        job_str = job_title.strip() + " " + str(Description)
        match_people = matching.job_m_resumes(job_str, Keywords)
        #resume_data = pd.read_csv('./resume_db.csv', index_col=0)

        result = viewing.dataframe(match_people)
        
    else:
        result = "Please enter Job Description for profile match"

    return render_template('JDPageResult.html', results = result)


@app.route('/QSSkillsResults', methods=['POST'])
def QSSkillsResults():
    keyword = request.form['name']
    # Following code is to job description file to server
    if keyword:
        keyword = request.form['name']
        quickcv = pd.read_csv('./DB/Resume.csv')
        filtered_resume = quickcv.sample(frac=1)
        filtered_resume = filtered_resume.loc[filtered_resume['Resume_str'].str.lower().str.contains(keyword.lower())].head(10)
        filtered_resume = filtered_resume.drop(columns= ['Resume_str', 'Resume_html'])
        filtered_resume["ID"] = filtered_resume["ID"].apply(int)
        result = viewing.dataframe(filtered_resume)
        #result = table.to_html()
        #result = result.to_html(classes='table table-stripped')
        
    else:
        result = "Please enter Job Description for profile match"

    return render_template('QSCandidatesResult.html', results = result)

@app.route('/QuickSearchJobs', methods=['POST'])
def QuickSearchJobs():
    keyword = request.form['name']
    if keyword:
        quickjob = pd.read_csv('./DB/jobs.csv', encoding="UTF-8")
        # print("alljob",quickjob.columns)
        filtered_jobs = quickjob.sample(frac=1)
        filtered_jobs = filtered_jobs.loc[filtered_jobs['jobtitle'].str.lower().str.contains(keyword.lower())].head(10)
        # filtered_jobs = filtered_jobs.drop(columns= ['education', 'experience', 'jobdescription',
        #                                         'joblocation_address', 'numberofpositions', 'payrate',
        #                                         'postdate', 'site_name', 'skills', 'uniq_id'])
        filtered_jobs = filtered_jobs[['jobid','company','jobtitle']]
        # Following code is to job description file to server
        filtered_jobs["jobid"] = filtered_jobs["jobid"].apply(int)
        result = viewing.dataframe(filtered_jobs)
    else:
        result = "Please enter keyword for a quick profile match"

    return render_template('QSJobsResult.html', results = result)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)