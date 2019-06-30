from flask import Flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Below are the available routes<br>"
        f"Precipitation: /api/v1.0/precipitation<br>"
        f"Stations: /api/v1.0/stations<br>"
        f"Stations: /api/v1.0/tobs<br>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
     return"precip"

@app.route("/api/v1.0/stations")
def stations():
     return"station"


@app.route("/api/v1.0/tobs")
def tobs():
     return"tobs"







if __name__ == "__main__":
    app.run(debug=True)
