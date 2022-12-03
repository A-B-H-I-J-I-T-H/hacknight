import tkinter as tk
import requests
import json

#Root
root=tk.Tk()
root.title("weather app") 
root.geometry("900x500+200+300")

#API
def getweather():
    api_key="6c52648bb9da951cab617126f0065892"

    city=textfield.get()
    
    print(city)
   


    base_url="https://api.openweathermap.org/data/2.5/weather?q="

    complete_url=base_url+city+"&appid="+api_key


    response=requests.get(complete_url)

    x=response.json()
    
    dis=x["weather"][0]["main"]
    Temperature=round(x["main"]["temp"]-273.15)
    pre=x["main"]["pressure"]/1000
    hum=x["main"]["humidity"]

    t.config(text=(Temperature,"°C"))
    d.config(text=dis)
    p.config(text=(pre,"bar"))
    h.config(text=(hum,"%"))

    
   
   
    
#Images box.png,search_icon.png,box.png,logo.png,search.png
#Should be in the same folder as this file.


#Searching
search_image=tk.PhotoImage(file=r"search.png")
myimage=tk.Label(image=search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon=tk.PhotoImage(file="search_icon.png")
myimage_icon=tk.Button(image=search_icon,borderwidth=0,bg="#404040",cursor="hand2",command=getweather)
myimage_icon.place(x=400,y=34)

#Logo
logo_image=tk.PhotoImage(file="logo.png")
logo=tk.Label(root,image=logo_image)
logo.place(x=150,y=150)

#Bottom Box
frame_image=tk.PhotoImage(file="box.png")
framemyimage=tk.Label(image=frame_image)
framemyimage.pack(padx=5,pady=5,side="bottom")


#Climate Characteristics Labels
label2=tk.Label(root,text="Description",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=220,y=400)

label3=tk.Label(root,text="Pressure",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=425,y=400)

label4=tk.Label(root,text="Humidity",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=635,y=400)

t=tk.Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

d=tk.Label(font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=225,y=430)

p=tk.Label(font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=418,y=430)


h=tk.Label(font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=640,y=430)


root.mainloop()
