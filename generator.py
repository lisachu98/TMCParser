import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon
import random

# Create an empty list to store the Multipatch geometries
multipatches = []

# Generate multiple Multipatch geometries
for _ in range(5):  # Generate 5 Multipatch geometries
    # Create an empty list to store the polygons of the Multipatch
    polygons = []

    # Generate multiple polygons for the Multipatch
    for _ in range(3):  # Generate 3 polygons for each Multipatch
        # Generate random coordinates for the polygon's exterior
        coords = [(random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10)) for _ in range(4)]

        # Create a polygon and append it to the list
        polygon = Polygon(coords)
        polygons.append(polygon)

    # Create a Multipolygon from the polygons and append it to the Multipatch list
    multipolygon = MultiPolygon(polygons)
    multipatches.append(multipolygon)
# Create a GeoDataFrame with the Multipatch geometries
gdf = gpd.GeoDataFrame(geometry=multipatches)
# Define the output shapefile path
output_shapefile = 'synthetic_multipatch.shp'

# Save the GeoDataFrame as a shapefile
gdf.to_file(output_shapefile)
