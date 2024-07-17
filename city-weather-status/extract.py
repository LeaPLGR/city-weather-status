import requests
from constants import AQI_KEY, AQI_URL_FEED, AQI_URL_MAP


def extract_AQI_city(city, key=AQI_KEY):
    params = {"token": AQI_KEY}
    response = requests.get(url=AQI_URL_FEED + city, params=params)
    response.raise_for_status()
    return response.json()


def extract_AQI_loc(lat, lng, key=AQI_KEY):
    params = {"token": AQI_KEY}
    response = requests.get(url=AQI_URL_FEED + "geo:" + lat + ";" + lng, params=params)
    response.raise_for_status()
    return response.json()


def extract_AQI_map(lat1, lat2, lng1, lng2, key=AQI_KEY):
    params = {
        "token": AQI_KEY,
        "latlng": f"{lat1},{lng1},{lat2},{lng2}",
        "networks": "all",
    }
    response = requests.get(url=AQI_URL_MAP, params=params)
    response.raise_for_status()
    return response.json()


print(extract_AQI_map(39.379436, 40.235643, 116.091230, 116.784382))
# https://api.waqi.info/v2/map/bounds?latlng=39.379436,116.091230,40.235643,116.784382&networks=all&token=demo
