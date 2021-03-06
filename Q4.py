
import networkx as nx
import matplotlib.pyplot as plt
import random
import math
  
def graph():

    # Take N number of nodes from user
    print("Enter number of nodes")
    N = int(input())
    
    
    # Take P probability value for edges
    print("Enter value of probability of every node")
    P = float(input())
    
    
    # Create an empty graph object
    g = nx.Graph()
    
    
    # Adding nodes
    g.add_nodes_from(range(1, N + 1))

    # run each iteration for atleast 30 times
    av_list=[] 
    cc_list=[] 
    for count in range(30):

        # Add edges to the graph randomly.
        for i in g.nodes():
            for j in g.nodes():
                if (i < j):
                    
                    # Take random number R.
                    R = random.random()
                    
                    # Check if R<P add the edge to the graph else ignore.
                    if (R < P):
                        g.add_edge(i, j)
            pos = nx.circular_layout(g)
        all_node_degree = list(dict((nx.degree(g))).values())
        average=sum(all_node_degree)/N
        av_list.append(average)
        cc_list.append(nx.average_clustering(g))
    print("Average Clustering Coefficent: ",sum(cc_list)/30)
    print("Average degree of network: ",sum(av_list)/30)
    print("The average path length: ", (math.log(N)/math.log(sum(av_list)/30)))
    # Display the social network 
    nx.draw(g, pos, with_labels=1)
    plt.show()
    

graph()
   
###References:
###https://www.geeksforgeeks.org/implementation-of-erdos-renyi-model-on-social-networks/ 
###https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cluster.average_clustering.html

