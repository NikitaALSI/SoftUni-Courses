def closest_point(x1, y1, x2, y2):
    from math import sqrt, floor
    dist1 = sqrt(x1**2 + y1**2)
    dist2 = sqrt(x2**2 + y2**2)
    if dist1 <= dist2:
        return f"({floor(x1)}, {floor(y1)})"
    return f"({floor(x2)}, {floor(y2)})"


x1, y1, x2, y2 = float(input()),float(input()),float(input()),float(input())
print(closest_point(x1, y1, x2, y2))
