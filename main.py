import shapefile
import binascii
import struct

path='cropPoints.shp'

with open(path, 'rb') as f:
    # Odczytaj nagłówek pliku shapefile (100 bajtów)
    header = f.read(100)

    # Odczytaj magiczną liczbę - kod pliku (4 bajty)
    file_code = int.from_bytes(header[:4], byteorder='big')
    print('Kod pliku:', file_code)

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
    file_length = int.from_bytes(header[24:28], byteorder='little')
    print('Długość pliku (file length):', file_length)

    f.seek(24) # przejście do pozycji 24 w pliku
    checksum = binascii.hexlify(f.read(4)).decode("utf-8") # odczytanie 4 bajtów i przekształcenie do postaci heksadecymalnej
    print("Suma kontrolna:", checksum)

    # Odczytaj nagłówek rekordów głównego pliku
    main_header = f.read(100)

    # Odczytaj numer rekordu (4 bajty)
    # record_number = int.from_bytes(main_header[0:4], byteorder='big')
    # print('Numer rekordu:', record_number)

    # Odczytaj długość zawartości rekordu (4 bajty)
    # content_length = int.from_bytes(main_header[4:8], byteorder='big')
    # print('Długość zawartości rekordu:', content_length)



    sf = shapefile.Reader(path, encoding="iso-8859-1")

    # odczytanie atrybutów pliku shapefile
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()

    # odczytanie geometrii obiektów pliku shapefile
    shapes = sf.shapes()

    # liczba obiektów
    leng = len(shapes)

    print(f"Liczba obiektow: {leng}")

    print("****************************")

    with shapefile.Reader(path, encoding="iso-8859-1") as sf:
        fields = [x[0] for x in sf.fields][1:]
        records = sf.records()
        shapes = sf.shapes()
        total_content_length=0

        # wyświetlenie atrybutów i geometrii obiektów pliku shapefile
        for i, rec in enumerate(records):
            shape = shapes[i]
            content_length = len(rec)
            print(f"Atrybuty obiektu {i + 1}: {rec}")
            print(f"Geometria obiektu {i + 1}: {shape}")
            print(f"Długość rekordu: {len(rec)}")

            # Obliczenie długości zawartości rekordu
            content_length = 4  # nagłówek rekordu zajmuje 4 bajty
            content_length += 8 * len(shape.parts)  # liczba części geometrii * 8 bajtów na część
            content_length += 16 * len(shape.points)  # liczba punktów geometrii * 16 bajtów na punkt

            # Wyświetlenie długości zawartości rekordu
            print(f"Długość zawartości rekordu (content length): {content_length}")

            # Dodanie obliczonej długości do sumy długości rekordów
            total_content_length += content_length
            print("****************************")

# Wyświetlenie całkowitej długości zawartości rekordów
print(f"Całkowita długość zawartości rekordów: {total_content_length}")


