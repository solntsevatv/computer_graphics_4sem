import math
import copy

CANV_X = 1000
CANV_Y = 800

def find_area(point1, point2, point3):
    """
        Find triangle area, circle area, radius of circle
    """
    triangle_area = 1e10
    circle_area = 0
    radius = 0

    rib1 = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    rib2 = math.sqrt((point3[0] - point2[0])**2 + (point3[1] - point2[1])**2)
    rib3 = math.sqrt((point3[0] - point1[0])**2 + (point3[1] - point1[1])**2)

    p = (rib1 + rib2 + rib3) / 2
    triangle_area = math.sqrt(p * (p - rib1) * (p - rib2) * (p - rib3))
    if triangle_area > 0:
        radius = rib1 * rib2 * rib3 / 4 / triangle_area
        circle_area = math.pi * (radius)**2

    #triangle_square = (point1[0] * (point2[1] - point3[1]) + point2[0] * \
    #(point3[1] - point1[1]) + point3[0] * (point1[1] - point2[1])) / 2

    return triangle_area, circle_area, radius

def transform_y_coord(coord):
    return 800-coord 
def transform_values(coords, circle_center, radius):
    coordinates = copy.deepcopy(coords)

    #scaling up
    k = (CANV_Y / 2 - 50) / radius
    radius *= k

    for i in range(3):
        coordinates[i][0] *= k
        coordinates[i][1] *= k
    
    new_circle_center = find_circle_center(coordinates[0][0], coordinates[0][1], \
                                            coordinates[1][0], coordinates[1][1], \
                                            coordinates[2][0], coordinates[2][1],)

    #transfer to old place
    x_change = new_circle_center[0] - CANV_X / 2
    y_change = new_circle_center[1] - CANV_Y / 2
    new_circle_center = (CANV_X / 2, CANV_Y / 2)

    for i in range(3):
        coordinates[i][0] -= x_change
        coordinates[i][1] -= y_change

    # to change y orientation
    for i in range(3):
        coordinates[i][1] = transform_y_coord(coordinates[i][1])

    return coordinates, new_circle_center, radius

def find_circle_center(x1, y1, x2, y2, x3, y3):
    while (x1 == x2):
        x1, y1, x2, y2, x3, y3 = x3, y3, x2, y2, x1, y1

    if (2 * ((x2-x3)*(y1-y2) - (x1-x2)*(y2-y3)) == 0):
        b = (x2-x3) * ((x1**2 - x2**2) + (y1**2 - y2**2)) + (x1-x2)*(x3**2-x2**2+y3**2-y2**2)
    else:
        b = ((x2-x3) * ((x1**2 - x2**2) + (y1**2 - y2**2)) + (x1-x2)*(x3**2-x2**2+y3**2-y2**2)) / \
        (2 * ((x2-x3)*(y1-y2) - (x1-x2)*(y2-y3)))

    if (x1 - x2 == 0):
        a = (x1**2 - x2**2 + y1**2 - y2**2) - 2*b*(y1-y2)
    else:
        a = ((x1**2 - x2**2 + y1**2 - y2**2) - 2*b*(y1-y2)) / (2 * (x1-x2))
    
    return a,b