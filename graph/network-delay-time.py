#Network Delay Time
#There are N network nodes, labelled 1 to N.
#Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
#Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#Note:
#    N will be in the range [1, 100].
#    K will be in the range [1, N].
#    The length of times will be in the range [1, 6000].
#    All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

#Space = (N+E)


# W/ DFS
#Time = O(N^N + E log E)
class Solution(object):

  def networkDelayTime(self, times, N, K):
    """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
    #Will there be any negative cost/weight?
    vxtIdxMap = collections.defaultdict(list)
    for (u, v, w) in times:
      vxtIdxMap[u].append(
          (w, v))  #Use of weight as first param is to sort the list
      #based on the weight
    #All nodes start from index 1
    dist = {node: float('inf') for node in xrange(1, N + 1)}

    #single source to all Nodes with DFS
    def getshortestPath(node, elapsed):
      if elapsed >= dist[node]:
        return
      dist[node] = elapsed
      for time, nei in sorted(vxtIdxMap[node]):  #Sorted by weight
        getshortestPath(nei, elapsed + time)

    getshortestPath(K, 0)

    #Get the maximum time from dict as everyone start bradcast the
    #message at the same time
    ans = max(dist.values())
    return ans if ans < float('inf') else -1


#Dijkstra w/ heap
#T : O(N log N)
class Solution(object):

  def networkDelayTime(self, times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
      graph[u].append((v, w))

    pq = [(0, K)]
    dist = {}
    while pq:
      d, node = heapq.heappop(pq)
      if node in dist:
        continue
      dist[node] = d
      for nei, d2 in graph[node]:
        if nei not in dist:
          heapq.heappush(pq, (d + d2, nei))

    return max(dist.values()) if len(dist) == N else -1


#Dijkstra w/ sort
#Time = O(N^2 + E)
class Solution(object):

  def networkDelayTime(self, times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
      graph[u].append((v, w))

    dist = {node: float('inf') for node in xrange(1, N + 1)}
    seen = [False] * (N + 1)
    dist[K] = 0

    while True:
      cand_node = -1
      cand_dist = float('inf')
      for i in xrange(1, N + 1):
        if not seen[i] and dist[i] < cand_dist:
          cand_dist = dist[i]
          cand_node = i

      if cand_node < 0:
        break
      seen[cand_node] = True
      for nei, d in graph[cand_node]:
        dist[nei] = min(dist[nei], dist[cand_node] + d)

    ans = max(dist.values())
    return ans if ans < float('inf') else -1
