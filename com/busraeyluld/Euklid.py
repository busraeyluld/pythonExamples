from math import sqrt
points = [(3, 4),(2,5),(6,8)]
def euclideanDistance(x,y):
    distance = sqrt(x*x + y*y)
    return distance
for point in points:
    x,y = point
    distance = euclideanDistance(x,y)
    print(f"({x},{y}) noktasının orijine göre uzaklığı: {distance}")
