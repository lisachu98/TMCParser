import shapefile
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import MultiPolygon
from dbfread import DBF
from mayavi import mlab
# from geopandas.datasets.naturalearth_creation import gdf
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

path1 = 'poland.shp'  # scieżka do pliku shp

sf1 = shapefile.Reader(path1) # wczytanie pliku shapefile

shape_ex1 = sf1.shape(4)  # odczytaj czwarty kształt (indeks 3) - woj kuj pom
print(shape_ex1)

numPoints1=len(shape_ex1.points)
print('Liczba punktów: ', numPoints1)

numParts1=len(shape_ex1.parts)
print('Liczba czesci: ', numParts1)

# utworzenie dwoch tablic o rozmiarze rownym liczbie punktow w ksztalcie
x_lon1 = np.zeros((len(shape_ex1.points), 1))
y_lat1 = np.zeros((len(shape_ex1.points), 1))


for ip in range(len(shape_ex1.points)):
    x_lon1[ip] = shape_ex1.points[ip][0]
    y_lat1[ip] = shape_ex1.points[ip][1]

# plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.get_yaxis().set_visible(True)
ax.get_xaxis().set_visible(True)
ax.set_frame_on(False)
plt.plot(x_lon1, y_lat1, 'k')

# Ustawiane są ograniczenia wykresu używając danych z bounding box (bbox) odczytanego kształtu
plt.xlim(shape_ex1.bbox[0], shape_ex1.bbox[2])
plt.show()

print("\n###########################################\n")

sf2 = shapefile.Reader('jezdnie.shp')
shape_ex2 = sf2.shape(3)
print(shape_ex2)

numPoints2=len(shape_ex2.points)
print('Liczba punktów: ', numPoints2)

numParts2=len(shape_ex2.parts)
print('Liczba czesci: ', numParts2)

x_lon2 = np.zeros((len(shape_ex2.points), 1))
y_lat2 = np.zeros((len(shape_ex2.points), 1))

print('Wspolrzedne punktow: ', shape_ex2.points)

for ip in range(len(shape_ex2.points)):
    x_lon2[ip] = shape_ex2.points[ip][0]
    y_lat2[ip] = shape_ex2.points[ip][1]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.get_yaxis().set_visible(True)
ax.get_xaxis().set_visible(True)
ax.set_frame_on(False)
plt.plot(x_lon2, y_lat2, 'k')

# Ustawiane są ograniczenia wykresu używając danych z bounding box (bbox) odczytanego kształtu
plt.xlim(shape_ex2.bbox[0], shape_ex2.bbox[2])
plt.show()

print("\n###########################################\n")

path3 = 'cropPoints.shp'
sf3 = shapefile.Reader(path3)

shape_ex3 = sf3.shape(0)  # Odczytaj kształt
print(shape_ex3)

xy3 = shape_ex3.points[0]
print('Wspolrzedne punktu: ', xy3)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.get_yaxis().set_visible(True)
ax.get_xaxis().set_visible(True)
ax.set_frame_on(False)
plt.plot(xy3[0], xy3[1], marker="o", markersize=10, markeredgecolor="black", markerfacecolor="black")

# Ustawiane są ograniczenia wykresu używając danych z bounding box (bbox) odczytanego kształtu
plt.show()

print("\n###########################################\n")
path4 = 'simple_roof_multipatch.shp'


sf4 = gpd.read_file(path4)
shape_ex4 = sf4.geometry[0]
print(shape_ex4)

gdf = gpd.read_file('simple_roof_multipatch.shp')

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Iterate over the geometries and plot them as 3D patches
colors = ['r','g','b','y']
i = 0
geom = gdf.loc[0, 'geometry']
for polygon in geom.geoms:
    x, y, z = zip(*polygon.exterior.coords)
    vertices = [list(zip(x, y, z))]
    ax.add_collection3d(Poly3DCollection(vertices, facecolors=colors[i], edgecolors='k'))
    i = i + 1

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the plot boundaries
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

# Display the plot
plt.show()




#
# sf4.plot()
# plt.show()

print("\n###########################################\n")

sf = shapefile.Reader('multipoint.shp')
shape_ex = sf.shape(0)  # Odczytaj czwarty kształt (indeks 3) - woj kuj pom



# Odczytaj współrzędne punktów
points = shape_ex.points

# Odczytaj liczbę punktów
num_points = len(points)

# Wyświetlanie współrzędnych punktów
for i, point in enumerate(points):
    x, y = point
    print(f'Punkt {i+1}: ({x}, {y})')

print('Liczba punktów:', num_points)
# record = records[0]  # Odczytaj czwarty rekord (indeks 3)

x_lon = np.zeros((len(shape_ex.points), 1))
y_lat = np.zeros((len(shape_ex.points), 1))

for ip in range(len(shape_ex.points)):
    x_lon[ip] = shape_ex.points[ip][0]
    y_lat[ip] = shape_ex.points[ip][1]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.get_yaxis().set_visible(True)
ax.get_xaxis().set_visible(True)
ax.set_frame_on(False)
plt.plot(x_lon, y_lat, 'o')

# Ustawiane są ograniczenia wykresu używając danych z bounding box (bbox) odczytanego kształtu
plt.xlim(shape_ex.bbox[0]-5, shape_ex.bbox[2]+5)
plt.show()