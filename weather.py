import datetime as dt
import requests
from tkinter import*
root =Tk()
e=Entry(root)
e.pack()
CITY="New Delhi"
BASE_URL ="http://api.openweathermap.org/data/2.5/weather?"
API_KEY ="4972da2187435137f20e0ec39c2fe24c"

# CITY=e.get()

url = BASE_URL +"appid="+API_KEY+"&q="+ CITY

response =requests.get(url).json()

def kel_to_cel(kelvin):
  celsius =kelvin-273.15
  return(celsius)

temp_k= response['main']['temp']
feels_like= response['main']['feels_like']
humidity =response['main']['humidity']
temp_cel=round(kel_to_cel(temp_k),2)
feels_cel=round(kel_to_cel(feels_like),2)

l1=Label(root,text=f"Temprature Today ==>  {temp_cel}",padx=40,pady=20)
l2=Label(root,text=f"Temprature feels like Today ==>  {feels_like}",padx=40,pady=20)
l3=Label(root,text=f"Humidity Today ==>  {humidity}",padx=40,pady=20)
def print_w():
  l1.pack()
  l2.pack()
  l3.pack()
  return
  

b1=Button(root,text="get temprature",padx=40,pady=20,command=print_w)
b1.pack()

root.mainloop()