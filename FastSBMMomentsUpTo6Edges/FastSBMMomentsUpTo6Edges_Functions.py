import numpy as np
from scipy.linalg import get_blas_funcs
from igraph import *
import csv
import time as time
import matplotlib.pyplot as plt
import IPython.display as display
import itertools as itertools
flatten = lambda l: [item for sublist in l for item in sublist]

# Edge list of all subgraphs with at most 6 edges
subgraphEdgeListUpTo6 = np.load('SubgraphEdgelistUpTo6.npy', allow_pickle=True)
# The same list as igraph objects
subgraphListUpTo6 = [Graph(subgraphEdgeListUpTo6[i]) for i in range(len(subgraphEdgeListUpTo6))]

# Functions for printing graphs
def print_graph(gIn):
	plotTemp = plot(gIn,vertex_color=[0,0,0])
	display.clear_output(wait=True)
	display.display(plotTemp)
	plt.gcf().clear()
def print_subgraph(indexIn):
	print_graph(subgraphListUpTo6[indexIn])

# Functions for converting from igraph object to subgraph index
def subgraph_to_index(gIn):
	for i in range(len(subgraphListUpTo6)):
		if gIn.isomorphic(subgraphListUpTo6[i]): return i
	print("DON'T HAVE THIS SUBGRAPH (yet)")
	return -1
def index_to_subgraph(indexIn):
	return subgraphListUpTo6[indexIn]


# Makes four matrices, all k-by-k^2, where 1,...,k are the communities of the SBM
# The columns are indexed by the ordered pairs of communities ((1,1),(1,2),...,(2,1),(2,2),...,(k,k-1),(k,k))
# The i (indicating) matrices are binary,
#	with entries equal to 1 if the row matches the first(second) community in the pair (for i0 and i1, respectively)
# The w (weighted) matrices have entries in the same spots,
#	but are weighted by the entry in the SBM matrix given by the pair
def make_i0_i1_b0_b1_from_bMat(bMatIn):
	kTemp = len(bMatIn)
	indexPairs = flatten([[[i,j] for j in range(kTemp)] for i in range(kTemp)])
	i0Out = np.zeros((len(bMatIn),len(indexPairs)))
	i1Out = np.zeros((len(bMatIn),len(indexPairs)))
	w0Out = np.zeros((len(bMatIn),len(indexPairs)))
	w1Out = np.zeros((len(bMatIn),len(indexPairs)))
	for index,pair in enumerate(indexPairs):
		i0Out[pair[0],index] = 1
		i1Out[pair[1],index] = 1
		w0Out[pair[0],index] = bMatIn[pair[0],pair[1]]
		w1Out[pair[1],index] = bMatIn[pair[1],pair[0]]
	return i0Out, i1Out, w0Out, w1Out

