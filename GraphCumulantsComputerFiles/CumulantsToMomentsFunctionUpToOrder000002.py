import numpy as np
def cumulants_to_moments(cumIn):
	numCum = len(cumIn)
	if numCum==1:
		orderTemp = 1
		momOut = np.zeros(1)
	elif numCum==3:
		orderTemp = 2
		momOut = np.zeros(3)
	else:
		print("ERROR IN cumulants_to_moments")
	if orderTemp>=1:
		momOut[0] = cumIn[0]
	if orderTemp>=2:
		momOut[1] = cumIn[0]**2 + cumIn[1]
		momOut[2] = cumIn[0]**2 + cumIn[2]
	return momOut