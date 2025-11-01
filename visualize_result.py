from plotgr import TourFunction

# Example demo data
Geometric_Points = [
    (10, 10),  # depot
    (20, 20),
    (30, 10),
    (25, 25),
    (15, 30),
    (40, 20),
    (35, 35),
    (45, 15),
    (20, 40),
    (10, 30),
]

ClusterList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

TourFunction(ClusterList, Geometric_Points)
