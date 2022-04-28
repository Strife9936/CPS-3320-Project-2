from tkinter import *
from PIL import ImageTk,Image
import requests
import json

#API KEY
#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07206&distance=5&API_KEY=2C545836-2481-4969-B829-283496B1A9B2

root = Tk()
root.title('Air Quality app')
root.geometry("400x40")



#requests for the api key in json format. Then translates info into python lists
#Variables such as date,city, etc are to parse through the api lists 
#And sets the variables as the specific list content such as AQI or StateCode
try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07206&distance=5&API_KEY=2C545836-2481-4969-B829-283496B1A9B2")
    api  = json.loads(api_request.content)
    date = api[1]['DateObserved']
    city = api[1]['ReportingArea']
    state = api[1]['StateCode']
    quality = api[1]['AQI']
    category = api[1]['Category']['Name']

#If/else statement to set the window background color depending on the category condition
    if category == "Good":
        color = "#0C0"
    elif category =="Moderate":
        color = "#FFFF00"
    elif category =="Unhealthy for Sensitive Groups":
        color = "#ff9900"
    elif category =="Unhealthy":
        color = "#FF0000"
    elif category =="Very Unhealthy":
        color = "#990066"
    elif category =="Hazardous":
        color = "#660000"

#Configures and packs the labels and background color to window
    root.configure(background = color)
    myLabel = Label(root, text=date + city +" " +  state + " " + "Air Quality: " + str(quality) + " "+ category, font =("Times New Roman", 15), background = color)
    myLabel.pack()
except Exception as e:
    api = "Error"   


root.mainloop()