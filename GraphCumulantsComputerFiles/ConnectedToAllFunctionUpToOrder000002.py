import numpy as np
def connected_to_disconnected(momIn,nIn):
	numMom = len(momIn)
	if numMom==1:
		orderTemp = 1
		momOut = np.zeros(1)
	elif numMom==2:
		orderTemp = 2
		momOut = np.zeros(3)
	else:
		print("ERROR IN connected_to_disconnected")
	if orderTemp>=1:
		num000000 = ((-1 + nIn)*nIn)/2.
	if orderTemp>=2:
		num000001 = ((-2 + nIn)*(-1 + nIn)*nIn)/2.
		num000002 = ((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/8.
	if orderTemp>=1:
		momOut[0] = momIn[0]
	if orderTemp>=2:
		momOut[1] = momIn[1]
		momOut[2] = (-(momOut[0]*num000000)/2. + (momOut[0]**2*num000000**2)/2. - momOut[1]*num000001)/num000002
	return momOut