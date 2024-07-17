import streamlit as st
import numpy as np
import pandas as pd
import transform as tf
import extract as ex
import folium
from streamlit_folium import st_folium
from constants import AQI_LEVELS


st.title("City Weather Status App")

with st.expander("About this app"):
    st.write(
        "Display weather features such as temperature, humidity, air quality and UV indexes for a chosen city"
    )

st.sidebar.header("Input")
user_city = st.sidebar.text_input("Chose a city")

st.header("Results")

col1, col2 = st.columns(2)

with col1:
    if user_city != "":
        data = ex.extract_AQI_city(user_city)
        coor = tf.get_coor(data)
        aqi = tf.get_aqi(data)

        # Display map with pin containing values
        m = folium.Map(tiles="OpenStreetMap", location=coor)
        folium.Marker(
            coor, icon=folium.Icon(color=tf.color(aqi))  # , prefix="fa", icon="star"
        ).add_to(m)
        st_folium(m, center=coor, height=300, width=300)

with col2:
    if user_city != "":
        data = ex.extract_AQI_city(user_city)
        temp = tf.get_temp(data)
        coor = tf.get_coor(data)
        lat, lon = coor[0], coor[1]
        hum = tf.get_hum(data)
        aqi = tf.get_aqi(data)
        pm25 = tf.get_pm25(data)
        pm10 = tf.get_pm10(data)
        df = pd.DataFrame(
            {
                "temperature": [temp],
                "humidity": [hum],
                "air quality index": [aqi],
                "pm25": [pm25],
                "pm10": [pm10],
            }
        )

        st.write(df.T)
        st.write(AQI_LEVELS.style.apply(tf.background_df, axis=1))
