from geopy.geocoders import Nominatim
from config import KEY, BASE_URL

geolocator = Nominatim(user_agent="tripadivsor")

f = open("data/user/address_user_new.txt", "r")

coordinates = f.readlines()

for coordinate in coordinates:

    location = geolocator.reverse(coordinate)
    print(coordinate)

    country = location.raw["address"].get("country") 
    region = location.raw["address"].get("region")
    tow = location.raw["address"].get("town")
    city = location.raw["address"].get("city")
    village = location.raw["address"].get("village")

    if tow:
        location = tow

    elif city:
        location = city
    
    elif village:
        location = village

    print(country," ", region, " ", location)
    with open('data/user/address_user_new_2.txt', 'a', encoding="utf-8") as f:
        f.write(str(country) + ',' + str(region) + ',' + str(location) + "," + coordinate)
        f.close()