# Gets the moments of connected subgraphs for an SBM
# Assumes uniform piVec, i.e., nodes are assigned uniform iid to the communities
def fast_connected_moments_of_sbm(bMatIn,getGradient=False):
	connectedNum = 52
	k = len(bMatIn)
	bMatFlat = np.array(flatten(bMatIn))
	bMatFlatRect = np.array([bMatFlat for _ in range(k)])

	gemmAdjMultiply = get_blas_funcs("gemm", [bMatIn,bMatIn])
	if getGradient:
		def m(matIn0,matIn1):
			return np.array([gemmAdjMultiply(1,matIn0[0],matIn1[0]),\
							gemmAdjMultiply(1,matIn0[0],matIn1[1])+gemmAdjMultiply(1,matIn0[1],matIn1[0])])#/k
		def h(matIn0,matIn1):
			return np.array([matIn0[0]*matIn1[0],matIn0[0]*matIn1[1]+matIn0[1]*matIn1[0]])#/k
		def t(matIn):
			return np.array([matIn[0].T,matIn[1].T])#/k
		def s(matIn):
			return np.array([np.diag(np.sum(matIn[0],axis=1)),np.diag(np.sum(matIn[1],axis=1))])#/k
		def fs(matIn):
			return np.array([np.sum(matIn[0]),np.sum(matIn[1])])
	else:
		def m(matIn0,matIn1):
			return gemmAdjMultiply(1,matIn0,matIn1)
		def h(matIn0,matIn1):
			return matIn0*matIn1
		def t(matIn):
			return matIn.T
		def s(matIn):
			return np.diag(np.sum(matIn,axis=1))
		def fs(matIn):
			return np.sum(matIn)

	if getGradient:
		numPerturbations = k**2
		dMomOut = np.zeros((k**2,connectedNum))
	else:
		numPerturbations = 1
	for perturbationIndex in range(numPerturbations):
		if getGradient:
			epsilonMat = np.zeros((k,k))
			epsilonMat[int(perturbationIndex/k),perturbationIndex%k] = 1
			aEdge01 = np.array([bMatIn,epsilonMat])
		else:
			aEdge01 = bMatIn
		aEdge00 = s(aEdge01)
		if getGradient:
			i0Mat,i1Mat,wEdge0x01,wEdge0x10 = make_i0_i1_b0_b1_from_bMat(bMatIn) ###FIX
			i0MatEps,i1MatEps,wEdge0x01Eps,wEdge0x10Eps = make_i0_i1_b0_b1_from_bMat(epsilonMat) ###FIX
			i0Mat = np.array([i0Mat,0*i0MatEps])
			i1Mat = np.array([i1Mat,0*i1MatEps])
			wEdge0x01 = np.array([wEdge0x01,wEdge0x01Eps])
			wEdge0x10 = np.array([wEdge0x10,wEdge0x10Eps])
		else:
			i0Mat,i1Mat,wEdge0x01,wEdge0x10 = make_i0_i1_b0_b1_from_bMat(bMatIn) ###FIX

		aWedge00 = h(aEdge00,aEdge00)
		aWedge01 = m(aEdge00,aEdge01)
		aWedge12 = m(aEdge01,aEdge01)
		aWedge11 = s(aWedge12)
		aWedge1x02 = m(aEdge01,wEdge0x01)
		aWedge0x12 = h(m(aEdge01,i0Mat),m(aEdge01,i1Mat))

		aTriangle01 = h(aWedge12,aEdge01)
		aTriangle00 = s(aTriangle01)
		aTriangle0x12 = h(aWedge1x02,m(aEdge01,i1Mat))
		aClaw00 = h(aWedge00,aEdge00)
		aClaw01 = m(aWedge00,aEdge01)
		aClaw12 = m(aEdge01,aWedge01)
		aClaw11 = s(aClaw12)
		aThreeline23 = m(aWedge12,aEdge01)
		aThreeline22 = s(aThreeline23)
		aThreeline01 = m(aWedge01,aEdge00)
		aThreeline00 = s(aThreeline01)

		aTriangleEdge00 = h(aTriangle00,aEdge00)
		aTriangleEdge01 = m(aEdge00,aTriangle01)
		aTriangleEdge12 = h(aClaw12,aEdge01)
		aTriangleEdge13 = m(aTriangle01,aEdge01)
		aSquare01 = h(aThreeline23,aEdge01)
		aSquare00 = s(aSquare01)
		aSquare02 = h(aWedge12,aWedge12)
		aCross00 = h(aClaw00,aEdge00)
		aCross01 = m(aClaw00,aEdge01)
		aClawEdge04 = m(aWedge00,aWedge12)
		aFourline34 = m(aThreeline23,aEdge01)
		aFourline00 = h(aWedge11,aWedge11)

		aBipyramid01 = h(aTriangle01,aWedge12)
		aBipyramid23 = m(aTriangle0x12,t(aWedge0x12))
		aBipyramid02 = h(aTriangleEdge13,aEdge01)
		aTriangleEdgeEdgeSame00 = h(aTriangleEdge00,aEdge00)
		aTriangleEdgeEdgeDifferent01 = m(aTriangleEdge01,aEdge00)
		aTriangleTwoline04 = m(aTriangle00,aWedge12)
		aSquareEdge00 = h(aSquare00,aEdge00)
		aSquareEdge01 = m(aEdge00,aSquare01)
		aSquareEdge04 = m(aEdge00,aSquare02)
		aFivecycle01 = h(aFourline34,aEdge01)
		aFivestar00 = h(aCross00,aEdge00)
		aCrossEdge05 = m(aCross01,aEdge01)
		aClawEdgeEdgeSame01 = m(aClaw01,aWedge00)
		aFourlineCenteredge00 = h(aFourline00,aEdge00)
		aClawTwoline05 = m(aClawEdge04,aEdge01)
		aFiveline45 = m(aFourline34,aEdge01)

		a6Kfour01 = h(aBipyramid23,aEdge01)
		a6BipyramidEdgeHighDegree01 = m(aEdge00,aBipyramid01)
		a6Butterfly00 = h(aTriangle00,aTriangle00)
		a6BipyramidEdgeLowDegree04 = m(aEdge00,aBipyramid23)
		a6House01 = h(aSquare01,aWedge12)
		a6Ktwothree01 = h(aSquare02,aWedge12)
		a6TriangleEdgeEdgeEdgeSame00 = h(aTriangleEdgeEdgeSame00,aEdge00)
		a6BullWithEarring01 = m(aEdge00,aTriangleEdgeEdgeDifferent01)
		a6TriangleEdgeTwolineSame00 = h(aTriangleEdge00,aWedge11)
		a6SquareEdgeEdgeSame00 = h(aSquareEdge00,aEdge00)
		a6TriangleEdgeEdgeEdgeDifferent01 = m(m(aEdge00,aTriangleEdge12),aEdge00)
		a6TriangleEdgeTwolineDifferent01 = m(m(aWedge11,aTriangle01),aEdge00)
		a6TriangleClaw03 = m(aTriangle00,t(aClaw01))
		a6SquareEdgeEdgeDifferentOne01 = m(aSquareEdge01,aEdge00)
		a6SquareEdgeEdgeDifferentTwo04 = m(aSquareEdge04,aEdge00)
		a6TriangleThreeline00 = h(aTriangle00,aThreeline22)
		a6SquareTwoline00 = h(aSquare00,aWedge11)
		a6FivecycleEdge01 = m(aEdge00,aFivecycle01)
		a6Sixcycle01 = h(aFiveline45,aEdge01)
		a6Sixstar00 = h(aFivestar00,aEdge00)
		a6FivestarEdge00 = h(aCross00,aWedge11)
		a6CrossEdgeEdgeSame01 = m(aClaw00,t(aClaw12))
		a6CrossEdgeEdgeDifferent00 = h(aWedge00,aFourline00)
		a6CrossTwoline00 = h(aClaw00,aThreeline22)
		a6ClawEdgeTwolineSame00 = h(aClaw11,aThreeline00)
		a6ClawClaw00 = h(aClaw11,aClaw11)
		a6ClawEdgeEdgeEdgeDifferent00 = h(aFourline00,aWedge11)
		a6ClawEdgeTwolineDifferent00 = h(aThreeline00,aThreeline22)
		a6ClawThreeline01 = m(aClaw01,aThreeline22)
		a6Sixline56 = m(aFiveline45,aEdge01)

		if getGradient:
			momOut = np.zeros((connectedNum,2))
		else:
			momOut = np.zeros(connectedNum)

		momOut[0] = fs(aEdge00)/(k**2)

		momOut[1] = fs(aWedge00)/(k**3)

		momOut[2] = fs(aTriangle00)/(k**3)
		momOut[3] = fs(aClaw00)/(k**4)
		momOut[4] = fs(aThreeline23)/(k**4)

		momOut[5] = fs(aTriangleEdge00)/(k**4)
		momOut[6] = fs(aSquare01)/(k**4)
		momOut[7] = fs(aCross00)/(k**5)
		momOut[8] = fs(aClawEdge04)/(k**5)
		momOut[9] = fs(aFourline34)/(k**5)

		momOut[10] = fs(aBipyramid01)/(k**4)
		momOut[11] = fs(aTriangleEdgeEdgeSame00)/(k**5)
		momOut[12] = fs(aTriangleEdgeEdgeDifferent01)/(k**5)
		momOut[13] = fs(aTriangleTwoline04)/(k**5)
		momOut[14] = fs(aSquareEdge00)/(k**5)
		momOut[15] = fs(aFivecycle01)/(k**5)
		momOut[16] = fs(aFivestar00)/(k**6)
		momOut[17] = fs(aCrossEdge05)/(k**6)
		momOut[18] = fs(aClawEdgeEdgeSame01)/(k**6)
		momOut[19] = fs(aFourlineCenteredge00)/(k**6)
		momOut[20] = fs(aClawTwoline05)/(k**6)
		momOut[21] = fs(aFiveline45)/(k**6)

		momOut[22] = fs(a6Kfour01)/(k**4)
		momOut[23] = fs(a6BipyramidEdgeHighDegree01)/(k**5)
		momOut[24] = fs(a6Butterfly00)/(k**5)
		momOut[25] = fs(a6BipyramidEdgeLowDegree04)/(k**5)
		momOut[26] = fs(a6House01)/(k**5)
		momOut[27] = fs(a6Ktwothree01)/(k**5)
		momOut[28] = fs(a6TriangleEdgeEdgeEdgeSame00)/(k**6)
		momOut[29] = fs(a6BullWithEarring01)/(k**6)
		momOut[30] = fs(a6TriangleEdgeTwolineSame00)/(k**6)
		momOut[31] = fs(a6SquareEdgeEdgeSame00)/(k**6)
		momOut[32] = fs(a6TriangleEdgeEdgeEdgeDifferent01)/(k**6)
		momOut[33] = fs(a6TriangleEdgeTwolineDifferent01)/(k**6)
		momOut[34] = fs(a6TriangleClaw03)/(k**6)
		momOut[35] = fs(a6SquareEdgeEdgeDifferentOne01)/(k**6)
		momOut[36] = fs(a6SquareEdgeEdgeDifferentTwo04)/(k**6)
		momOut[37] = fs(a6TriangleThreeline00)/(k**6)
		momOut[38] = fs(a6SquareTwoline00)/(k**6)
		momOut[39] = fs(a6FivecycleEdge01)/(k**6)
		momOut[40] = fs(a6Sixcycle01)/(k**6)
		momOut[41] = fs(a6Sixstar00)/(k**7)
		momOut[42] = fs(a6FivestarEdge00)/(k**7)
		momOut[43] = fs(a6CrossEdgeEdgeSame01)/(k**7)
		momOut[44] = fs(a6CrossEdgeEdgeDifferent00)/(k**7)
		momOut[45] = fs(a6CrossTwoline00)/(k**7)
		momOut[46] = fs(a6ClawEdgeTwolineSame00)/(k**7)
		momOut[47] = fs(a6ClawClaw00)/(k**7)
		momOut[48] = fs(a6ClawEdgeEdgeEdgeDifferent00)/(k**7)
		momOut[49] = fs(a6ClawEdgeTwolineDifferent00)/(k**7)
		momOut[50] = fs(a6ClawThreeline01)/(k**7)
		momOut[51] = fs(a6Sixline56)/(k**7)

		if getGradient:
			dMomOut[perturbationIndex,:] = momOut[:,1]

	if getGradient:
		return np.array(momOut[:,0]), np.array(dMomOut)
	else:
		return np.array(momOut)



