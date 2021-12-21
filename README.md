# How Often Does It Really Rain?

# Introduction
The answer to the question” How often does its rain?” has been tried to be derived by considering three prominent factors - amount, frequency and intensity). Amount of rainfall depends majorly upon the energy availability and temperature changes which are mostly responsible for intensity/ frequency changes. The threshold rainfall intensity considered here is 0.02mm/hr. Rainfall data has to be interpreted hour-wise and contour is plotted in reference to the data which contains percentage time during which intensity of precipitation exceeds 0.02 mm/hour. The dataset extracted and used for making our contour in this project is from 90 degrees North to 90 degrees south.

# Objectives
--> Collections of global area surface precipitation data(90 0 N to 90 0 S) from ECMWF(European Centre for Medium - Range Weather Forecast) ERA 5 data set.

--> Plot the retrieved data into a single global contour.

--> To anlayze the data and establish a general trend of the retrived global precipitation.


# Data
DATA SOURCE - https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview

1. HORIZONTAL COVERAGE	           -          Global 
2. HORIZONTAL RESOLUTION	         -          Reanalysis: 0.250 * 0.250 
3. TEMPORAL COVERAGE	             -          1998 to 2018 
4. TEMPORAL RESOLUTION	           -          Hourly 
5. FILE FORMAT	                   -          netCDF

# PLOTTING THE MAP  
Using these csv files, a plot is made by using the matplotlib library. First the data is loaded into python using these csv files as numpy array then used the “basemap” module in matlplotlib in order to create the plot.


# Result
![plot](https://user-images.githubusercontent.com/93081077/146894489-c735d88a-1f53-4356-b51b-114f1bd88d72.png)

# General Trends 
1. The maximum percentage time of precipitation lies between 30%-40% if the average threshold value for the rainfall intensity is 0.02mm/hr. 
2. Precipitation occurs more over the oceanic regions where there is an abundant supply of water.
