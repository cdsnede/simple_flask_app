## Project Description
"Eat Healthy" is a simple Flask web app for busy people who have no time and need to eat a fast food meal, but still want to eat something healthy. With this program users can:
1. Input their zipcode.
2. Get a list of nearby fast food restaurant chains.
3. Choose one restaurant from the list.
4. See up to 10 menu items at that restaurant that are all under 800 calories and less than 100 carbs.

I made this for a class project.

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

## Sources used
  - https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms/Form_validation
  - https://www.w3schools.com/html/html_css.asp
  - Calorie limit info: https://www.livestrong.com/article/440135-recommended-calorie-intake-for-one-meal/
  - Carbohydrate limit info: https://www.livestrong.com/article/427735-number-of-carbohydrates-needed-per-meal/
