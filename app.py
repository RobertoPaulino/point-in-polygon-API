import geopandas as gpd
import googlemaps
import os

from shapely.geometry import Point
from dotenv import load_dotenv
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/get-eligibility/<address>")
def get_eligibility(address):
    """
    get_eligibility is a GET method that takes an address as a parameter and converts it to coordinates and find out if
    it is inside any of the polygons in the shape file

    :param address: receives a full address as a string
    :return: JSON object with the address, the coordinates, and its eligibility based on the shapefile
    """
    geocode = address_to_coordinates(address)
    coordinates = geocode['geometry']['location']['lng'], geocode['geometry']['location']['lat']
    eligibility = "eligible" if is_eligible(coordinates) else "not eligible"

    address_data = {
        "address": address,
        "coordinates": coordinates,
        "is_eligible": eligibility
    }

    return jsonify(address_data), 200


def configure():
    """
    loads the .env file containing the API key
    """
    load_dotenv()


def is_eligible(point_coordinates):
    """
    is_eligible returns true if the given coordinates are inside the polygon

    :param point_coordinates: is a longitude and latitude tuple
    :return: boolean indicating if the given coordinates are inside the polygon
    """

    # reads the file for eligibility, currently using the information for the USDA loan eligibility that can be found
    # in the following website: https://catalog.data.gov/dataset/usda-rural-development-property-eligibility-sfh-mfh
    # this data is set in the .gitignore if you want to make a folder called shapefile with the files and edit the path
    eligibility_map = gpd.read_file("shapefile/SFH_MFH_Ineligible.shp")
    eligibility_map = eligibility_map.to_crs("EPSG:4326")
    coordinates = Point(point_coordinates)

    eligibility_map.contains(coordinates)

    inside_polygon = eligibility_map.geometry.apply(lambda polygon: polygon.contains(coordinates)).any()

    return ~inside_polygon


def address_to_coordinates(address):
    """
    address_to_coordinates takes a full address as a parameter and converts it to coordinates using the googlemaps API

    :param address: full address as a string
    :return: coordinates as a tuple
    """
    gmaps = googlemaps.Client(key=os.getenv("API_KEY"))
    geocode = gmaps.geocode(address)[0]
    return geocode


if __name__ == '__main__':
    # configures dotenv file
    configure()

    # runs application
    app.run(debug=True)
