from secrets import *
import requests
import requests_cache
import json


################
##set up cache##
################

requests_cache.install_cache('cachefile')

##################
##set up classes##
##################

class Restaurant():
    def __init__(self, name, address):
        self.name=name
        self.address=address

    def __str__(self):
        return "{}: {}".format(self.name, self.address)

class MenuItem():
    def __init__(self, title, photourl=None):
        self.title=title
        self.photourl=photourl

    def __str__(self):
        return "{}".format(self.title)


####################
##set up functions##
####################

def getCoordinates(zip):
    #Calls Google Place location search API for lat/lon coordinates
    paramsdict = {}
    paramsdict['key'] = google_places_key
    paramsdict['input'] = '{}'.format(zip)
    paramsdict['inputtype'] = 'textquery'
    paramsdict['fields'] = 'geometry'
    site_base = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    coordinate_response = requests.get(site_base, paramsdict)
    findcoords = json.loads(coordinate_response.text)
    latitude = 0
    longitude = 0
    for place in findcoords['candidates']:
            try:
                latitude = place['geometry']['location']['lat']
                longitude = place['geometry']['location']['lng']
                return latitude, longitude
            except:
                return latitude, longitude


def getChains(zip):
    #Calls Google Place nearby search to get fast food chains near specified coordinates
    coords=getCoordinates(zip)
    latlon = str(coords[0])+','+str(coords[1])
    chainsDict = {}
    chainsDict['location'] = latlon
    chainsDict['key'] = google_places_key
    chainsDict['type'] = "restaurant"
    chainsDict['keyword'] = "fast food restaurant"
    chainsDict['rankby'] = "distance"
    chains_base = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    chainsresponse = requests.get(chains_base, chainsDict)
    print(chainsresponse.from_cache)
    chainsjson = json.loads(chainsresponse.text)
    nearby_chains_list = []
    for loc in chainsjson['results']:
        name = loc['name']
        address = loc['vicinity']
        nearby_chains_list.append(Restaurant(name, address))
    return nearby_chains_list

def getMenuItems(restaurant):
    #Calls Spoonacular to get menu items at 1 restaurant 
    menu_list=[]
    menu_base = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/search'
    menu_paramsdict={}
    menu_paramsdict['offset'] = '0'
    menu_paramsdict['number'] = '10'
    menu_paramsdict['maxCalories'] = '800'
    menu_paramsdict['maxProtein'] = '100'
    menu_paramsdict['maxFat'] = '100'
    menu_paramsdict['maxCarbs'] = '100'
    menu_paramsdict['query'] = restaurant.name
    headers={}
    headers['X-RapidAPI-Key'] = spoonacular_key
    menu_response = requests.get(menu_base, menu_paramsdict, headers=headers)
    obj=json.loads(menu_response.text)
    for food_item in obj['menuItems']:
        title=food_item['title']
        pic_url=food_item['image']
        item=MenuItem(title, pic_url)
        menu_list.append(item)
    return menu_list
