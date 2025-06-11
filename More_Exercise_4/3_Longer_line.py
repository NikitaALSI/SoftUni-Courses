from math import sqrt, floor


def closest_point(point1, point2):
    from math import sqrt, floor
    dist1 = sqrt(point1[0]**2 + point1[1]**2)
    dist2 = sqrt(point2[0]**2 + point2[1]**2)
    if dist1 <= dist2:
        return f"({floor(point1[0])}, {floor(point1[1])})"
    return f"({floor(point2[0])}, {floor(point2[1])})"


def furthest_point(point1, point2):
    from math import sqrt, floor
    dist1 = sqrt(point1[0] ** 2 + point1[1] ** 2)
    dist2 = sqrt(point2[0] ** 2 + point2[1] ** 2)
    if dist1 > dist2:
        return f"({floor(point1[0])}, {floor(point1[1])})"
    return f"({floor(point2[0])}, {floor(point2[1])})"


def longer_line(pair1, pair2):
    from math import sqrt, floor

    line1 = sqrt((pair1[0][0] - pair1[1][0]) ** 2 + (pair1[0][1] - pair1[1][1]) ** 2)
    line2 = sqrt((pair2[0][0] - pair2[1][0]) ** 2 + (pair2[0][1] - pair2[1][1]) ** 2)

    if line1 >= line2:
        return f"{closest_point(pair1[0], pair1[1])}{furthest_point(pair1[0], pair1[1])}"
    return f"{closest_point(pair2[0], pair2[1])}{furthest_point(pair2[0], pair2[1])}"


x1, y1, x2, y2, x3, y3, x4, y4 = float(input()),float(input()),float(input()),float(input()), float(input()),float(input()),float(input()),float(input())
first_pair = ((x1, y1), (x2, y2))
second_pair = ((x3, y3), (x4, y4))

print(longer_line(first_pair, second_pair))