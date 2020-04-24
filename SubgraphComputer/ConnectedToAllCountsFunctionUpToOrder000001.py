import numpy as np
def connected_to_disconnected_counts(cIn):
	numC = len(cIn)
	if numC==1:
		orderTemp = 1
		cOut = np.zeros(1)
	else:
		print("ERROR IN connected_to_disconnected")
	if orderTemp>=1:
		cOut[0] = cIn[0]
	return cOut