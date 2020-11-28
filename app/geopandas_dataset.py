from  geopy.geocoders import GoogleV3
from utils import get_address_df, get_user_location
from config import KEY, BASE_URL

user_location = get_user_location()

geolocator = GoogleV3(api_key=KEY)

latitude = []
longitude = []
display_name = []

cont = 1

for location in user_location:
  
    print("Location ", cont, " " , location)
    try:
        geolocation = geolocator.geocode(location)
        latitude = geolocation.latitude
        longitude = geolocation.longitude

        print(geolocation)
        with open('data/user/address_user_new.txt', 'a', encoding="utf-8") as f:
            f.write(str(latitude) + ',' + str(longitude) + '\n')
            f.close()
    except:
        with open('data/address_user_new.txt', 'a', encoding="utf-8") as f:
            f.write("," + '\n')
            f.close()


    cont = cont + 1