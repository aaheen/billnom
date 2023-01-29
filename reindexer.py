import json
import os
mydir = os.path.dirname(__file__) or "."

with open(os.path.join(mydir,"BillData.json"), "r") as read_content:
    data = json.load(read_content)
reDict = {}

for item in data:
    reDict.update({data[item]["BILL_URL"] : item})


with open(os.path.join(mydir,"UrlIndex.json"), "w") as outfile:
    json.dump(reDict, outfile, indent=4)
