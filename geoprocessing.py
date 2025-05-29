# Sample geoprocessing function
import geopandas as gpd

def load_geodata(filepath):
    return gpd.read_file(filepath)
