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
	elif numMom==45:
		orderTemp = 5
		cumOut = np.zeros(45)
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
	if orderTemp>=5:
		cumOut[19] = 24*momIn[0]**5 - 48*momIn[0]**3*momIn[1] + 20*momIn[0]*momIn[1]**2 - 12*momIn[0]**3*momIn[2] + 8*momIn[0]*momIn[1]*momIn[2] + 2*momIn[0]*momIn[2]**2 + 4*momIn[0]**2*momIn[3] - 2*momIn[1]*momIn[3] + 4*momIn[0]**2*momIn[4] - 2*momIn[1]*momIn[4] + 12*momIn[0]**2*momIn[5] - 4*momIn[1]*momIn[5] - 2*momIn[2]*momIn[5] - 4*momIn[0]*momIn[8] - momIn[0]*momIn[9] + momIn[19]
		cumOut[20] = 24*momIn[0]**5 - 48*momIn[0]**3*momIn[1] + 18*momIn[0]*momIn[1]**2 - 12*momIn[0]**3*momIn[2] + 12*momIn[0]*momIn[1]*momIn[2] + 2*momIn[0]**2*momIn[3] - momIn[1]*momIn[3] + 8*momIn[0]**2*momIn[4] - 2*momIn[1]*momIn[4] - 2*momIn[2]*momIn[4] + 8*momIn[0]**2*momIn[5] - 4*momIn[1]*momIn[5] + 2*momIn[0]**2*momIn[6] - momIn[1]*momIn[6] - 2*momIn[0]*momIn[8] - momIn[0]*momIn[10] - 2*momIn[0]*momIn[11] + momIn[20]
		cumOut[21] = 24*momIn[0]**5 - 42*momIn[0]**3*momIn[1] + 14*momIn[0]*momIn[1]**2 - 18*momIn[0]**3*momIn[2] + 14*momIn[0]*momIn[1]*momIn[2] + 2*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[3] - momIn[2]*momIn[3] + 4*momIn[0]**2*momIn[4] - 2*momIn[1]*momIn[4] + 10*momIn[0]**2*momIn[5] - 3*momIn[1]*momIn[5] - 2*momIn[2]*momIn[5] + 4*momIn[0]**2*momIn[6] - 2*momIn[1]*momIn[6] - 2*momIn[0]*momIn[8] - 2*momIn[0]*momIn[11] - momIn[0]*momIn[12] + momIn[21]
		cumOut[22] = 24*momIn[0]**5 - 36*momIn[0]**3*momIn[1] + 10*momIn[0]*momIn[1]**2 - 24*momIn[0]**3*momIn[2] + 16*momIn[0]*momIn[1]*momIn[2] + 4*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[3] - momIn[1]*momIn[3] + 2*momIn[0]**2*momIn[4] - momIn[2]*momIn[4] + 8*momIn[0]**2*momIn[5] - 2*momIn[1]*momIn[5] - 2*momIn[2]*momIn[5] + 8*momIn[0]**2*momIn[6] - 3*momIn[1]*momIn[6] - momIn[2]*momIn[6] - momIn[0]*momIn[8] - momIn[0]*momIn[11] - 2*momIn[0]*momIn[12] - momIn[0]*momIn[13] + momIn[22]
		cumOut[23] = 24*momIn[0]**5 - 36*momIn[0]**3*momIn[1] + 12*momIn[0]*momIn[1]**2 - 24*momIn[0]**3*momIn[2] + 12*momIn[0]*momIn[1]*momIn[2] + 6*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[4] - momIn[1]*momIn[4] + 12*momIn[0]**2*momIn[5] - 4*momIn[1]*momIn[5] - 2*momIn[2]*momIn[5] + 6*momIn[0]**2*momIn[6] - momIn[1]*momIn[6] - 2*momIn[2]*momIn[6] - momIn[0]*momIn[9] - 2*momIn[0]*momIn[11] - 2*momIn[0]*momIn[12] + momIn[23]
		cumOut[24] = 24*momIn[0]**5 - 30*momIn[0]**3*momIn[1] + 10*momIn[0]*momIn[1]**2 - 30*momIn[0]**3*momIn[2] + 10*momIn[0]*momIn[1]*momIn[2] + 10*momIn[0]*momIn[2]**2 + 10*momIn[0]**2*momIn[5] - 5*momIn[1]*momIn[5] + 10*momIn[0]**2*momIn[6] - 5*momIn[2]*momIn[6] - 5*momIn[0]*momIn[12] + momIn[24]
		cumOut[25] = 24*momIn[0]**5 - 60*momIn[0]**3*momIn[1] + 30*momIn[0]*momIn[1]**2 + 20*momIn[0]**2*momIn[4] - 10*momIn[1]*momIn[4] - 5*momIn[0]*momIn[10] + momIn[25]
		cumOut[26] = 24*momIn[0]**5 - 42*momIn[0]**3*momIn[1] + 12*momIn[0]*momIn[1]**2 - 18*momIn[0]**3*momIn[2] + 18*momIn[0]*momIn[1]*momIn[2] + 8*momIn[0]**2*momIn[4] - momIn[1]*momIn[4] - 3*momIn[2]*momIn[4] + 6*momIn[0]**2*momIn[5] - 3*momIn[1]*momIn[5] + 6*momIn[0]**2*momIn[6] - 3*momIn[1]*momIn[6] - momIn[0]*momIn[10] - 3*momIn[0]*momIn[11] - momIn[0]*momIn[14] + momIn[26]
		cumOut[27] = 24*momIn[0]**5 - 36*momIn[0]**3*momIn[1] + 10*momIn[0]*momIn[1]**2 - 24*momIn[0]**3*momIn[2] + 16*momIn[0]*momIn[1]*momIn[2] + 4*momIn[0]*momIn[2]**2 + 4*momIn[0]**2*momIn[4] - 2*momIn[1]*momIn[4] + 8*momIn[0]**2*momIn[5] - 4*momIn[2]*momIn[5] + 8*momIn[0]**2*momIn[6] - 4*momIn[1]*momIn[6] - 4*momIn[0]*momIn[11] - momIn[0]*momIn[16] + momIn[27]
		cumOut[28] = 24*momIn[0]**5 - 30*momIn[0]**3*momIn[1] + 6*momIn[0]*momIn[1]**2 - 30*momIn[0]**3*momIn[2] + 18*momIn[0]*momIn[1]*momIn[2] + 6*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[4] - momIn[2]*momIn[4] + 8*momIn[0]**2*momIn[5] - 2*momIn[1]*momIn[5] - 2*momIn[2]*momIn[5] + 8*momIn[0]**2*momIn[6] - 2*momIn[1]*momIn[6] - 2*momIn[2]*momIn[6] + 2*momIn[0]**2*momIn[7] - momIn[1]*momIn[7] - 2*momIn[0]*momIn[11] - momIn[0]*momIn[12] - 2*momIn[0]*momIn[15] + momIn[28]
		cumOut[29] = 24*momIn[0]**5 - 30*momIn[0]**3*momIn[1] + 8*momIn[0]*momIn[1]**2 - 30*momIn[0]**3*momIn[2] + 14*momIn[0]*momIn[1]*momIn[2] + 8*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[4] - momIn[1]*momIn[4] + 6*momIn[0]**2*momIn[5] - momIn[1]*momIn[5] - 2*momIn[2]*momIn[5] + 12*momIn[0]**2*momIn[6] - 3*momIn[1]*momIn[6] - 3*momIn[2]*momIn[6] - momIn[0]*momIn[11] - 2*momIn[0]*momIn[12] - momIn[0]*momIn[14] - momIn[0]*momIn[16] + momIn[29]
		cumOut[30] = 24*momIn[0]**5 - 24*momIn[0]**3*momIn[1] + 6*momIn[0]*momIn[1]**2 - 36*momIn[0]**3*momIn[2] + 12*momIn[0]*momIn[1]*momIn[2] + 12*momIn[0]*momIn[2]**2 + 6*momIn[0]**2*momIn[5] - 2*momIn[1]*momIn[5] - momIn[2]*momIn[5] + 12*momIn[0]**2*momIn[6] - 2*momIn[1]*momIn[6] - 4*momIn[2]*momIn[6] + 2*momIn[0]**2*momIn[7] - momIn[2]*momIn[7] - 2*momIn[0]*momIn[12] - 2*momIn[0]*momIn[15] - momIn[0]*momIn[16] + momIn[30]
		cumOut[31] = 24*momIn[0]**5 - 30*momIn[0]**3*momIn[1] + 4*momIn[0]*momIn[1]**2 - 30*momIn[0]**3*momIn[2] + 22*momIn[0]*momIn[1]*momIn[2] + 4*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[3] - momIn[2]*momIn[3] + 2*momIn[0]**2*momIn[4] - momIn[2]*momIn[4] + 4*momIn[0]**2*momIn[5] - 2*momIn[2]*momIn[5] + 10*momIn[0]**2*momIn[6] - 4*momIn[1]*momIn[6] - momIn[2]*momIn[6] + 2*momIn[0]**2*momIn[7] - momIn[1]*momIn[7] - momIn[0]*momIn[8] - momIn[0]*momIn[13] - momIn[0]*momIn[14] - 2*momIn[0]*momIn[15] + momIn[31]
		cumOut[32] = 24*momIn[0]**5 - 24*momIn[0]**3*momIn[1] + 6*momIn[0]*momIn[1]**2 - 36*momIn[0]**3*momIn[2] + 12*momIn[0]*momIn[1]*momIn[2] + 12*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[3] - momIn[1]*momIn[3] + 18*momIn[0]**2*momIn[6] - 3*momIn[1]*momIn[6] - 6*momIn[2]*momIn[6] - 2*momIn[0]*momIn[13] - 3*momIn[0]*momIn[16] + momIn[32]
		cumOut[33] = 24*momIn[0]**5 - 24*momIn[0]**3*momIn[1] + 4*momIn[0]*momIn[1]**2 - 36*momIn[0]**3*momIn[2] + 16*momIn[0]*momIn[1]*momIn[2] + 10*momIn[0]*momIn[2]**2 + 8*momIn[0]**2*momIn[5] - 4*momIn[2]*momIn[5] + 8*momIn[0]**2*momIn[6] - 4*momIn[1]*momIn[6] + 4*momIn[0]**2*momIn[7] - 2*momIn[2]*momIn[7] - momIn[0]*momIn[9] - 4*momIn[0]*momIn[15] + momIn[33]
		cumOut[34] = 24*momIn[0]**5 - 36*momIn[0]**3*momIn[1] + 6*momIn[0]*momIn[1]**2 - 24*momIn[0]**3*momIn[2] + 24*momIn[0]*momIn[1]*momIn[2] + 8*momIn[0]**2*momIn[4] - 4*momIn[2]*momIn[4] + 12*momIn[0]**2*momIn[6] - 6*momIn[1]*momIn[6] - momIn[0]*momIn[10] - 4*momIn[0]*momIn[14] + momIn[34]
		cumOut[35] = 24*momIn[0]**5 - 24*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - 36*momIn[0]**3*momIn[2] + 20*momIn[0]*momIn[1]*momIn[2] + 8*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[4] - momIn[2]*momIn[4] + 4*momIn[0]**2*momIn[5] - 2*momIn[2]*momIn[5] + 10*momIn[0]**2*momIn[6] - 2*momIn[1]*momIn[6] - 3*momIn[2]*momIn[6] + 4*momIn[0]**2*momIn[7] - 2*momIn[1]*momIn[7] - momIn[0]*momIn[11] - momIn[0]*momIn[14] - 2*momIn[0]*momIn[15] - momIn[0]*momIn[17] + momIn[35]
		cumOut[36] = 24*momIn[0]**5 - 24*momIn[0]**3*momIn[1] + 6*momIn[0]*momIn[1]**2 - 36*momIn[0]**3*momIn[2] + 12*momIn[0]*momIn[1]*momIn[2] + 12*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[4] - momIn[1]*momIn[4] + 18*momIn[0]**2*momIn[6] - 3*momIn[1]*momIn[6] - 6*momIn[2]*momIn[6] - 2*momIn[0]*momIn[14] - 3*momIn[0]*momIn[16] + momIn[36]
		cumOut[37] = 24*momIn[0]**5 - 18*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - 42*momIn[0]**3*momIn[2] + 14*momIn[0]*momIn[1]*momIn[2] + 14*momIn[0]*momIn[2]**2 + 4*momIn[0]**2*momIn[5] - 2*momIn[2]*momIn[5] + 10*momIn[0]**2*momIn[6] - 2*momIn[1]*momIn[6] - 3*momIn[2]*momIn[6] + 6*momIn[0]**2*momIn[7] - momIn[1]*momIn[7] - 2*momIn[2]*momIn[7] - momIn[0]*momIn[12] - 2*momIn[0]*momIn[15] - 2*momIn[0]*momIn[17] + momIn[37]
		cumOut[38] = 24*momIn[0]**5 - 18*momIn[0]**3*momIn[1] + 4*momIn[0]*momIn[1]**2 - 42*momIn[0]**3*momIn[2] + 10*momIn[0]*momIn[1]*momIn[2] + 16*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[5] - momIn[1]*momIn[5] + 14*momIn[0]**2*momIn[6] - 2*momIn[1]*momIn[6] - 5*momIn[2]*momIn[6] + 4*momIn[0]**2*momIn[7] - 2*momIn[2]*momIn[7] - 2*momIn[0]*momIn[15] - 2*momIn[0]*momIn[16] - momIn[0]*momIn[17] + momIn[38]
		cumOut[39] = 24*momIn[0]**5 - 18*momIn[0]**3*momIn[1] - 42*momIn[0]**3*momIn[2] + 18*momIn[0]*momIn[1]*momIn[2] + 12*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[3] - momIn[2]*momIn[3] + 12*momIn[0]**2*momIn[6] - 6*momIn[2]*momIn[6] + 6*momIn[0]**2*momIn[7] - 3*momIn[1]*momIn[7] - 2*momIn[0]*momIn[13] - 3*momIn[0]*momIn[17] + momIn[39]
		cumOut[40] = 24*momIn[0]**5 - 18*momIn[0]**3*momIn[1] - 42*momIn[0]**3*momIn[2] + 18*momIn[0]*momIn[1]*momIn[2] + 12*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[4] - momIn[2]*momIn[4] + 12*momIn[0]**2*momIn[6] - 6*momIn[2]*momIn[6] + 6*momIn[0]**2*momIn[7] - 3*momIn[1]*momIn[7] - 2*momIn[0]*momIn[14] - 3*momIn[0]*momIn[17] + momIn[40]
		cumOut[41] = 24*momIn[0]**5 - 12*momIn[0]**3*momIn[1] - 48*momIn[0]**3*momIn[2] + 12*momIn[0]*momIn[1]*momIn[2] + 18*momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[5] - momIn[2]*momIn[5] + 8*momIn[0]**2*momIn[6] - 4*momIn[2]*momIn[6] + 10*momIn[0]**2*momIn[7] - 2*momIn[1]*momIn[7] - 3*momIn[2]*momIn[7] - 2*momIn[0]*momIn[15] - 2*momIn[0]*momIn[17] - momIn[0]*momIn[18] + momIn[41]
		cumOut[42] = 24*momIn[0]**5 - 12*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - 48*momIn[0]**3*momIn[2] + 8*momIn[0]*momIn[1]*momIn[2] + 20*momIn[0]*momIn[2]**2 + 12*momIn[0]**2*momIn[6] - 2*momIn[1]*momIn[6] - 4*momIn[2]*momIn[6] + 8*momIn[0]**2*momIn[7] - 4*momIn[2]*momIn[7] - momIn[0]*momIn[16] - 4*momIn[0]*momIn[17] + momIn[42]
		cumOut[43] = 24*momIn[0]**5 - 6*momIn[0]**3*momIn[1] - 54*momIn[0]**3*momIn[2] + 6*momIn[0]*momIn[1]*momIn[2] + 24*momIn[0]*momIn[2]**2 + 6*momIn[0]**2*momIn[6] - 3*momIn[2]*momIn[6] + 14*momIn[0]**2*momIn[7] - momIn[1]*momIn[7] - 6*momIn[2]*momIn[7] - 3*momIn[0]*momIn[17] - 2*momIn[0]*momIn[18] + momIn[43]
		cumOut[44] = 24*momIn[0]**5 - 60*momIn[0]**3*momIn[2] + 30*momIn[0]*momIn[2]**2 + 20*momIn[0]**2*momIn[7] - 10*momIn[2]*momIn[7] - 5*momIn[0]*momIn[18] + momIn[44]
	return cumOut