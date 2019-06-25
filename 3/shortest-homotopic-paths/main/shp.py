from main.utils import *
import matplotlib.pyplot as plt


def main():
    """
    find the shortest path homotopic to a given path
    """

#    obstacle = [(10, 20), (58, 4), (-10, 30), (19, 41), (60, 50), (35, -8)]
#    path = [(-15, 32), (44, 33), (65, 60), (58, -4), (52, 66), (72, 34), (56, -15), (15, 51), (16, -10), (20, 1)]

    obstacle = [(5, 30), (10, -11), (30, 1), (40, 40), (60, 20)]
    path = [(20, 20), (30, -10), (40, 0), (20, 5), (8, -20), (0, 35), (70, 20), (55 ,15), (40, 45), (35, 30), (65, 25), (66, 2)]

    hull, triangulation = graham_scan(obstacle)

    cross_seq, path_edges = cross(path, triangulation)

    reduce_cross_seq = reduce(cross_seq)

    hull.append(hull[0])
    plt.scatter([p[0] for p in obstacle], [p[1] for p in obstacle], c='red')
    # plt.plot([p[0] for p in hull], [p[1] for p in hull], c='red')

    for e in triangulation:
        plt.plot([p[0] for p in e], [p[1] for p in e], c='black')

    for e in path_edges:
        plt.plot([p[0] for p in e], [p[1] for p in e], c='orange')

    for e in cross_seq:
        plt.plot([p[0] for p in e], [p[1] for p in e], c='pink')

    for e in reduce_cross_seq:
        plt.plot([p[0] for p in e], [p[1] for p in e], c='green')


    plt.show()


def graham_scan(points):
    """
    Point triangulation using Graham’s scan
    """

    # find point p smallest lexicographic
    p, rest = take_smallest(points)

    # sort points orientation (p, p1, p2)
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
