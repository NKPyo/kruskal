============================
Kruskal's Algorithm Library
============================

This library allows you to create graphs and run the Kruskal's algorithm to find the minimum spanning tree of a weighted graph. The Kruskal's algorithm is a greedy algorithm that iterates through all edges and tries to find the minimum spanning tree while avoiding any cycles in the graph. The average case time complexity for the algorithm is O(m log n), where m is the number of edges and n is the number of vertices.

***************
Installation
***************
Type the following line in command line:

``pip install kruskal``

Requirements
===============
This library requires installation of another standard library called networkx. In order to use this library for your own purposes, you will have to create the graph using the networkx library and then pass it as an input in the kruskal() function.

***************
Usage
***************

``import kruskal as k``

``x=k.randomgraph(12,5)``

``mst=k.kruskal(x)``

``print mst``

``Output: [(1, 6), (4, 10), (4, 5), (2, 5), (2, 11), (0, 9), (3, 8), (2, 7), (3, 7), (0, 1), (1, 11)]``
