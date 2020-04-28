import numpy as np
def cumulants_to_moments(cumIn):
	numCum = len(cumIn)
	if numCum==1:
		orderTemp = 1
		momOut = np.zeros(1)
	else:
		print("ERROR IN cumulants_to_moments")
	if orderTemp>=1:
		momOut[0] = cumIn[0]
	return momOut