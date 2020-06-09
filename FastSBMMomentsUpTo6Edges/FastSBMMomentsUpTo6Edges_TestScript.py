import numpy as np
from scipy.linalg import get_blas_funcs
from igraph import *
import csv
import matplotlib.pyplot as plt
import itertools as itertools
from FastSBMMomentsUpTo6Edges_Functions import *
flatten = lambda l: [item for sublist in l for item in sublist]

##################################################################################
### Quickly obtaining the moments and gradients of a SBM with many communities ###
##################################################################################
#
# - Currently assumes nodes are assigned iid uniform to the communities (uniform piVec)
# - Currently hardcoded for all graph moments with at most 6 edges
# - The 113 subgraphs are in a canonical order (indexed 0,...,112),
#     - up to third order, they are:
#			0: Edge
#			1: Wedge (or cherry)
#			2: Edge+Edge
#			3: Triangle
#			4: Star with 3 edges
#			5: Path with 3 edges 
#			6: Edge+Wedge
#			7: Edge+Edge+Edge


# Use the functions below to see each subgraph or ask the index of a subgraph
print_subgraph(8) #If you have the index and want to see the subgraph
subgraph24 = index_to_subgraph(24) #If you want the igraph object instead
print(subgraph_to_index(subgraph24)==24) #If you have the igraph object for a subgraph 
										 #and want to know its subgraph index


# Generating a random SBM
numBlocks = 16 #The method is quite fast, can easily handle ~128 communities
np.random.seed(257)
bMat = np.random.random(size=(numBlocks,numBlocks))
bMat = (bMat+bMat.T)/2 # Clearly, it only works for symmetric bMat

print("Getting the moments of an SBM")
start = time.time()
momentsOfSBM = bmat_dbmat_to_moments_dmoments(bMat)
end = time.time()
print("That took ", end - start, " seconds.")
print("Moments: ",momentsOfSBM)


print("Getting the gradient of the moments of an SBM")
start = time.time()
momentsOfSBM, dMomentsOfSBM = bmat_dbmat_to_moments_dmoments(bMat,getGradient=True)
end = time.time()
print("That took ", end - start, " seconds.")
print("Moments: ",momentsOfSBM)
print("Gradient of moments: ",dMomentsOfSBM)


print("Testing the gradient of the moments of an SBM")
dbMat = np.random.normal(size=(numBlocks,numBlocks))
dbMat = (dbMat+dbMat.T)/2 #Again, only for symmetric perturbations
dbMatFlat = np.array(flatten(dbMat)) #Need to flatten the perturbation
directionalDerivative = dbMatFlat @ dMomentsOfSBM #And dot (flattened dbMat)dot(gradient of SBM)
print("Directional derivative: ",directionalDerivative) #Limit of (mu(bMat + eps*dbMat)-mu(bMat))/eps as eps->0


# Demonstrating convergence of the gradient 
epsilonList = [10**-i for i in range(3,7)] 
errorList = []
for epsilon in epsilonList:
	bMatPert = bMat + epsilon*dbMat
	momentsOfSBMPert = bmat_dbmat_to_moments_dmoments(bMatPert)
	approximateDirectionalDerivative = (momentsOfSBMPert - momentsOfSBM)/epsilon
	error = np.abs(approximateDirectionalDerivative - directionalDerivative)
	print("Error in approximate derivative: ",np.linalg.norm(error))
	errorList.append(error)
errorList = np.array(errorList)
print("Error convergence:")
for moment in range(1,113): #The edge density is exact, so screws up the log plot
	plt.loglog(epsilonList,errorList[:,moment])
plt.show()


