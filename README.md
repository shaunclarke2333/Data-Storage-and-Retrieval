# Using Python and SQLAlchemy to do basic climate analysis and data exploration of a climate database

Using Python and SQLAlchemy to do basic climate analysis and data exploration of a climate database. The analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


Precipitation Analysis


Design a query to retrieve the last 12 months of precipitation data.
Select only the date and prcp values.
Load the query results into a Pandas DataFrame and set the index to the date column.
Sort the DataFrame values by date.
Plot the results using the DataFrame plot method.


Use Pandas to print the summary statistics for the precipitation data.


Station Analysis


Design a query to calculate the total number of stations.

Design a query to find the most active stations.


List the stations and observation counts in descending order.
Which station has the highest number of observations?
Hint: You may need to use functions such as func.min, func.max, func.avg, and func.count in your queries.



Design a query to retrieve the last 12 months of temperature observation data (tobs).


Filter by the station with the highest number of observations.
Plot the results as a histogram with bins=12.



Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.


Use FLASK to create your routes.



Routes



/


Home page.
List all routes that are available.



/api/v1.0/precipitation


Convert the query results to a Dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary.



/api/v1.0/stations


Return a JSON list of stations from the dataset.



/api/v1.0/tobs


query for the dates and temperature observations from a year from the last data point.
Return a JSON list of Temperature Observations (tobs) for the previous year.
