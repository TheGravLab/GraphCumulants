import numpy as np
def moments_to_unbiased_cumulants(momIn):
	numMom = len(momIn)
	if numMom==1:
		orderTemp = 1
		cumOut = np.zeros(1)
	elif numMom==3:
		orderTemp = 2
		cumOut = np.zeros(3)
	elif numMom==8:
		orderTemp = 3
		cumOut = np.zeros(8)
	else:
		print("ERROR IN moments_to_unbiased_cumulants")
	if orderTemp>=1:
		cumOut[0] = momIn[0]
	if orderTemp>=2:
		cumOut[1] = momIn[1] - momIn[2]
		cumOut[2] = 0
	if orderTemp>=3:
		cumOut[3] = momIn[3] - 3*momIn[6] + 2*momIn[7]
		cumOut[4] = momIn[4] - 3*momIn[6] + 2*momIn[7]
		cumOut[5] = momIn[5] - 2*momIn[6] + momIn[7]
		cumOut[6] = 0
		cumOut[7] = 0
	return cumOut