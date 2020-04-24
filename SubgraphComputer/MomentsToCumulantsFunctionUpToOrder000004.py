import numpy as np
def moments_to_cumulants(momIn):
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
		print("ERROR IN moments_to_cumulants")
	if orderTemp>=1:
		cumOut[0] = momIn[0]
	if orderTemp>=2:
		cumOut[1] = -momIn[0]**2 + momIn[1]
		cumOut[2] = -momIn[0]**2 + momIn[2]
	if orderTemp>=3:
		cumOut[3] = 2*momIn[0]**3 - 3*momIn[0]*momIn[1] + momIn[3]
		cumOut[4] = 2*momIn[0]**3 - 3*momIn[0]*momIn[1] + momIn[4]
		cumOut[5] = 2*momIn[0]**3 - 2*momIn[0]*momIn[1] - momIn[0]*momIn[2] + momIn[5]
		cumOut[6] = 2*momIn[0]**3 - momIn[0]*momIn[1] - 2*momIn[0]*momIn[2] + momIn[6]
		cumOut[7] = 2*momIn[0]**3 - 3*momIn[0]*momIn[2] + momIn[7]
	if orderTemp>=4:
		cumOut[8] = -6*momIn[0]**4 + 10*momIn[0]**2*momIn[1] - 2*momIn[1]**2 + 2*momIn[0]**2*momIn[2] - momIn[1]*momIn[2] - momIn[0]*momIn[3] - momIn[0]*momIn[4] - 2*momIn[0]*momIn[5] + momIn[8]
		cumOut[9] = -6*momIn[0]**4 + 8*momIn[0]**2*momIn[1] - 2*momIn[1]**2 + 4*momIn[0]**2*momIn[2] - momIn[2]**2 - 4*momIn[0]*momIn[5] + momIn[9]
		cumOut[10] = -6*momIn[0]**4 + 12*momIn[0]**2*momIn[1] - 3*momIn[1]**2 - 4*momIn[0]*momIn[4] + momIn[10]
		cumOut[11] = -6*momIn[0]**4 + 8*momIn[0]**2*momIn[1] - momIn[1]**2 + 4*momIn[0]**2*momIn[2] - 2*momIn[1]*momIn[2] - momIn[0]*momIn[4] - 2*momIn[0]*momIn[5] - momIn[0]*momIn[6] + momIn[11]
		cumOut[12] = -6*momIn[0]**4 + 6*momIn[0]**2*momIn[1] - momIn[1]**2 + 6*momIn[0]**2*momIn[2] - momIn[1]*momIn[2] - momIn[2]**2 - 2*momIn[0]*momIn[5] - 2*momIn[0]*momIn[6] + momIn[12]
		cumOut[13] = -6*momIn[0]**4 + 6*momIn[0]**2*momIn[1] + 6*momIn[0]**2*momIn[2] - 3*momIn[1]*momIn[2] - momIn[0]*momIn[3] - 3*momIn[0]*momIn[6] + momIn[13]
		cumOut[14] = -6*momIn[0]**4 + 6*momIn[0]**2*momIn[1] + 6*momIn[0]**2*momIn[2] - 3*momIn[1]*momIn[2] - momIn[0]*momIn[4] - 3*momIn[0]*momIn[6] + momIn[14]
		cumOut[15] = -6*momIn[0]**4 + 4*momIn[0]**2*momIn[1] + 8*momIn[0]**2*momIn[2] - 2*momIn[1]*momIn[2] - momIn[2]**2 - momIn[0]*momIn[5] - 2*momIn[0]*momIn[6] - momIn[0]*momIn[7] + momIn[15]
		cumOut[16] = -6*momIn[0]**4 + 4*momIn[0]**2*momIn[1] - momIn[1]**2 + 8*momIn[0]**2*momIn[2] - 2*momIn[2]**2 - 4*momIn[0]*momIn[6] + momIn[16]
		cumOut[17] = -6*momIn[0]**4 + 2*momIn[0]**2*momIn[1] + 10*momIn[0]**2*momIn[2] - momIn[1]*momIn[2] - 2*momIn[2]**2 - 2*momIn[0]*momIn[6] - 2*momIn[0]*momIn[7] + momIn[17]
		cumOut[18] = -6*momIn[0]**4 + 12*momIn[0]**2*momIn[2] - 3*momIn[2]**2 - 4*momIn[0]*momIn[7] + momIn[18]
	return cumOut