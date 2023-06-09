# Import the dependencies.
from flask import Flask, jsonify



#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


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
