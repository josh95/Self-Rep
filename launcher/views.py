from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from github import Github
# Create your views here.

clientID = "9f81a88b0163d675a0b0"
clientsecret = "41d213a9b76245f290c58eaf160fefc61a90a78b"

def callback(request):
    ##get access token from github api
    callbackCode = request.GET['code']
    r = requests.post("https://github.com/login/oauth/access_token", data={"client_id" : clientID,
                       "client_secret" : clientsecret,
                       "code" : callbackCode})
    content = (r.content.decode("utf-8"))
    access_token = content.split("&")[0].replace("access_token=", "")

    ##create instance of github class and starting making requests
    g = Github(access_token)
    user = g.get_user()

    try:
        existingRepos = [x.name for x in user.get_repos()]
    except:
        context = {"clientID" : clientID}
        return render(request, "index.html", context)
    
    if "Self-Rep" in existingRepos:
        print("Self Replicating repo already exists")
        return render(request, "errorpage.html")
    else: 
        myfork = user.create_fork(g.get_user("josh95").get_repo("Self-Rep"))
        return render(request, "callback.html")

def main(request):
    context = {"clientID" : clientID}
    return render(request, "index.html", context)


