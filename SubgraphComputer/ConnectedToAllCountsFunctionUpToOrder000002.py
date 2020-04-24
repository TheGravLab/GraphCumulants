import numpy as np
def connected_to_disconnected_counts(cIn):
	numC = len(cIn)
	if numC==1:
		orderTemp = 1
		cOut = np.zeros(1)
	elif numC==2:
		orderTemp = 2
		cOut = np.zeros(3)
	else:
		print("ERROR IN connected_to_disconnected")
	if orderTemp>=1:
		cOut[0] = cIn[0]
	if orderTemp>=2:
		cOut[1] = cIn[1]
		cOut[2] = -cOut[0]/2. + cOut[0]**2/2. - cOut[1]
	return cOut