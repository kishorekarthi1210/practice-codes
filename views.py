from django.shortcuts import render
import json
class userprofile:
    json_obj=open('C:/Users/Admin/Desktop/django/genomics/static/Userdata.json')
    data=json.load(json_obj)
    profile=data["profile"]
    for i in range(len(profile)): 
        userid=profile[i]["user"]["userid"]
        username=profile[i]["user"]["name"]["first"]

def index(request):
    data=userprofile()
        
    
    return render(request,"index.html",{"userid":id})
