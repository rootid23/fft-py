#Course Schedule
#There are a total of n courses you have to take, labeled from 0 to n - 1.
#Some courses may have prerequisites, for example to take course 0 you have to
#first take course 1, which is expressed as a pair: [0,1]
#Given the total number of courses and a list of prerequisite pairs, is it
#possible for you to finish all courses?
#For example:
#2, [[1,0]] 1<- 0
#There are a total of 2 courses to take. To take course 1 you should have
#finished course 0. So it is possible.
#2, [[1,0],[0,1]]
#There are a total of 2 courses to take. To take course 1 you should have
#finished course 0, and to take course 0 you should also have finished course
#1. So it is impossible.
#Note:
#The input prerequisites is a graph represented by a list of edges, not
#adjacency matrices. Read more about how a graph is represented.
#You may assume that there are no duplicate edges in the input prerequisites.

from collections import defaultdict


class Solution(object):

  def canFinish(self, numCourses, prerequisites):
    """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
    #create graph
    graph = defaultdict()
    for dep in prerequisites:
      if (dep[0] not in graph):
        graph[dep[0]] = []
      graph[dep[0]].append(dep[1])

    #detect cycle with dfs
    def dfs(src, parent, graph):
      flg = False
      if (src in graph):
        for nbr in graph[src]:
          if (nbr not in parent):
            parent[nbr] = src
            flg = dfs(nbr, parent, graph)
          else:
            #print parent, "src = " , src, " nbr = ",nbr
            if (parent[nbr] == None):
              return True
      return flg

    #Why visited? -> we need to detect cycle start from an
    visited = [False] * numCourses
    for vx in graph.keys():
      if (visited[vx] == False):
        parent = defaultdict()
        parent[vx] = None
        if (True == dfs(vx, parent, graph)):
          return False
        visited[vx] = True

    return True
