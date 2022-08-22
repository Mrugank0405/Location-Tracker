
from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz
from playsound import playsound

playsound("C:\\Users\\mruga\\Downloads\\1_notification ringtone.mp3")  # copy path or relative path of '1_notification ringtone.mp3'. Use '\\' instead of '\'

root=Tk()
root.title("Phone Number Tracker")
root.geometry("364x584")
# root.resizable(False,False)

root.iconbitmap('"C:\\Users\\mruga\\Downloads\\2_icon.ico"') # copy path or relative path of '2_logo image.png'.

def track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)
    #country
    locate=geocoder.description_for_number(number,'en')
    country.config(text=locate)
    
    #operator like idea, airtel, jio and many other
    operator=carrier.name_for_number(number,"en")
    sim.config(text=operator)

    #phone timezone
    time=timezone.time_zones_for_number(number)
    zone.config(text=time)

    #longitude and latitude
    geolocator=Nominatim(user_agent="geopiExercises")
    location=geolocator.geocode(locate)

    lng=location.longitude
    lat=location.latitude
    long.config(text=lng)
    latit.config(text=lat)

    #time showing in phone
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    locate_time=datetime.now(home)
    current_time=locate_time.strftime("%I:%M:%p")
    clock.config(text=current_time)

# logo
logo= PhotoImage(file="C:\\Users\\mruga\\Downloads\\3_logo image.png") # copy path or relative path of '3_logo image.png'. 
Label(root,image=logo).place(x=240,y=70)

Heading=Label(root,text="NUMBER TRACKER",font=("arial",15,"bold"))
Heading.place(x=90,y=110)

# entry
Entry_back=PhotoImage(file="C:\\Users\\mruga\\Downloads\\4_entry_area.png") # copy path or relative path of '4_entry_area.png'
Label(root,image=Entry_back).place(x=20,y=190)

entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,bd=0,font=('arial',20))
enter_number.place(x=50,y=220)

# button
Search_image=PhotoImage(file="C:\\Users\\mruga\\Downloads\\5_button.png") # copy path or relative path of '5_button.png'
search=Button(image=Search_image,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=track)
search.place(x=35,y=300)

# bottom box
Box=PhotoImage(file="C:\\Users\\mruga\\Downloads\\6_bottom.png") # copy path or relative path of '6_bottom.png'
Label(root,image=Box).place(x=-2,y=355)

country=Label(root,text="Country:",bg="#57adff",fg="black",font=("arial",10,"bold"))
country.place(x=50,y=400)

sim=Label(root,text="SIM",bg="#57adff",fg="black",font=("arial",10,"bold"))
sim.place(x=200,y=400)

zone=Label(root,text="TimeZone",bg="#57adff",fg="black",font=("arial",10,"bold"))
zone.place(x=50,y=450)

clock=Label(root,text="Country",bg="#57adff",fg="black",font=("arial",10,"bold"))
clock.place(x=200,y=450)

long=Label(root,text="Longitude",bg="#57adff",fg="black",font=("arial",10,"bold"))
long.place(x=50,y=500)

latit=Label(root,text="Latitude",bg="#57adff",fg="black",font=("arial",10,"bold"))
latit.place(x=200,y=500)

root.mainloop()

