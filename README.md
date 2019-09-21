## Project Description
"Eat Healthy" is a simple Flask web app for busy people who have no time and need to eat a fast food meal, but still want to eat something healthy. With this program users can:
1. Input their zipcode.
2. Get a list of nearby fast food restaurant chains.
3. Choose one restaurant from the list.
4. See up to 10 menu items at that restaurant that are all under 800 calories and less than 100 carbs.

## Sample Output
Example output of restaurant choices for "48313":

![alt text](https://github.com/cdsnede/SI508-FinalProject/blob/master/Example_Restaurant_List_48313.png "Example Restaurant List for 48313")

Example output when choosing "2" (McDonald's), from the above list, as your restaurant:

![alt text](https://github.com/cdsnede/SI508-FinalProject/blob/master/mcdonalds_sample_output.png "Example McDonald's Output")

## Dependencies
This is a python program (works with Python3). The following need to be pip installed:
  - Flask, flask_script [Installation instructions](http://flask.pocoo.org/docs/1.0/installation/)
  - requests [Installation instructions](http://docs.python-requests.org/en/master/user/install/)
  - requests_cache [Installation instructions](https://requests-cache.readthedocs.io/en/latest/user_guide.html#installation)

It also uses:
  - json
  - unittest

## API Keys needed
Save both keys in the `secrets.py` file.
  - GooglePlaces API (2 endpoints will be called during one run of this program. [Get a key.](https://developers.google.com/places/web-service/get-api-key)
  - Spoonacular API (Menu Items endpoint). [Get a key.](https://rapidapi.com/spoonacular/api/recipe-food-nutrition) Note this API limits free accounts to 50 calls/day.

## Running the Program
Once you've downloaded this repository and put your API keys in the `secrets.py` file:
  - Run this command in Terminal
```python
python3 eat_healthy.py runserver
```
  - The program then runs on your localhost: http://127.0.0.1:5000/

Other files:
  - The functions used in the Flask app are in the `functions.py` file.
  - HTML templates are all in the templates folder.  
  - The program will set up `cachefile.sqlite` once run.
  - The .png files in the repository are examples of output.


## Test Suite
Run this command for the test suite
```python
python3 tests.py
```

## Final Project Requirements Fulfilled
The following is the list of requirements from our instructions document that my program fulfilled:

  - Your project must rely on Python programming/program(s).
  - Two data sources used in total: I used 2 APIs (Google Places and Spoonacular), based on user input.
  - Caching must be implemented: All API calls are cached.
  - Process data from each source: All json data from the APIs is parsed so that it can be turned into class instances.
  - Import and use functionality from at least one Python module that is not json, random, or requests: I used requests_cache and unittest
  - A test suite file containing at least 2 unittest.TestSuite subclasses and at least 10 test methods: My test file is tests.py and has 4 subclasses and 13 test methods.
  - Running the project should produce a product that is the result of processing data: It produces html pages with Flask.
  - Define at least 2 classes and create and use instance(s) of each of them: I made a Restaurant class and MenuItem class, which are used in other functions. The attributes of these instances are also used on the HTML pages to show names, addresses and images.
  - Include in your repository an example of your output: See above. Or the .png files in this repository.
  - Errors must be handled gracefully IF there is user input: I made html error pages if the user types in bad input or if there are no results. Also I made the input boxes check for non-numbers before the user hits the submit button.
  - Using a library in Python that we did not study in SI 508 or use in any assignment: requests_cache
  - Accessing a REST API that we have not included in any meeting or assignment: Spoonacular (which gets the menu items)
  - A clear visualization of data: HTML pages served in a Flask application
  - An interactive project: The results are all user-driven, like in Project 2


## Sources used
  - https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation
  - https://www.w3schools.com/html/html_css.asp
  - Calorie limit info: https://www.livestrong.com/article/440135-recommended-calorie-intake-for-one-meal/
  - Carbohydrate limit info: https://www.livestrong.com/article/427735-number-of-carbohydrates-needed-per-meal/
