from main.utils import *


def main():
    """
    find the shortest path homotopic to a given path
    """
    obstacle, path = get_input()

    hull, triangulation = graham_scan(obstacle)

    cross_seq, path_edges = cross(path, triangulation)

    reduce_cross_seq = reduce(cross_seq)

    show_out(obstacle, path_edges, triangulation, reduce_cross_seq)


def graham_scan(points):
    """
    Point triangulation using Graham’s scan
    """
    p, rest = take_smallest(points)
    sorted_points = orientation_sort(rest, p)
    triangulation = []
    hull = [p]
    for q in sorted_points:
        hull_edges = connect_points(hull)
        candidates = [(q, h) for h in hull]
        for c in candidates:
            if all((has_common_point(c, h)) or (not line_intersection(c, h)) for h in hull_edges):
                triangulation.append(c)

        while len(hull) > 2:
            if (orientation(hull[-1], hull[-2], q)) > 0:
                hull.pop()
            else:
                break
        hull.append(q)
    return hull, triangulation


def cross(path, triangulation):
    """
    compute the crossing sequence of the input path
    """
    path_edges = connect_points(path, False)
    cross_seq = []
    for e in path_edges:
        for t in triangulation:
            if line_intersection(e, t):
                cross_seq.append(t)
    return cross_seq, path_edges


def reduce(edges):
    """
    reduces the crossing sequence by repeatedly removing any adjacent pairs of the same label
    """
    t = 0
    s = [() for i in range(len(edges) + 1)]
    for i in range(len(edges)):
        if edges[i] == s[t]:
            t = t - 1
        else:
            t = t + 1
            s[t] = edges[i]

    return s[1:t]


if __name__ == "__main__":
    main()
