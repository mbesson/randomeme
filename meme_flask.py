#!/bin/python3

from flask import Flask, render_template
import requests
import json
import urllib.request

app = Flask(__name__)

def get_conf():
    return {"host": urllib.request.urlopen('https://v4.ident.me').read().decode('utf8'), "port": 80, "route": "api"}
    
def give_me_the_refresh():
    return "http://{host}:{port}/{route}".format(host=get_conf()["host"], port=get_conf()["port"], route=get_conf()["route"])

def get_meme():
    #Uncomment these two lines and comment out the other url line if you want to use a specific meme subreddt
    # sr = "/wholesomememes"
    # url = "<https://meme-api.herokuapp.com/gimme>" + sr
    url = "https://meme-api.herokuapp.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/api", methods=['GET'])
def index():
    meme_pic,subreddit = get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit, refresh_url=give_me_the_refresh())

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host=get_conf()["host"], port=get_conf()["port"])
