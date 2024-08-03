import geopandas as gpd
import googlemaps
from shapely.geometry import Point
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


def is_eligible(point_coordinates):

    eligiblity_map = gpd.read_file("shapefile/SFH_MFH_Ineligible.shp")
    eligiblity_map = eligiblity_map.to_crs("EPSG:4326")
    coordinates = Point(point_coordinates)

    eligiblity_map.contains(coordinates)

    inside_polygon = eligiblity_map.geometry.apply(lambda polygon: polygon.contains(coordinates)).any()

    return inside_polygon


def address_to_coordinates(address):
    gmaps = googlemaps.Client(key=os.getenv("API_KEY"))
    geocode = gmaps.geocode(address)[0]
    return geocode



if __name__ == '__main__':
    configure()
    geocode = address_to_coordinates(input("Enter address:  "))
    coordinates = geocode['geometry']['location']['lng'], geocode['geometry']['location']['lat']

    print(f'{coordinates} is {is_eligible(coordinates)}')
