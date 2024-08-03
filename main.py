import geopandas as gpd
from shapely.geometry import Point, Polygon


def is_eligible(point_coordinates):

    eligiblity_map = gpd.read_file("shapefile/SFH_MFH_Ineligible.shp")
    eligiblity_map = eligiblity_map.to_crs("EPSG:4326")
    coordinates = Point(point_coordinates)

    eligiblity_map.contains(coordinates)

    inside_polygon = eligiblity_map.geometry.apply(lambda polygon: polygon.contains(coordinates)).any()

    return inside_polygon


if __name__ == '__main__':
    orlando = (-81.324921, 28.516623)
    wedgefield = (-81.073523, 28.479016)

    print(is_eligible(orlando))
    print(is_eligible(wedgefield))

