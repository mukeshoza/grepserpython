from geopy import geocoders
from pygeocoder import Geocoder
import pandas as pd
import numpy as np
gn = geocoders.GeoNames(username="mukeshojha")
cityname = input('Enter city name: ')
place, (lat, lng) = gn.geocode(cityname)
print("%s: %.5f, %.5f" % (place, lat, lng))

# data = {'Site 1': '31.336968, -109.560959',
#         'Site 2': '31.347745, -108.229963',
#         'Site 3': '32.277621, -107.734724',
#         'Site 4': '31.655494, -106.420484',
#         'Site 5': '30.295053, -104.014528'}
#
# df = pd.DataFrame.from_dict(data, orient='index')
#
# # Create two lists for the loop results to be placed
# lat = []
# lon = []
#
# # For each row in a varible,
# for row in df[0]:
#     # Try to,
#     try:
#         # Split the row by comma, convert to float, and append
#         # everything before the comma to lat
#         lat.append(float(row.split(',')[0]))
#         # Split the row by comma, convert to float, and append
#         # everything after the comma to lon
#         lon.append(float(row.split(',')[1]))
#     # But if you get an error
#     except:
#         # append a missing value to lat
#         lat.append(np.NaN)
#         # append a missing value to lon
#         lon.append(np.NaN)
#
# # Create two new columns from lat and lon
# df['latitude'] = lat
# df['longitude'] = lon
#
# print(df)
