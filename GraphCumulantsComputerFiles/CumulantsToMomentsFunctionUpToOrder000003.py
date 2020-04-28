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
	return momOut