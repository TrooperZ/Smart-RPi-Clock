#-*- coding:utf-8-*-
import forecastio

#If data not avalible, comment it for now. That data may not be avalible
#on the database

api_key = "Your API Key"
lat = Your latitude
lng = Your longitude
forecast = forecastio.load_forecast(api_key, lat, lng)
cur = forecast.currently()
print cur.summary
print cur.icon
print cur.temperature
#print cur.temperatureMax
#print cur.temperatureMin
#print cur.temperatureMinTime
#print cur.temperatureMaxTime
#print cur.apparentTemperatureMin
#print cur.apparentTemperatureMinTime
#print cur.apparentTemperatureMax
#print cur.apparentTemperatureMaxTime
print cur.nearestStormDistance
print cur.precipIntensity
#print cur.precipIntensityMax
#print cur.precipIntensityError
print cur.precipProbability
#print cur.precipType
#print cur.precipAccumulation
print cur.apparentTemperature
print cur.dewPoint
print cur.humidity
print cur.pressure
print cur.windSpeed
print cur.windGust
print cur.windBearing
print cur.cloudCover
print cur.uvIndex
print cur.visibility
print cur.ozone
