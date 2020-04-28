import numpy as np
def connected_to_disconnected_counts(cIn):
	numC = len(cIn)
	if numC==1:
		orderTemp = 1
		cOut = np.zeros(1)
	elif numC==2:
		orderTemp = 2
		cOut = np.zeros(3)
	elif numC==5:
		orderTemp = 3
		cOut = np.zeros(8)
	elif numC==10:
		orderTemp = 4
		cOut = np.zeros(19)
	elif numC==22:
		orderTemp = 5
		cOut = np.zeros(45)
	elif numC==52:
		orderTemp = 6
		cOut = np.zeros(113)
	else:
		print("ERROR IN connected_to_disconnected")
	if orderTemp>=1:
		cOut[0] = cIn[0]
	if orderTemp>=2:
		cOut[1] = cIn[1]
		cOut[2] = -cOut[0]/2. + cOut[0]**2/2. - cOut[1]
	if orderTemp>=3:
		cOut[3] = cIn[2]
		cOut[4] = cIn[3]
		cOut[5] = cIn[4]
		cOut[6] = -2*cOut[1] + cOut[0]*cOut[1] - 3*cOut[3] - 3*cOut[4] - 2*cOut[5]
		cOut[7] = -cOut[0]/6. + cOut[0]**3/6. - cOut[1] - cOut[2] - cOut[3] - cOut[4] - cOut[5] - cOut[6]
	if orderTemp>=4:
		cOut[8] = cIn[5]
		cOut[9] = cIn[6]
		cOut[10] = cIn[7]
		cOut[11] = cIn[8]
		cOut[12] = cIn[9]
		cOut[13] = -3*cOut[3] + cOut[0]*cOut[3] - cOut[8]
		cOut[14] = -3*cOut[4] + cOut[0]*cOut[4] - cOut[8] - 4*cOut[10] - cOut[11]
		cOut[15] = -3*cOut[5] + cOut[0]*cOut[5] - 2*cOut[8] - 4*cOut[9] - 2*cOut[11] - 2*cOut[12]
		cOut[16] = -cOut[1]/2. + cOut[1]**2/2. - 3*cOut[3] - 3*cOut[4] - cOut[5] - 2*cOut[8] - 2*cOut[9] - 3*cOut[10] - cOut[11] - cOut[12]
		cOut[17] = -2*cOut[1] + (cOut[0]**2*cOut[1])/2. - (15*cOut[3])/2. - (15*cOut[4])/2. - 5*cOut[5] - (5*cOut[6])/2. - 5*cOut[8] - 4*cOut[9] - 6*cOut[10] - 4*cOut[11] - 3*cOut[12] - 3*cOut[13] - 3*cOut[14] - 2*cOut[15] - 2*cOut[16]
		cOut[18] = -cOut[0]/24. + cOut[0]**4/24. - (7*cOut[1])/12. - (7*cOut[2])/12. - (3*cOut[3])/2. - (3*cOut[4])/2. - (3*cOut[5])/2. - (3*cOut[6])/2. - (3*cOut[7])/2. - cOut[8] - cOut[9] - cOut[10] - cOut[11] - cOut[12] - cOut[13] - cOut[14] - cOut[15] - cOut[16] - cOut[17]
	if orderTemp>=5:
		cOut[19] = cIn[10]
		cOut[20] = cIn[11]
		cOut[21] = cIn[12]
		cOut[22] = cIn[13]
		cOut[23] = cIn[14]
		cOut[24] = cIn[15]
		cOut[25] = cIn[16]
		cOut[26] = cIn[17]
		cOut[27] = cIn[18]
		cOut[28] = cIn[19]
		cOut[29] = cIn[20]
		cOut[30] = cIn[21]
		cOut[31] = -4*cOut[8] + cOut[0]*cOut[8] - 4*cOut[19] - 2*cOut[20] - 2*cOut[21] - cOut[22]
		cOut[32] = -3*cOut[3] + cOut[1]*cOut[3] - 2*cOut[8] - 2*cOut[19] - cOut[20] - cOut[22]
		cOut[33] = -4*cOut[9] + cOut[0]*cOut[9] - cOut[19] - cOut[23]
		cOut[34] = -4*cOut[10] + cOut[0]*cOut[10] - cOut[20] - 5*cOut[25] - cOut[26]
		cOut[35] = -4*cOut[11] + cOut[0]*cOut[11] - 2*cOut[20] - 2*cOut[21] - cOut[22] - 2*cOut[23] - 3*cOut[26] - 4*cOut[27] - 2*cOut[28] - cOut[29]
		cOut[36] = -3*cOut[4] + cOut[1]*cOut[4] - 2*cOut[8] - 12*cOut[10] - cOut[11] - 2*cOut[19] - 2*cOut[20] - 2*cOut[21] - cOut[23] - 10*cOut[25] - cOut[26] - 2*cOut[27] - cOut[29]
		cOut[37] = -4*cOut[12] + cOut[0]*cOut[12] - cOut[21] - 2*cOut[22] - 2*cOut[23] - 5*cOut[24] - cOut[28] - 2*cOut[29] - 2*cOut[30]
		cOut[38] = -2*cOut[5] + cOut[1]*cOut[5] - 6*cOut[8] - 8*cOut[9] - 4*cOut[11] - 2*cOut[12] - 4*cOut[19] - 4*cOut[20] - 3*cOut[21] - 2*cOut[22] - 4*cOut[23] - 5*cOut[24] - 3*cOut[26] - 2*cOut[28] - cOut[29] - 2*cOut[30]
		cOut[39] = (-9*cOut[3])/2. + (cOut[0]**2*cOut[3])/2. - (7*cOut[8])/2. - (7*cOut[13])/2. - 2*cOut[19] - cOut[20] - cOut[21] - cOut[22] - cOut[31] - cOut[32]
		cOut[40] = (-9*cOut[4])/2. + (cOut[0]**2*cOut[4])/2. - (7*cOut[8])/2. - 14*cOut[10] - (7*cOut[11])/2. - (7*cOut[14])/2. - 2*cOut[19] - 4*cOut[20] - 2*cOut[21] - cOut[22] - cOut[23] - 10*cOut[25] - 4*cOut[26] - 2*cOut[27] - cOut[28] - cOut[29] - cOut[31] - 4*cOut[34] - cOut[35] - cOut[36]
		cOut[41] = (-9*cOut[5])/2. + (cOut[0]**2*cOut[5])/2. - 7*cOut[8] - 14*cOut[9] - 7*cOut[11] - 7*cOut[12] - (7*cOut[15])/2. - 6*cOut[19] - 4*cOut[20] - 5*cOut[21] - 4*cOut[22] - 6*cOut[23] - 5*cOut[24] - 3*cOut[26] - 4*cOut[27] - 4*cOut[28] - 3*cOut[29] - 3*cOut[30] - 2*cOut[31] - 4*cOut[33] - 2*cOut[35] - 2*cOut[37] - cOut[38]
		cOut[42] = -cOut[1] + (cOut[0]*cOut[1]**2)/2. - (21*cOut[3])/2. - (21*cOut[4])/2. - 4*cOut[5] - cOut[6]/2. - 16*cOut[8] - 12*cOut[9] - 24*cOut[10] - 9*cOut[11] - 6*cOut[12] - 3*cOut[13] - 3*cOut[14] - cOut[15] - 4*cOut[16] - 10*cOut[19] - 9*cOut[20] - 7*cOut[21] - 5*cOut[22] - 6*cOut[23] - 5*cOut[24] - 15*cOut[25] - 6*cOut[26] - 5*cOut[27] - 3*cOut[28] - 4*cOut[29] - 3*cOut[30] - 2*cOut[31] - 3*cOut[32] - 2*cOut[33] - 3*cOut[34] - cOut[35] - 3*cOut[36] - cOut[37] - 2*cOut[38]
		cOut[43] = (-4*cOut[1])/3. + (cOut[0]**3*cOut[1])/6. - (19*cOut[3])/2. - (19*cOut[4])/2. - (19*cOut[5])/3. - (19*cOut[6])/6. - 15*cOut[8] - 12*cOut[9] - 18*cOut[10] - 12*cOut[11] - 9*cOut[12] - 9*cOut[13] - 9*cOut[14] - 6*cOut[15] - 6*cOut[16] - 3*cOut[17] - 8*cOut[19] - 8*cOut[20] - 7*cOut[21] - 6*cOut[22] - 6*cOut[23] - 5*cOut[24] - 10*cOut[25] - 7*cOut[26] - 6*cOut[27] - 5*cOut[28] - 5*cOut[29] - 4*cOut[30] - 5*cOut[31] - 4*cOut[32] - 4*cOut[33] - 6*cOut[34] - 4*cOut[35] - 4*cOut[36] - 3*cOut[37] - 3*cOut[38] - 3*cOut[39] - 3*cOut[40] - 2*cOut[41] - 2*cOut[42]
		cOut[44] = -cOut[0]/120. + cOut[0]**5/120. - cOut[1]/4. - cOut[2]/4. - (5*cOut[3])/4. - (5*cOut[4])/4. - (5*cOut[5])/4. - (5*cOut[6])/4. - (5*cOut[7])/4. - 2*cOut[8] - 2*cOut[9] - 2*cOut[10] - 2*cOut[11] - 2*cOut[12] - 2*cOut[13] - 2*cOut[14] - 2*cOut[15] - 2*cOut[16] - 2*cOut[17] - 2*cOut[18] - cOut[19] - cOut[20] - cOut[21] - cOut[22] - cOut[23] - cOut[24] - cOut[25] - cOut[26] - cOut[27] - cOut[28] - cOut[29] - cOut[30] - cOut[31] - cOut[32] - cOut[33] - cOut[34] - cOut[35] - cOut[36] - cOut[37] - cOut[38] - cOut[39] - cOut[40] - cOut[41] - cOut[42] - cOut[43]
	if orderTemp>=6:
		cOut[45] = cIn[22]
		cOut[46] = cIn[23]
		cOut[47] = cIn[24]
		cOut[48] = cIn[25]
		cOut[49] = cIn[26]
		cOut[50] = cIn[27]
		cOut[51] = cIn[28]
		cOut[52] = cIn[29]
		cOut[53] = cIn[30]
		cOut[54] = cIn[31]
		cOut[55] = cIn[32]
		cOut[56] = cIn[33]
		cOut[57] = cIn[34]
		cOut[58] = cIn[35]
		cOut[59] = cIn[36]
		cOut[60] = cIn[37]
		cOut[61] = cIn[38]
		cOut[62] = cIn[39]
		cOut[63] = cIn[40]
		cOut[64] = cIn[41]
		cOut[65] = cIn[42]
		cOut[66] = cIn[43]
		cOut[67] = cIn[44]
		cOut[68] = cIn[45]
		cOut[69] = cIn[46]
		cOut[70] = cIn[47]
		cOut[71] = cIn[48]
		cOut[72] = cIn[49]
		cOut[73] = cIn[50]
		cOut[74] = cIn[51]
		cOut[75] = -5*cOut[19] + cOut[0]*cOut[19] - 6*cOut[45] - cOut[46] - cOut[48]
		cOut[76] = -cOut[3]/2. + cOut[3]**2/2. - cOut[19] - cOut[47]
		cOut[77] = -5*cOut[20] + cOut[0]*cOut[20] - 2*cOut[46] - 2*cOut[47] - 3*cOut[51] - cOut[52] - cOut[53]
		cOut[78] = -5*cOut[21] + cOut[0]*cOut[21] - 2*cOut[46] - 2*cOut[48] - cOut[49] - 2*cOut[52] - 3*cOut[55] - cOut[56]
		cOut[79] = -5*cOut[22] + cOut[0]*cOut[22] - 4*cOut[47] - 2*cOut[48] - 2*cOut[49] - cOut[53] - cOut[56] - 2*cOut[57] - cOut[60]
		cOut[80] = -5*cOut[8] + cOut[1]*cOut[8] - 12*cOut[19] - 6*cOut[20] - 4*cOut[21] - cOut[22] - 12*cOut[45] - 4*cOut[46] - 4*cOut[47] - 3*cOut[48] - 2*cOut[49] - 3*cOut[51] - cOut[52] - cOut[53] - cOut[56] - cOut[57] - cOut[60]
		cOut[81] = cOut[3]*cOut[4] - cOut[8] - 2*cOut[20] - 4*cOut[45] - cOut[48] - cOut[51] - cOut[57]
		cOut[82] = -5*cOut[23] + cOut[0]*cOut[23] - cOut[46] - cOut[48] - 2*cOut[49] - 6*cOut[50] - 2*cOut[54] - 2*cOut[58] - 2*cOut[59] - cOut[61]
		cOut[83] = cOut[3]*cOut[5] - 2*cOut[8] - 4*cOut[19] - cOut[21] - 2*cOut[22] - 2*cOut[46] - cOut[49] - cOut[53] - cOut[60]
		cOut[84] = -4*cOut[9] + cOut[1]*cOut[9] - 4*cOut[19] - 2*cOut[23] - cOut[46] - cOut[49] - 3*cOut[50] - cOut[54] - cOut[61]
		cOut[85] = -5*cOut[24] + cOut[0]*cOut[24] - cOut[49] - cOut[62]
		cOut[86] = -5*cOut[25] + cOut[0]*cOut[25] - cOut[51] - 6*cOut[64] - cOut[65]
		cOut[87] = -5*cOut[26] + cOut[0]*cOut[26] - 2*cOut[51] - cOut[52] - cOut[53] - 2*cOut[54] - 4*cOut[65] - 2*cOut[66] - 2*cOut[67] - cOut[68]
		cOut[88] = -6*cOut[10] + cOut[1]*cOut[10] - 2*cOut[20] - 20*cOut[25] - cOut[26] - cOut[46] - 2*cOut[51] - cOut[52] - cOut[54] - 15*cOut[64] - cOut[65] - cOut[66] - cOut[68]
		cOut[89] = -5*cOut[27] + cOut[0]*cOut[27] - cOut[52] - cOut[57] - cOut[58] - 3*cOut[66] - cOut[69]
		cOut[90] = -cOut[4]/2. + cOut[4]**2/2. - 6*cOut[10] - cOut[19] - cOut[21] - 15*cOut[25] - cOut[27] - cOut[46] - cOut[50] - cOut[52] - cOut[59] - 10*cOut[64] - cOut[66] - cOut[70]
		cOut[91] = -5*cOut[28] + cOut[0]*cOut[28] - 2*cOut[53] - 3*cOut[55] - cOut[56] - 2*cOut[58] - 2*cOut[61] - cOut[62] - 2*cOut[67] - 2*cOut[69] - 3*cOut[71] - cOut[72]
		cOut[92] = -5*cOut[29] + cOut[0]*cOut[29] - cOut[52] - 2*cOut[54] - cOut[56] - 2*cOut[57] - 4*cOut[59] - cOut[60] - 2*cOut[62] - 3*cOut[68] - cOut[69] - 4*cOut[70] - cOut[72] - cOut[73]
		cOut[93] = -4*cOut[11] + cOut[1]*cOut[11] - 8*cOut[20] - 6*cOut[21] - 2*cOut[22] - 4*cOut[23] - 9*cOut[26] - 8*cOut[27] - 2*cOut[28] - cOut[29] - 3*cOut[46] - 4*cOut[48] - 2*cOut[49] - 6*cOut[50] - 6*cOut[51] - 4*cOut[52] - 2*cOut[53] - 2*cOut[54] - 6*cOut[55] - cOut[56] - 2*cOut[57] - 4*cOut[58] - 4*cOut[59] - cOut[61] - 2*cOut[62] - 6*cOut[65] - 3*cOut[66] - 2*cOut[67] - 2*cOut[69] - 2*cOut[70] - cOut[72] - cOut[73]
		cOut[94] = cOut[4]*cOut[5] - 2*cOut[8] - 2*cOut[11] - 4*cOut[19] - 8*cOut[20] - 2*cOut[21] - 2*cOut[23] - 6*cOut[26] - cOut[29] - 2*cOut[46] - 2*cOut[48] - 2*cOut[49] - 6*cOut[51] - cOut[52] - 2*cOut[54] - 3*cOut[55] - cOut[56] - 2*cOut[58] - cOut[62] - 4*cOut[65] - cOut[68] - cOut[69] - cOut[73]
		cOut[95] = -5*cOut[30] + cOut[0]*cOut[30] - cOut[56] - cOut[58] - 2*cOut[60] - 2*cOut[61] - 2*cOut[62] - 6*cOut[63] - cOut[72] - 2*cOut[73] - 2*cOut[74]
		cOut[96] = -3*cOut[12] + cOut[1]*cOut[12] - 4*cOut[21] - 6*cOut[22] - 6*cOut[23] - 10*cOut[24] - 2*cOut[28] - 4*cOut[29] - 2*cOut[30] - 2*cOut[46] - 4*cOut[47] - 2*cOut[48] - 4*cOut[49] - 2*cOut[52] - 2*cOut[53] - 4*cOut[54] - 2*cOut[56] - 2*cOut[58] - 2*cOut[59] - 2*cOut[60] - 2*cOut[61] - 4*cOut[62] - 6*cOut[63] - cOut[67] - 3*cOut[68] - 3*cOut[71] - cOut[72] - cOut[73] - 2*cOut[74]
		cOut[97] = -cOut[5]/2. + cOut[5]**2/2. - cOut[8] - 6*cOut[9] - cOut[11] - cOut[12] - 5*cOut[19] - 2*cOut[20] - 5*cOut[21] - 2*cOut[22] - 5*cOut[23] - 5*cOut[24] - 2*cOut[27] - 3*cOut[28] - cOut[30] - 6*cOut[45] - 2*cOut[46] - 4*cOut[47] - 2*cOut[48] - 2*cOut[49] - 6*cOut[50] - 2*cOut[52] - 2*cOut[53] - 2*cOut[54] - cOut[56] - cOut[58] - 2*cOut[59] - 2*cOut[61] - 2*cOut[62] - 3*cOut[63] - 2*cOut[67] - cOut[72] - cOut[74]
		cOut[98] = -8*cOut[8] + (cOut[0]**2*cOut[8])/2. - 18*cOut[19] - 9*cOut[20] - 9*cOut[21] - (9*cOut[22])/2. - (9*cOut[31])/2. - 12*cOut[45] - 6*cOut[46] - 4*cOut[47] - 5*cOut[48] - 2*cOut[49] - 3*cOut[51] - 3*cOut[52] - 2*cOut[53] - 3*cOut[55] - 2*cOut[56] - cOut[57] - cOut[60] - 4*cOut[75] - 2*cOut[77] - 2*cOut[78] - cOut[79] - cOut[80]
		cOut[99] = -9*cOut[3] + cOut[0]*cOut[1]*cOut[3] - 11*cOut[8] - 3*cOut[13] - 18*cOut[19] - 9*cOut[20] - 4*cOut[21] - 7*cOut[22] - 2*cOut[31] - 5*cOut[32] - 12*cOut[45] - 4*cOut[46] - 6*cOut[47] - 4*cOut[48] - 2*cOut[49] - 3*cOut[51] - cOut[52] - 2*cOut[53] - cOut[56] - 3*cOut[57] - 2*cOut[60] - 2*cOut[75] - 6*cOut[76] - cOut[77] - cOut[79] - cOut[80] - 3*cOut[81] - 2*cOut[83]
		cOut[100] = -8*cOut[9] + (cOut[0]**2*cOut[9])/2. - (9*cOut[19])/2. - (9*cOut[23])/2. - (9*cOut[33])/2. - 3*cOut[45] - cOut[46] - cOut[48] - cOut[49] - 3*cOut[50] - cOut[54] - cOut[58] - cOut[59] - cOut[61] - cOut[75] - cOut[82] - cOut[84]
		cOut[101] = -8*cOut[10] + (cOut[0]**2*cOut[10])/2. - (9*cOut[20])/2. - (45*cOut[25])/2. - (9*cOut[26])/2. - (9*cOut[34])/2. - cOut[46] - cOut[47] - 5*cOut[51] - cOut[52] - cOut[53] - cOut[54] - 15*cOut[64] - 5*cOut[65] - cOut[66] - cOut[67] - cOut[68] - cOut[77] - 5*cOut[86] - cOut[87] - cOut[88]
		cOut[102] = -8*cOut[11] + (cOut[0]**2*cOut[11])/2. - 9*cOut[20] - 9*cOut[21] - (9*cOut[22])/2. - 9*cOut[23] - (27*cOut[26])/2. - 18*cOut[27] - 9*cOut[28] - (9*cOut[29])/2. - (9*cOut[35])/2. - 5*cOut[46] - 4*cOut[47] - 4*cOut[48] - 4*cOut[49] - 6*cOut[50] - 6*cOut[51] - 7*cOut[52] - 5*cOut[53] - 6*cOut[54] - 6*cOut[55] - 3*cOut[56] - 4*cOut[57] - 6*cOut[58] - 4*cOut[59] - cOut[60] - 3*cOut[61] - 2*cOut[62] - 6*cOut[65] - 9*cOut[66] - 6*cOut[67] - 3*cOut[68] - 5*cOut[69] - 2*cOut[70] - 3*cOut[71] - 2*cOut[72] - cOut[73] - 2*cOut[77] - 2*cOut[78] - cOut[79] - 2*cOut[82] - 3*cOut[87] - 4*cOut[89] - 2*cOut[91] - cOut[92] - cOut[93]
		cOut[103] = -9*cOut[4] + cOut[0]*cOut[1]*cOut[4] - 11*cOut[8] - 60*cOut[10] - 7*cOut[11] - 3*cOut[14] - 18*cOut[19] - 28*cOut[20] - 16*cOut[21] - 3*cOut[22] - 7*cOut[23] - 110*cOut[25] - 20*cOut[26] - 14*cOut[27] - 2*cOut[28] - 6*cOut[29] - 2*cOut[31] - 12*cOut[34] - cOut[35] - 5*cOut[36] - 12*cOut[45] - 11*cOut[46] - 4*cOut[47] - 7*cOut[48] - 4*cOut[49] - 6*cOut[50] - 18*cOut[51] - 10*cOut[52] - 3*cOut[53] - 6*cOut[54] - 6*cOut[55] - 3*cOut[56] - 4*cOut[57] - 4*cOut[58] - 6*cOut[59] - cOut[60] - cOut[61] - 2*cOut[62] - 60*cOut[64] - 14*cOut[65] - 9*cOut[66] - 2*cOut[67] - 5*cOut[68] - 3*cOut[69] - 6*cOut[70] - cOut[72] - 2*cOut[73] - 2*cOut[75] - 2*cOut[77] - 2*cOut[78] - cOut[80] - 3*cOut[81] - cOut[82] - 10*cOut[86] - cOut[87] - 4*cOut[88] - 2*cOut[89] - 6*cOut[90] - cOut[92] - cOut[93] - 2*cOut[94]
		cOut[104] = -8*cOut[12] + (cOut[0]**2*cOut[12])/2. - (9*cOut[21])/2. - 9*cOut[22] - 9*cOut[23] - (45*cOut[24])/2. - (9*cOut[28])/2. - 9*cOut[29] - 9*cOut[30] - (9*cOut[37])/2. - 2*cOut[46] - 4*cOut[47] - 4*cOut[48] - 7*cOut[49] - 6*cOut[50] - 2*cOut[52] - 2*cOut[53] - 4*cOut[54] - 3*cOut[55] - 4*cOut[56] - 4*cOut[57] - 4*cOut[58] - 6*cOut[59] - 4*cOut[60] - 4*cOut[61] - 7*cOut[62] - 6*cOut[63] - cOut[67] - 3*cOut[68] - 2*cOut[69] - 4*cOut[70] - 3*cOut[71] - 3*cOut[72] - 3*cOut[73] - 3*cOut[74] - cOut[78] - 2*cOut[79] - 2*cOut[82] - 5*cOut[85] - cOut[91] - 2*cOut[92] - 2*cOut[95] - cOut[96]
		cOut[105] = -6*cOut[5] + cOut[0]*cOut[1]*cOut[5] - 28*cOut[8] - 40*cOut[9] - 20*cOut[11] - 12*cOut[12] - 2*cOut[15] - 52*cOut[19] - 40*cOut[20] - 37*cOut[21] - 24*cOut[22] - 40*cOut[23] - 35*cOut[24] - 27*cOut[26] - 16*cOut[27] - 20*cOut[28] - 13*cOut[29] - 14*cOut[30] - 6*cOut[31] - 8*cOut[33] - 4*cOut[35] - 2*cOut[37] - 5*cOut[38] - 24*cOut[45] - 22*cOut[46] - 16*cOut[47] - 18*cOut[48] - 20*cOut[49] - 24*cOut[50] - 18*cOut[51] - 14*cOut[52] - 13*cOut[53] - 16*cOut[54] - 15*cOut[55] - 10*cOut[56] - 6*cOut[57] - 14*cOut[58] - 12*cOut[59] - 7*cOut[60] - 12*cOut[61] - 13*cOut[62] - 12*cOut[63] - 12*cOut[65] - 6*cOut[66] - 10*cOut[67] - 6*cOut[68] - 6*cOut[69] - 4*cOut[70] - 6*cOut[71] - 6*cOut[72] - 6*cOut[73] - 6*cOut[74] - 4*cOut[75] - 4*cOut[77] - 3*cOut[78] - 2*cOut[79] - 2*cOut[80] - 4*cOut[82] - 3*cOut[83] - 4*cOut[84] - 5*cOut[85] - 3*cOut[87] - 2*cOut[91] - cOut[92] - 2*cOut[93] - 3*cOut[94] - 2*cOut[95] - 2*cOut[96] - 4*cOut[97]
		cOut[106] = -cOut[1]/6. + cOut[1]**3/6. - 4*cOut[3] - 4*cOut[4] - cOut[5] - 10*cOut[8] - 6*cOut[9] - 19*cOut[10] - 4*cOut[11] - 2*cOut[12] - cOut[16] - 16*cOut[19] - 13*cOut[20] - 9*cOut[21] - 5*cOut[22] - 7*cOut[23] - 5*cOut[24] - 30*cOut[25] - 6*cOut[26] - 6*cOut[27] - 2*cOut[28] - 4*cOut[29] - 2*cOut[30] - 3*cOut[32] - 3*cOut[36] - cOut[38] - 8*cOut[45] - 6*cOut[46] - 4*cOut[47] - 4*cOut[48] - 4*cOut[49] - 4*cOut[50] - 6*cOut[51] - 4*cOut[52] - 2*cOut[53] - 4*cOut[54] - 2*cOut[55] - 2*cOut[56] - 2*cOut[57] - 2*cOut[58] - 2*cOut[59] - 2*cOut[60] - 2*cOut[61] - 2*cOut[62] - 2*cOut[63] - 15*cOut[64] - 3*cOut[65] - 3*cOut[66] - cOut[67] - 3*cOut[68] - cOut[69] - cOut[70] - cOut[71] - cOut[72] - cOut[73] - cOut[74] - 2*cOut[80] - 2*cOut[84] - 3*cOut[88] - cOut[93] - cOut[96]
		cOut[107] = (-9*cOut[4])/2. + (cOut[0]**3*cOut[4])/6. - (37*cOut[8])/6. - (74*cOut[10])/3. - (37*cOut[11])/6. - (37*cOut[14])/6. - 8*cOut[19] - 16*cOut[20] - 8*cOut[21] - 4*cOut[22] - 4*cOut[23] - 40*cOut[25] - 16*cOut[26] - 8*cOut[27] - 4*cOut[28] - 4*cOut[29] - 4*cOut[31] - 16*cOut[34] - 4*cOut[35] - 4*cOut[36] - 4*cOut[40] - 4*cOut[45] - 5*cOut[46] - 4*cOut[47] - 3*cOut[48] - 2*cOut[49] - 2*cOut[50] - 10*cOut[51] - 5*cOut[52] - 4*cOut[53] - 4*cOut[54] - 3*cOut[55] - 2*cOut[56] - 2*cOut[57] - 2*cOut[58] - 2*cOut[59] - cOut[60] - cOut[61] - cOut[62] - 20*cOut[64] - 10*cOut[65] - 5*cOut[66] - 4*cOut[67] - 4*cOut[68] - 2*cOut[69] - 2*cOut[70] - cOut[71] - cOut[72] - cOut[73] - 2*cOut[75] - 4*cOut[77] - 2*cOut[78] - cOut[79] - cOut[80] - cOut[81] - cOut[82] - 10*cOut[86] - 4*cOut[87] - 4*cOut[88] - 2*cOut[89] - 2*cOut[90] - cOut[91] - cOut[92] - cOut[93] - cOut[94] - cOut[98] - 4*cOut[101] - cOut[102] - cOut[103]
		cOut[108] = (-9*cOut[5])/2. + (cOut[0]**3*cOut[5])/6. - (37*cOut[8])/3. - (74*cOut[9])/3. - (37*cOut[11])/3. - (37*cOut[12])/3. - (37*cOut[15])/6. - 24*cOut[19] - 16*cOut[20] - 20*cOut[21] - 16*cOut[22] - 24*cOut[23] - 20*cOut[24] - 12*cOut[26] - 16*cOut[27] - 16*cOut[28] - 12*cOut[29] - 12*cOut[30] - 8*cOut[31] - 16*cOut[33] - 8*cOut[35] - 8*cOut[37] - 4*cOut[38] - 4*cOut[41] - 12*cOut[45] - 10*cOut[46] - 8*cOut[47] - 10*cOut[48] - 10*cOut[49] - 12*cOut[50] - 6*cOut[51] - 8*cOut[52] - 7*cOut[53] - 8*cOut[54] - 9*cOut[55] - 7*cOut[56] - 6*cOut[57] - 9*cOut[58] - 8*cOut[59] - 5*cOut[60] - 8*cOut[61] - 7*cOut[62] - 6*cOut[63] - 4*cOut[65] - 6*cOut[66] - 6*cOut[67] - 4*cOut[68] - 6*cOut[69] - 4*cOut[70] - 6*cOut[71] - 5*cOut[72] - 4*cOut[73] - 4*cOut[74] - 6*cOut[75] - 4*cOut[77] - 5*cOut[78] - 4*cOut[79] - 2*cOut[80] - 6*cOut[82] - cOut[83] - 4*cOut[84] - 5*cOut[85] - 3*cOut[87] - 4*cOut[89] - 4*cOut[91] - 3*cOut[92] - 2*cOut[93] - cOut[94] - 3*cOut[95] - 2*cOut[96] - 2*cOut[97] - 2*cOut[98] - 4*cOut[100] - 2*cOut[102] - 2*cOut[104] - cOut[105]
		cOut[109] = -cOut[1] + (cOut[0]**2*cOut[1]**2)/4. - (69*cOut[3])/4. - (69*cOut[4])/4. - 7*cOut[5] - (5*cOut[6])/4. - (93*cOut[8])/2. - 32*cOut[9] - 69*cOut[10] - (55*cOut[11])/2. - (33*cOut[12])/2. - 12*cOut[13] - 12*cOut[14] - (9*cOut[15])/2. - 9*cOut[16] - cOut[17]/2. - 63*cOut[19] - (119*cOut[20])/2. - (91*cOut[21])/2. - (65*cOut[22])/2. - 36*cOut[23] - (55*cOut[24])/2. - (195*cOut[25])/2. - 42*cOut[26] - (65*cOut[27])/2. - (41*cOut[28])/2. - 24*cOut[29] - (33*cOut[30])/2. - 17*cOut[31] - (33*cOut[32])/2. - 13*cOut[33] - (51*cOut[34])/2. - (19*cOut[35])/2. - (33*cOut[36])/2. - (13*cOut[37])/2. - 10*cOut[38] - 3*cOut[39] - 3*cOut[40] - cOut[41] - (9*cOut[42])/2. - 30*cOut[45] - 24*cOut[46] - 19*cOut[47] - 20*cOut[48] - 17*cOut[49] - 18*cOut[50] - 27*cOut[51] - 19*cOut[52] - 14*cOut[53] - 16*cOut[54] - 15*cOut[55] - 12*cOut[56] - 13*cOut[57] - 13*cOut[58] - 14*cOut[59] - 10*cOut[60] - 10*cOut[61] - 11*cOut[62] - 9*cOut[63] - 45*cOut[64] - 21*cOut[65] - 15*cOut[66] - 10*cOut[67] - 12*cOut[68] - 9*cOut[69] - 11*cOut[70] - 6*cOut[71] - 7*cOut[72] - 8*cOut[73] - 6*cOut[74] - 10*cOut[75] - 9*cOut[76] - 9*cOut[77] - 7*cOut[78] - 5*cOut[79] - 7*cOut[80] - 9*cOut[81] - 6*cOut[82] - 6*cOut[83] - 6*cOut[84] - 5*cOut[85] - 15*cOut[86] - 6*cOut[87] - 9*cOut[88] - 5*cOut[89] - 9*cOut[90] - 3*cOut[91] - 4*cOut[92] - 5*cOut[93] - 6*cOut[94] - 3*cOut[95] - 4*cOut[96] - 4*cOut[97] - 2*cOut[98] - 3*cOut[99] - 2*cOut[100] - 3*cOut[101] - cOut[102] - 3*cOut[103] - cOut[104] - 2*cOut[105] - 3*cOut[106]
		cOut[110] = (-9*cOut[3])/2. + (cOut[0]**3*cOut[3])/6. - (37*cOut[8])/6. - (37*cOut[13])/6. - 8*cOut[19] - 4*cOut[20] - 4*cOut[21] - 4*cOut[22] - 4*cOut[31] - 4*cOut[32] - 4*cOut[39] - 4*cOut[45] - 2*cOut[46] - 2*cOut[47] - 2*cOut[48] - cOut[49] - cOut[51] - cOut[52] - cOut[53] - cOut[55] - cOut[56] - cOut[57] - cOut[60] - 2*cOut[75] - 2*cOut[76] - cOut[77] - cOut[78] - cOut[79] - cOut[80] - cOut[81] - cOut[83] - cOut[98] - cOut[99]
		cOut[111] = (-2*cOut[1])/3. + (cOut[0]**4*cOut[1])/24. - (65*cOut[3])/8. - (65*cOut[4])/8. - (65*cOut[5])/12. - (65*cOut[6])/24. - (275*cOut[8])/12. - (55*cOut[9])/3. - (55*cOut[10])/2. - (55*cOut[11])/3. - (55*cOut[12])/4. - (55*cOut[13])/4. - (55*cOut[14])/4. - (55*cOut[15])/6. - (55*cOut[16])/6. - (55*cOut[17])/12. - 28*cOut[19] - 28*cOut[20] - (49*cOut[21])/2. - 21*cOut[22] - 21*cOut[23] - (35*cOut[24])/2. - 35*cOut[25] - (49*cOut[26])/2. - 21*cOut[27] - (35*cOut[28])/2. - (35*cOut[29])/2. - 14*cOut[30] - (35*cOut[31])/2. - 14*cOut[32] - 14*cOut[33] - 21*cOut[34] - 14*cOut[35] - 14*cOut[36] - (21*cOut[37])/2. - (21*cOut[38])/2. - (21*cOut[39])/2. - (21*cOut[40])/2. - 7*cOut[41] - 7*cOut[42] - (7*cOut[43])/2. - 12*cOut[45] - 11*cOut[46] - 10*cOut[47] - 10*cOut[48] - 9*cOut[49] - 9*cOut[50] - 12*cOut[51] - 10*cOut[52] - 9*cOut[53] - 9*cOut[54] - 9*cOut[55] - 8*cOut[56] - 8*cOut[57] - 8*cOut[58] - 8*cOut[59] - 7*cOut[60] - 7*cOut[61] - 7*cOut[62] - 6*cOut[63] - 15*cOut[64] - 11*cOut[65] - 9*cOut[66] - 8*cOut[67] - 8*cOut[68] - 7*cOut[69] - 7*cOut[70] - 6*cOut[71] - 6*cOut[72] - 6*cOut[73] - 5*cOut[74] - 8*cOut[75] - 6*cOut[76] - 8*cOut[77] - 7*cOut[78] - 6*cOut[79] - 6*cOut[80] - 6*cOut[81] - 6*cOut[82] - 5*cOut[83] - 5*cOut[84] - 5*cOut[85] - 10*cOut[86] - 7*cOut[87] - 7*cOut[88] - 6*cOut[89] - 6*cOut[90] - 5*cOut[91] - 5*cOut[92] - 5*cOut[93] - 5*cOut[94] - 4*cOut[95] - 4*cOut[96] - 4*cOut[97] - 5*cOut[98] - 4*cOut[99] - 4*cOut[100] - 6*cOut[101] - 4*cOut[102] - 4*cOut[103] - 3*cOut[104] - 3*cOut[105] - 3*cOut[106] - 3*cOut[107] - 2*cOut[108] - 2*cOut[109] - 3*cOut[110]
		cOut[112] = -cOut[0]/720. + cOut[0]**6/720. - (31*cOut[1])/360. - (31*cOut[2])/360. - (3*cOut[3])/4. - (3*cOut[4])/4. - (3*cOut[5])/4. - (3*cOut[6])/4. - (3*cOut[7])/4. - (13*cOut[8])/6. - (13*cOut[9])/6. - (13*cOut[10])/6. - (13*cOut[11])/6. - (13*cOut[12])/6. - (13*cOut[13])/6. - (13*cOut[14])/6. - (13*cOut[15])/6. - (13*cOut[16])/6. - (13*cOut[17])/6. - (13*cOut[18])/6. - (5*cOut[19])/2. - (5*cOut[20])/2. - (5*cOut[21])/2. - (5*cOut[22])/2. - (5*cOut[23])/2. - (5*cOut[24])/2. - (5*cOut[25])/2. - (5*cOut[26])/2. - (5*cOut[27])/2. - (5*cOut[28])/2. - (5*cOut[29])/2. - (5*cOut[30])/2. - (5*cOut[31])/2. - (5*cOut[32])/2. - (5*cOut[33])/2. - (5*cOut[34])/2. - (5*cOut[35])/2. - (5*cOut[36])/2. - (5*cOut[37])/2. - (5*cOut[38])/2. - (5*cOut[39])/2. - (5*cOut[40])/2. - (5*cOut[41])/2. - (5*cOut[42])/2. - (5*cOut[43])/2. - (5*cOut[44])/2. - cOut[45] - cOut[46] - cOut[47] - cOut[48] - cOut[49] - cOut[50] - cOut[51] - cOut[52] - cOut[53] - cOut[54] - cOut[55] - cOut[56] - cOut[57] - cOut[58] - cOut[59] - cOut[60] - cOut[61] - cOut[62] - cOut[63] - cOut[64] - cOut[65] - cOut[66] - cOut[67] - cOut[68] - cOut[69] - cOut[70] - cOut[71] - cOut[72] - cOut[73] - cOut[74] - cOut[75] - cOut[76] - cOut[77] - cOut[78] - cOut[79] - cOut[80] - cOut[81] - cOut[82] - cOut[83] - cOut[84] - cOut[85] - cOut[86] - cOut[87] - cOut[88] - cOut[89] - cOut[90] - cOut[91] - cOut[92] - cOut[93] - cOut[94] - cOut[95] - cOut[96] - cOut[97] - cOut[98] - cOut[99] - cOut[100] - cOut[101] - cOut[102] - cOut[103] - cOut[104] - cOut[105] - cOut[106] - cOut[107] - cOut[108] - cOut[109] - cOut[110] - cOut[111]
	return cOut