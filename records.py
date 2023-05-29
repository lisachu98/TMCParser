import shapefile
import numpy as np
import matplotlib.pyplot as plt
from dbfread import DBF

path = 'poland.dbf'  # Ścieżka do pliku DBF

table = DBF(path, encoding='latin-1')

records = list(table)  # Odczytaj wszystkie rekordy

print(len(records))  # Liczba rekordów w pliku

# Get the first shape and record
sf = shapefile.Reader('poland.shp')
shape_ex = sf.shape(3)  # Odczytaj czwarty kształt (indeks 3) - woj kuj pom

record = records[3]  # Odczytaj czwarty rekord (indeks 3)

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
plt.plot(x_lon, y_lat, 'k')

# Ustawiane są ograniczenia wykresu używając danych z bounding box (bbox) odczytanego kształtu
plt.xlim(shape_ex.bbox[0], shape_ex.bbox[2])
plt.show()

sf = shapefile.Reader('jezdnie.shp')
shape_ex = sf.shape(3)  # Odczytaj czwarty kształt (indeks 3) - woj kuj pom

record = records[3]  # Odczytaj czwarty rekord (indeks 3)

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
plt.plot(x_lon, y_lat, 'k')

# Ustawiane są ograniczenia wykresu używając danych z bounding box (bbox) odczytanego kształtu
plt.xlim(shape_ex.bbox[0], shape_ex.bbox[2])
plt.show()

sf = shapefile.Reader('cropPoints.dbf')
shape_ex = sf.shape(3)  # Odczytaj czwarty kształt (indeks 3) - woj kuj pom

record = records[3]  # Odczytaj czwarty rekord (indeks 3)

x_lon = shape_ex.points[0]

# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.get_yaxis().set_visible(True)
ax.get_xaxis().set_visible(True)
ax.set_frame_on(False)
plt.plot(x_lon[0], x_lon[1], marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")

# Ustawiane są ograniczenia wykresu używając danych z bounding box (bbox) odczytanego kształtu
plt.show()

sf = shapefile.Reader('upenn-tc_br18s22_2r.shp')
shape_ex = sf.shape(0)  # Odczytaj czwarty kształt (indeks 3) - woj kuj pom

record = records[0]  # Odczytaj czwarty rekord (indeks 3)

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
