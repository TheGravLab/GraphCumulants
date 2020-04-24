import numpy as np
def moments_to_unbiased_cumulants(momIn):
	numMom = len(momIn)
	if numMom==1:
		orderTemp = 1
		cumOut = np.zeros(1)
	elif numMom==3:
		orderTemp = 2
		cumOut = np.zeros(3)
	else:
		print("ERROR IN moments_to_unbiased_cumulants")
	if orderTemp>=1:
		cumOut[0] = momIn[0]
	if orderTemp>=2:
		cumOut[1] = momIn[1] - momIn[2]
		cumOut[2] = 0
	return cumOut