#!/bin/python3

from flask import Flask, render_template
import requests
import json
import urllib.request

app = Flask(__name__)

class FlaskApp:
  def __init__(self, port, api):
    self.host = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
    self.port = port
    self.refresh = "http://{host}:{port}/{route}".format(host=self.host, port=self.port, route=api)

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

    myApp=FlaskApp(80, "api")
 
    # run() method of Flask class runs the application
    # on the local development server.
    myApp.app.run(host=myApp.host, port=myApp.port)
