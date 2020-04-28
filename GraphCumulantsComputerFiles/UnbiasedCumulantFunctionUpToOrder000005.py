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
	elif numMom==45:
		orderTemp = 5
		cumOut = np.zeros(45)
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
	if orderTemp>=5:
		cumOut[19] = momIn[19] - 4*momIn[31] - 2*momIn[32] - momIn[33] - 2*momIn[36] - 4*momIn[38] + 4*momIn[39] + 4*momIn[40] + 10*momIn[41] + 20*momIn[42] - 40*momIn[43] + 14*momIn[44]
		cumOut[20] = momIn[20] - 2*momIn[31] - momIn[32] - momIn[34] - 2*momIn[35] - 2*momIn[36] - 4*momIn[38] + 2*momIn[39] + 6*momIn[40] + 8*momIn[41] + 17*momIn[42] - 34*momIn[43] + 12*momIn[44]
		cumOut[21] = momIn[21] - 2*momIn[31] - 2*momIn[35] - 2*momIn[36] - momIn[37] - 3*momIn[38] + momIn[39] + 4*momIn[40] + 8*momIn[41] + 12*momIn[42] - 24*momIn[43] + 8*momIn[44]
		cumOut[22] = momIn[22] - momIn[31] - momIn[32] - momIn[35] - 2*momIn[37] - 2*momIn[38] + momIn[39] + momIn[40] + 6*momIn[41] + 7*momIn[42] - 13*momIn[43] + 4*momIn[44]
		cumOut[23] = momIn[23] - momIn[33] - 2*momIn[35] - momIn[36] - 2*momIn[37] - 4*momIn[38] + 2*momIn[40] + 10*momIn[41] + 11*momIn[42] - 20*momIn[43] + 6*momIn[44]
		cumOut[24] = momIn[24] - 5*momIn[37] - 5*momIn[38] + 10*momIn[41] + 10*momIn[42] - 15*momIn[43] + 4*momIn[44]
		cumOut[25] = momIn[25] - 5*momIn[34] - 10*momIn[36] + 20*momIn[40] + 30*momIn[42] - 60*momIn[43] + 24*momIn[44]
		cumOut[26] = momIn[26] - momIn[34] - 3*momIn[35] - momIn[36] - 3*momIn[38] + 4*momIn[40] + 6*momIn[41] + 9*momIn[42] - 18*momIn[43] + 6*momIn[44]
		cumOut[27] = momIn[27] - 4*momIn[35] - 2*momIn[36] + 4*momIn[40] + 4*momIn[41] + 5*momIn[42] - 12*momIn[43] + 4*momIn[44]
		cumOut[28] = momIn[28] - 2*momIn[35] - momIn[37] - 2*momIn[38] + momIn[40] + 4*momIn[41] + 4*momIn[42] - 7*momIn[43] + 2*momIn[44]
		cumOut[29] = momIn[29] - momIn[35] - momIn[36] - 2*momIn[37] - momIn[38] + momIn[40] + 4*momIn[41] + 4*momIn[42] - 7*momIn[43] + 2*momIn[44]
		cumOut[30] = momIn[30] - 2*momIn[37] - 2*momIn[38] + 3*momIn[41] + 3*momIn[42] - 4*momIn[43] + momIn[44]
		cumOut[31] = 0
		cumOut[32] = 0
		cumOut[33] = 0
		cumOut[34] = 0
		cumOut[35] = 0
		cumOut[36] = 0
		cumOut[37] = 0
		cumOut[38] = 0
		cumOut[39] = 0
		cumOut[40] = 0
		cumOut[41] = 0
		cumOut[42] = 0
		cumOut[43] = 0
		cumOut[44] = 0
	return cumOut