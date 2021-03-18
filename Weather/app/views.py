from django.shortcuts import render,HttpResponse
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

def final(request):
    city=request.POST.get('city')
    x=requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city +"&units=metric&appid=816c3b6e6c7dd36a977639784c3c7309").json()
    # print(x['coord'])


    if(x['cod']==200):
        context={
            'description':x['weather'][0]['description'],
            'temp':x['main']['temp_max'],
            'wind_speed':x['wind']['speed'],
            'city_name':x['name'],
            'icon':x['weather'][0]['icon'],
            'Humidity':x['main']['humidity']
            }
        return render(request,'final.html',context)
    else:
        return render(request,'error.html')
    