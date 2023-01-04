# How are CodeUp students using the curriculum?
## Anomaly detection group project
- by Woody Sims, John "Chris" Rosenberger, Cristina Lucin




### Project Description
### Provided a sample prompt, produce a slide and a more detailed email response to your employer

***You are a junior data scientist on CodeUp data science team and recieve the following email in your inbox:***

    Hello,


    I have some questions for you that I need to be answered before the board meeting Wednesday afternoon. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.


    1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
    2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
    4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
    5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
    6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
    7. Which lessons are least accessed?
    8. Anything else I should be aware of?


    Thank you,

## Data Dictionary

| Feature | Definition | Manipulations applied|Data Type|
|--------|-----------|-----------|-----------|
||
|||**Categorical and Object Data**
||
|*cohort_name*| Name of codeUp Cohort  | | category
|*program_name*| CodeUp program type  | PHP or Java (web developers) or Data-Science| category
|*page*| Webpage accessed by person  | CodeUp curriculum is hosted on server and any part can be accessed via internet| object
|*id*| id of person who accessed webpage  | id is associated with students and staff individuals and anonymized| category
|*ip*| ipaddress of computer which accessed webpage | | category
||
|||**Chronological Data**
||
|*date*|  date the webpage was accessed | | DatetimeIndex
|*start_date*|  date a student began program with codeUp | year, month, day format| datetime64
|*end_date*|  date a student finished program with codeUp | year, month, day format| datetime64
|*program_length*|  duration of student's time with codeUp | year, month, day format| datetime64
||



## Steps to Reproduce
**note: A .txt file accompanied the email which will not be provided in this repo for security purposes.**
**If you do not have a copy of that .txt file, you will not be able to reproduce this project**
1) Clone this repo into your computer.
2) Modules and data are expected to be contained in the project folder
3) Run the cells in the ```final_project_notebook.ipynb``` file.