def connected_to_all_moments_sbm(momIn):
	momOut = np.zeros(113)
	momOut[0] = momIn[0]
	momOut[1] = momIn[1]
	momOut[2] = momOut[0]**2
	momOut[3] = momIn[2]
	momOut[4] = momIn[3]
	momOut[5] = momIn[4]
	momOut[6] = momOut[0]*momOut[1]
	momOut[7] = momOut[0]**3
	momOut[8] = momIn[5]
	momOut[9] = momIn[6]
	momOut[10] = momIn[7]
	momOut[11] = momIn[8]
	momOut[12] = momIn[9]
	momOut[13] = momOut[0]*momOut[3]
	momOut[14] = momOut[0]*momOut[4]
	momOut[15] = momOut[0]*momOut[5]
	momOut[16] = momOut[1]**2
	momOut[17] = momOut[0]**2*momOut[1]
	momOut[18] = momOut[0]**4
	momOut[19] = momIn[10]
	momOut[20] = momIn[11]
	momOut[21] = momIn[12]
	momOut[22] = momIn[13]
	momOut[23] = momIn[14]
	momOut[24] = momIn[15]
	momOut[25] = momIn[16]
	momOut[26] = momIn[17]
	momOut[27] = momIn[18]
	momOut[28] = momIn[19]
	momOut[29] = momIn[20]
	momOut[30] = momIn[21]
	momOut[31] = momOut[0]*momOut[8]
	momOut[32] = momOut[1]*momOut[3]
	momOut[33] = momOut[0]*momOut[9]
	momOut[34] = momOut[0]*momOut[10]
	momOut[35] = momOut[0]*momOut[11]
	momOut[36] = momOut[1]*momOut[4]
	momOut[37] = momOut[0]*momOut[12]
	momOut[38] = momOut[1]*momOut[5]
	momOut[39] = momOut[0]**2*momOut[3]
	momOut[40] = momOut[0]**2*momOut[4]
	momOut[41] = momOut[0]**2*momOut[5]
	momOut[42] = momOut[0]*momOut[1]**2
	momOut[43] = momOut[0]**3*momOut[1]
	momOut[44] = momOut[0]**5
	momOut[45] = momIn[22]
	momOut[46] = momIn[23]
	momOut[47] = momIn[24]
	momOut[48] = momIn[25]
	momOut[49] = momIn[26]
	momOut[50] = momIn[27]
	momOut[51] = momIn[28]
	momOut[52] = momIn[29]
	momOut[53] = momIn[30]
	momOut[54] = momIn[31]
	momOut[55] = momIn[32]
	momOut[56] = momIn[33]
	momOut[57] = momIn[34]
	momOut[58] = momIn[35]
	momOut[59] = momIn[36]
	momOut[60] = momIn[37]
	momOut[61] = momIn[38]
	momOut[62] = momIn[39]
	momOut[63] = momIn[40]
	momOut[64] = momIn[41]
	momOut[65] = momIn[42]
	momOut[66] = momIn[43]
	momOut[67] = momIn[44]
	momOut[68] = momIn[45]
	momOut[69] = momIn[46]
	momOut[70] = momIn[47]
	momOut[71] = momIn[48]
	momOut[72] = momIn[49]
	momOut[73] = momIn[50]
	momOut[74] = momIn[51]
	momOut[75] = momOut[0]*momOut[19]
	momOut[76] = momOut[3]**2
	momOut[77] = momOut[0]*momOut[20]
	momOut[78] = momOut[0]*momOut[21]
	momOut[79] = momOut[0]*momOut[22]
	momOut[80] = momOut[1]*momOut[8]
	momOut[81] = momOut[3]*momOut[4]
	momOut[82] = momOut[0]*momOut[23]
	momOut[83] = momOut[3]*momOut[5]
	momOut[84] = momOut[1]*momOut[9]
	momOut[85] = momOut[0]*momOut[24]
	momOut[86] = momOut[0]*momOut[25]
	momOut[87] = momOut[0]*momOut[26]
	momOut[88] = momOut[1]*momOut[10]
	momOut[89] = momOut[0]*momOut[27]
	momOut[90] = momOut[4]**2
	momOut[91] = momOut[0]*momOut[28]
	momOut[92] = momOut[0]*momOut[29]
	momOut[93] = momOut[1]*momOut[11]
	momOut[94] = momOut[4]*momOut[5]
	momOut[95] = momOut[0]*momOut[30]
	momOut[96] = momOut[1]*momOut[12]
	momOut[97] = momOut[5]**2
	momOut[98] = momOut[0]**2*momOut[8]
	momOut[99] = momOut[0]*momOut[1]*momOut[3]
	momOut[100] = momOut[0]**2*momOut[9]
	momOut[101] = momOut[0]**2*momOut[10]
	momOut[102] = momOut[0]**2*momOut[11]
	momOut[103] = momOut[0]*momOut[1]*momOut[4]
	momOut[104] = momOut[0]**2*momOut[12]
	momOut[105] = momOut[0]*momOut[1]*momOut[5]
	momOut[106] = momOut[1]**3
	momOut[107] = momOut[0]**3*momOut[4]
	momOut[108] = momOut[0]**3*momOut[5]
	momOut[109] = momOut[0]**2*momOut[1]**2
	momOut[110] = momOut[0]**3*momOut[3]
	momOut[111] = momOut[0]**4*momOut[1]
	momOut[112] = momOut[0]**6
	return momOut

