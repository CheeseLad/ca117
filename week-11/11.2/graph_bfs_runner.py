#!/usr/bin/env python3

import sys

from graph_bfs_112 import Graph, BFSPaths

def main():

    with open('graph_input_00_112.txt', 'r') as f:

        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    bfs = BFSPaths(g, 4)

    print(bfs.hasPathTo(2))

    print(bfs.pathTo(2))

if __name__ == '__main__':
    main()