import numpy as np
def moments_to_cumulants(momIn):
	numMom = len(momIn)
	if numMom==1:
		orderTemp = 1
		cumOut = np.zeros(1)
	else:
		print("ERROR IN moments_to_cumulants")
	if orderTemp>=1:
		cumOut[0] = momIn[0]
	return cumOut