import numpy as np
def connected_to_disconnected_counts(cIn):
	numC = len(cIn)
	if numC==1:
		orderTemp = 1
		cOut = np.zeros(1)
	elif numC==2:
		orderTemp = 2
		cOut = np.zeros(3)
	elif numC==5:
		orderTemp = 3
		cOut = np.zeros(8)
	elif numC==10:
		orderTemp = 4
		cOut = np.zeros(19)
	elif numC==22:
		orderTemp = 5
		cOut = np.zeros(45)
	else:
		print("ERROR IN connected_to_disconnected")
	if orderTemp>=1:
		cOut[0] = cIn[0]
	if orderTemp>=2:
		cOut[1] = cIn[1]
		cOut[2] = -cOut[0]/2. + cOut[0]**2/2. - cOut[1]
	if orderTemp>=3:
		cOut[3] = cIn[2]
		cOut[4] = cIn[3]
		cOut[5] = cIn[4]
		cOut[6] = -2*cOut[1] + cOut[0]*cOut[1] - 3*cOut[3] - 3*cOut[4] - 2*cOut[5]
		cOut[7] = -cOut[0]/6. + cOut[0]**3/6. - cOut[1] - cOut[2] - cOut[3] - cOut[4] - cOut[5] - cOut[6]
	if orderTemp>=4:
		cOut[8] = cIn[5]
		cOut[9] = cIn[6]
		cOut[10] = cIn[7]
		cOut[11] = cIn[8]
		cOut[12] = cIn[9]
		cOut[13] = -3*cOut[3] + cOut[0]*cOut[3] - cOut[8]
		cOut[14] = -3*cOut[4] + cOut[0]*cOut[4] - cOut[8] - 4*cOut[10] - cOut[11]
		cOut[15] = -3*cOut[5] + cOut[0]*cOut[5] - 2*cOut[8] - 4*cOut[9] - 2*cOut[11] - 2*cOut[12]
		cOut[16] = -cOut[1]/2. + cOut[1]**2/2. - 3*cOut[3] - 3*cOut[4] - cOut[5] - 2*cOut[8] - 2*cOut[9] - 3*cOut[10] - cOut[11] - cOut[12]
		cOut[17] = -2*cOut[1] + (cOut[0]**2*cOut[1])/2. - (15*cOut[3])/2. - (15*cOut[4])/2. - 5*cOut[5] - (5*cOut[6])/2. - 5*cOut[8] - 4*cOut[9] - 6*cOut[10] - 4*cOut[11] - 3*cOut[12] - 3*cOut[13] - 3*cOut[14] - 2*cOut[15] - 2*cOut[16]
		cOut[18] = -cOut[0]/24. + cOut[0]**4/24. - (7*cOut[1])/12. - (7*cOut[2])/12. - (3*cOut[3])/2. - (3*cOut[4])/2. - (3*cOut[5])/2. - (3*cOut[6])/2. - (3*cOut[7])/2. - cOut[8] - cOut[9] - cOut[10] - cOut[11] - cOut[12] - cOut[13] - cOut[14] - cOut[15] - cOut[16] - cOut[17]
	if orderTemp>=5:
		cOut[19] = cIn[10]
		cOut[20] = cIn[11]
		cOut[21] = cIn[12]
		cOut[22] = cIn[13]
		cOut[23] = cIn[14]
		cOut[24] = cIn[15]
		cOut[25] = cIn[16]
		cOut[26] = cIn[17]
		cOut[27] = cIn[18]
		cOut[28] = cIn[19]
		cOut[29] = cIn[20]
		cOut[30] = cIn[21]
		cOut[31] = -4*cOut[8] + cOut[0]*cOut[8] - 4*cOut[19] - 2*cOut[20] - 2*cOut[21] - cOut[22]
		cOut[32] = -3*cOut[3] + cOut[1]*cOut[3] - 2*cOut[8] - 2*cOut[19] - cOut[20] - cOut[22]
		cOut[33] = -4*cOut[9] + cOut[0]*cOut[9] - cOut[19] - cOut[23]
		cOut[34] = -4*cOut[10] + cOut[0]*cOut[10] - cOut[20] - 5*cOut[25] - cOut[26]
		cOut[35] = -4*cOut[11] + cOut[0]*cOut[11] - 2*cOut[20] - 2*cOut[21] - cOut[22] - 2*cOut[23] - 3*cOut[26] - 4*cOut[27] - 2*cOut[28] - cOut[29]
		cOut[36] = -3*cOut[4] + cOut[1]*cOut[4] - 2*cOut[8] - 12*cOut[10] - cOut[11] - 2*cOut[19] - 2*cOut[20] - 2*cOut[21] - cOut[23] - 10*cOut[25] - cOut[26] - 2*cOut[27] - cOut[29]
		cOut[37] = -4*cOut[12] + cOut[0]*cOut[12] - cOut[21] - 2*cOut[22] - 2*cOut[23] - 5*cOut[24] - cOut[28] - 2*cOut[29] - 2*cOut[30]
		cOut[38] = -2*cOut[5] + cOut[1]*cOut[5] - 6*cOut[8] - 8*cOut[9] - 4*cOut[11] - 2*cOut[12] - 4*cOut[19] - 4*cOut[20] - 3*cOut[21] - 2*cOut[22] - 4*cOut[23] - 5*cOut[24] - 3*cOut[26] - 2*cOut[28] - cOut[29] - 2*cOut[30]
		cOut[39] = (-9*cOut[3])/2. + (cOut[0]**2*cOut[3])/2. - (7*cOut[8])/2. - (7*cOut[13])/2. - 2*cOut[19] - cOut[20] - cOut[21] - cOut[22] - cOut[31] - cOut[32]
		cOut[40] = (-9*cOut[4])/2. + (cOut[0]**2*cOut[4])/2. - (7*cOut[8])/2. - 14*cOut[10] - (7*cOut[11])/2. - (7*cOut[14])/2. - 2*cOut[19] - 4*cOut[20] - 2*cOut[21] - cOut[22] - cOut[23] - 10*cOut[25] - 4*cOut[26] - 2*cOut[27] - cOut[28] - cOut[29] - cOut[31] - 4*cOut[34] - cOut[35] - cOut[36]
		cOut[41] = (-9*cOut[5])/2. + (cOut[0]**2*cOut[5])/2. - 7*cOut[8] - 14*cOut[9] - 7*cOut[11] - 7*cOut[12] - (7*cOut[15])/2. - 6*cOut[19] - 4*cOut[20] - 5*cOut[21] - 4*cOut[22] - 6*cOut[23] - 5*cOut[24] - 3*cOut[26] - 4*cOut[27] - 4*cOut[28] - 3*cOut[29] - 3*cOut[30] - 2*cOut[31] - 4*cOut[33] - 2*cOut[35] - 2*cOut[37] - cOut[38]
		cOut[42] = -cOut[1] + (cOut[0]*cOut[1]**2)/2. - (21*cOut[3])/2. - (21*cOut[4])/2. - 4*cOut[5] - cOut[6]/2. - 16*cOut[8] - 12*cOut[9] - 24*cOut[10] - 9*cOut[11] - 6*cOut[12] - 3*cOut[13] - 3*cOut[14] - cOut[15] - 4*cOut[16] - 10*cOut[19] - 9*cOut[20] - 7*cOut[21] - 5*cOut[22] - 6*cOut[23] - 5*cOut[24] - 15*cOut[25] - 6*cOut[26] - 5*cOut[27] - 3*cOut[28] - 4*cOut[29] - 3*cOut[30] - 2*cOut[31] - 3*cOut[32] - 2*cOut[33] - 3*cOut[34] - cOut[35] - 3*cOut[36] - cOut[37] - 2*cOut[38]
		cOut[43] = (-4*cOut[1])/3. + (cOut[0]**3*cOut[1])/6. - (19*cOut[3])/2. - (19*cOut[4])/2. - (19*cOut[5])/3. - (19*cOut[6])/6. - 15*cOut[8] - 12*cOut[9] - 18*cOut[10] - 12*cOut[11] - 9*cOut[12] - 9*cOut[13] - 9*cOut[14] - 6*cOut[15] - 6*cOut[16] - 3*cOut[17] - 8*cOut[19] - 8*cOut[20] - 7*cOut[21] - 6*cOut[22] - 6*cOut[23] - 5*cOut[24] - 10*cOut[25] - 7*cOut[26] - 6*cOut[27] - 5*cOut[28] - 5*cOut[29] - 4*cOut[30] - 5*cOut[31] - 4*cOut[32] - 4*cOut[33] - 6*cOut[34] - 4*cOut[35] - 4*cOut[36] - 3*cOut[37] - 3*cOut[38] - 3*cOut[39] - 3*cOut[40] - 2*cOut[41] - 2*cOut[42]
		cOut[44] = -cOut[0]/120. + cOut[0]**5/120. - cOut[1]/4. - cOut[2]/4. - (5*cOut[3])/4. - (5*cOut[4])/4. - (5*cOut[5])/4. - (5*cOut[6])/4. - (5*cOut[7])/4. - 2*cOut[8] - 2*cOut[9] - 2*cOut[10] - 2*cOut[11] - 2*cOut[12] - 2*cOut[13] - 2*cOut[14] - 2*cOut[15] - 2*cOut[16] - 2*cOut[17] - 2*cOut[18] - cOut[19] - cOut[20] - cOut[21] - cOut[22] - cOut[23] - cOut[24] - cOut[25] - cOut[26] - cOut[27] - cOut[28] - cOut[29] - cOut[30] - cOut[31] - cOut[32] - cOut[33] - cOut[34] - cOut[35] - cOut[36] - cOut[37] - cOut[38] - cOut[39] - cOut[40] - cOut[41] - cOut[42] - cOut[43]
	return cOut