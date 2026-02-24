#!/usr/bin/env python3

from dotenv import load_dotenv
import os, requests, json

load_dotenv()

TVDB_URL = "https://api4.thetvdb.com/v4/series/188331/episodes/default" # 188331 = Eisenbahn-Romantik

thetvdb_episodes = {}
headers = {
    "Authorization": "Bearer " + os.getenv("THETVDB_BEARER"), # Bearer Token must be obtained once a month via the api key (see https://thetvdb.github.io/v4-api/#/Login/post_login)
    "Accept": "application/json"
}

r = requests.get(TVDB_URL, headers=headers)
thetvdb_episodes = r.json()

while thetvdb_episodes["links"]["next"] != None:
    print(thetvdb_episodes["links"]["next"])
    r = requests.get(thetvdb_episodes["links"]["next"], headers=headers)
    new_episodes = r.json()
    thetvdb_episodes["links"] = new_episodes["links"] # pagination
    for episode in new_episodes["data"]["episodes"]:
        thetvdb_episodes["data"]["episodes"].append(episode)

with open("./json/thetvdb_episode_list.json", "w") as f:
    json.dump(thetvdb_episodes, f)
