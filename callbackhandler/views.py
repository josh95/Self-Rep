from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from github import Github
import os
# Create your views here.

clientID = "9f81a88b0163d675a0b0"
clientsecret = "41d213a9b76245f290c58eaf160fefc61a90a78b"

def index(request):
    print(os.getcwd())
    ##get access token from github api
    callbackCode = request.GET['code']
    r = requests.post("https://github.com/login/oauth/access_token", data={"client_id" : clientID,
                       "client_secret" : clientsecret,
                       "code" : callbackCode})
                      #accept="json")
    content = (r.content.decode("utf-8"))
    access_token = content.split("&")[0].replace("access_token=", "")

    ##create instance of github class and starting making requests
    g = Github(access_token)
    user = g.get_user()

    existingRepos = [x.name for x in user.get_repos()]
    
    if "Self-Rep" in existingRepos:
        print("Self Replicating repo already exists")
        #replicatedRepo = user.get_repo("Self-Rep")

    else: 
        """replicatedRepo = user.create_repo(name = "Self-Rep",
                                                  private = False,
                                                  description = "self replicating repo")"""

        myfork = user.create_fork(g.get_user("josh95").get_repo("Self-Rep"))
    
    """t1 = replicatedRepo.create_git_tree([InputGitTreeElement("test.txt","100644","blob",content="File created by PyGithub")])
    c1 = replicatedRepo.create_git_commit(tree=t1, message="first commit", parents=[])
    ref = replicatedRepo.create_git_ref(ref="refs/heads/feature", sha=c1.sha)"""
    #repoToClone = g.get_user("josh95").get_repo("swipr")
    #print(repo.name)
        
    context = {}
    return render(request, "index.html", context)
