#importing the needed dependencies
from flask import Flask, jsonify
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#setting up the database connection
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflecting an existing database into a new model
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

#saving  table references
Measurement = Base.classes.measurement
Station = Base.classes.station

#Createting the session (link) from python to the DB
session = Session(engine)

#configuring Flask
app = Flask(__name__)

#setting up routes
@app.route("/")
def home():
    return (
        f"<center><h1>Climate Data Analysis API<h1><center>"
        f"<img src='http://slideplayer.com/slide/2332097/8/images/1/Weather+%26+Climate.jpg' width=700, height=200/>"
        f"<hr>"
        f"<h5>List of Available Routes<h5>"
        f"<h6>Precipitation: /api/v1.0/precipitation<h6>"
        f"<h6>Stations: /api/v1.0/stations<h6>"
        f"Temp Observations: /api/v1.0/tobs<br>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
     prcp_date_resu = session.query(Measurement.date, Measurement.prcp).all()
     precip = list(np.ravel(prcp_date_resu))
     return jsonify(precip)
     

@app.route("/api/v1.0/stations")
def stations():
     all_stations = session.query(Measurement.station).all()
     all_output = list(np.ravel(all_stations))

     
     return jsonify(all_output)


@app.route("/api/v1.0/tobs")
def tobs():
     tobs = session.query(Measurement.date, Measurement.tobs).\
     filter(Measurement.date >= dt.date(2016, 8, 23)).all()
     all_temp = list(np.ravel(tobs))

     return jsonify(all_temp)


if __name__ == "__main__":
    app.run(debug=True)
