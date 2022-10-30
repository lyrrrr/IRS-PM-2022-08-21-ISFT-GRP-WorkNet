## SECTION 1 : PROJECT TITLE

## **Bidirectional Job & Resume Matching System**

![image-20221030183558730](/Users/liyurui/Library/Application Support/typora-user-images/image-20221030183558730.png)

------

## SECTION 2 : EXECUTIVE SUMMARY

In the currents economy environment where there is a huge demand for talent, the problems of how job seekers find their desirable job efficiently, and how enterprises choose the right candidates they need, has become a social issue that needs to be further addressed. The existing diverse platforms, such as the LinkIn and JobStreet, they do provide various of information, but it is always difficult for users to accurately find the jobs or candidates they want or match their requirements from such a large amount of information, which leads to an low efficiency for job search and recruitment.

In this project, a Bidirectional Job & Resume Matching System is proposed which will provide a platform for both HR managers and job seekers to upload their profiles, make a quick search, and get the recommendation results of best matching candidates and jobs. Doc2Vec model and Term Frequency-inverse Document Frequency (TF-IDF) model were selected and trained to process with the data and achieve the function of accurately matching by extracting the features from information from the upload files. A website based on the Flask framework was also built to provide simple interactive interface. It is hoped that through this streamlined interface, the unnecessary information and steps in the job search and recruitment process can be reduced.

This report will introduce and analyse the project through 6 sections, which are the Business Problem Background, the Market Research, the Problem Description, the Project Solution, the Project Implementation and the Project Performance & Validation to present the project concept and project results.

------

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name     | Student ID (MTech Applicable) | Work Items (Who Did What)                                    | Email (Optional)   |
| ---------------------- | ----------------------------- | ------------------------------------------------------------ | ------------------ |
| LI YURUI               | A0261750J                     | System Architecture Design<br />Data Acquisition and Processing <br />Retrieval Model Development | E0983144@u.nus.edu |
| LI FANGQING            | A0261793W                     | Product Prototype Design<br/> Business Flow Design<br/> Report Writing and Video Recording | E0983187@u.nus.edu |
| PRADEEP KUMAR ARUMUGAM | A0261606J                     | User Interface Development Website Development Video Recording | e0983000@u.nus.edu |

------

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

## Marketing Video

[![](/Users/liyurui/Library/Application Support/typora-user-images/image-20221030182319245.png)](https://youtu.be/5CQ3vliPs-s )

## Technical Video

[![截屏2022-10-30 下午6.27.21](/Users/liyurui/Desktop/截屏2022-10-30 下午6.27.21.png)](https://youtu.be/g8jw_G5u2wQ)

------

## SECTION 5 : USER GUIDE

[UserGuide](https://github.com/lyrrrr/IRS-PM-2022-08-21-ISFT-GRP-WorkNet/tree/main/ProjectReport)

### [ 1 ] To run the webapp in local machine

>  (Notes: Preferred Python 3.7 or above)

> Open up your command prompt/terminal

> Do git clone https://github.com/lyrrrr/IRS-PM-2022-08-21-ISFT-GRP-WorkNet or go to git url mentioned above to directly download the project, unzip and keep it in your folder directory.

> pip install the components from requirements.txt

> cd <your folder path>\Systemcode\WORKNET	

> Run the server.py with python
>
> - py server.py
> - py3 server.py (if you have different versions of python)

> Once it’s done, you’ll see this line in your command prompt “Running on http://192.168.10.106:8080/ (Press CTRL+C to quit)” wither copy paste this url or directly go to any of your web browser and type http://localhost:8080/ and you’ll be able to access our webapp



### [ 2 ] To run the webapp in VM

> Open up your terminal

> git clone <https://github.com/lyrrrr/IRS-PM-2022-08-21-ISFT-GRP-WorkNet>

> pip install the components from Systemcode\WORKNET\requirements.txt

> cd <your folder path>\Systemcode\WORKNET	

> Run the server.py with python
>
> - $python server.py
>
> - $python3 server.py (if you have different versions of python)

> Go to URL using web browser http://localhost:8080/ or http://192.168.10.106:8080/



### [ 3 ] Additional comments

You might encounter issues with libraries like numpy/pandas. During such instances, please ensure to install those libraries in the environment where your python path variable is configured. This is common compatibility issue if you have multiple setups in different environments depending on the setup of your system. A simple solution might be to uninstall and reinstall those libraries.



The data preprocess and modelling is develop in colab environment. If you want to regenerate the feature vector dataset and model used in website, please run code in folder of *data_preprocess_and_modelling*. The folder content is shown as followed:

- data: store the raw datasets of our project

- data_gathering: do some preprocess, analysis and visualization of dataset

- Modelling: build, train models, and generate feature vectors of datasets

- models: store trained model

- matching: test on colab for vector matching



Datasource we used:

​			[Job Dataset](https://www.kaggle.com/PromptCloudHQ/jobs-on-naukricom)

​			[Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)

------

## SECTION 6 : PROJECT REPORT / PAPER

[ProjectReport](https://github.com/lyrrrr/IRS-PM-2022-08-21-ISFT-GRP-WorkNet/tree/main/ProjectReport)

------

## SECTION 7 : MISCELLANEOUS

[Miscellaneous](https://github.com/lyrrrr/IRS-PM-2022-08-21-ISFT-GRP-WorkNet/tree/main/Miscellaneous)

