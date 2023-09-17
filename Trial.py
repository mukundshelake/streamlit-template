import json

with open("rangeMaster.json", "r") as f:
    rangeMaster = json.load(f)
print(rangeMaster['LJ']['LJ_2X_vsBB']['QJo'])