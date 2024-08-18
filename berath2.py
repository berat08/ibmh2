import math

points = [(0, 0), (1, 2), (3, 5), (4, 8)]


# Fonksiyonun tanımı
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Tüm uzaklıkları tutacak olan array
distances = []

# İç içe for döngüsü kullanarak tüm noktaların arasındaki uzaklığı bulma
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Uzaklıkların arasındaki en küçüğü belirleme
min_distance = min(distances)

# Uzaklıkları virgülden sonra 2 basamak olacak şekilde düzenleme
formatted_distances = [f"{d:.2f}" for d in distances]
formatted_min_distance = f"{min_distance:.2f}"

# Sonuçları bastırma
print("Mesafeler:", formatted_distances)
print("Minimum Mesafe:", formatted_min_distance)
