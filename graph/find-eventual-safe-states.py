#In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.
#If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.
#Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal
#node. More specifically, there exists a natural number K so that for any choice of where to walk, we
#must have stopped at a terminal node in less than K steps.
#Which nodes are eventually safe?  Return them as an array in sorted order.
#The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph. The graph
#is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge
#of the graph.
#Example:
#Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
#Output: [2,4,5,6]
#Here is a diagram of the above graph.
#Illustration of graph
#Note:
#    graph will have length at most 10000.
#    The number of edges in the graph will not exceed 32000.
#    Each graph[i] will be a sorted list of different integers, chosen within the range [0,
#graph.length - 1].


### work for few

        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        #O(n^2) - visit each an explore it
        #[[1,2],[2,3],[5],[0],[5],[],[]]
        #0 -> (1,2), 1->(2,3) , 2->(5), 3->(0), 4->(5), 5->(), 6()
        #0-> (2,3)
        #p= [2,3]
        #0 is not safe
        #

class Solution(object):

    def eventualSafeNodes(self, graph):


        def iscycle(i):

            visited[i] = 0
            for v in graph[i]:
                #1.already visited
                if (visited[v] == 0):
                    return True
                #2.already explored and has cycle
                if(visited[v] == -1 and iscycle(v)) :
                    return True
            #completely visited
            visited[i] = 1
            #no cycle found
            safe_state.add(i)
            return False

        visited, safe_state = [-1] * len(graph), set()

        for i in range(len(graph)):
            #if not visited
            if visited[i] == -1:
                iscycle(i)

        return sorted(list(safe_state))
