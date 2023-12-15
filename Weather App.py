import tkinter as tk 
from tkinter import messagebox
from geopy.geocoders import Nominatim
from datetime import datetime 
import pytz 
import requests
from timezonefinder import TimezoneFinder

def get_weather ():
    try:
    #Location
     city=textfield.get()
     geolocator = Nominatim(user_agent="geopiExercises")
     location=geolocator.geocode(city)
     lat=location.latitude
     lng=location.longitude 
     obj=TimezoneFinder()
     result=obj.timezone_at(lng=lng, lat=lat)
     city_label.config(text=result.split("/")[1])
     print(result)
    
    #Time
     home = pytz.timezone(result)
     local_time=datetime.now(home)
     current_time=local_time.strftime("%I:%M %p")
     clock.config(text="local_time")
     time_label.config(text=current_time)
     
    #Weather and API1
     apikey="974326ea0dbe12bd923fc15598bfb098"
     api=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={apikey}"
     json_data=requests.get(api).json()
     condition=json_data["weather"][0]["main"]
     description=json_data["weather"][0]["description"]
     temp=int(json_data["main"]["temp"]-273.15) 
     pressure=json_data["main"]["pressure"]
     humidity=json_data["main"]["humidity"]
     wind=json_data["wind"]["speed"]


     temp_label.config(text=f"{temp} °")
     condition_label.config(text=f"{condition}|FEELS LIKE {temp} °")
     condition_label.place(x=550,y=300)
     wind_label.config(text=wind)   
     humidity_label.config(text=humidity)
     description_label.config(text=description)
     pressure_label.config(text=pressure)

    except Exception as error:
        print(error)
        messagebox.showerror("Weather App","invalid Entry")


root=tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200") #setting the size of App 
root.resizable(False,False)
root.iconbitmap("E:\My python projects\Weather App\Weather.ico")
#Search Bar  

search_image=tk.PhotoImage(file='search.png')
search_image_label=tk.Label(root, image=search_image)
search_image_label.pack(pady=20, side=tk.TOP) #set the height of search  bar

textfield=tk.Entry(root, justify='center',width=17, font=("arial",25,"bold"), bg="#404040", fg="white" , border=0) #make a textfield  , #fg=text_color 
#Boarder=0:Remove The egds of search bar
textfield.place(x=250, y=35)

search_icon=tk.PhotoImage(file="search_icon.png")
search_icon_Button=tk.Button(root,image=search_icon , border=0,cursor="hand2",bg="#404040", command=get_weather)
#cursor=hand2: setting the type of mouse pointer
search_icon_Button.place(x=250, y=35)

#Logo
logo_image=tk.PhotoImage(file="logo.png")
logo_label=tk.Label(root, image=logo_image)
logo_label.pack(side=tk.TOP)

#Frame
Frame_image=tk.PhotoImage(file="box.png")
Frame_label=tk.Label(root, image=Frame_image)
Frame_label.pack(pady=10, side=tk.BOTTOM)

#City Name
city_label=tk.Label(root, font=("arial",40,"bold"), fg="#e355cd")
city_label.place(x=61, y=100)

#Time
time_label=tk.Label(root, font=("arial", 20, "bold"), fg="#4b4bcc")
time_label.place(x=100, y=180)

#clock
clock=tk.Label(root,font=("Hevetica",20),fg="#4b4bcc")

#Labels
LABEL1=tk.Label(root,text="WIND",font=("Helvetica",15,"bold"), fg="white", bg="#1ab5ef")
LABEL1.place(x=120 , y=400)

LABEL2=tk.Label(root,text="HUMIDITY",font=("Hevetica",15,"bold"),fg="white",bg="#1ab5ef")
LABEL2.place(x=280 , y=400)

LABEL3=tk.Label(root,text="DESCRIPTION",font=("Hevetica",15,"bold"),fg="white",bg="#1ab5ef")
LABEL3.place(x=450,y=400)

LABEL4=tk.Label(root,text="PRESSURE",font=("Hevetica",15,"bold"),fg="white",bg="#1ab5ef")
LABEL4.place(x=670 , y=400)

temp_label=tk.Label(root,font=("arial",70,"bold"), fg="#4b4bcc")
temp_label.place(x=590, y=170)

condition_label=tk.Label(root,font=("arial",15,"bold"), fg="#4b4bcc")
condition_label.place(x=590, y=270)

wind_label=tk.Label(root,text="..." , font=("arial",20,"bold" ),bg="#1ab5ef", fg="#404040")
wind_label.place(x=120, y=430)

humidity_label=tk.Label(root,text="..." , font=("arial",20,"bold" ),bg="#1ab5ef", fg="#404040")
humidity_label.place(x=280, y=430)

description_label=tk.Label(root,text="..." , font=("arial",20,"bold" ),bg="#1ab5ef", fg="#404040")
description_label.place(x=450, y=430)

pressure_label=tk.Label(root,text="..." , font=("arial",20,"bold" ),bg="#1ab5ef", fg="#404040")
pressure_label.place(x=670, y=430)

root.mainloop()

