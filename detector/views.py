from django.http import HttpResponse
from django.shortcuts import render
import json#To parse data in json format (weather information)
import urllib.request # 

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST.get('city')
        res = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=270f3faf9b167ad932411682756acd35").read()
        json_data = json.loads(res)

        #For more weather option visit here: https://openweathermap.org

        #json_data is a dictionary (json format) where get access to all weather attribute (because of a API call.)
        # a = {"A": [1, 2, 30]} => print(a["A"][2]) => Result: 30
        data = {
            "country": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "wind": str(json_data['wind']['speed']),
        }

    else:
        data = {}   
    return render(request, "index.html", {
        'aa': city,
        'data': data
    })