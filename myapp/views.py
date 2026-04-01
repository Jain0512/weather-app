from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
from django.conf import settings
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city= request.POST['city']
    else:
        city='Delhi'
    
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6c6ad1796a542eb3b4504e7eef339134'
    PARAMS = {"units":'metric'}

    import requests

    PEXELS_API_KEY = settings.PEXELS_API_KEY

    query = city + " city"

    pexels_url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": 1
    }

    response = requests.get(pexels_url, headers=headers, params=params)
    pexels_data = response.json()

    if pexels_data.get("photos"):
        image_url = pexels_data["photos"][0]["src"]["landscape"]
    else:
        image_url = "https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg"
    try:
        data= requests.get(url,params=PARAMS).json()

        description = data["weather"][0]['description']
        icon = data["weather"][0]['icon']
        temp = data['main']['temp']
        day= datetime.date.today()

        return render(request,'myapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occured':False,'image_url':image_url})
    
    except :
        exception_occured=True
        messages.error(request,"Entered city is not available.")
        day= datetime.date.today()
        return render(request,'myapp/index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day,'city':'Delhi','exception_occured':exception_occured})
        