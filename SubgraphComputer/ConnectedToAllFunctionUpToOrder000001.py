import numpy as np
def connected_to_disconnected(momIn,nIn):
	numMom = len(momIn)
	if numMom==1:
		orderTemp = 1
		momOut = np.zeros(1)
	else:
		print("ERROR IN connected_to_disconnected")
	if orderTemp>=1:
		num000000 = ((-1 + nIn)*nIn)/2.
	if orderTemp>=1:
		momOut[0] = momIn[0]
	return momOut