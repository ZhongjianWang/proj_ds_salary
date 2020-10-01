# Data Science Job in Germany(Düsseldorf): Project Overview 
I want to land a data scientist job in Düsseldorf, so i want to find out the most important qualifications companies are looking for when recruiting a data scientist in Germany and especially in Düsseldorf
* Scraped 900 job descriptions from glassdoor.de using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and SAP. 
* exploratory data analysis, get an overall idea how to prepare for appying such a job 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  

## Web Scraping
Tweaked the web scraper github repo (above) to scrape 900 job postings from glassdoor.de. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company 
*	Location
*	Company Headquarters 
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue
*	Competitors 

## Data Cleaning
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R  
    * Excel  
    * AWS  
    * ML 
    * SAP
*	Column for simplified job title and Seniority 
*	Column for description length 

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. A few highlights are listed below. Here are some interesting aspects i found out: 
* SQL,ML,Python are the three main requirements in term of skillsets
* SAP knowledge is not mandatory in most companies which is not what i expected
* The word cloud is based on the job description in which **Team** and **Kunden** really stand out

![alt text](https://github.com/ZhongjianWang/proj_ds_salary/blob/master/company.png "Recruiters Name")
![alt text](https://github.com/ZhongjianWang/proj_ds_salary/blob/master/business_sector.png "Recruiters Business Sector")
![alt text](https://github.com/ZhongjianWang/proj_ds_salary/blob/master/SQL.png "SQL Requirement")
![alt text](https://github.com/ZhongjianWang/proj_ds_salary/blob/master/ML.png "Machine Learning Requirement ")
![alt text](https://github.com/ZhongjianWang/proj_ds_salary/blob/master/python.png "Python Requirement")
![alt text](https://github.com/ZhongjianWang/proj_ds_salary/blob/master/SAP.png "SAP Requirement")

![alt text](https://github.com/ZhongjianWang/proj_ds_salary/blob/master/GlassdoorDUS.png "DUS job word cloud")



## Resources
This project is mainly following the toturials from Ken Jee anaysing data scientist salaries in the USA
https://github.com/PlayingNumbers/ds_salary_proj

https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

