# Noktalar listesi tanımlama
points = [(1, 2), (4, 6), (5, 1), (0, 0), (3, 4)]  # Noktalar burada temsil ediliyor.

def euclideanDistance(point1, point2):
    """
    İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
    :param point1: Birinci nokta (x1, y1)
    :param point2: İkinci nokta (x2, y2)
    :return: İki nokta arasındaki mesafe
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # Formül: d = sqrt((x2-x1)^2 + (y2-y1)^2)
    return distance

# Mesafeleri saklamak için boş bir liste oluşturma
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplamak için döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı çiftlerin tekrarlanmaması için j=i+1'den başlar
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
        print(f"{points[i]} ile {points[j]} arasındaki mesafe: {dist:.2f}")

# Minimum mesafeyi bulma
min_distance = min(distances)
print(f"\nEn küçük mesafe: {min_distance:.2f}")
