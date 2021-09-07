# Olympics

#### Overview: A streamlit app that analysis the data of 120 years of Summer Olympics games.

#### Dataset: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

#### About the project:
The main goal of this project is to analyse the 120 years of Olympics dataset and to create a POC. The dataset was collected from Kaggle which contains two csv files. In the "athlete_events.csv" each row is an athlete-event, that has features like name, sex, height, weight, sport, team, etc. The other dataset, "noc_regions.csv" contains information about NOC (National Olympic Committee, 3 letter code), Country name and notes. We have data till 2016 Olympics. I have considered only Summer Olympics in this entire project and based on that all the analysis were performed. I have used a jupyter Notebook file for the entire analysis and three python files for creating the application. App was created using Streamlit. All the functions present in the python files are also there in the jupyter notebook which will give a clear understanding about the entire code. The analysis was divided into four parts like Medall Tally, Overall Analysis, Country wise Analysis and Athlete wise Analysis. There were some problems with the dataset due to historical reasons, which I tried to handle with utmost efficiency. For medal tally, I have used one hot encoding to get individual features for Gold, Silver and Bronze. Here, according to my analysis USA won 2472 Gold Medals but in reality they won around 1022 Gold medals. When I considerd India it was comming somewhere around rank 25 with 131 Gold Medals where as in reality India won 9 Gold Medals till 2016. It was a problem with the dataset as we have athlete wise data. A team comprising of 11 players winning a Gold medal was considered a Gold Medal won by every player. Hence, this increased the medal counts. To resolve this issue, I removed the duplicate rows from the features Team, NOC, Games, Year, City, Sports and Events. Then medal tally was counted by grouping NOC with Gold, Silver and Bronze medals. Still some amount of exceptions were present mainly due to the reason of hstorical partitions of countries or name changes.  Here, in the dataset, 29 times Olympics was held before 2021. But the fact is, it was held 28 times according to records. The reason here is that there was an Olympic that was held back in 1906. But due to some reasons that Olympic game was no more considered. So I had to take 28 for our further analysis.

## Installation
The Code is written in Python 3.7.3 If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:

##### 1. First create a virtual environment by using this command:
```bash
conda create -n myenv python=3.7
```
##### 2. Activate the environment using the below command:
```bash
conda activate myenv
```
##### 3. Then install all the packages by using the following command
```bash
pip install -r requirements.txt
```
##### 4. Then, in cmd or Anaconda prompt write the following code:
```bash
streamlit run app.py
```
##### Make sure to change the directory to the root folder.  


## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download Heroku CLI to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── Olympic Data Analysis.ipynb
├── helper.py
├── Procfile
├── README.md
├── app.py
├── olympic.png
├── preprocessor.py
├── setup.sh
├── requirements.txt
```

## Front end using Streamlit
Demo view: https://olympicseda-sm.herokuapp.com/

![Screenshot (135)](https://user-images.githubusercontent.com/75041273/132350953-c2e82abd-e718-41cf-a959-54370e26e39c.png)
![Screenshot (136)](https://user-images.githubusercontent.com/75041273/132350800-961f5ddb-b7cc-44dd-ad86-c1391021f01d.png)
![Screenshot (146) (1)](https://user-images.githubusercontent.com/75041273/132352416-ed7cd2d6-5c72-42ce-b82b-fa4783cf2781.png)
![Screenshot (144)](https://user-images.githubusercontent.com/75041273/132351831-c192620b-7a2e-4391-8eee-31830c153cca.png)
![Screenshot (145) (1)](https://user-images.githubusercontent.com/75041273/132352032-371cde59-47b1-48c3-a8b6-9fc575eebbc3.png)
![Screenshot (137)](https://user-images.githubusercontent.com/75041273/132351014-5af80e25-4731-4332-81fd-0611a1b26dc7.png)
![Screenshot (138)](https://user-images.githubusercontent.com/75041273/132351034-e8910a45-d8b3-4e4d-955e-25e06035cdcf.png)
![Screenshot (140)](https://user-images.githubusercontent.com/75041273/132351055-e324b880-54a9-40ff-96b7-16cb60b55c1e.png)
![Screenshot (141)](https://user-images.githubusercontent.com/75041273/132351077-34f62d91-d8b0-4702-a226-745624c85d4f.png)
![Screenshot (142)](https://user-images.githubusercontent.com/75041273/132351100-4f52f6d0-8fd0-4b58-9b00-ae40ef998e1e.png)
![Screenshot (143)](https://user-images.githubusercontent.com/75041273/132351168-d94d8bb0-5854-414a-b3a2-d7dce8ac9f3e.png)


