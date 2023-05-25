# Import the dependencies.
from flask import Flask, jsonify

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
# Create an app, being sure to pass __name__
app = Flask(__name__)




#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return "Hi"

if __name__ == "__main__":
    app.run(debug=True)
