import json
file= open("data.json","w")
# data=json.load(file)
# print(data)
data={
    "name":"Bhargavi",
    "Intitute": "Iare"
}
json.dump(data,file)