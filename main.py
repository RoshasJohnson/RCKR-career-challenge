import requests
from math import radians, cos, sin, asin, sqrt
data_set = requests.get(
    'https://cdn.jsdelivr.net/gh/apilayer/restcountries@3dc0fb110cd97bce9ddf27b3e8e1f7fbe115dc3c/src/main/resources/countriesV2.json')

data_set = data_set.json()

curr_using = {}  # get countries currencies
for i in data_set:
    for j in i["currencies"]:
        if j['code'] in curr_using.keys():
            curr_using[j['code']] += 1
        else:
            curr_using[j['code']] = 1
top_20 = []  # getting countries those have unique currencies

population_limit  =510713

print(curr_using)
for i in data_set:
    flag = 0  # For avoiding repetitions

    for j in i["currencies"]:
        if curr_using[j["code"]] == 1:
            flag = 1
            break
    if flag == 1 and i["population"] >= population_limit :
        top_20.append(i)


print(len(top_20))

# Geting top 20 countries ordered by  populations
top_20 = sorted(top_20, key=lambda x: x['population'], reverse=True)
top_20 =top_20[0:20]

# using Haversine formula for get distance between to places
def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)


    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return(c * r)


distance_sum = 0
while top_20:
    country = top_20.pop(0)
    for i in top_20:

        distance_sum = round(distance_sum + distance(
            country['latlng'][0], (i['latlng'][0]), country['latlng'][1], i['latlng'][1]), 3)


print(distance_sum)
