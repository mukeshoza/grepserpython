from geopy.geocoders import Nominatim
from geopy import geocoders
# geolocator = Nominatim()
gn = geocoders.GeoNames(username="mukeshojha")
import numpy as np


def geolocate(city=None, country=None, zip=None):
    '''
    Inputs city and country, or just country. Returns the lat/long coordinates of
    either the city if possible, if not, then returns lat/long of the center of the country.
    '''

    # If the city exists,
    if city != None:
        # Try
        try:
            # To geolocate the city and country
            loc = gn.geocode(str(city + ',' + country + ',' + zip))
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan
    # If the city doesn't exist
    else:
        # Try
        try:
            # Geolocate the center of the country
            loc = gn.geocode(country)
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        # Otherwise
        except:
            # Return missing value
            return np.nan

# Geolocate a city and country
abc = geolocate(city='Dallas', country='USA', zip='75001')
print(abc)