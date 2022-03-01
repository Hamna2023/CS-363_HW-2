
from cProfile import label
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
    return g
    # Display 
    # nx.draw(g, pos, with_labels=1)
    # plt.show()
   
# Distribution graph for Erdos_Renyi model
def distribution_graph(g,x):
    all_node_degree = list(dict((nx.degree(g))).values())
    unique_degree = list(set(all_node_degree))
    unique_degree.sort()
    nodes_with_degree = []
    for i in unique_degree:
        nodes_with_degree.append(all_node_degree.count(i))

    plt.plot(unique_degree, nodes_with_degree,label=x)  #x represents G(n,p) pair
    plt.xlabel("Degrees")
    plt.ylabel("No. of nodes")
    plt.title("Degree distribution")
    

def main():
    for x in range(3):
        distribution_graph(graph(),x)
    plt.show()


main()