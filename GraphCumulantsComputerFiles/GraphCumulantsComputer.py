import numpy as np
import scipy.special as spspec
import itertools
import matplotlib.pyplot as plt
import csv
import sys
import time
from datetime import datetime
import IPython.display as display
from igraph import *
import GraphCumulantsComputerFiles
flatten = lambda l: [item for sublist in l for item in sublist]
def chunks(l, n):
	n = max(1, n)
	return [l[i:i+n] for i in range(0, len(l), n)]
def falling_factorial(n,p):
	return 1.0/spspec.poch(n+1,-p)



class GraphCumulantsComputer():

	def __init__(self,orderIn):
		self.orderMain = orderIn

		if self.orderMain<=8:

			self.ConnectedToAllCounts = __import__('GraphCumulantsComputerFiles.ConnectedToAllCountsFunctionUpToOrder'+str(self.orderMain).zfill(6), \
				globals=None, locals=None, fromlist=('connected_to_disconnected_counts'), level=0)
			self.MomentsToCumulants = __import__('GraphCumulantsComputerFiles.MomentsToCumulantsFunctionUpToOrder'+str(self.orderMain).zfill(6), \
				globals=None, locals=None, fromlist=('moments_to_cumulants'), level=0)
			self.MomentsToUnbiasedCumulants = __import__('GraphCumulantsComputerFiles.UnbiasedCumulantFunctionUpToOrder'+str(self.orderMain).zfill(6), \
				globals=None, locals=None, fromlist=('moments_to_unbiased_cumulants'), level=0)
			self.CumulantsToMoments = __import__('GraphCumulantsComputerFiles.CumulantsToMomentsFunctionUpToOrder'+str(self.orderMain).zfill(6), \
				globals=None, locals=None, fromlist=('cumulants_to_moments'), level=0)
			self.MomentsToUnbiasedCumulantsCovariance = __import__('GraphCumulantsComputerFiles.UnbiasedCumulantCovarianceFunctionUpToOrder'+str(self.orderMain).zfill(6), \
				globals=None, locals=None, fromlist=('moments_to_unbiased_cumulants_covariance'), level=0)

			self.subgraphEdgeListByOrder = self.import_edgelist('./GraphCumulantsComputerFiles/SubgraphEdgeListSimpleOrder')
			self.subgraphNumNodesAutomorphismListByOrder = self.import_csv_int_multiple('./GraphCumulantsComputerFiles/SubgraphNodeAutomorphismListSimpleOrder')
			self.subgraphConnectedIndicesListByOrder = self.import_csv_int('./GraphCumulantsComputerFiles/SubgraphConnectedIndicesListSimpleOrder'+str(self.orderMain).zfill(6))
				# ^^^ NEED TO FIX THIS I THINK, it works fine, but it's not exactly what it claims to be - 20200426L

			self.subgraphEdgeList = flatten(self.subgraphEdgeListByOrder)
			self.subgraphNumNodesAutomorphismList = flatten(self.subgraphNumNodesAutomorphismListByOrder)
			self.subgraphConnectedIndicesList = flatten(self.subgraphConnectedIndicesListByOrder)

			self.subgraphList = [Graph(item) for item in self.subgraphEdgeList]
			self.subgraphConnectedList = [self.subgraphList[index] for index in self.subgraphConnectedIndicesList]		
			self.subgraphOrderList = [len(item) for item in self.subgraphEdgeList]
			self.subgraphConnectedOrderList = [self.subgraphOrderList[index] for index in self.subgraphConnectedIndicesList]
			self.subgraphConnectedNumUpToOrderList = np.cumsum(np.bincount(self.subgraphConnectedOrderList)[1:])
			self.subgraphConnectedNumNodesAutomorphismList = [self.subgraphNumNodesAutomorphismList[index] for index in self.subgraphConnectedIndicesList]
			self.subgraphNumUpToOrderList = np.cumsum(np.bincount(self.subgraphOrderList)[1:])
		else:
			print('ERROR: order not implemented yet')

	def import_csv_int(self,fileNameIn):
		with open(fileNameIn+'.csv') as fileIn:
			lines=fileIn.readlines()
		lineNum = 0
		outList = []
		while lineNum < len(lines):
			outList.append([int(item) for item in (lines[lineNum].split(','))])
			lineNum += 1
		return outList


	def import_csv_int_multiple(self,fileNameIn):
		dataOuter = []
		for orderI in range(self.orderMain):
			fileNameTemp = fileNameIn+str(orderI+1).zfill(6)+'.csv'
			dataInner = []
			with open(fileNameTemp) as csvFile:
				csvReader = csv.reader(csvFile, delimiter=',')
				lineCount = 0
				for row in csvReader:
					dataInner.append([int(item) for item in row])
			dataOuter.append(dataInner)
		return dataOuter


	def import_edgelist(self,fileNameIn):
		return [[chunks(innerItem,2) for innerItem in outerItem] for outerItem in self.import_csv_int_multiple(fileNameIn)]


	def print_graph(self,gIn):
		plotTemp = plot(gIn,vertex_color=[0,0,0])
		display.clear_output(wait=True)
		display.display(plotTemp)
		plt.gcf().clear()


	def print_subgraph(self,indexIn):
		self.print_graph(self.subgraphList[indexIn])


	def get_connected_subgraph_counts(self,gIn,maxOrderIn='auto'):
		if maxOrderIn=='auto':
			maxOrder = self.orderMain
		else:
			maxOrder = maxOrderIn
		numMom = self.subgraphConnectedNumUpToOrderList[maxOrder-1]
		countsListOut = [0 for _ in range(numMom)]
		for index in range(numMom):
			countsListOut[index] = gIn.count_subisomorphisms_vf2(self.subgraphConnectedList[index])/self.subgraphConnectedNumNodesAutomorphismList[index][1]
		return countsListOut


	def connected_subgraph_counts_to_all_counts(self,cIn):
		return self.ConnectedToAllCounts.connected_to_disconnected_counts(cIn)


	def get_complete_counts_list(self,nIn):
		return np.array([falling_factorial(nIn,item[0])/item[1] for item in self.subgraphNumNodesAutomorphismList])


	def counts_to_moments(self,cIn,nIn):
		return np.array(cIn)/self.get_complete_counts_list(nIn)[:len(cIn)]


	def get_graph_moments(self,gIn,maxOrderIn='auto'):
		countsConnectedTemp = self.get_connected_subgraph_counts(gIn,maxOrderIn=maxOrderIn)
		countsTemp = self.connected_subgraph_counts_to_all_counts(countsConnectedTemp)
		momentsOut = self.counts_to_moments(countsTemp,gIn.vcount())
		return momentsOut


	def distribution_moments_to_distribution_cumulants(self,momIn):
		return self.MomentsToCumulants.moments_to_cumulants(momIn)


	def graph_moments_to_graph_unbiased_cumulants(self,momIn):
		return self.MomentsToUnbiasedCumulants.moments_to_unbiased_cumulants(momIn)


	def distribution_cumulants_to_distribution_moments(self,cumIn):
		return self.CumulantsToMoments.cumulants_to_moments(cumIn)


	def distribution_moments_to_covariance_of_graph_unbiased_cumulants(self,momIn,nIn):
		return self.MomentsToUnbiasedCumulantsCovariance.moments_to_unbiased_cumulants_covariance(momIn,nIn)

