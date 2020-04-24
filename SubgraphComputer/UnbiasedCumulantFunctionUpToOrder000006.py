import numpy as np
def moments_to_unbiased_cumulants(momIn):
	numMom = len(momIn)
	if numMom==1:
		orderTemp = 1
		cumOut = np.zeros(1)
	elif numMom==3:
		orderTemp = 2
		cumOut = np.zeros(3)
	elif numMom==8:
		orderTemp = 3
		cumOut = np.zeros(8)
	elif numMom==19:
		orderTemp = 4
		cumOut = np.zeros(19)
	elif numMom==45:
		orderTemp = 5
		cumOut = np.zeros(45)
	elif numMom==113:
		orderTemp = 6
		cumOut = np.zeros(113)
	else:
		print("ERROR IN moments_to_unbiased_cumulants")
	if orderTemp>=1:
		cumOut[0] = momIn[0]
	if orderTemp>=2:
		cumOut[1] = momIn[1] - momIn[2]
		cumOut[2] = 0
	if orderTemp>=3:
		cumOut[3] = momIn[3] - 3*momIn[6] + 2*momIn[7]
		cumOut[4] = momIn[4] - 3*momIn[6] + 2*momIn[7]
		cumOut[5] = momIn[5] - 2*momIn[6] + momIn[7]
		cumOut[6] = 0
		cumOut[7] = 0
	if orderTemp>=4:
		cumOut[8] = momIn[8] - momIn[13] - momIn[14] - 2*momIn[15] - 2*momIn[16] + 9*momIn[17] - 4*momIn[18]
		cumOut[9] = momIn[9] - 4*momIn[15] - 2*momIn[16] + 8*momIn[17] - 3*momIn[18]
		cumOut[10] = momIn[10] - 4*momIn[14] - 3*momIn[16] + 12*momIn[17] - 6*momIn[18]
		cumOut[11] = momIn[11] - momIn[14] - 2*momIn[15] - momIn[16] + 5*momIn[17] - 2*momIn[18]
		cumOut[12] = momIn[12] - 2*momIn[15] - momIn[16] + 3*momIn[17] - momIn[18]
		cumOut[13] = 0
		cumOut[14] = 0
		cumOut[15] = 0
		cumOut[16] = 0
		cumOut[17] = 0
		cumOut[18] = 0
	if orderTemp>=5:
		cumOut[19] = momIn[19] - 4*momIn[31] - 2*momIn[32] - momIn[33] - 2*momIn[36] - 4*momIn[38] + 4*momIn[39] + 4*momIn[40] + 10*momIn[41] + 20*momIn[42] - 40*momIn[43] + 14*momIn[44]
		cumOut[20] = momIn[20] - 2*momIn[31] - momIn[32] - momIn[34] - 2*momIn[35] - 2*momIn[36] - 4*momIn[38] + 2*momIn[39] + 6*momIn[40] + 8*momIn[41] + 17*momIn[42] - 34*momIn[43] + 12*momIn[44]
		cumOut[21] = momIn[21] - 2*momIn[31] - 2*momIn[35] - 2*momIn[36] - momIn[37] - 3*momIn[38] + momIn[39] + 4*momIn[40] + 8*momIn[41] + 12*momIn[42] - 24*momIn[43] + 8*momIn[44]
		cumOut[22] = momIn[22] - momIn[31] - momIn[32] - momIn[35] - 2*momIn[37] - 2*momIn[38] + momIn[39] + momIn[40] + 6*momIn[41] + 7*momIn[42] - 13*momIn[43] + 4*momIn[44]
		cumOut[23] = momIn[23] - momIn[33] - 2*momIn[35] - momIn[36] - 2*momIn[37] - 4*momIn[38] + 2*momIn[40] + 10*momIn[41] + 11*momIn[42] - 20*momIn[43] + 6*momIn[44]
		cumOut[24] = momIn[24] - 5*momIn[37] - 5*momIn[38] + 10*momIn[41] + 10*momIn[42] - 15*momIn[43] + 4*momIn[44]
		cumOut[25] = momIn[25] - 5*momIn[34] - 10*momIn[36] + 20*momIn[40] + 30*momIn[42] - 60*momIn[43] + 24*momIn[44]
		cumOut[26] = momIn[26] - momIn[34] - 3*momIn[35] - momIn[36] - 3*momIn[38] + 4*momIn[40] + 6*momIn[41] + 9*momIn[42] - 18*momIn[43] + 6*momIn[44]
		cumOut[27] = momIn[27] - 4*momIn[35] - 2*momIn[36] + 4*momIn[40] + 4*momIn[41] + 5*momIn[42] - 12*momIn[43] + 4*momIn[44]
		cumOut[28] = momIn[28] - 2*momIn[35] - momIn[37] - 2*momIn[38] + momIn[40] + 4*momIn[41] + 4*momIn[42] - 7*momIn[43] + 2*momIn[44]
		cumOut[29] = momIn[29] - momIn[35] - momIn[36] - 2*momIn[37] - momIn[38] + momIn[40] + 4*momIn[41] + 4*momIn[42] - 7*momIn[43] + 2*momIn[44]
		cumOut[30] = momIn[30] - 2*momIn[37] - 2*momIn[38] + 3*momIn[41] + 3*momIn[42] - 4*momIn[43] + momIn[44]
		cumOut[31] = 0
		cumOut[32] = 0
		cumOut[33] = 0
		cumOut[34] = 0
		cumOut[35] = 0
		cumOut[36] = 0
		cumOut[37] = 0
		cumOut[38] = 0
		cumOut[39] = 0
		cumOut[40] = 0
		cumOut[41] = 0
		cumOut[42] = 0
		cumOut[43] = 0
		cumOut[44] = 0
	if orderTemp>=6:
		cumOut[45] = momIn[45] - 6*momIn[75] - 12*momIn[80] - 4*momIn[81] - 6*momIn[97] + 24*momIn[98] + 24*momIn[99] + 3*momIn[100] + 24*momIn[103] + 48*momIn[105] + 16*momIn[106] - 24*momIn[107] - 48*momIn[108] - 168*momIn[109] - 24*momIn[110] + 216*momIn[111] - 64*momIn[112]
		cumOut[46] = momIn[46] - momIn[75] - 2*momIn[77] - 2*momIn[78] - 4*momIn[80] - momIn[82] - 2*momIn[83] - momIn[84] - momIn[88] - momIn[90] - 3*momIn[93] - 2*momIn[94] - 2*momIn[96] - 2*momIn[97] + 10*momIn[98] + 8*momIn[99] + 2*momIn[100] + 2*momIn[101] + 8*momIn[102] + 21*momIn[103] + 4*momIn[104] + 42*momIn[105] + 12*momIn[106] - 22*momIn[107] - 44*momIn[108] - 118*momIn[109] - 8*momIn[110] + 148*momIn[111] - 42*momIn[112]
		cumOut[47] = momIn[47] - momIn[76] - 2*momIn[77] - 4*momIn[79] - 4*momIn[80] - 4*momIn[96] - 4*momIn[97] + 8*momIn[98] + 10*momIn[99] + momIn[101] + 4*momIn[102] + 4*momIn[103] + 8*momIn[104] + 32*momIn[105] + 8*momIn[106] - 8*momIn[107] - 32*momIn[108] - 73*momIn[109] - 8*momIn[110] + 88*momIn[111] - 24*momIn[112]
		cumOut[48] = momIn[48] - momIn[75] - 2*momIn[78] - 2*momIn[79] - 3*momIn[80] - momIn[81] - momIn[82] - 4*momIn[93] - 2*momIn[94] - 2*momIn[96] - 2*momIn[97] + 8*momIn[98] + 6*momIn[99] + momIn[100] + 8*momIn[102] + 14*momIn[103] + 6*momIn[104] + 32*momIn[105] + 8*momIn[106] - 14*momIn[107] - 36*momIn[108] - 82*momIn[109] - 6*momIn[110] + 102*momIn[111] - 28*momIn[112]
		cumOut[49] = momIn[49] - momIn[78] - 2*momIn[79] - 2*momIn[80] - 2*momIn[82] - momIn[83] - momIn[84] - momIn[85] - 2*momIn[93] - 2*momIn[94] - 4*momIn[96] - 2*momIn[97] + 4*momIn[98] + 4*momIn[99] + 2*momIn[100] + 6*momIn[102] + 8*momIn[103] + 11*momIn[104] + 37*momIn[105] + 8*momIn[106] - 8*momIn[107] - 40*momIn[108] - 74*momIn[109] - 3*momIn[110] + 86*momIn[111] - 22*momIn[112]
		cumOut[50] = momIn[50] - 6*momIn[82] - 3*momIn[84] - momIn[90] - 6*momIn[93] - 6*momIn[97] + 6*momIn[100] + 12*momIn[102] + 12*momIn[103] + 6*momIn[104] + 48*momIn[105] + 8*momIn[106] - 12*momIn[107] - 48*momIn[108] - 87*momIn[109] + 102*momIn[111] - 26*momIn[112]
		cumOut[51] = momIn[51] - 3*momIn[77] - 3*momIn[80] - momIn[81] - momIn[86] - 2*momIn[87] - 2*momIn[88] - 6*momIn[93] - 6*momIn[94] + 6*momIn[98] + 6*momIn[99] + 7*momIn[101] + 12*momIn[102] + 32*momIn[103] + 36*momIn[105] + 12*momIn[106] - 34*momIn[107] - 36*momIn[108] - 126*momIn[109] - 6*momIn[110] + 162*momIn[111] - 48*momIn[112]
		cumOut[52] = momIn[52] - momIn[77] - 2*momIn[78] - momIn[80] - momIn[87] - momIn[88] - momIn[89] - momIn[90] - momIn[92] - 4*momIn[93] - momIn[94] - 2*momIn[96] - 2*momIn[97] + 4*momIn[98] + momIn[99] + 2*momIn[101] + 11*momIn[102] + 17*momIn[103] + 4*momIn[104] + 25*momIn[105] + 7*momIn[106] - 18*momIn[107] - 28*momIn[108] - 68*momIn[109] - 2*momIn[110] + 86*momIn[111] - 24*momIn[112]
		cumOut[53] = momIn[53] - momIn[77] - momIn[79] - momIn[80] - momIn[83] - momIn[87] - 2*momIn[91] - 2*momIn[93] - 2*momIn[96] - 2*momIn[97] + 2*momIn[98] + 3*momIn[99] + momIn[101] + 7*momIn[102] + 3*momIn[103] + 4*momIn[104] + 21*momIn[105] + 4*momIn[106] - 6*momIn[107] - 20*momIn[108] - 39*momIn[109] - 2*momIn[110] + 46*momIn[111] - 12*momIn[112]
		cumOut[54] = momIn[54] - 2*momIn[82] - momIn[84] - 2*momIn[87] - momIn[88] - 2*momIn[92] - 2*momIn[93] - 2*momIn[94] - 4*momIn[96] - 2*momIn[97] + 2*momIn[100] + 2*momIn[101] + 8*momIn[102] + 10*momIn[103] + 8*momIn[104] + 30*momIn[105] + 7*momIn[106] - 10*momIn[107] - 32*momIn[108] - 60*momIn[109] + 70*momIn[111] - 18*momIn[112]
		cumOut[55] = momIn[55] - 3*momIn[78] - 3*momIn[91] - 6*momIn[93] - 3*momIn[94] + 3*momIn[98] + 12*momIn[102] + 12*momIn[103] + 3*momIn[104] + 21*momIn[105] + 4*momIn[106] - 12*momIn[107] - 24*momIn[108] - 48*momIn[109] - momIn[110] + 60*momIn[111] - 16*momIn[112]
		cumOut[56] = momIn[56] - momIn[78] - momIn[79] - momIn[80] - momIn[91] - momIn[92] - momIn[93] - momIn[94] - momIn[95] - 2*momIn[96] - momIn[97] + 2*momIn[98] + momIn[99] + 4*momIn[102] + 4*momIn[103] + 6*momIn[104] + 15*momIn[105] + 3*momIn[106] - 4*momIn[107] - 16*momIn[108] - 28*momIn[109] - momIn[110] + 32*momIn[111] - 8*momIn[112]
		cumOut[57] = momIn[57] - 2*momIn[79] - momIn[80] - momIn[81] - momIn[89] - 2*momIn[92] - 2*momIn[93] + 2*momIn[98] + 3*momIn[99] + 6*momIn[102] + 6*momIn[103] + 4*momIn[104] + 6*momIn[105] + 2*momIn[106] - 6*momIn[107] - 12*momIn[108] - 23*momIn[109] - 2*momIn[110] + 30*momIn[111] - 8*momIn[112]
		cumOut[58] = momIn[58] - 2*momIn[82] - momIn[89] - 2*momIn[91] - 4*momIn[93] - 2*momIn[94] - momIn[95] - 2*momIn[96] - momIn[97] + momIn[100] + 10*momIn[102] + 8*momIn[103] + 6*momIn[104] + 22*momIn[105] + 4*momIn[106] - 8*momIn[107] - 24*momIn[108] - 41*momIn[109] + 48*momIn[111] - 12*momIn[112]
		cumOut[59] = momIn[59] - 2*momIn[82] - momIn[90] - 4*momIn[92] - 4*momIn[93] - 2*momIn[96] - 2*momIn[97] + momIn[100] + 8*momIn[102] + 10*momIn[103] + 8*momIn[104] + 20*momIn[105] + 4*momIn[106] - 8*momIn[107] - 24*momIn[108] - 41*momIn[109] + 48*momIn[111] - 12*momIn[112]
		cumOut[60] = momIn[60] - momIn[79] - momIn[80] - momIn[83] - momIn[92] - 2*momIn[95] - 2*momIn[96] + momIn[98] + 2*momIn[99] + momIn[102] + momIn[103] + 6*momIn[104] + 9*momIn[105] + 2*momIn[106] - momIn[107] - 10*momIn[108] - 16*momIn[109] - momIn[110] + 17*momIn[111] - 4*momIn[112]
		cumOut[61] = momIn[61] - momIn[82] - momIn[84] - 2*momIn[91] - momIn[93] - 2*momIn[95] - 2*momIn[96] - 2*momIn[97] + momIn[100] + 4*momIn[102] + momIn[103] + 6*momIn[104] + 18*momIn[105] + 3*momIn[106] - 2*momIn[107] - 16*momIn[108] - 25*momIn[109] + 26*momIn[111] - 6*momIn[112]
		cumOut[62] = momIn[62] - momIn[85] - momIn[91] - 2*momIn[92] - 2*momIn[93] - momIn[94] - 2*momIn[95] - 4*momIn[96] - 2*momIn[97] + 4*momIn[102] + 4*momIn[103] + 11*momIn[104] + 23*momIn[105] + 4*momIn[106] - 3*momIn[107] - 22*momIn[108] - 34*momIn[109] + 35*momIn[111] - 8*momIn[112]
		cumOut[63] = momIn[63] - 6*momIn[95] - 6*momIn[96] - 3*momIn[97] + 12*momIn[104] + 24*momIn[105] + 4*momIn[106] - 18*momIn[108] - 27*momIn[109] + 24*momIn[111] - 5*momIn[112]
		cumOut[64] = momIn[64] - 6*momIn[86] - 15*momIn[88] - 10*momIn[90] + 30*momIn[101] + 120*momIn[103] + 30*momIn[106] - 120*momIn[107] - 270*momIn[109] + 360*momIn[111] - 120*momIn[112]
		cumOut[65] = momIn[65] - momIn[86] - 4*momIn[87] - momIn[88] - 6*momIn[93] - 4*momIn[94] + 5*momIn[101] + 12*momIn[102] + 18*momIn[103] + 24*momIn[105] + 6*momIn[106] - 20*momIn[107] - 24*momIn[108] - 66*momIn[109] + 84*momIn[111] - 24*momIn[112]
		cumOut[66] = momIn[66] - 2*momIn[87] - momIn[88] - 3*momIn[89] - momIn[90] - 3*momIn[93] + 2*momIn[101] + 12*momIn[102] + 12*momIn[103] + 6*momIn[105] + 3*momIn[106] - 14*momIn[107] - 12*momIn[108] - 30*momIn[109] + 42*momIn[111] - 12*momIn[112]
		cumOut[67] = momIn[67] - 2*momIn[87] - 2*momIn[91] - 2*momIn[93] - momIn[96] - 2*momIn[97] + momIn[101] + 6*momIn[102] + 2*momIn[103] + 2*momIn[104] + 14*momIn[105] + 2*momIn[106] - 4*momIn[107] - 12*momIn[108] - 21*momIn[109] + 24*momIn[111] - 6*momIn[112]
		cumOut[68] = momIn[68] - momIn[87] - momIn[88] - 3*momIn[92] - momIn[94] - 3*momIn[96] + momIn[101] + 3*momIn[102] + 5*momIn[103] + 6*momIn[104] + 9*momIn[105] + 3*momIn[106] - 4*momIn[107] - 12*momIn[108] - 21*momIn[109] + 24*momIn[111] - 6*momIn[112]
		cumOut[69] = momIn[69] - momIn[89] - 2*momIn[91] - momIn[92] - 2*momIn[93] - momIn[94] + 6*momIn[102] + 4*momIn[103] + 2*momIn[104] + 6*momIn[105] + momIn[106] - 4*momIn[107] - 8*momIn[108] - 13*momIn[109] + 16*momIn[111] - 4*momIn[112]
		cumOut[70] = momIn[70] - momIn[90] - 4*momIn[92] - 2*momIn[93] + 4*momIn[102] + 6*momIn[103] + 4*momIn[104] + 4*momIn[105] + momIn[106] - 4*momIn[107] - 8*momIn[108] - 13*momIn[109] + 16*momIn[111] - 4*momIn[112]
		cumOut[71] = momIn[71] - 3*momIn[91] - 3*momIn[96] + 3*momIn[102] + 3*momIn[104] + 6*momIn[105] + 2*momIn[106] - momIn[107] - 6*momIn[108] - 9*momIn[109] + 9*momIn[111] - 2*momIn[112]
		cumOut[72] = momIn[72] - momIn[91] - momIn[92] - momIn[93] - momIn[95] - momIn[96] - momIn[97] + 2*momIn[102] + momIn[103] + 3*momIn[104] + 7*momIn[105] + momIn[106] - momIn[107] - 6*momIn[108] - 9*momIn[109] + 9*momIn[111] - 2*momIn[112]
		cumOut[73] = momIn[73] - momIn[92] - momIn[93] - momIn[94] - 2*momIn[95] - momIn[96] + momIn[102] + 2*momIn[103] + 4*momIn[104] + 6*momIn[105] + momIn[106] - momIn[107] - 6*momIn[108] - 9*momIn[109] + 9*momIn[111] - 2*momIn[112]
		cumOut[74] = momIn[74] - 2*momIn[95] - 2*momIn[96] - momIn[97] + 3*momIn[104] + 6*momIn[105] + momIn[106] - 4*momIn[108] - 6*momIn[109] + 5*momIn[111] - momIn[112]
		cumOut[75] = 0
		cumOut[76] = 0
		cumOut[77] = 0
		cumOut[78] = 0
		cumOut[79] = 0
		cumOut[80] = 0
		cumOut[81] = 0
		cumOut[82] = 0
		cumOut[83] = 0
		cumOut[84] = 0
		cumOut[85] = 0
		cumOut[86] = 0
		cumOut[87] = 0
		cumOut[88] = 0
		cumOut[89] = 0
		cumOut[90] = 0
		cumOut[91] = 0
		cumOut[92] = 0
		cumOut[93] = 0
		cumOut[94] = 0
		cumOut[95] = 0
		cumOut[96] = 0
		cumOut[97] = 0
		cumOut[98] = 0
		cumOut[99] = 0
		cumOut[100] = 0
		cumOut[101] = 0
		cumOut[102] = 0
		cumOut[103] = 0
		cumOut[104] = 0
		cumOut[105] = 0
		cumOut[106] = 0
		cumOut[107] = 0
		cumOut[108] = 0
		cumOut[109] = 0
		cumOut[110] = 0
		cumOut[111] = 0
		cumOut[112] = 0
	return cumOut