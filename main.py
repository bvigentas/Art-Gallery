def read_points():
    points = []
    with open('points', 'r') as file:
        for line in file:
            if ',' not in line:
                if len(points) > 0:
                    processed_points = grahan_scan(points)
                    if len(processed_points) == len(points):
                        print('No')
                    else:
                        print('Yes')

                else:
                    points = []
            else:
                x, y = ''.join(line.split()).split(',')
                point = [float(x), float(y)]
                points.append(point)


def grahan_scan(points):
    points = sort_points(points)
    l_sup = [points[0], points[1]]

    for i in range(2, len(points)):
        l_sup.append(points[i])

        while (len(l_sup) > 2) and cross_product(l_sup[len(l_sup)-3], l_sup[len(l_sup)-2], l_sup[len(l_sup)-1]) > 0:
            l_sup.pop(len(l_sup)-2)

    l_inf = [points[len(points)-1], points[len(points)-2]]

    for i in range(len(points)-3, -1, -1):
        l_inf.append(points[i])

        while (len(l_inf) > 2) and cross_product(l_inf[len(l_inf)-3], l_inf[len(l_inf)-2], l_inf[len(l_inf)-1]) > 0:
            l_inf.pop(len(l_inf)-2)

    l_sup.pop(0)
    l_inf.pop(0)

    joined_points = l_sup + l_inf

    return joined_points


def sort_points(points):
    return sorted(points, key=lambda k: k[0])


def cross_product(point1, point2, point3):
    return ((point2[0] - point1[0])*(point3[1] - point1[1]) - (point2[1] - point1[1])*(point3[0] - point1[0]));


if __name__ == '__main__':
    print(read_points())
