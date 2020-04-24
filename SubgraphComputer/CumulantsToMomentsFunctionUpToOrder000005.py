import numpy as np
def cumulants_to_moments(cumIn):
	numCum = len(cumIn)
	if numCum==1:
		orderTemp = 1
		momOut = np.zeros(1)
	elif numCum==3:
		orderTemp = 2
		momOut = np.zeros(3)
	elif numCum==8:
		orderTemp = 3
		momOut = np.zeros(8)
	elif numCum==19:
		orderTemp = 4
		momOut = np.zeros(19)
	elif numCum==45:
		orderTemp = 5
		momOut = np.zeros(45)
	else:
		print("ERROR IN cumulants_to_moments")
	if orderTemp>=1:
		momOut[0] = cumIn[0]
	if orderTemp>=2:
		momOut[1] = cumIn[0]**2 + cumIn[1]
		momOut[2] = cumIn[0]**2 + cumIn[2]
	if orderTemp>=3:
		momOut[3] = cumIn[0]**3 + 3*cumIn[0]*cumIn[1] + cumIn[3]
		momOut[4] = cumIn[0]**3 + 3*cumIn[0]*cumIn[1] + cumIn[4]
		momOut[5] = cumIn[0]**3 + 2*cumIn[0]*cumIn[1] + cumIn[0]*cumIn[2] + cumIn[5]
		momOut[6] = cumIn[0]**3 + cumIn[0]*cumIn[1] + 2*cumIn[0]*cumIn[2] + cumIn[6]
		momOut[7] = cumIn[0]**3 + 3*cumIn[0]*cumIn[2] + cumIn[7]
	if orderTemp>=4:
		momOut[8] = cumIn[0]**4 + 5*cumIn[0]**2*cumIn[1] + 2*cumIn[1]**2 + cumIn[0]**2*cumIn[2] + cumIn[1]*cumIn[2] + cumIn[0]*cumIn[3] + cumIn[0]*cumIn[4] + 2*cumIn[0]*cumIn[5] + cumIn[8]
		momOut[9] = cumIn[0]**4 + 4*cumIn[0]**2*cumIn[1] + 2*cumIn[1]**2 + 2*cumIn[0]**2*cumIn[2] + cumIn[2]**2 + 4*cumIn[0]*cumIn[5] + cumIn[9]
		momOut[10] = cumIn[0]**4 + 6*cumIn[0]**2*cumIn[1] + 3*cumIn[1]**2 + 4*cumIn[0]*cumIn[4] + cumIn[10]
		momOut[11] = cumIn[0]**4 + 4*cumIn[0]**2*cumIn[1] + cumIn[1]**2 + 2*cumIn[0]**2*cumIn[2] + 2*cumIn[1]*cumIn[2] + cumIn[0]*cumIn[4] + 2*cumIn[0]*cumIn[5] + cumIn[0]*cumIn[6] + cumIn[11]
		momOut[12] = cumIn[0]**4 + 3*cumIn[0]**2*cumIn[1] + cumIn[1]**2 + 3*cumIn[0]**2*cumIn[2] + cumIn[1]*cumIn[2] + cumIn[2]**2 + 2*cumIn[0]*cumIn[5] + 2*cumIn[0]*cumIn[6] + cumIn[12]
		momOut[13] = cumIn[0]**4 + 3*cumIn[0]**2*cumIn[1] + 3*cumIn[0]**2*cumIn[2] + 3*cumIn[1]*cumIn[2] + cumIn[0]*cumIn[3] + 3*cumIn[0]*cumIn[6] + cumIn[13]
		momOut[14] = cumIn[0]**4 + 3*cumIn[0]**2*cumIn[1] + 3*cumIn[0]**2*cumIn[2] + 3*cumIn[1]*cumIn[2] + cumIn[0]*cumIn[4] + 3*cumIn[0]*cumIn[6] + cumIn[14]
		momOut[15] = cumIn[0]**4 + 2*cumIn[0]**2*cumIn[1] + 4*cumIn[0]**2*cumIn[2] + 2*cumIn[1]*cumIn[2] + cumIn[2]**2 + cumIn[0]*cumIn[5] + 2*cumIn[0]*cumIn[6] + cumIn[0]*cumIn[7] + cumIn[15]
		momOut[16] = cumIn[0]**4 + 2*cumIn[0]**2*cumIn[1] + cumIn[1]**2 + 4*cumIn[0]**2*cumIn[2] + 2*cumIn[2]**2 + 4*cumIn[0]*cumIn[6] + cumIn[16]
		momOut[17] = cumIn[0]**4 + cumIn[0]**2*cumIn[1] + 5*cumIn[0]**2*cumIn[2] + cumIn[1]*cumIn[2] + 2*cumIn[2]**2 + 2*cumIn[0]*cumIn[6] + 2*cumIn[0]*cumIn[7] + cumIn[17]
		momOut[18] = cumIn[0]**4 + 6*cumIn[0]**2*cumIn[2] + 3*cumIn[2]**2 + 4*cumIn[0]*cumIn[7] + cumIn[18]
	if orderTemp>=5:
		momOut[19] = cumIn[0]**5 + 8*cumIn[0]**3*cumIn[1] + 10*cumIn[0]*cumIn[1]**2 + 2*cumIn[0]**3*cumIn[2] + 4*cumIn[0]*cumIn[1]*cumIn[2] + cumIn[0]*cumIn[2]**2 + 2*cumIn[0]**2*cumIn[3] + 2*cumIn[1]*cumIn[3] + 2*cumIn[0]**2*cumIn[4] + 2*cumIn[1]*cumIn[4] + 6*cumIn[0]**2*cumIn[5] + 4*cumIn[1]*cumIn[5] + 2*cumIn[2]*cumIn[5] + 4*cumIn[0]*cumIn[8] + cumIn[0]*cumIn[9] + cumIn[19]
		momOut[20] = cumIn[0]**5 + 8*cumIn[0]**3*cumIn[1] + 9*cumIn[0]*cumIn[1]**2 + 2*cumIn[0]**3*cumIn[2] + 6*cumIn[0]*cumIn[1]*cumIn[2] + cumIn[0]**2*cumIn[3] + cumIn[1]*cumIn[3] + 4*cumIn[0]**2*cumIn[4] + 2*cumIn[1]*cumIn[4] + 2*cumIn[2]*cumIn[4] + 4*cumIn[0]**2*cumIn[5] + 4*cumIn[1]*cumIn[5] + cumIn[0]**2*cumIn[6] + cumIn[1]*cumIn[6] + 2*cumIn[0]*cumIn[8] + cumIn[0]*cumIn[10] + 2*cumIn[0]*cumIn[11] + cumIn[20]
		momOut[21] = cumIn[0]**5 + 7*cumIn[0]**3*cumIn[1] + 7*cumIn[0]*cumIn[1]**2 + 3*cumIn[0]**3*cumIn[2] + 7*cumIn[0]*cumIn[1]*cumIn[2] + cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[3] + cumIn[2]*cumIn[3] + 2*cumIn[0]**2*cumIn[4] + 2*cumIn[1]*cumIn[4] + 5*cumIn[0]**2*cumIn[5] + 3*cumIn[1]*cumIn[5] + 2*cumIn[2]*cumIn[5] + 2*cumIn[0]**2*cumIn[6] + 2*cumIn[1]*cumIn[6] + 2*cumIn[0]*cumIn[8] + 2*cumIn[0]*cumIn[11] + cumIn[0]*cumIn[12] + cumIn[21]
		momOut[22] = cumIn[0]**5 + 6*cumIn[0]**3*cumIn[1] + 5*cumIn[0]*cumIn[1]**2 + 4*cumIn[0]**3*cumIn[2] + 8*cumIn[0]*cumIn[1]*cumIn[2] + 2*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[3] + cumIn[1]*cumIn[3] + cumIn[0]**2*cumIn[4] + cumIn[2]*cumIn[4] + 4*cumIn[0]**2*cumIn[5] + 2*cumIn[1]*cumIn[5] + 2*cumIn[2]*cumIn[5] + 4*cumIn[0]**2*cumIn[6] + 3*cumIn[1]*cumIn[6] + cumIn[2]*cumIn[6] + cumIn[0]*cumIn[8] + cumIn[0]*cumIn[11] + 2*cumIn[0]*cumIn[12] + cumIn[0]*cumIn[13] + cumIn[22]
		momOut[23] = cumIn[0]**5 + 6*cumIn[0]**3*cumIn[1] + 6*cumIn[0]*cumIn[1]**2 + 4*cumIn[0]**3*cumIn[2] + 6*cumIn[0]*cumIn[1]*cumIn[2] + 3*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[4] + cumIn[1]*cumIn[4] + 6*cumIn[0]**2*cumIn[5] + 4*cumIn[1]*cumIn[5] + 2*cumIn[2]*cumIn[5] + 3*cumIn[0]**2*cumIn[6] + cumIn[1]*cumIn[6] + 2*cumIn[2]*cumIn[6] + cumIn[0]*cumIn[9] + 2*cumIn[0]*cumIn[11] + 2*cumIn[0]*cumIn[12] + cumIn[23]
		momOut[24] = cumIn[0]**5 + 5*cumIn[0]**3*cumIn[1] + 5*cumIn[0]*cumIn[1]**2 + 5*cumIn[0]**3*cumIn[2] + 5*cumIn[0]*cumIn[1]*cumIn[2] + 5*cumIn[0]*cumIn[2]**2 + 5*cumIn[0]**2*cumIn[5] + 5*cumIn[1]*cumIn[5] + 5*cumIn[0]**2*cumIn[6] + 5*cumIn[2]*cumIn[6] + 5*cumIn[0]*cumIn[12] + cumIn[24]
		momOut[25] = cumIn[0]**5 + 10*cumIn[0]**3*cumIn[1] + 15*cumIn[0]*cumIn[1]**2 + 10*cumIn[0]**2*cumIn[4] + 10*cumIn[1]*cumIn[4] + 5*cumIn[0]*cumIn[10] + cumIn[25]
		momOut[26] = cumIn[0]**5 + 7*cumIn[0]**3*cumIn[1] + 6*cumIn[0]*cumIn[1]**2 + 3*cumIn[0]**3*cumIn[2] + 9*cumIn[0]*cumIn[1]*cumIn[2] + 4*cumIn[0]**2*cumIn[4] + cumIn[1]*cumIn[4] + 3*cumIn[2]*cumIn[4] + 3*cumIn[0]**2*cumIn[5] + 3*cumIn[1]*cumIn[5] + 3*cumIn[0]**2*cumIn[6] + 3*cumIn[1]*cumIn[6] + cumIn[0]*cumIn[10] + 3*cumIn[0]*cumIn[11] + cumIn[0]*cumIn[14] + cumIn[26]
		momOut[27] = cumIn[0]**5 + 6*cumIn[0]**3*cumIn[1] + 5*cumIn[0]*cumIn[1]**2 + 4*cumIn[0]**3*cumIn[2] + 8*cumIn[0]*cumIn[1]*cumIn[2] + 2*cumIn[0]*cumIn[2]**2 + 2*cumIn[0]**2*cumIn[4] + 2*cumIn[1]*cumIn[4] + 4*cumIn[0]**2*cumIn[5] + 4*cumIn[2]*cumIn[5] + 4*cumIn[0]**2*cumIn[6] + 4*cumIn[1]*cumIn[6] + 4*cumIn[0]*cumIn[11] + cumIn[0]*cumIn[16] + cumIn[27]
		momOut[28] = cumIn[0]**5 + 5*cumIn[0]**3*cumIn[1] + 3*cumIn[0]*cumIn[1]**2 + 5*cumIn[0]**3*cumIn[2] + 9*cumIn[0]*cumIn[1]*cumIn[2] + 3*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[4] + cumIn[2]*cumIn[4] + 4*cumIn[0]**2*cumIn[5] + 2*cumIn[1]*cumIn[5] + 2*cumIn[2]*cumIn[5] + 4*cumIn[0]**2*cumIn[6] + 2*cumIn[1]*cumIn[6] + 2*cumIn[2]*cumIn[6] + cumIn[0]**2*cumIn[7] + cumIn[1]*cumIn[7] + 2*cumIn[0]*cumIn[11] + cumIn[0]*cumIn[12] + 2*cumIn[0]*cumIn[15] + cumIn[28]
		momOut[29] = cumIn[0]**5 + 5*cumIn[0]**3*cumIn[1] + 4*cumIn[0]*cumIn[1]**2 + 5*cumIn[0]**3*cumIn[2] + 7*cumIn[0]*cumIn[1]*cumIn[2] + 4*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[4] + cumIn[1]*cumIn[4] + 3*cumIn[0]**2*cumIn[5] + cumIn[1]*cumIn[5] + 2*cumIn[2]*cumIn[5] + 6*cumIn[0]**2*cumIn[6] + 3*cumIn[1]*cumIn[6] + 3*cumIn[2]*cumIn[6] + cumIn[0]*cumIn[11] + 2*cumIn[0]*cumIn[12] + cumIn[0]*cumIn[14] + cumIn[0]*cumIn[16] + cumIn[29]
		momOut[30] = cumIn[0]**5 + 4*cumIn[0]**3*cumIn[1] + 3*cumIn[0]*cumIn[1]**2 + 6*cumIn[0]**3*cumIn[2] + 6*cumIn[0]*cumIn[1]*cumIn[2] + 6*cumIn[0]*cumIn[2]**2 + 3*cumIn[0]**2*cumIn[5] + 2*cumIn[1]*cumIn[5] + cumIn[2]*cumIn[5] + 6*cumIn[0]**2*cumIn[6] + 2*cumIn[1]*cumIn[6] + 4*cumIn[2]*cumIn[6] + cumIn[0]**2*cumIn[7] + cumIn[2]*cumIn[7] + 2*cumIn[0]*cumIn[12] + 2*cumIn[0]*cumIn[15] + cumIn[0]*cumIn[16] + cumIn[30]
		momOut[31] = cumIn[0]**5 + 5*cumIn[0]**3*cumIn[1] + 2*cumIn[0]*cumIn[1]**2 + 5*cumIn[0]**3*cumIn[2] + 11*cumIn[0]*cumIn[1]*cumIn[2] + 2*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[3] + cumIn[2]*cumIn[3] + cumIn[0]**2*cumIn[4] + cumIn[2]*cumIn[4] + 2*cumIn[0]**2*cumIn[5] + 2*cumIn[2]*cumIn[5] + 5*cumIn[0]**2*cumIn[6] + 4*cumIn[1]*cumIn[6] + cumIn[2]*cumIn[6] + cumIn[0]**2*cumIn[7] + cumIn[1]*cumIn[7] + cumIn[0]*cumIn[8] + cumIn[0]*cumIn[13] + cumIn[0]*cumIn[14] + 2*cumIn[0]*cumIn[15] + cumIn[31]
		momOut[32] = cumIn[0]**5 + 4*cumIn[0]**3*cumIn[1] + 3*cumIn[0]*cumIn[1]**2 + 6*cumIn[0]**3*cumIn[2] + 6*cumIn[0]*cumIn[1]*cumIn[2] + 6*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[3] + cumIn[1]*cumIn[3] + 9*cumIn[0]**2*cumIn[6] + 3*cumIn[1]*cumIn[6] + 6*cumIn[2]*cumIn[6] + 2*cumIn[0]*cumIn[13] + 3*cumIn[0]*cumIn[16] + cumIn[32]
		momOut[33] = cumIn[0]**5 + 4*cumIn[0]**3*cumIn[1] + 2*cumIn[0]*cumIn[1]**2 + 6*cumIn[0]**3*cumIn[2] + 8*cumIn[0]*cumIn[1]*cumIn[2] + 5*cumIn[0]*cumIn[2]**2 + 4*cumIn[0]**2*cumIn[5] + 4*cumIn[2]*cumIn[5] + 4*cumIn[0]**2*cumIn[6] + 4*cumIn[1]*cumIn[6] + 2*cumIn[0]**2*cumIn[7] + 2*cumIn[2]*cumIn[7] + cumIn[0]*cumIn[9] + 4*cumIn[0]*cumIn[15] + cumIn[33]
		momOut[34] = cumIn[0]**5 + 6*cumIn[0]**3*cumIn[1] + 3*cumIn[0]*cumIn[1]**2 + 4*cumIn[0]**3*cumIn[2] + 12*cumIn[0]*cumIn[1]*cumIn[2] + 4*cumIn[0]**2*cumIn[4] + 4*cumIn[2]*cumIn[4] + 6*cumIn[0]**2*cumIn[6] + 6*cumIn[1]*cumIn[6] + cumIn[0]*cumIn[10] + 4*cumIn[0]*cumIn[14] + cumIn[34]
		momOut[35] = cumIn[0]**5 + 4*cumIn[0]**3*cumIn[1] + cumIn[0]*cumIn[1]**2 + 6*cumIn[0]**3*cumIn[2] + 10*cumIn[0]*cumIn[1]*cumIn[2] + 4*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[4] + cumIn[2]*cumIn[4] + 2*cumIn[0]**2*cumIn[5] + 2*cumIn[2]*cumIn[5] + 5*cumIn[0]**2*cumIn[6] + 2*cumIn[1]*cumIn[6] + 3*cumIn[2]*cumIn[6] + 2*cumIn[0]**2*cumIn[7] + 2*cumIn[1]*cumIn[7] + cumIn[0]*cumIn[11] + cumIn[0]*cumIn[14] + 2*cumIn[0]*cumIn[15] + cumIn[0]*cumIn[17] + cumIn[35]
		momOut[36] = cumIn[0]**5 + 4*cumIn[0]**3*cumIn[1] + 3*cumIn[0]*cumIn[1]**2 + 6*cumIn[0]**3*cumIn[2] + 6*cumIn[0]*cumIn[1]*cumIn[2] + 6*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[4] + cumIn[1]*cumIn[4] + 9*cumIn[0]**2*cumIn[6] + 3*cumIn[1]*cumIn[6] + 6*cumIn[2]*cumIn[6] + 2*cumIn[0]*cumIn[14] + 3*cumIn[0]*cumIn[16] + cumIn[36]
		momOut[37] = cumIn[0]**5 + 3*cumIn[0]**3*cumIn[1] + cumIn[0]*cumIn[1]**2 + 7*cumIn[0]**3*cumIn[2] + 7*cumIn[0]*cumIn[1]*cumIn[2] + 7*cumIn[0]*cumIn[2]**2 + 2*cumIn[0]**2*cumIn[5] + 2*cumIn[2]*cumIn[5] + 5*cumIn[0]**2*cumIn[6] + 2*cumIn[1]*cumIn[6] + 3*cumIn[2]*cumIn[6] + 3*cumIn[0]**2*cumIn[7] + cumIn[1]*cumIn[7] + 2*cumIn[2]*cumIn[7] + cumIn[0]*cumIn[12] + 2*cumIn[0]*cumIn[15] + 2*cumIn[0]*cumIn[17] + cumIn[37]
		momOut[38] = cumIn[0]**5 + 3*cumIn[0]**3*cumIn[1] + 2*cumIn[0]*cumIn[1]**2 + 7*cumIn[0]**3*cumIn[2] + 5*cumIn[0]*cumIn[1]*cumIn[2] + 8*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[5] + cumIn[1]*cumIn[5] + 7*cumIn[0]**2*cumIn[6] + 2*cumIn[1]*cumIn[6] + 5*cumIn[2]*cumIn[6] + 2*cumIn[0]**2*cumIn[7] + 2*cumIn[2]*cumIn[7] + 2*cumIn[0]*cumIn[15] + 2*cumIn[0]*cumIn[16] + cumIn[0]*cumIn[17] + cumIn[38]
		momOut[39] = cumIn[0]**5 + 3*cumIn[0]**3*cumIn[1] + 7*cumIn[0]**3*cumIn[2] + 9*cumIn[0]*cumIn[1]*cumIn[2] + 6*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[3] + cumIn[2]*cumIn[3] + 6*cumIn[0]**2*cumIn[6] + 6*cumIn[2]*cumIn[6] + 3*cumIn[0]**2*cumIn[7] + 3*cumIn[1]*cumIn[7] + 2*cumIn[0]*cumIn[13] + 3*cumIn[0]*cumIn[17] + cumIn[39]
		momOut[40] = cumIn[0]**5 + 3*cumIn[0]**3*cumIn[1] + 7*cumIn[0]**3*cumIn[2] + 9*cumIn[0]*cumIn[1]*cumIn[2] + 6*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[4] + cumIn[2]*cumIn[4] + 6*cumIn[0]**2*cumIn[6] + 6*cumIn[2]*cumIn[6] + 3*cumIn[0]**2*cumIn[7] + 3*cumIn[1]*cumIn[7] + 2*cumIn[0]*cumIn[14] + 3*cumIn[0]*cumIn[17] + cumIn[40]
		momOut[41] = cumIn[0]**5 + 2*cumIn[0]**3*cumIn[1] + 8*cumIn[0]**3*cumIn[2] + 6*cumIn[0]*cumIn[1]*cumIn[2] + 9*cumIn[0]*cumIn[2]**2 + cumIn[0]**2*cumIn[5] + cumIn[2]*cumIn[5] + 4*cumIn[0]**2*cumIn[6] + 4*cumIn[2]*cumIn[6] + 5*cumIn[0]**2*cumIn[7] + 2*cumIn[1]*cumIn[7] + 3*cumIn[2]*cumIn[7] + 2*cumIn[0]*cumIn[15] + 2*cumIn[0]*cumIn[17] + cumIn[0]*cumIn[18] + cumIn[41]
		momOut[42] = cumIn[0]**5 + 2*cumIn[0]**3*cumIn[1] + cumIn[0]*cumIn[1]**2 + 8*cumIn[0]**3*cumIn[2] + 4*cumIn[0]*cumIn[1]*cumIn[2] + 10*cumIn[0]*cumIn[2]**2 + 6*cumIn[0]**2*cumIn[6] + 2*cumIn[1]*cumIn[6] + 4*cumIn[2]*cumIn[6] + 4*cumIn[0]**2*cumIn[7] + 4*cumIn[2]*cumIn[7] + cumIn[0]*cumIn[16] + 4*cumIn[0]*cumIn[17] + cumIn[42]
		momOut[43] = cumIn[0]**5 + cumIn[0]**3*cumIn[1] + 9*cumIn[0]**3*cumIn[2] + 3*cumIn[0]*cumIn[1]*cumIn[2] + 12*cumIn[0]*cumIn[2]**2 + 3*cumIn[0]**2*cumIn[6] + 3*cumIn[2]*cumIn[6] + 7*cumIn[0]**2*cumIn[7] + cumIn[1]*cumIn[7] + 6*cumIn[2]*cumIn[7] + 3*cumIn[0]*cumIn[17] + 2*cumIn[0]*cumIn[18] + cumIn[43]
		momOut[44] = cumIn[0]**5 + 10*cumIn[0]**3*cumIn[2] + 15*cumIn[0]*cumIn[2]**2 + 10*cumIn[0]**2*cumIn[7] + 10*cumIn[2]*cumIn[7] + 5*cumIn[0]*cumIn[18] + cumIn[44]
	return momOut