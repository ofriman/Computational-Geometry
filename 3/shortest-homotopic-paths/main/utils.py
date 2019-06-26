def _lexicographic_comp(p, q, _):
    return p[0] < q[0] or (p[0] == q[0] and p[1] <= q[1])


def _orientation_comp(p1, p2, p):
    return orientation(p, p1, p2) > 0


def lexicographic_sort(points):
    return merge_sort(points, _lexicographic_comp, {})


def orientation_sort(points, p):
    return merge_sort(points, _orientation_comp, p)


def merge_sort(points, comp, p):
    if len(points) < 2:
        return points
    mid = len(points) // 2
    return merge(merge_sort(points[:mid], comp, p), merge_sort(points[mid:], comp, p), comp, p)


def merge(left, right, comp, p):
    combined = []
    left_index = right_index = 0
    left_len = len(left)
    right_len = len(right)
    while left_index < left_len and right_index < right_len:
        if comp(left[left_index], right[right_index], p):
            combined.append(left[left_index])
            left_index += 1
        else:
            combined.append(right[right_index])
            right_index += 1
    combined = combined + left[left_index:] + right[right_index:]
    return combined


def orientation(p, q, r):
    orient = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    if orient > 0:
        return 1
    if orient < 0:
        return -1

    return 0


def take_smallest(points):
    rest = []
    p = points[0]
    for q in points[1:]:
        if q[0] < p[0] or (q[0] == p[0] and q[1] < p[1]):
            p = q
    for q in points:
        if q != p:
            rest.append(q)
    return p, rest


def line_intersection(s1, s2):
    return (orientation(s1[0], s1[1], s2[0]) != orientation(s1[0], s1[1], s2[1])) and\
           (orientation(s2[0], s2[1], s1[0]) != orientation(s2[0], s2[1], s1[1]))


def has_common_point(s1, s2):
    return s1[0] == s2[0] or s1[1] == s2[0] or s1[0] == s2[1] or s1[1] == s2[1]


def connect_points(points, close=True):
    edges = []
    for i in range(len(points) - (0 if close else 1)):
        edges.append([points[i], points[(i + 1) % len(points)]])
    return edges


def get_tuples(txt, dimension=2, delimiter=' '):
    str_split = txt.rstrip().split(delimiter)
    return list(map(lambda a: tuple(map(int, a)),
                    [str_split[i:i + dimension] for i in range(0, len(str_split), dimension)]))

