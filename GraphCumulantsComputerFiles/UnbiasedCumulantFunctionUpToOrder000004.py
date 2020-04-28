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
	elif numMom==19:
		orderTemp = 4
		cumOut = np.zeros(19)
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
	if orderTemp>=4:
		cumOut[8] = momIn[8] - momIn[13] - momIn[14] - 2*momIn[15] - 2*momIn[16] + 9*momIn[17] - 4*momIn[18]
		cumOut[9] = momIn[9] - 4*momIn[15] - 2*momIn[16] + 8*momIn[17] - 3*momIn[18]
		cumOut[10] = momIn[10] - 4*momIn[14] - 3*momIn[16] + 12*momIn[17] - 6*momIn[18]
		cumOut[11] = momIn[11] - momIn[14] - 2*momIn[15] - momIn[16] + 5*momIn[17] - 2*momIn[18]
		cumOut[12] = momIn[12] - 2*momIn[15] - momIn[16] + 3*momIn[17] - momIn[18]
		cumOut[13] = 0
		cumOut[14] = 0
		cumOut[15] = 0
		cumOut[16] = 0
		cumOut[17] = 0
		cumOut[18] = 0
	return cumOut