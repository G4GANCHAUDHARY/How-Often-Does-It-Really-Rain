# numpy to handle large arrays of coordinates data 
# matplotlib pyplot to represent the data on to the map
# Basemap to represent a world map with parallels, meridians, coastlines, countries, states etc.
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Storing data in numpy arrays from .csv files
lat = np.genfromtxt('latitude.csv', delimiter=",")
lon = np.genfromtxt('longitude.csv', delimiter=",")
data = np.genfromtxt('Data.csv', delimiter=",")

# Taking longitude and latitude mean as origin for basemap,i.e., lon_0,lat_0 = 180 , 0
lon_0 = lon.mean()
lat_0 = lat.mean()

# Basemap 
m = Basemap(resolution='c',lat_0=lat_0,lon_0=lon_0)

# preparing a matrix(numpy meshgrid) to store precipitation data for a particular longitude and latitude
lons, lats = np.meshgrid(lon, lat)
xi, yi = m(lons, lats)

# representing data for each grid as a color to distinguish 
my_cmap = plt.get_cmap('rainbow')
my_cmap.set_under('white')
cs = m.pcolormesh(xi,yi,data,cmap = my_cmap)

# parallels, meridians, coastlines, countries, states for basemap
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 20.), labels=[0,0,0,1], fontsize=10)

m.drawcoastlines()
m.drawstates()
m.drawcountries()

# bar to recognise the data value for a particualr color in a grid
cbar = m.colorbar(cs, size='5%', location='bottom', pad="10%")
cbar.set_ticks([i for i in range(0,101,5)])


# Plot the final map
plt.title('Total Precipitation')

plt.show()