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
	return cOut