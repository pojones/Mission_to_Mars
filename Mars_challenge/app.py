

from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
# use flask to render a template, redirect to another url, and creating a url
# use pymongo to interact with our database
# to use scraping code, we will convert from jupyter notebook to python

app = Flask(__name__)

#* Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# our app will connect to mongo using a URI, a uniform resource identifier, similar to a URL
mongo = PyMongo(app)

@app.route("/")
# the route tells Flask what to display when we're looking at the homepage, index.html. This
# means that when we visit our web app's html page, we will see the home page
def index():
   mars = mongo.db.mars.find_one()
   # uses pymongo to find the "Mars" collection in our database, which we will create when we
   # convert our Jupyter scraping code to Python Script. We also assign that path to the 
   # 'mars' variable for use later
   return render_template("index.html", mars=mars)
   # tells Flask to return an HTML template using an index.html file. We'll create this file
   # after we build the flask routes. 'mars=mars' tells flask to use the 'mars' collection 
   # in MongoDB

@app.route("/scrape")
# defines the route that Flask will be using. This route, "/scrape" will run the function 
# that we create just beneath it
def scrape():
   mars = mongo.db.mars
   # assign a new variable that points to our Mongo database
   mars_data = scraping.scrape_all()
   # next, we create a new variable to hold the newly scraped data. Here, we're referencing
   # the 'scrape_all()' function in the scraping .py file exported from jupyter notebook
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   # here, we're inserting data, but not if an identical one exists. In the query_parameter,
   # we can specify a field, in which case MongoDB will update a document with a match. Or
   # it can be left empty '{}' to update the first matching document in the collection. Next,
   # we use the data we have stored in 'mars_data'. The syntax used here is '{$set:data}'.
   # This means the document will be modified with the data in question. Finally, the option
   # we include is 'upset=True'. This indicates to Mongo to create a new document if one 
   # doesn't already exist, and new data will always be saved
   return redirect('/', code=302)
   # finally, we will add a redirect after successfully scraping the data. This will 
   # navigate our page back to '/' where we can see the updated content

## final bit of code we need is to tell Flask to run
if __name__ == "__main__":
   app.run(debug=True)


