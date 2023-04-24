import shapefile
import binascii
import struct

path='poland.shp'

with open(path, 'rb') as f:
    # Odczytaj nagłówek pliku shapefile (100 bajtów)
    header = f.read(100)

    # Odczytaj magiczną liczbę (4 bajty)
    magic_number = int.from_bytes(header[:4], byteorder='big')
    print('Magiczna liczba:', magic_number)

    # Odczytaj wersję (4 bajty)
    version = int.from_bytes(header[28:32], byteorder='little')
    print('Wersja:', version)

    # Odczytaj typ geometrii (4 bajty)
    shape_type = int.from_bytes(header[32:36], byteorder='little')
    print('Typ geometrii:', shape_type)

    # Odczytaj bounding box (32 bajty)
    bbox = struct.unpack('<4d', header[36:68])
    print('Bounding box:', bbox)

    # Odczytaj liczbę rekordów (4 bajty)
    num_records = int.from_bytes(header[24:28], byteorder='big')
    print('Liczba rekordów:', num_records)

    f.seek(24) # przejście do pozycji 24 w pliku
    checksum = binascii.hexlify(f.read(4)).decode("utf-8") # odczytanie 4 bajtów i przekształcenie do postaci heksadecymalnej
    print("Suma kontrolna:", checksum)

    f.seek(24)
    file_length = int.from_bytes(f.read(4), byteorder='big') * 2

    # Odczytaj długość nagłówka SHP (100 bajtów)
    header_length = 100

    # Oblicz długość zawartości SHP
    content_length = file_length - header_length

    # Wyświetl wyniki
    print("File length:", file_length)
    print("Content length:", content_length)

    while True:
        record = f.read(8)
        if not record:
            break
        recHeader = int.from_bytes(record[:4], byteorder='big')
        recLength = int.from_bytes(record[4:], byteorder='big')
        print("Record header:", recHeader)
        print("Record length:", recLength)