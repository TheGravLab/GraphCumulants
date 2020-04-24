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
	elif numMom==10:
		orderTemp = 4
		momOut = np.zeros(19)
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
	if orderTemp>=4:
		num000008 = ((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/2.
		num000009 = ((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/8.
		num000010 = ((-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/24.
		num000011 = ((-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/2.
		num000012 = ((-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/2.
		num000013 = ((-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/12.
		num000014 = ((-5 + nIn)*(-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/12.
		num000015 = ((-5 + nIn)*(-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/4.
		num000016 = ((-5 + nIn)*(-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/8.
		num000017 = ((-6 + nIn)*(-5 + nIn)*(-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/16.
		num000018 = ((-7 + nIn)*(-6 + nIn)*(-5 + nIn)*(-4 + nIn)*(-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)/384.
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
	if orderTemp>=4:
		momOut[8] = momIn[5]
		momOut[9] = momIn[6]
		momOut[10] = momIn[7]
		momOut[11] = momIn[8]
		momOut[12] = momIn[9]
		momOut[13] = (-3*momOut[3]*num000003 + momOut[0]*momOut[3]*num000000*num000003 - momOut[8]*num000008)/num000013
		momOut[14] = (-3*momOut[4]*num000004 + momOut[0]*momOut[4]*num000000*num000004 - momOut[8]*num000008 - 4*momOut[10]*num000010 - momOut[11]*num000011)/num000014
		momOut[15] = (-3*momOut[5]*num000005 + momOut[0]*momOut[5]*num000000*num000005 - 2*momOut[8]*num000008 - 4*momOut[9]*num000009 - 2*momOut[11]*num000011 - 2*momOut[12]*num000012)/num000015
		momOut[16] = (-(momOut[1]*num000001)/2. + (momOut[1]**2*num000001**2)/2. - 3*momOut[3]*num000003 - 3*momOut[4]*num000004 - momOut[5]*num000005 - 2*momOut[8]*num000008 - 2*momOut[9]*num000009 - 3*momOut[10]*num000010 - momOut[11]*num000011 - momOut[12]*num000012)/num000016
		momOut[17] = (-2*momOut[1]*num000001 + (momOut[0]**2*momOut[1]*num000000**2*num000001)/2. - (15*momOut[3]*num000003)/2. - (15*momOut[4]*num000004)/2. - 5*momOut[5]*num000005 - (5*momOut[6]*num000006)/2. - 5*momOut[8]*num000008 - 4*momOut[9]*num000009 - 6*momOut[10]*num000010 - 4*momOut[11]*num000011 - 3*momOut[12]*num000012 - 3*momOut[13]*num000013 - 3*momOut[14]*num000014 - 2*momOut[15]*num000015 - 2*momOut[16]*num000016)/num000017
		momOut[18] = (-(momOut[0]*num000000)/24. + (momOut[0]**4*num000000**4)/24. - (7*momOut[1]*num000001)/12. - (7*momOut[2]*num000002)/12. - (3*momOut[3]*num000003)/2. - (3*momOut[4]*num000004)/2. - (3*momOut[5]*num000005)/2. - (3*momOut[6]*num000006)/2. - (3*momOut[7]*num000007)/2. - momOut[8]*num000008 - momOut[9]*num000009 - momOut[10]*num000010 - momOut[11]*num000011 - momOut[12]*num000012 - momOut[13]*num000013 - momOut[14]*num000014 - momOut[15]*num000015 - momOut[16]*num000016 - momOut[17]*num000017)/num000018
	return momOut