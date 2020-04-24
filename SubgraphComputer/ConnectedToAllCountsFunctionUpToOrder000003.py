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
	return cOut