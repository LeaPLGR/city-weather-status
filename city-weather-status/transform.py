import json
import extract
import numpy as np


def det_status(data):
    return data.get("status", "Not found")


def get_aqi(data):
    return data.get("data").get("aqi", np.nan)


def get_coor(data):
    return data.get("data").get("city").get("geo", np.nan)


def get_hum(data):
    return data.get("data").get("iaqi").get("h").get("v", np.nan)


def get_temp(data):
    return data.get("data").get("iaqi").get("t").get("v", np.nan)


def get_pm25(data):
    return data.get("data").get("iaqi").get("pm25").get("v", np.nan)


def get_pm10(data):
    d = data.get("data").get("iaqi").get("pm10", np.nan)
    if d != np.nan:
        return data.get("data").get("iaqi").get("pm10").get("v", np.nan)
    else:
        return np.nan


def get_forecast_pm25(data):
    return data.get("data").get("forecast").get("daily").get("pm25", np.nan)


def color(n):
    if n >= 0 and n <= 50:
        return "green"
    elif n > 50 and n <= 100:
        return "yellow"
    elif n > 100 and n <= 150:
        return "orange"
    elif n > 150 and n <= 200:
        return "red"
    elif n > 200 and n <= 300:
        return "purple"
    else:
        return "black"


def background_df(n):
    if n["AQI"] == "0-50":
        return f"background-color: 'green'"
    elif n["AQI"] == "50-100":
        return f"background-color: 'yellow'"
    elif n["AQI"] == "100-150":
        return f"background-color: 'orange'"
    elif n["AQI"] == "150-200":
        return f"background-color: 'red'"
    elif n["AQI"] == "200-300":
        return f"background-color: 'purple'"
    else:
        return f"background-color: 'black'"


# print(get_forecast_pm25(extract.extract_AQI_city("London")))
