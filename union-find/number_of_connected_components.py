#!/usr/bin/env python

# UF - works well w/ UGRPH , DRGRH - DFS/BFS
#Number of Connected Components in an Undirected Graph
#Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
#edge is a pair of nodes), write a function to find the number of connected
#components in an undirected graph.
#Example 1:
#     0          3
#     |          |
#     1 --- 2    4
#Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
#Example 2:
#     0           4
#     |           |
#     1 --- 2 --- 3
#Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
#Note:
#You can assume that no duplicate edges will appear in edges. Since all edges
#are undirected, [0, 1] is the same as [1, 0] and thus will not appear
#together in edges.
#(1,2) (3,5) (6,7) (7,2)
# 0, 0, 2, 3, 2, 5, 6, 6

## Ways
#1.
#frm  - 1


# Quick-find
def countComponents(n, edges):

  cnt = [n]  # of connected components
  grph = range(n)

  def find(idx):
    return grph[idx]

  def union(e):
    nodes = [e[0], e[1]]
    frmV, toV = map(find, nodes)
    if (frmV == toV):
      return
    for i in range(len(grph)):
      if (grph[i] == frmV):
        grph[i] = toV
    cnt[0] -= 1

  for idx in range(len(edges)):
    union(edges[idx])
  print cnt[0]
  return cnt[0]


#Quick-union
def countComponents(n, edges):

  #Py limitation cannot use pass be reference
  cnt = [n]  # of connected components
  grph = range(n)

  def find(idx):
    while (idx != grph[idx]):
      idx = grph[idx]
    return grph[idx]

  def union(e):
    nodes = [e[0], e[1]]
    frmV, toV = map(find, nodes)
    if (frmV == toV):
      return
    for i in range(len(grph)):
      if (grph[i] == frmV):
        grph[i] = toV
    cnt[0] -= 1

  for idx in range(len(edges)):
    union(edges[idx])
  print cnt[0]
  return cnt[0]


#Path compression
def countComponents(n, edges):

  #Py limitation cannot use pass be reference
  cnt = [n]  # of connected components
  grph = range(n)

  def find(idx):
    while (idx != grph[idx]):
      grph[idx] = grph[grph[idx]]  # path compression
    return grph[idx]

  def union(e):
    nodes = [e[0], e[1]]
    frmV, toV = map(find, nodes)
    if (frmV == toV):
      return
    for i in range(len(grph)):
      if (grph[i] == frmV):
        grph[i] = toV
    cnt[0] -= 1

  for idx in range(len(edges)):
    union(edges[idx])
  print cnt[0]
  return cnt[0]


#countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
