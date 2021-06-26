# 2021-06-26-23-30-08.png
# because we know that all the weights are positives we are gonna use dijkstra algo.

from queue import PriorityQueue


def minCost():
    # def minCost(graph, source, destination):
    pq = PriorityQueue()
    pq.put((4, 'Read'))
    pq.put((2, 'Play'))
    pq.put((5, 'Write'))
    pq.put((1, 'Code'))
    pq.put((3, 'Study'))
    pq.put((0, 'Study'))
    while not pq.empty():
        next_item = pq.get()
        print(next_item)


if __name__ == '__main__':
    minCost()
