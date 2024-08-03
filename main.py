import geopandas as gpd
import googlemaps
from shapely.geometry import Point
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


def is_eligible(coordinates):
    eligiblity_map = gpd.read_file("shapefile/SFH_MFH_Ineligible.shp")
    eligiblity_map = eligiblity_map.to_crs("EPSG:4326")
    coordinates_point = Point(coordinates)

    eligiblity_map.contains(coordinates_point)

    inside_polygon = eligiblity_map.geometry.apply(lambda polygon: polygon.contains(coordinates)).any()

    return inside_polygon


def address_to_coordinates(address):
    configure()
    return 0



if __name__ == '__main__':
    print(address_to_coordinates(input("Enter address:  ")))
