v = {'A', 'B', 'C', 'D', 'E'}
e = {'A': {'B': 6, 'D': 1},
     'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
     'C': {'B': 5, 'E': 5},
     'D': {'A': 1, 'B': 2, 'E': 1},
     'E': {'B': 2, 'C': 5, 'D': 1}}

def dijkstr(gr, intial, goal):
    unseen_g = gr
    infinity = 9999
    shorted_dist = {}
    preeceding_eg = {}
    final_path = [intial]

    for i in unseen_g:
        shorted_dist[i] = infinity
    shorted_dist[intial] = 0

    print(shorted_dist)

    while unseen_g:
        minNode = None
        for j in unseen_g:  #slecting shorted distAnce node from shorted_dist
            if minNode is None:
                minNode = j
            elif shorted_dist[j] < shorted_dist[minNode]:
                minNode = j

        for childNode, weight in unseen_g[minNode].items():
            if weight+shorted_dist[minNode] < shorted_dist[childNode]:
                shorted_dist[childNode] = weight + shorted_dist[minNode]
                preeceding_eg[childNode] = minNode
        unseen_g.pop(minNode)
    print(shorted_dist)
    print(preeceding_eg)


    current = goal
    while current != intial:
        try:
            final_path.insert(1, current)
            current = preeceding_eg[current]
        except:
            print("no path exist")
            break

    print(f"shortest distance is {shorted_dist[goal]} and path is {final_path} ")


if __name__ == "__main__":
     dijkstr(e, 'A', 'C')

     # s = 0
     # for i in e:
     #     # print(e[i].items())
     #     for l in e[i]:
     #         s+=1
     #         print(f"vertex {i} -> {l} weight {e[i][l]}")
     #
     # print(f"total no. of eages {s}")