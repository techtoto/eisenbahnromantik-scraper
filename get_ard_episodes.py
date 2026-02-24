#!/usr/bin/env python3

import requests, json, time

PAGE_SIZE = 200
ASSET_ID = "Y3JpZDovL3N3ci5kZS8yMjUwOTg2"

episodes = []
new_episode_list = []

def append_episodes(episode_list):
    [episodes.append(episode) for episode in episode_list]

def get_episode_list():
    r = requests.get(f"https://api.ardmediathek.de/page-gateway/widgets/ard/asset/{ASSET_ID}?pageNumber=0&pageSize={PAGE_SIZE}")
    r_json = r.json()
    total_elements = r_json["pagination"]["totalElements"]

    append_episodes(r_json["teasers"])

    for page_number in range(1, total_elements // PAGE_SIZE + 1):
        r = requests.get(f"https://api.ardmediathek.de/page-gateway/widgets/ard/asset/{ASSET_ID}?pageNumber={page_number}&pageSize={PAGE_SIZE}")
        append_episodes(r.json()["teasers"])

    with open("./json/ard_episodes_original.json", "w") as f:
        json.dump(episodes, f)

def get_episode_details():
    for episode in episodes:
        r = requests.get(f"https://api.ardmediathek.de/page-gateway/pages/ard/item/{episode["id"]}?embedded=false&mcV6=true")
        new_episode_list.append({
            "id": episode["id"],
            "longTitle": episode["longTitle"],
            "duration": episode["duration"],
            "broadcastedOn": episode["broadcastedOn"],
            "coreAssetType": episode["coreAssetType"],
            "synopsis": r.json()["widgets"][0]["synopsis"],
        })
        print(r.json()["widgets"][0]["synopsis"])
        print()

    with open("./json/ard_episode_list.json", "w") as f:
        json.dump(new_episode_list, f)

get_episode_list()
get_episode_details()
