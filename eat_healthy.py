import requests
import requests_cache
import json
from flask import Flask, render_template, request
from flask_script import Manager
from functions import *
from secrets import *


app = Flask(__name__)
manager = Manager(app)

placelist=[]

@app.route('/',methods=['GET'])
def get_zip_code():
	s = """<h1>Enter a valid US zip code:</h1>
<form action="http://localhost:5000/chainresults" method="GET">
  <input type="number" name="zip">
  <input type="submit" value="Submit">
</form>"""
	return s


@app.route('/chainresults', methods=['GET'])
def show_chains():
    if request.method == "GET":
        result = request.args
        zipcode = result.get('zip')
        global placelist
        try:
        	placelist = getChains(zipcode)
        	return render_template('restaurants.html', chains_list=placelist, loc=zipcode)
        except:
            return render_template('ziperror.html')


@app.route('/menuitems', methods=['GET'])
def show_menuitems():
    if request.method == "GET":
        result = request.args
        num = result.get('num')
        try:
            num = int(num)
            index = num-1
            restaurant=placelist[index]
            menu=getMenuItems(restaurant)
            if len(menu) == 0:
                return render_template('noresults.html', no_place=restaurant.name)
            else:
                return render_template('food.html', place=restaurant.name, menu_items_list=menu)
        except:
            return render_template('menuerror.html')


if __name__ == '__main__':
    manager.run()
