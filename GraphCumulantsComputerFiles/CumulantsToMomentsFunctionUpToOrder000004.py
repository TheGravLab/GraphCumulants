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
	return momOut