# From the connected moments gets all moments
def connected_to_all_dmoments_sbm(momIn,dMomIn):
	dMomOut = np.zeros(113)
	dMomOut[0] = dMomIn[0]
	dMomOut[1] = dMomIn[1]
	dMomOut[2] = dMomIn[0]*momIn[0] + dMomIn[0]*momIn[0]
	dMomOut[3] = dMomIn[2]
	dMomOut[4] = dMomIn[3]
	dMomOut[5] = dMomIn[4]
	dMomOut[6] = dMomIn[1]*momIn[0] + dMomIn[0]*momIn[1]
	dMomOut[7] = dMomIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]
	dMomOut[8] = dMomIn[5]
	dMomOut[9] = dMomIn[6]
	dMomOut[10] = dMomIn[7]
	dMomOut[11] = dMomIn[8]
	dMomOut[12] = dMomIn[9]
	dMomOut[13] = dMomIn[2]*momIn[0] + dMomIn[0]*momIn[2]
	dMomOut[14] = dMomIn[3]*momIn[0] + dMomIn[0]*momIn[3]
	dMomOut[15] = dMomIn[4]*momIn[0] + dMomIn[0]*momIn[4]
	dMomOut[16] = dMomIn[1]*momIn[1] + dMomIn[1]*momIn[1]
	dMomOut[17] = dMomIn[1]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0]
	dMomOut[18] = dMomIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]
	dMomOut[19] = dMomIn[10]
	dMomOut[20] = dMomIn[11]
	dMomOut[21] = dMomIn[12]
	dMomOut[22] = dMomIn[13]
	dMomOut[23] = dMomIn[14]
	dMomOut[24] = dMomIn[15]
	dMomOut[25] = dMomIn[16]
	dMomOut[26] = dMomIn[17]
	dMomOut[27] = dMomIn[18]
	dMomOut[28] = dMomIn[19]
	dMomOut[29] = dMomIn[20]
	dMomOut[30] = dMomIn[21]
	dMomOut[31] = dMomIn[5]*momIn[0] + dMomIn[0]*momIn[5]
	dMomOut[32] = dMomIn[2]*momIn[1] + dMomIn[1]*momIn[2]
	dMomOut[33] = dMomIn[6]*momIn[0] + dMomIn[0]*momIn[6]
	dMomOut[34] = dMomIn[7]*momIn[0] + dMomIn[0]*momIn[7]
	dMomOut[35] = dMomIn[8]*momIn[0] + dMomIn[0]*momIn[8]
	dMomOut[36] = dMomIn[3]*momIn[1] + dMomIn[1]*momIn[3]
	dMomOut[37] = dMomIn[9]*momIn[0] + dMomIn[0]*momIn[9]
	dMomOut[38] = dMomIn[4]*momIn[1] + dMomIn[1]*momIn[4]
	dMomOut[39] = dMomIn[2]*momIn[0]*momIn[0] + dMomIn[0]*momIn[2]*momIn[0] + dMomIn[0]*momIn[2]*momIn[0]
	dMomOut[40] = dMomIn[3]*momIn[0]*momIn[0] + dMomIn[0]*momIn[3]*momIn[0] + dMomIn[0]*momIn[3]*momIn[0]
	dMomOut[41] = dMomIn[4]*momIn[0]*momIn[0] + dMomIn[0]*momIn[4]*momIn[0] + dMomIn[0]*momIn[4]*momIn[0]
	dMomOut[42] = dMomIn[1]*momIn[1]*momIn[0] + dMomIn[1]*momIn[1]*momIn[0] + dMomIn[0]*momIn[1]*momIn[1]
	dMomOut[43] = dMomIn[1]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0]*momIn[0]
	dMomOut[44] = dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0]
	dMomOut[45] = dMomIn[22]
	dMomOut[46] = dMomIn[23]
	dMomOut[47] = dMomIn[24]
	dMomOut[48] = dMomIn[25]
	dMomOut[49] = dMomIn[26]
	dMomOut[50] = dMomIn[27]
	dMomOut[51] = dMomIn[28]
	dMomOut[52] = dMomIn[29]
	dMomOut[53] = dMomIn[30]
	dMomOut[54] = dMomIn[31]
	dMomOut[55] = dMomIn[32]
	dMomOut[56] = dMomIn[33]
	dMomOut[57] = dMomIn[34]
	dMomOut[58] = dMomIn[35]
	dMomOut[59] = dMomIn[36]
	dMomOut[60] = dMomIn[37]
	dMomOut[61] = dMomIn[38]
	dMomOut[62] = dMomIn[39]
	dMomOut[63] = dMomIn[40]
	dMomOut[64] = dMomIn[41]
	dMomOut[65] = dMomIn[42]
	dMomOut[66] = dMomIn[43]
	dMomOut[67] = dMomIn[44]
	dMomOut[68] = dMomIn[45]
	dMomOut[69] = dMomIn[46]
	dMomOut[70] = dMomIn[47]
	dMomOut[71] = dMomIn[48]
	dMomOut[72] = dMomIn[49]
	dMomOut[73] = dMomIn[50]
	dMomOut[74] = dMomIn[51]
	dMomOut[75] = dMomIn[10]*momIn[0] + dMomIn[0]*momIn[10]
	dMomOut[76] = dMomIn[2]*momIn[2] + dMomIn[2]*momIn[2]
	dMomOut[77] = dMomIn[11]*momIn[0] + dMomIn[0]*momIn[11]
	dMomOut[78] = dMomIn[12]*momIn[0] + dMomIn[0]*momIn[12]
	dMomOut[79] = dMomIn[13]*momIn[0] + dMomIn[0]*momIn[13]
	dMomOut[80] = dMomIn[5]*momIn[1] + dMomIn[1]*momIn[5]
	dMomOut[81] = dMomIn[3]*momIn[2] + dMomIn[2]*momIn[3]
	dMomOut[82] = dMomIn[14]*momIn[0] + dMomIn[0]*momIn[14]
	dMomOut[83] = dMomIn[4]*momIn[2] + dMomIn[2]*momIn[4]
	dMomOut[84] = dMomIn[6]*momIn[1] + dMomIn[1]*momIn[6]
	dMomOut[85] = dMomIn[15]*momIn[0] + dMomIn[0]*momIn[15]
	dMomOut[86] = dMomIn[16]*momIn[0] + dMomIn[0]*momIn[16]
	dMomOut[87] = dMomIn[17]*momIn[0] + dMomIn[0]*momIn[17]
	dMomOut[88] = dMomIn[7]*momIn[1] + dMomIn[1]*momIn[7]
	dMomOut[89] = dMomIn[18]*momIn[0] + dMomIn[0]*momIn[18]
	dMomOut[90] = dMomIn[3]*momIn[3] + dMomIn[3]*momIn[3]
	dMomOut[91] = dMomIn[19]*momIn[0] + dMomIn[0]*momIn[19]
	dMomOut[92] = dMomIn[20]*momIn[0] + dMomIn[0]*momIn[20]
	dMomOut[93] = dMomIn[8]*momIn[1] + dMomIn[1]*momIn[8]
	dMomOut[94] = dMomIn[3]*momIn[4] + dMomIn[4]*momIn[3]
	dMomOut[95] = dMomIn[21]*momIn[0] + dMomIn[0]*momIn[21]
	dMomOut[96] = dMomIn[9]*momIn[1] + dMomIn[1]*momIn[9]
	dMomOut[97] = dMomIn[4]*momIn[4] + dMomIn[4]*momIn[4]
	dMomOut[98] = dMomIn[5]*momIn[0]*momIn[0] + dMomIn[0]*momIn[5]*momIn[0] + dMomIn[0]*momIn[5]*momIn[0]
	dMomOut[99] = dMomIn[2]*momIn[1]*momIn[0] + dMomIn[1]*momIn[2]*momIn[0] + dMomIn[0]*momIn[2]*momIn[1]
	dMomOut[100] = dMomIn[6]*momIn[0]*momIn[0] + dMomIn[0]*momIn[6]*momIn[0] + dMomIn[0]*momIn[6]*momIn[0]
	dMomOut[101] = dMomIn[7]*momIn[0]*momIn[0] + dMomIn[0]*momIn[7]*momIn[0] + dMomIn[0]*momIn[7]*momIn[0]
	dMomOut[102] = dMomIn[8]*momIn[0]*momIn[0] + dMomIn[0]*momIn[8]*momIn[0] + dMomIn[0]*momIn[8]*momIn[0]
	dMomOut[103] = dMomIn[3]*momIn[1]*momIn[0] + dMomIn[1]*momIn[3]*momIn[0] + dMomIn[0]*momIn[3]*momIn[1]
	dMomOut[104] = dMomIn[9]*momIn[0]*momIn[0] + dMomIn[0]*momIn[9]*momIn[0] + dMomIn[0]*momIn[9]*momIn[0]
	dMomOut[105] = dMomIn[4]*momIn[1]*momIn[0] + dMomIn[1]*momIn[4]*momIn[0] + dMomIn[0]*momIn[4]*momIn[1]
	dMomOut[106] = dMomIn[1]*momIn[1]*momIn[1] + dMomIn[1]*momIn[1]*momIn[1] + dMomIn[1]*momIn[1]*momIn[1]
	dMomOut[107] = dMomIn[3]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[3]*momIn[0]*momIn[0] + dMomIn[0]*momIn[3]*momIn[0]*momIn[0] + dMomIn[0]*momIn[3]*momIn[0]*momIn[0]
	dMomOut[108] = dMomIn[4]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[4]*momIn[0]*momIn[0] + dMomIn[0]*momIn[4]*momIn[0]*momIn[0] + dMomIn[0]*momIn[4]*momIn[0]*momIn[0]
	dMomOut[109] = dMomIn[1]*momIn[1]*momIn[0]*momIn[0] + dMomIn[1]*momIn[1]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[1]*momIn[0] + dMomIn[0]*momIn[1]*momIn[1]*momIn[0]
	dMomOut[110] = dMomIn[2]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[2]*momIn[0]*momIn[0] + dMomIn[0]*momIn[2]*momIn[0]*momIn[0] + dMomIn[0]*momIn[2]*momIn[0]*momIn[0]
	dMomOut[111] = dMomIn[1]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[1]*momIn[0]*momIn[0]*momIn[0]
	dMomOut[112] = dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0] + dMomIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0]*momIn[0]
	return dMomOut


# Ties a neat little bow on the whole thing! :) 
def bmat_dbmat_to_moments_dmoments(bMatIn,getGradient=False):
	if getGradient==False:
		connectedMoments = fast_connected_moments_of_sbm(bMatIn)
		allMoments = connected_to_all_moments_sbm(connectedMoments)
		return allMoments
	else:
		connectedMoments, dconnectedMoments = fast_connected_moments_of_sbm(bMatIn,getGradient=True)
		allMoments = connected_to_all_moments_sbm(connectedMoments)
		allDMoments = [connected_to_all_dmoments_sbm(connectedMoments,dconnectedMoments[index]) \
		for index in range(len(dconnectedMoments))]
		return allMoments, allDMoments


