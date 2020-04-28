import numpy as np
from igraph import *
from GraphCumulantsComputer import GraphCumulantsComputer


# Initialize the subgraph computer object
# The input is a positive integer that denotes the maximum number of edges in a subgraph
# Currently this is implemented up to 6 edges
maxOrder = 6
computer = GraphCumulantsComputer(maxOrder)


# The GraphCumulantsComputer object uses igraph objects
numNodes = 256
averageDegree = 2
assortativity = 0.5

def sample_from_SBM(nIn,bMatIn,piVecIn):
	piVecTemp = piVecIn/np.sum(piVecIn)
	groupListTemp = np.random.choice(range(len(piVecTemp)),p=piVecTemp,size=nIn,replace=True)
	pMatTemp = np.array([[bMatIn[groupListTemp[i]][groupListTemp[j]] for j in range(nIn)] for i in range(nIn)])
	for i in range(nIn):
		for j in range(i,nIn):
			pMatTemp[i,j] = 0
	adjOut = (pMatTemp > np.random.uniform(size=np.shape(pMatTemp)))*1
	adjOut = adjOut+adjOut.T
	gOut = Graph.Adjacency(np.ndarray.tolist(adjOut),mode=ADJ_UNDIRECTED)
	return gOut

a = averageDegree*(1+assortativity)/(numNodes-1)
b = averageDegree*(1-assortativity)/(numNodes-1)
bMat = [[a,b],[b,a]]
piVec = [1/2,1/2]
graphTest = sample_from_SBM(numNodes,bMat,piVec)


# print_graph(gIn):
#     eats: an igraph object
#     returns: a plot of the graph
computer.print_graph(graphTest)

# print_subgraph(gIn):
#     eats: the index of a subgraph
#     returns: a plot of the subgraph
# for subgraphIndex in range(8):
# 	print("subgraph index ",subgraphIndex,":")
# 	computer.print_subgraph(subgraphIndex)


# get_connected_subgraph_counts(gIn):
#     eats: an igraph object
#     returns: the counts of the connected subgraphs
connectedSubgraphCounts = computer.get_connected_subgraph_counts(graphTest)


# connected_subgraph_counts_to_all_counts(cIn):
#     eats: the list of connected subgraph counts
#     returns: the list of all subgraph counts using the subgraph count "product rules"
allSubgraphCounts = computer.connected_subgraph_counts_to_all_counts(connectedSubgraphCounts)


# counts_to_moments(cIn,nIn):
#     eats: the list of all subgraph counts and the number of nodes in the graph
#     returns: the subgraph densities/graph moments
graphMoments = computer.counts_to_moments(allSubgraphCounts,numNodes)


# alternatively, get_graph_moments(gIn) does all these steps together
# get_graph_moments(gIn):
#     eats: an igraph object
#     returns: its graph moments
graphMoments = computer.get_graph_moments(graphTest)


# The combinatorial cumulants can be used on the moments of a distribution to obtain that distribution's cumulants,
#     but they yield biased estimators of these cumulants if applied to individual graphs sampled from this distribution
# distribution_moments_to_distribution_cumulants(momIn):
#     eats: a list of moments
#     returns: the cumulants as obtained by the combinatorial expressions
biasedGraphCumulants = computer.distribution_moments_to_distribution_cumulants(graphMoments)


# graph_moments_to_graph_unbiased_cumulants(momIn,nIn):
#     eats: the list of moments and the number of nodes in the graph
#     returns: the unbiased estimators of the cumulants of the underlying distribution/kernel
unbiasedGraphCumulants = computer.graph_moments_to_graph_unbiased_cumulants(graphMoments,numNodes)


# distribution_cumulants_to_distribution_moments(cumIn):
#     eats: the list of cumulants of an underlying distribution/kernel
#     returns: the list of moments of an underlying distribution/kernel
unbiasedGraphMoments = computer.distribution_cumulants_to_distribution_moments(unbiasedGraphCumulants)


# distribution_moments_to_covariance_of_graph_unbiased_cumulants(momIn,nIn):
#     eats: the list of moments of an underlying distribution/kernel
#     returns: the covariance matrix of the unbiased estimators
unbiasedGraphCumulantsCovariance = computer.distribution_moments_to_covariance_of_graph_unbiased_cumulants(unbiasedGraphMoments,\
	numNodes)



