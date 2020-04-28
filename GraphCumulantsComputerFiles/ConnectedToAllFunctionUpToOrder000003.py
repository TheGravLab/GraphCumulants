import numpy as np
def connected_to_disconnected(momIn,nIn):
	numMom = len(momIn)
	if numMom==1:
		orderTemp = 1
		momOut = np.zeros(1)
	elif numMom==2:
		orderTemp = 2
		momOut = np.zeros(3)
	elif numMom==5:
		orderTemp = 3
		momOut = np.zeros(8)
	else:
		print("ERROR IN connected_to_disconnected")
	if orderTemp>=1:
		num000000 = ((-1 + nIn)*nIn)/2.
	if orderTemp>=2:
		num000001 = ((-2 + nIn)*(-1 + nIn)*nIn)/2.
		num000002 = ((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/8.
	if orderTemp>=3:
		num000003 = ((-2 + nIn)*(-1 + nIn)*nIn)/6.
		num000004 = ((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/6.
		num000005 = ((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/2.
		num000006 = ((-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/4.
		num000007 = ((-5 + nIn)*(-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/48.
	if orderTemp>=1:
		momOut[0] = momIn[0]
	if orderTemp>=2:
		momOut[1] = momIn[1]
		momOut[2] = (-(momOut[0]*num000000)/2. + (momOut[0]**2*num000000**2)/2. - momOut[1]*num000001)/num000002
	if orderTemp>=3:
		momOut[3] = momIn[2]
		momOut[4] = momIn[3]
		momOut[5] = momIn[4]
		momOut[6] = (-2*momOut[1]*num000001 + momOut[0]*momOut[1]*num000000*num000001 - 3*momOut[3]*num000003 - 3*momOut[4]*num000004 - 2*momOut[5]*num000005)/num000006
		momOut[7] = (-(momOut[0]*num000000)/6. + (momOut[0]**3*num000000**3)/6. - momOut[1]*num000001 - momOut[2]*num000002 - momOut[3]*num000003 - momOut[4]*num000004 - momOut[5]*num000005 - momOut[6]*num000006)/num000007
	return momOut