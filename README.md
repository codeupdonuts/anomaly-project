# clustering-project
Clustering Project by Chis Rosenberger and Nadia Paz
#### Where did Zillow go wrong?
##### Predicting errors on Zestimates - December 2, 2022

## Project's Goal
Create cluster groups for the zillo data. Create machine learning models that will predict zestimate's ```logerror```

## Project's Purpose
Evaluate if clusters help with improving prediction results.

## Steps to Reproduce
1) Clone this repo into your computer.
2) Acquire the data from databaase using your ```env.py``` file
3) Put the data in the file containing the cloned repo.
4) Run the ```presentation_notebook.ipynb``` file.

## Project's pipeline

### Aqcuire and prepare
1. Acquire'zillow 2017' data from the public facing CodeUp database. Transform the data to a Pandas dataframe for manipulating using Jupyter Notebook.
2. Prepare the data for exploration and analysis. Find out if there are some values missing and find a way to handle those missing values.
3. Change the data types if needed
4. Find if there are features which can be created to simplify the exploration process.
5. Determine which observations are outliers and handle them.
6. Create a data dictionary.
7. Split the data into 3 data sets: train, validate and test data (56%, 24%, and 20% respectively)

### Explore and pre-process
1. Explore the train data set through visualizations and statistical tests. 
2. Determine which variables have statistically significant relationships with zestimates errors. 
2. Make the exploration summary and document the main takeaways.
3. Impute the missing values if needed.
4. Pick the features which can help to build a good prediction model.
5. Identify if new features must be created to improve the model's accuracy.
6. Encode the categorical variables.
7. Split dataframe into segments if those segments represent different populations.
8. Split the target variable from the data sets.
9. Scale the data prior to modeling.

### Explore clusters to add features to model
1. Create clusters using based on KMeans algorithm.
2. Determine if any or all clusters crafted add useful information to model by running them on our models.

### Build a regression model
1. Pick the regression algorithms for creating the prediction model.
2. Create the models and evaluate regressors using **Adjusted R-Squared** score on the train data set.
3. Create models based on obtained clusters.
4. Split data sets based on the location and create regression models.
4. Find out which of data splits provides best results.
5. Make predictions for the test data set.
6. Evaluate the results.

### Report results from models built

### Draw conclusions

## Data Dictionary


| Feature | Definition | Manipulations applied|Data Type|
|--------|-----------|-----------|-----------|
||
|||**Categorical Data**
||
|*county_name*| Identifying Regions: counties and LA city proper  | Used fips and city ID to determine 'LA', 'Orange', 'Ventura' counties and 'LA_city' proper| category
|||**Numerical Data**
||
|*beds*|  Number of bedrooms | Changed the type into integer| integer
|*bath*|  Number of bathrooms | Half-bathrooms were turned into whole number, changed the type intoto integer| integer
|*bed_bath_ratio*|  The ratio of bedrooms to bathrooms | Divided bedroom number by bathroom number | float
|*lot_sqft*| Size of the plot of land the house sits on | Changed the type into integer| integer
|*age*| Age of the house | Created the column by subtracting the year_built from 2017| integer
|*tax_amount*| The home value assessed by the tax collection authority | integer
|*garage_sqft*| Size of the garage with the property | Changed the type into integer| integer
||
|||**Boolean Data**
|*fireplace*| Identifies whether a home has a hottub or a spa | |boolean
|*hottub_spa*| Identifies whether a home has a hottub or a spa | |boolean
|*garage*| Identifies whether a home has a garage | | boolean
|||**Target Data**
||
|**logerror** | **The difference between Zillow's estimated price and actual sale price** | **standardized using logarithmic ratio** | **float**

#### Data preparation takeaways:
To clean data:
- Removed duplicates
- Removed all columns with id numbers
- Removed some of the outliers:
    * min ```sq_feet = 300``` and max ```sq_feet = 300``` 
    * maximum ```bedrooms = 6```
    * maximum ```bathrooms = 6```
    * data where both ```bedrooms``` and ```bathrooms``` are equal to 0
    * half ```bathrooms``` turned into whole bathrooms (2.5 bathrooms = 2)
    * ```logerror``` outliers below ```-0.55``` and above ```0.55```
- Filled the ```null``` values with zeros in the columns that represent facilities such as quantity of garages, pools, fireplaces etc. 
**Final results**
- After the cleaning the data set contains 49,380 rows and 23 columns.
- Approx. 5.6% of the observations were removed from the original data set.

#### Exploration Takeaways
- There is a significant difference in means among different locations. Splitting data based on location might be a good idea.
- ```zip``` codes can not provide us with the information that can potentially be usefull in the clustering or modeling
- ```latitude``` and ```longitude``` are potentially good variables for clustering.
- Continious features don't show much correlation with our target variable. 

#### Clustering Takeaways
Some of cluster groups showed significant difference between the group's ```logerror``` mean and the population ```logerror``` mean. That's why we are going to create different models based on the clusters.

#### Modeling summary
- All models predict logerror score terribly. 
- Creating clusters helped to improve some models' results by a bit.
- Splitting the data into different data sets helped to improve some of results.
- Even though we specifically chose features which appear to tell us something about the log error, as eyeballing the data and our statistical tests showed, we were unable to create models which reliably were able to demonstrate that we could improve the zestimate model's performance. 

### Next steps and recommendations
To begin, it is important to stress that it is difficult to work with and understand what the zillow estimate model takes into account. Furthermore, not understanding how the ```logerror``` figure was transformed and standardized makes it difficult to work a model that properly targets variables which are not being properly utilized by the zillow data science team. 

Based on our best efforts, we were unable to significantly improve upon the zestimate model. It is likely that with the data that we were given to work with, there are important factors which are either not measurable or they simply have not been brought into the data which we are working with. 

If the goal is for zillow to best predict the selling price for a home a couple of counfounding factors that might be incorporated into the model might include estimates for the place the economy is in regarding the business cycle. At the height of the business cycle, homes sell for more while in a trough (recession), homes sell for less. Other facts which may be required to judge the selling price of any individual house is a quick inspection regarding the aesthetic value of the house compared to its neighbors in a certain range of location - a service which many realtors provide to their customers, for which zillow could contract.

Without critical information such as those postulated above, quirks which do not show up in raw numbers in any given day's home selling will be difficult if not impossible to ascertain and leads to the errors not unlike those which zillow's zestimates produced over the year 2017. 