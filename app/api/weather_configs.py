"""
Date: 01/14/2026
Author: Michael Baburyan

Details: 
    - configurations for weather api
	- params is injected into weather api's forecast endpoint query
	- retrieve data from response, format using pandas and numpy
"""

import pandas as pd
import numpy

from openmeteo_sdk.WeatherApiResponse import WeatherApiResponse
from config import latitude, longitude, timezone

# weather parameters for NY, taken form the api documentation
def getParams() -> dict:
	params = {
		"latitude": latitude,
		"longitude": longitude,
		"daily": ["temperature_2m_max", "temperature_2m_min", "uv_index_max", "sunset"],
		"hourly": ["precipitation_probability", "precipitation"],
		"timezone": timezone,
		"forecast_days": 1,
		"wind_speed_unit": "mph",
		"temperature_unit": "fahrenheit",
		"precipitation_unit": "inch",
	}

	return params

# process hourly data. The order of variables needs to be the same as requested.
def getHourlyWeather(response: WeatherApiResponse) -> str:

	# pull hourly data from response; see parameters for schema 
	hourly = response.Hourly()
	hourly_precipitation_probability = hourly.Variables(0).ValuesAsNumpy().astype(int)
	hourly_precipitation = hourly.Variables(1).ValuesAsNumpy().round(1)

	# create dict to store response data with times
	hourly_data = {"time": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	).strftime("%H:00")}

	# add response data to dict
	hourly_data["Chance of Rain"] = hourly_precipitation_probability.astype(str) + " %"
	hourly_data["Inches of Rain"] = hourly_precipitation.astype(str) + " Inches"

	# create pandas dataframe from dict; convert to html
	hourly_dataframe = pd.DataFrame(data = hourly_data).reset_index(drop=True).to_html(
		index=False,
		border=1,
		classes="dataframe",
		justify="center"
	)

	# return html as string
	return hourly_dataframe

# process daily data. The order of variables needs to be the same as requested.
def getDailyWeather(response: WeatherApiResponse) -> str:

	# pull daily data from response; see parameters for schema 
	daily = response.Daily()
	daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy().astype(int)
	daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy().astype(int)
	daily_uv_index_max = daily.Variables(2).ValuesAsNumpy()

	# sunset time returned as unix timestamp, use pandas to convert to ISO format
	daily_sunset = (pd.to_datetime(daily.Variables(3).ValuesInt64AsNumpy(), unit="s", utc=True)
					.tz_convert(response.Timezone().decode("utf-8"))
					.strftime("%H:%M")
	)

	# create dict to store response data
	daily_data = {}

	# add response data to dict
	daily_data["Max Temp"] = daily_temperature_2m_max. astype(str) + " °F"
	daily_data["Min Temp"] = daily_temperature_2m_min.astype(str) + " °F"
	daily_data["UV Index"] = daily_uv_index_max
	daily_data["Sunset"] = daily_sunset

	# create pandas dataframe from dict; convert to html
	daily_dataframe = pd.DataFrame(data = daily_data).to_html(
		index=False,
		border=1,
		classes="dataframe"
	)

	# return html as string
	return daily_dataframe