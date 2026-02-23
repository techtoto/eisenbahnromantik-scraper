#!/usr/bin/env python3

import tabulate, json, datetime

with open("episodes_original.json") as f:
    episodes = json.load(f)

episode_table = []
for episode in episodes:
    if episode["coreAssetType"] == "EPISODE":
        episode_table.append({
            "id": episode["id"],
            "longTitle": episode["longTitle"],
            "duration": str(datetime.timedelta(seconds=episode["duration"])),
            "broadcastedOn": episode["broadcastedOn"]
        })

print(tabulate.tabulate(episode_table, headers="keys"))
print(len(episode_table))
