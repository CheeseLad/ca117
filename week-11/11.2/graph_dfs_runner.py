#!/usr/bin/env python3

import sys

from graph_dfs_112 import Graph, DFSPaths

def main():

    with open('graph_input_00_112.txt', 'r') as f:

        V = int(f.readline().strip())

        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    dfs = DFSPaths(g, 4)

    print(dfs.hasPathTo(2))

    print(dfs.pathTo(2))

if __name__ == '__main__':
    main()