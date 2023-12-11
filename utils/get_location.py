from aiogram import types


# function for calc distance between two locations (lat1, lon1) and (lat2, lon2)
async def calc_distance(lat1, lon1, lat2, lon2):
    from math import sin, cos, sqrt, atan2, radians

    # approximate radius of earth in km
    radius = 6373.0

    # convert degrees to radians
    lat1 = radians(float(lat1))
    lon1 = radians(float(lon1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(lon2))

    # calculate difference between latitudes and longitudes
    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1

    # calculate distance
    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
    distance = 2 * radius * atan2(sqrt(a), sqrt(1 - a))

    return round(distance, 2)


# choose the nearest location from the list
def show_gmaps(lat, lon):
    return f'https://www.google.com/maps?q={lat},{lon}'


async def choose_nearest_location(location: types.Location):
    distances = []
    for shop_name, shop_location in SHOPS:
        distances.append(
            (shop_name,
             await calc_distance(location.latitude, location.longitude, shop_location['lat'], shop_location['lon']),
             show_gmaps(shop_location['lat'], shop_location['lon']),
             shop_location)
        )
