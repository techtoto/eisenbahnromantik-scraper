#!/usr/bin/env python3

import requests, json

PAGE_SIZE = 200
ASSET_ID = "Y3JpZDovL3N3ci5kZS8yMjUwOTg2"

episodes = []

def append_episodes(episode_list):
    [episodes.append(episode) for episode in episode_list]

r = requests.get(f"https://api.ardmediathek.de/page-gateway/widgets/ard/asset/{ASSET_ID}?pageNumber=0&pageSize={PAGE_SIZE}")
r_json = r.json()
total_elements = r_json["pagination"]["totalElements"]

append_episodes(r_json["teasers"])

for page_number in range(1, total_elements // PAGE_SIZE + 1):
    r = requests.get(f"https://api.ardmediathek.de/page-gateway/widgets/ard/asset/{ASSET_ID}?pageNumber={page_number}&pageSize={PAGE_SIZE}")
    append_episodes(r.json()["teasers"])

with open("episodes.json", "w") as f:
    json.dump(episodes, f)
