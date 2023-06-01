import geopandas as gpd
from shapely.geometry import MultiPolygon, Polygon

# Create an empty list to store the polygons of the Multipatch
polygons = []

# Generate the four triangle polygons for the roof
triangle1 = Polygon([(0, 0, 0), (5, 0, 0), (2.5, 2.5, 5)])
triangle2 = Polygon([(5, 0, 0), (5, 5, 0), (2.5, 2.5, 5)])
triangle3 = Polygon([(5, 5, 0), (0, 5, 0), (2.5, 2.5, 5)])
triangle4 = Polygon([(0, 5, 0), (0, 0, 0), (2.5, 2.5, 5)])

# Add the triangle polygons to the list
polygons.extend([triangle1, triangle2, triangle3, triangle4])

# Create a Multipolygon from the polygons
multipolygon = MultiPolygon(polygons)

# Create a GeoDataFrame with the Multipatch geometry
gdf = gpd.GeoDataFrame(geometry=[multipolygon])

# Define the output shapefile path
output_shapefile = 'simple_roof_multipatch.shp'

# Save the GeoDataFrame as a shapefile
gdf.to_file(output_shapefile)