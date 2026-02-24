#!/usr/bin/env python3

import tabulate, json, datetime

with open("./json/ard_episode_list.json") as f:
    episodes = json.load(f)

print(tabulate.tabulate(episodes, headers="keys", maxcolwidths=[None, None, None, None, None, 40]))
