import json

with open("BIBI.json", "r") as file:
    a = json.load(file)

print(a["Учень1"]["имя"])
