
# to find the country location
import phonenumbers
from MyPhone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,'en')
print(location)


# To find the service provider of simcard
from phonenumbers import carrier

service_Pro = phonenumbers.parse(number)
service_provider = carrier.name_for_number(service_Pro,"en")
print(service_provider)

# Opencage for lattitude and longitude
from opencage.geocoder import OpenCageGeocode

key='8ec93a5440e2434d86324382861bca5d'
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
print(result)
lat = result[0]['geometry']['lat']

# {'lat': "22° 21' 4.01328'' N", 'lng': "78° 40' 3.87408'' E"}
lng = result[0]['geometry']['lng']
print(lat,lng)

import folium
MyMap = folium.Map(location=[lat,lng],zoom_start = 9)
folium.Marker([lat,lng],popup=location).add_to(MyMap)
MyMap.save("myloc.html")