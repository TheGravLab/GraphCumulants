import numpy as np
def moments_to_unbiased_cumulants_covariance(momIn,nIn):
	covarOut = np.zeros((19,19)) # Disconnected will be zero.
	covarOut[0,0] = -momIn[0]**2 + momIn[2]*(1 + 2/(-1 + nIn) - 6/nIn) + (2*momIn[0])/((-1 + nIn)*nIn) + (4*momIn[1]*(-2 + nIn))/((-1 + nIn)*nIn)
	covarOut[0,1] = momIn[0]**3 - momIn[0]*momIn[1] + momIn[6]*(1 + 30/(-1 + nIn) - 44/nIn) + momIn[7]*(-1 - 12/(-1 + nIn) + 20/nIn) + (4*momIn[1])/((-1 + nIn)*nIn) + (2*momIn[3])/((-1 + nIn)*nIn) + (4*momIn[5]*(-5 + nIn))/((-1 + nIn)*nIn) + (2*momIn[4]*(-3 + nIn))/((-1 + nIn)*nIn) + (4*momIn[2])/(nIn - nIn**2)
	covarOut[0,3] = -2*momIn[0]**4 + 3*momIn[0]**2*momIn[1] - momIn[0]*momIn[3] + momIn[18]*(2 + 60/(-1 + nIn) - 84/nIn) + (momIn[13]*(-6 + nIn))/nIn + (6*momIn[3])/((-1 + nIn)*nIn) + (12*momIn[7])/((-1 + nIn)*nIn) - (12*momIn[15]*(-9 + nIn))/((-1 + nIn)*nIn) - (3*momIn[17]*(-13 + nIn)*(-6 + nIn))/((-1 + nIn)*nIn) - (6*momIn[14]*(-5 + nIn))/((-1 + nIn)*nIn) - (12*momIn[16]*(-5 + nIn))/((-1 + nIn)*nIn) + (6*momIn[8]*(-3 + nIn))/((-1 + nIn)*nIn) + (18*momIn[6])/(nIn - nIn**2) + (12*momIn[11])/(nIn - nIn**2) + (24*momIn[12])/(nIn - nIn**2)
	covarOut[0,4] = -2*momIn[0]**4 + 3*momIn[0]**2*momIn[1] - momIn[0]*momIn[4] + momIn[18]*(2 + 60/(-1 + nIn) - 84/nIn) + momIn[14]*(1 + 36/(-1 + nIn) - 50/nIn) + (6*momIn[4])/((-1 + nIn)*nIn) + (12*momIn[7])/((-1 + nIn)*nIn) + (6*momIn[8])/((-1 + nIn)*nIn) - (12*momIn[15]*(-9 + nIn))/((-1 + nIn)*nIn) + (6*momIn[11]*(-6 + nIn))/((-1 + nIn)*nIn) - (3*momIn[17]*(-13 + nIn)*(-6 + nIn))/((-1 + nIn)*nIn) - (12*momIn[16]*(-5 + nIn))/((-1 + nIn)*nIn) + (2*momIn[10]*(-4 + nIn))/((-1 + nIn)*nIn) + (18*momIn[6])/(nIn - nIn**2) + (24*momIn[12])/(nIn - nIn**2) + (6*momIn[13])/(nIn - nIn**2)
	covarOut[0,5] = -2*momIn[0]**4 + 2*momIn[0]**2*momIn[1] + momIn[0]**2*momIn[2] - momIn[0]*momIn[5] + momIn[15]*(1 + 68/(-1 + nIn) - 84/nIn) + (6*momIn[5])/((-1 + nIn)*nIn) + (6*momIn[7])/((-1 + nIn)*nIn) + (4*momIn[8])/((-1 + nIn)*nIn) + (2*momIn[9])/((-1 + nIn)*nIn) + (4*momIn[12]*(-8 + nIn))/((-1 + nIn)*nIn) + (4*momIn[11]*(-6 + nIn))/((-1 + nIn)*nIn) - (2*momIn[17]*(-11 + nIn)*(-6 + nIn))/((-1 + nIn)*nIn) + (momIn[18]*(-7 + nIn)*(-6 + nIn))/((-1 + nIn)*nIn) - (4*momIn[14]*(-5 + nIn))/((-1 + nIn)*nIn) - (8*momIn[16]*(-5 + nIn))/((-1 + nIn)*nIn) + (12*momIn[6])/(nIn - nIn**2) + (4*momIn[13])/(nIn - nIn**2)
	covarOut[0,8] = 6*momIn[0]**5 - 10*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - 2*momIn[0]**3*momIn[2] + momIn[0]*momIn[1]*momIn[2] + momIn[0]**2*momIn[3] + momIn[0]**2*momIn[4] + 2*momIn[0]**2*momIn[5] - momIn[0]*momIn[8] + momIn[43]*(9 + 826/(-1 + nIn) - 1016/nIn) + momIn[31]*(1 + 22/(-1 + nIn) - 36/nIn) + momIn[39]*(-1 - 2/(-1 + nIn) + 12/nIn) + momIn[41]*(-2 - 468/(-1 + nIn) + 528/nIn) + (8*momIn[8])/((-1 + nIn)*nIn) + (72*momIn[17])/((-1 + nIn)*nIn) + (4*momIn[19])/((-1 + nIn)*nIn) - (8*momIn[37]*(-24 + nIn))/((-1 + nIn)*nIn) + (2*momIn[22]*(-10 + nIn))/((-1 + nIn)*nIn) - (24*momIn[38]*(-9 + nIn))/((-1 + nIn)*nIn) - (4*momIn[44]*(-9 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) - (2*momIn[42]*(-42 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (momIn[40]*(-24 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (2*momIn[34]*(-6 + nIn))/((-1 + nIn)*nIn) - (12*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) + (2*momIn[20]*(-4 + nIn))/((-1 + nIn)*nIn) + (4*momIn[21]*(-4 + nIn))/((-1 + nIn)*nIn) - (4*momIn[32]*(-3 + nIn))/((-1 + nIn)*nIn) - (2*momIn[35]*(-78 + 7*nIn))/((-1 + nIn)*nIn) + (8*momIn[13])/(nIn - nIn**2) + (8*momIn[14])/(nIn - nIn**2) + (16*momIn[15])/(nIn - nIn**2) + (16*momIn[16])/(nIn - nIn**2) + (32*momIn[18])/(nIn - nIn**2) + (4*momIn[26])/(nIn - nIn**2) + (4*momIn[27])/(nIn - nIn**2) + (16*momIn[28])/(nIn - nIn**2) + (28*momIn[29])/(nIn - nIn**2) + (32*momIn[30])/(nIn - nIn**2) + (4*momIn[33])/(nIn - nIn**2)
	covarOut[0,9] = 6*momIn[0]**5 - 8*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - 4*momIn[0]**3*momIn[2] + momIn[0]*momIn[2]**2 + 4*momIn[0]**2*momIn[5] - momIn[0]*momIn[9] + momIn[33]*(1 + 4/(-1 + nIn) - 12/nIn) + momIn[41]*(-4 - 456/(-1 + nIn) + 536/nIn) + (8*momIn[9])/((-1 + nIn)*nIn) + (64*momIn[17])/((-1 + nIn)*nIn) + (4*momIn[19])/((-1 + nIn)*nIn) + (16*momIn[39])/((-1 + nIn)*nIn) - (16*momIn[37]*(-14 + nIn))/((-1 + nIn)*nIn) - (16*momIn[35]*(-10 + nIn))/((-1 + nIn)*nIn) - (32*momIn[38]*(-8 + nIn))/((-1 + nIn)*nIn) + (8*momIn[43]*(-13 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) - (3*momIn[44]*(-9 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) + (16*momIn[40]*(-7 + nIn))/((-1 + nIn)*nIn) - (2*momIn[42]*(-38 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (8*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) + (8*momIn[23]*(-4 + nIn))/((-1 + nIn)*nIn) + (32*momIn[15])/(nIn - nIn**2) + (16*momIn[16])/(nIn - nIn**2) + (24*momIn[18])/(nIn - nIn**2) + (4*momIn[27])/(nIn - nIn**2) + (32*momIn[28])/(nIn - nIn**2) + (16*momIn[29])/(nIn - nIn**2) + (48*momIn[30])/(nIn - nIn**2) + (16*momIn[31])/(nIn - nIn**2) + (8*momIn[32])/(nIn - nIn**2)
	covarOut[0,10] = 6*momIn[0]**5 - 12*momIn[0]**3*momIn[1] + 3*momIn[0]*momIn[1]**2 + 4*momIn[0]**2*momIn[4] - momIn[0]*momIn[10] + momIn[34]*(1 + 60/(-1 + nIn) - 78/nIn) + (8*momIn[10])/((-1 + nIn)*nIn) + (96*momIn[17])/((-1 + nIn)*nIn) + (12*momIn[20])/((-1 + nIn)*nIn) + (192*momIn[37])/((-1 + nIn)*nIn) + (24*momIn[39])/((-1 + nIn)*nIn) + (48*momIn[41]*(-13 + nIn))/((-1 + nIn)*nIn) - (24*momIn[35]*(-10 + nIn))/((-1 + nIn)*nIn) - (24*momIn[38]*(-10 + nIn))/((-1 + nIn)*nIn) + (12*momIn[43]*(-15 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) - (6*momIn[44]*(-9 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) + (8*momIn[26]*(-7 + nIn))/((-1 + nIn)*nIn) - (3*momIn[42]*(-38 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (4*momIn[40]*(-12 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (28*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) + (2*momIn[25]*(-5 + nIn))/((-1 + nIn)*nIn) + (32*momIn[14])/(nIn - nIn**2) + (24*momIn[16])/(nIn - nIn**2) + (48*momIn[18])/(nIn - nIn**2) + (6*momIn[27])/(nIn - nIn**2) + (72*momIn[29])/(nIn - nIn**2) + (24*momIn[30])/(nIn - nIn**2) + (24*momIn[31])/(nIn - nIn**2) + (12*momIn[32])/(nIn - nIn**2)
	covarOut[0,11] = 6*momIn[0]**5 - 8*momIn[0]**3*momIn[1] + momIn[0]*momIn[1]**2 - 4*momIn[0]**3*momIn[2] + 2*momIn[0]*momIn[1]*momIn[2] + momIn[0]**2*momIn[4] + 2*momIn[0]**2*momIn[5] + momIn[0]**2*momIn[6] - momIn[0]*momIn[11] + momIn[43]*(5 + 434/(-1 + nIn) - 536/nIn) + momIn[40]*(-1 - 90/(-1 + nIn) + 112/nIn) + momIn[41]*(-2 - 276/(-1 + nIn) + 320/nIn) + (8*momIn[11])/((-1 + nIn)*nIn) + (40*momIn[17])/((-1 + nIn)*nIn) + (2*momIn[20])/((-1 + nIn)*nIn) + (4*momIn[21])/((-1 + nIn)*nIn) + (2*momIn[22])/((-1 + nIn)*nIn) + (4*momIn[23])/((-1 + nIn)*nIn) + (10*momIn[39])/((-1 + nIn)*nIn) - (8*momIn[37]*(-16 + nIn))/((-1 + nIn)*nIn) + (2*momIn[29]*(-15 + nIn))/((-1 + nIn)*nIn) + (momIn[35]*(-14 + nIn)*(-11 + nIn))/((-1 + nIn)*nIn) + (4*momIn[28]*(-9 + nIn))/((-1 + nIn)*nIn) - (2*momIn[44]*(-9 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) + (2*momIn[26]*(-7 + nIn))/((-1 + nIn)*nIn) - (momIn[42]*(-46 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) + (2*momIn[27]*(-6 + nIn))/((-1 + nIn)*nIn) - (2*momIn[34]*(-6 + nIn))/((-1 + nIn)*nIn) - (8*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) - (8*momIn[38]*(-17 + 2*nIn))/((-1 + nIn)*nIn) + (8*momIn[14])/(nIn - nIn**2) + (16*momIn[15])/(nIn - nIn**2) + (8*momIn[16])/(nIn - nIn**2) + (16*momIn[18])/(nIn - nIn**2) + (24*momIn[30])/(nIn - nIn**2) + (14*momIn[31])/(nIn - nIn**2) + (4*momIn[32])/(nIn - nIn**2) + (4*momIn[33])/(nIn - nIn**2)
	covarOut[0,12] = 6*momIn[0]**5 - 6*momIn[0]**3*momIn[1] + momIn[0]*momIn[1]**2 - 6*momIn[0]**3*momIn[2] + momIn[0]*momIn[1]*momIn[2] + momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[5] + 2*momIn[0]**2*momIn[6] - momIn[0]*momIn[12] + momIn[43]*(3 + 238/(-1 + nIn) - 296/nIn) + momIn[37]*(1 + 108/(-1 + nIn) - 126/nIn) + momIn[44]*(-1 - 56/(-1 + nIn) + 72/nIn) + (8*momIn[12])/((-1 + nIn)*nIn) + (24*momIn[17])/((-1 + nIn)*nIn) + (2*momIn[21])/((-1 + nIn)*nIn) + (4*momIn[22])/((-1 + nIn)*nIn) + (4*momIn[23])/((-1 + nIn)*nIn) + (2*momIn[24])/((-1 + nIn)*nIn) + (6*momIn[39])/((-1 + nIn)*nIn) + (2*momIn[28]*(-13 + nIn))/((-1 + nIn)*nIn) + (4*momIn[30]*(-11 + nIn))/((-1 + nIn)*nIn) - (8*momIn[35]*(-9 + nIn))/((-1 + nIn)*nIn) + (4*momIn[29]*(-7 + nIn))/((-1 + nIn)*nIn) + (6*momIn[40]*(-7 + nIn))/((-1 + nIn)*nIn) - (momIn[42]*(-30 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (4*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) - (8*momIn[38]*(-15 + 2*nIn))/((-1 + nIn)*nIn) + (16*momIn[15])/(nIn - nIn**2) + (8*momIn[16])/(nIn - nIn**2) + (8*momIn[18])/(nIn - nIn**2) + (2*momIn[27])/(nIn - nIn**2) + (8*momIn[31])/(nIn - nIn**2) + (4*momIn[32])/(nIn - nIn**2) + (4*momIn[33])/(nIn - nIn**2) + momIn[41]*(216/nIn - (2*(89 + nIn))/(-1 + nIn))
	covarOut[1,0] = momIn[0]**3 - momIn[0]*momIn[1] + momIn[6]*(1 + 30/(-1 + nIn) - 44/nIn) + momIn[7]*(-1 - 12/(-1 + nIn) + 20/nIn) + (4*momIn[1])/((-1 + nIn)*nIn) + (2*momIn[3])/((-1 + nIn)*nIn) + (4*momIn[5]*(-5 + nIn))/((-1 + nIn)*nIn) + (2*momIn[4]*(-3 + nIn))/((-1 + nIn)*nIn) + (4*momIn[2])/(nIn - nIn**2)
	covarOut[1,1] = -momIn[0]**4 + 2*momIn[0]**2*momIn[1] - momIn[1]**2 + momIn[10]*(1/(-2 + nIn) - 6/(-1 + nIn) + 6/nIn) + (4*momIn[11]*(-11 + nIn)*(-4 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) - (8*momIn[14]*(-5 + nIn)*(-4 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) - (16*momIn[6]*(-5 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (8*momIn[7]*(-5 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[17]*(-11 + nIn)*(-6 + nIn)*(-5 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[18]*(-7 + nIn)*(-6 + nIn)*(-5 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (16*momIn[15]*(-5 + nIn)**2*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (4*momIn[12]*(-4 + nIn)*(37 + (-10 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[16]*(-5 + nIn)*(-4 + nIn)*(41 + (-6 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[1])/(nIn*(2 - 3*nIn + nIn**2)) + (4*momIn[3])/(nIn*(2 - 3*nIn + nIn**2)) + (4*momIn[5]*(-11 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) + (8*momIn[8]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (8*momIn[13]*(-4 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) + (4*momIn[4]*(-3 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) + (8*momIn[2])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (2*momIn[9]*(17 - 6*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3))
	covarOut[1,3] = 2*momIn[0]**5 - 5*momIn[0]**3*momIn[1] + 3*momIn[0]*momIn[1]**2 + momIn[0]**2*momIn[3] - momIn[1]*momIn[3] + momIn[32]*(1 - 16/(-3 + nIn) + 78/(-2 + nIn) - 96/(-1 + nIn) + 25/nIn) + (3*momIn[20]*(-5 + nIn))/((-1 + nIn)*nIn) - (3*momIn[34]*(-6 + nIn)*(-5 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) - (24*momIn[18]*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[44]*(-9 + nIn)*(-8 + nIn)*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (48*momIn[41]*(-7 + nIn)**2*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[15]*(-19 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[16]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (36*momIn[29]*(-7 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (6*momIn[36]*(-11 + nIn)*(-6 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[14]*(-5 + nIn)**2)/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (24*momIn[40]*(-7 + nIn)*(-6 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (momIn[39]*(-9 + nIn)*(-6 + nIn)*(-4 + nIn)*(1 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[43]*(-8 + nIn)*(-7 + nIn)*(-6 + nIn)*(-69 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (12*momIn[17]*(-6 + nIn)*(-37 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[35]*(-6 + nIn)*(69 + (-22 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[37]*(-6 + nIn)*(89 + (-18 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[38]*(-6 + nIn)*(97 + (-18 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (3*momIn[42]*(-7 + nIn)*(-6 + nIn)*(119 + (-16 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[31]*(-8 + (-5 + nIn)**2*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (6*momIn[3])/(nIn*(2 - 3*nIn + nIn**2)) - (36*momIn[11])/(nIn*(2 - 3*nIn + nIn**2)) + (12*momIn[8]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (12*momIn[26]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (12*momIn[27]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) + (6*momIn[19]*(-3 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (24*momIn[21]*(-3 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (48*momIn[7])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (48*momIn[24])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (6*momIn[6]*(-11 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (12*momIn[23]*(-11 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (48*momIn[12]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[28]*(47 - 16*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[30]*(71 - 16*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (6*momIn[33]*(31 - 8*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (12*momIn[13]*(7 - 6*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + momIn[22]*(10/nIn - (4*(-13 + nIn**2))/(-6 + 11*nIn - 6*nIn**2 + nIn**3))
	covarOut[1,4] = 2*momIn[0]**5 - 5*momIn[0]**3*momIn[1] + 3*momIn[0]*momIn[1]**2 + momIn[0]**2*momIn[4] - momIn[1]*momIn[4] + momIn[34]*(4/(-3 + nIn) - 66/(-2 + nIn) + 180/(-1 + nIn) - 125/nIn) + (3*momIn[27]*(-8 + nIn)*(-5 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) - (24*momIn[18]*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[44]*(-9 + nIn)*(-8 + nIn)*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (48*momIn[41]*(-7 + nIn)**2*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[15]*(-19 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[16]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (6*momIn[32]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (24*momIn[39]*(-6 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (momIn[40]*(-29 + nIn)*(-7 + nIn)*(-6 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[14]*(-5 + nIn)*(-9 + 2*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[43]*(-8 + nIn)*(-7 + nIn)*(-6 + nIn)*(-69 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (12*momIn[17]*(-6 + nIn)*(-37 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[26]*(-5 + nIn)*(78 + (-25 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[37]*(-6 + nIn)*(89 + (-18 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[38]*(-6 + nIn)*(97 + (-18 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (3*momIn[42]*(-7 + nIn)*(-6 + nIn)*(119 + (-16 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (6*momIn[29]*(-5 + nIn)*(54 + (-13 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[36]*(-6 + nIn)*(-5 + nIn)*(78 + (-13 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (6*momIn[4])/(nIn*(2 - 3*nIn + nIn**2)) + (6*momIn[19])/(nIn*(2 - 3*nIn + nIn**2)) + (12*momIn[21]*(-6 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) + (6*momIn[10]*(-4 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (48*momIn[7])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (48*momIn[24])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (momIn[22]*(252 - 60*nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (6*momIn[6]*(-11 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (12*momIn[8]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (48*momIn[12]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (12*momIn[13]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (6*momIn[11]*(62 - 21*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[30]*(71 - 16*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (6*momIn[20]*(31 - 12*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (6*momIn[23]*(34 - 9*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (6*momIn[33]*(31 - 8*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[28]*(67 - 25*nIn + 2*nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (12*momIn[31]*(72 - 31*nIn + 3*nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (momIn[25]*(20 - 9*nIn + nIn**2))/(2*nIn - 3*nIn**2 + nIn**3) - (12*momIn[35]*(-6 + nIn)*(89 + nIn*(-31 + 2*nIn)))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)
	covarOut[1,5] = 2*momIn[0]**5 - 4*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - momIn[0]**3*momIn[2] + momIn[0]*momIn[1]*momIn[2] + momIn[0]**2*momIn[5] - momIn[1]*momIn[5] + momIn[38]*(1 + 176/(-3 + nIn) - 924/(-2 + nIn) + 1500/(-1 + nIn) - 772/nIn) + (2*momIn[26]*(-8 + nIn)*(-5 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[34]*(-6 + nIn)*(-5 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) + (36*momIn[17]*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[18]*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (momIn[44]*(-9 + nIn)*(-8 + nIn)*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (8*momIn[16]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (4*momIn[32]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (4*momIn[36]*(-11 + nIn)*(-6 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (8*momIn[14]*(-5 + nIn)**2)/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (8*momIn[27]*(-5 + nIn)*(-7 + 2*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[43]*(-8 + nIn)*(-7 + nIn)*(-6 + nIn)*(-37 + 3*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (4*momIn[15]*(-5 + nIn)*(-46 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[39]*(-6 + nIn)*(-29 + 7*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[40]*(-7 + nIn)*(-6 + nIn)*(-29 + 7*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (momIn[41]*(-7 + nIn)*(-6 + nIn)*(208 + (-37 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[29]*(-5 + nIn)*(128 + (-27 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (4*momIn[28]*(-4 + nIn)*(79 + (-16 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[42]*(-7 + nIn)*(-6 + nIn)*(103 + (-16 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (16*momIn[37]*(-6 + nIn)*(49 + (-13 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (12*momIn[8])/(nIn*(2 - 3*nIn + nIn**2)) + (4*momIn[20]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (24*momIn[7])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (4*momIn[6]*(-11 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[5]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[9]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (8*momIn[13]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[19]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[12]*(84 - 23*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[22]*(54 - 17*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (8*momIn[11]*(29 - 12*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[31]*(23 - 10*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (8*momIn[23]*(31 - 10*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (2*momIn[24]*(28 - 7*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (4*momIn[33]*(47 - 17*nIn + 2*nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (2*momIn[21]*(92 - 37*nIn + 3*nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (8*momIn[35]*(-6 + nIn)*(83 + nIn*(-29 + 2*nIn)))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (4*momIn[30]*(-368 + nIn*(129 + (-18 + nIn)*nIn)))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)
	covarOut[3,0] = -2*momIn[0]**4 + 3*momIn[0]**2*momIn[1] - momIn[0]*momIn[3] + momIn[18]*(2 + 60/(-1 + nIn) - 84/nIn) + (momIn[13]*(-6 + nIn))/nIn + (6*momIn[3])/((-1 + nIn)*nIn) + (12*momIn[7])/((-1 + nIn)*nIn) - (12*momIn[15]*(-9 + nIn))/((-1 + nIn)*nIn) - (3*momIn[17]*(-13 + nIn)*(-6 + nIn))/((-1 + nIn)*nIn) - (6*momIn[14]*(-5 + nIn))/((-1 + nIn)*nIn) - (12*momIn[16]*(-5 + nIn))/((-1 + nIn)*nIn) + (6*momIn[8]*(-3 + nIn))/((-1 + nIn)*nIn) + (18*momIn[6])/(nIn - nIn**2) + (12*momIn[11])/(nIn - nIn**2) + (24*momIn[12])/(nIn - nIn**2)
	covarOut[3,1] = 2*momIn[0]**5 - 5*momIn[0]**3*momIn[1] + 3*momIn[0]*momIn[1]**2 + momIn[0]**2*momIn[3] - momIn[1]*momIn[3] + momIn[32]*(1 - 16/(-3 + nIn) + 78/(-2 + nIn) - 96/(-1 + nIn) + 25/nIn) + (3*momIn[20]*(-5 + nIn))/((-1 + nIn)*nIn) - (3*momIn[34]*(-6 + nIn)*(-5 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) - (24*momIn[18]*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[44]*(-9 + nIn)*(-8 + nIn)*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (48*momIn[41]*(-7 + nIn)**2*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[15]*(-19 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[16]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (36*momIn[29]*(-7 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (6*momIn[36]*(-11 + nIn)*(-6 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[14]*(-5 + nIn)**2)/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (24*momIn[40]*(-7 + nIn)*(-6 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (momIn[39]*(-9 + nIn)*(-6 + nIn)*(-4 + nIn)*(1 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[43]*(-8 + nIn)*(-7 + nIn)*(-6 + nIn)*(-69 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (12*momIn[17]*(-6 + nIn)*(-37 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[35]*(-6 + nIn)*(69 + (-22 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[37]*(-6 + nIn)*(89 + (-18 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[38]*(-6 + nIn)*(97 + (-18 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (3*momIn[42]*(-7 + nIn)*(-6 + nIn)*(119 + (-16 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[31]*(-8 + (-5 + nIn)**2*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (6*momIn[3])/(nIn*(2 - 3*nIn + nIn**2)) - (36*momIn[11])/(nIn*(2 - 3*nIn + nIn**2)) + (12*momIn[8]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (12*momIn[26]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (12*momIn[27]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) + (6*momIn[19]*(-3 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (24*momIn[21]*(-3 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (48*momIn[7])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (48*momIn[24])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (6*momIn[6]*(-11 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (12*momIn[23]*(-11 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (48*momIn[12]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[28]*(47 - 16*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[30]*(71 - 16*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (6*momIn[33]*(31 - 8*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (12*momIn[13]*(7 - 6*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + momIn[22]*(10/nIn - (4*(-13 + nIn**2))/(-6 + 11*nIn - 6*nIn**2 + nIn**3))
	covarOut[4,0] = -2*momIn[0]**4 + 3*momIn[0]**2*momIn[1] - momIn[0]*momIn[4] + momIn[18]*(2 + 60/(-1 + nIn) - 84/nIn) + momIn[14]*(1 + 36/(-1 + nIn) - 50/nIn) + (6*momIn[4])/((-1 + nIn)*nIn) + (12*momIn[7])/((-1 + nIn)*nIn) + (6*momIn[8])/((-1 + nIn)*nIn) - (12*momIn[15]*(-9 + nIn))/((-1 + nIn)*nIn) + (6*momIn[11]*(-6 + nIn))/((-1 + nIn)*nIn) - (3*momIn[17]*(-13 + nIn)*(-6 + nIn))/((-1 + nIn)*nIn) - (12*momIn[16]*(-5 + nIn))/((-1 + nIn)*nIn) + (2*momIn[10]*(-4 + nIn))/((-1 + nIn)*nIn) + (18*momIn[6])/(nIn - nIn**2) + (24*momIn[12])/(nIn - nIn**2) + (6*momIn[13])/(nIn - nIn**2)
	covarOut[4,1] = 2*momIn[0]**5 - 5*momIn[0]**3*momIn[1] + 3*momIn[0]*momIn[1]**2 + momIn[0]**2*momIn[4] - momIn[1]*momIn[4] + momIn[34]*(4/(-3 + nIn) - 66/(-2 + nIn) + 180/(-1 + nIn) - 125/nIn) + (3*momIn[27]*(-8 + nIn)*(-5 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) - (24*momIn[18]*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[44]*(-9 + nIn)*(-8 + nIn)*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (48*momIn[41]*(-7 + nIn)**2*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[15]*(-19 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[16]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (6*momIn[32]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (24*momIn[39]*(-6 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (momIn[40]*(-29 + nIn)*(-7 + nIn)*(-6 + nIn)*(-4 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[14]*(-5 + nIn)*(-9 + 2*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[43]*(-8 + nIn)*(-7 + nIn)*(-6 + nIn)*(-69 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (12*momIn[17]*(-6 + nIn)*(-37 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[26]*(-5 + nIn)*(78 + (-25 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[37]*(-6 + nIn)*(89 + (-18 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[38]*(-6 + nIn)*(97 + (-18 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (3*momIn[42]*(-7 + nIn)*(-6 + nIn)*(119 + (-16 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (6*momIn[29]*(-5 + nIn)*(54 + (-13 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[36]*(-6 + nIn)*(-5 + nIn)*(78 + (-13 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (6*momIn[4])/(nIn*(2 - 3*nIn + nIn**2)) + (6*momIn[19])/(nIn*(2 - 3*nIn + nIn**2)) + (12*momIn[21]*(-6 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) + (6*momIn[10]*(-4 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (48*momIn[7])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (48*momIn[24])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (momIn[22]*(252 - 60*nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (6*momIn[6]*(-11 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (12*momIn[8]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (48*momIn[12]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (12*momIn[13]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (6*momIn[11]*(62 - 21*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[30]*(71 - 16*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (6*momIn[20]*(31 - 12*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (6*momIn[23]*(34 - 9*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (6*momIn[33]*(31 - 8*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[28]*(67 - 25*nIn + 2*nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (12*momIn[31]*(72 - 31*nIn + 3*nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (momIn[25]*(20 - 9*nIn + nIn**2))/(2*nIn - 3*nIn**2 + nIn**3) - (12*momIn[35]*(-6 + nIn)*(89 + nIn*(-31 + 2*nIn)))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)
	covarOut[5,0] = -2*momIn[0]**4 + 2*momIn[0]**2*momIn[1] + momIn[0]**2*momIn[2] - momIn[0]*momIn[5] + momIn[15]*(1 + 68/(-1 + nIn) - 84/nIn) + (6*momIn[5])/((-1 + nIn)*nIn) + (6*momIn[7])/((-1 + nIn)*nIn) + (4*momIn[8])/((-1 + nIn)*nIn) + (2*momIn[9])/((-1 + nIn)*nIn) + (4*momIn[12]*(-8 + nIn))/((-1 + nIn)*nIn) + (4*momIn[11]*(-6 + nIn))/((-1 + nIn)*nIn) - (2*momIn[17]*(-11 + nIn)*(-6 + nIn))/((-1 + nIn)*nIn) + (momIn[18]*(-7 + nIn)*(-6 + nIn))/((-1 + nIn)*nIn) - (4*momIn[14]*(-5 + nIn))/((-1 + nIn)*nIn) - (8*momIn[16]*(-5 + nIn))/((-1 + nIn)*nIn) + (12*momIn[6])/(nIn - nIn**2) + (4*momIn[13])/(nIn - nIn**2)
	covarOut[5,1] = 2*momIn[0]**5 - 4*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - momIn[0]**3*momIn[2] + momIn[0]*momIn[1]*momIn[2] + momIn[0]**2*momIn[5] - momIn[1]*momIn[5] + momIn[38]*(1 + 176/(-3 + nIn) - 924/(-2 + nIn) + 1500/(-1 + nIn) - 772/nIn) + (2*momIn[26]*(-8 + nIn)*(-5 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[34]*(-6 + nIn)*(-5 + nIn))/((-2 + nIn)*(-1 + nIn)*nIn) + (36*momIn[17]*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (12*momIn[18]*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (momIn[44]*(-9 + nIn)*(-8 + nIn)*(-7 + nIn)*(-6 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (8*momIn[16]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (4*momIn[32]*(-11 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (4*momIn[36]*(-11 + nIn)*(-6 + nIn)*(-5 + nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (8*momIn[14]*(-5 + nIn)**2)/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (8*momIn[27]*(-5 + nIn)*(-7 + 2*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (momIn[43]*(-8 + nIn)*(-7 + nIn)*(-6 + nIn)*(-37 + 3*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (4*momIn[15]*(-5 + nIn)*(-46 + 5*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[39]*(-6 + nIn)*(-29 + 7*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[40]*(-7 + nIn)*(-6 + nIn)*(-29 + 7*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (momIn[41]*(-7 + nIn)*(-6 + nIn)*(208 + (-37 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (2*momIn[29]*(-5 + nIn)*(128 + (-27 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (4*momIn[28]*(-4 + nIn)*(79 + (-16 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (2*momIn[42]*(-7 + nIn)*(-6 + nIn)*(103 + (-16 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) - (16*momIn[37]*(-6 + nIn)*(49 + (-13 + nIn)*nIn))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (12*momIn[8])/(nIn*(2 - 3*nIn + nIn**2)) + (4*momIn[20]*(-5 + nIn))/(nIn*(2 - 3*nIn + nIn**2)) - (24*momIn[7])/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (4*momIn[6]*(-11 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[5]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[9]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (8*momIn[13]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[19]*(-5 + nIn))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[12]*(84 - 23*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (4*momIn[22]*(54 - 17*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (8*momIn[11]*(29 - 12*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (24*momIn[31]*(23 - 10*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (8*momIn[23]*(31 - 10*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (2*momIn[24]*(28 - 7*nIn + nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (4*momIn[33]*(47 - 17*nIn + 2*nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) + (2*momIn[21]*(92 - 37*nIn + 3*nIn**2))/(nIn*(-6 + 11*nIn - 6*nIn**2 + nIn**3)) - (8*momIn[35]*(-6 + nIn)*(83 + nIn*(-29 + 2*nIn)))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn) + (4*momIn[30]*(-368 + nIn*(129 + (-18 + nIn)*nIn)))/((-3 + nIn)*(-2 + nIn)*(-1 + nIn)*nIn)
	covarOut[8,0] = 6*momIn[0]**5 - 10*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - 2*momIn[0]**3*momIn[2] + momIn[0]*momIn[1]*momIn[2] + momIn[0]**2*momIn[3] + momIn[0]**2*momIn[4] + 2*momIn[0]**2*momIn[5] - momIn[0]*momIn[8] + momIn[43]*(9 + 826/(-1 + nIn) - 1016/nIn) + momIn[31]*(1 + 22/(-1 + nIn) - 36/nIn) + momIn[39]*(-1 - 2/(-1 + nIn) + 12/nIn) + momIn[41]*(-2 - 468/(-1 + nIn) + 528/nIn) + (8*momIn[8])/((-1 + nIn)*nIn) + (72*momIn[17])/((-1 + nIn)*nIn) + (4*momIn[19])/((-1 + nIn)*nIn) - (8*momIn[37]*(-24 + nIn))/((-1 + nIn)*nIn) + (2*momIn[22]*(-10 + nIn))/((-1 + nIn)*nIn) - (24*momIn[38]*(-9 + nIn))/((-1 + nIn)*nIn) - (4*momIn[44]*(-9 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) - (2*momIn[42]*(-42 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (momIn[40]*(-24 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (2*momIn[34]*(-6 + nIn))/((-1 + nIn)*nIn) - (12*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) + (2*momIn[20]*(-4 + nIn))/((-1 + nIn)*nIn) + (4*momIn[21]*(-4 + nIn))/((-1 + nIn)*nIn) - (4*momIn[32]*(-3 + nIn))/((-1 + nIn)*nIn) - (2*momIn[35]*(-78 + 7*nIn))/((-1 + nIn)*nIn) + (8*momIn[13])/(nIn - nIn**2) + (8*momIn[14])/(nIn - nIn**2) + (16*momIn[15])/(nIn - nIn**2) + (16*momIn[16])/(nIn - nIn**2) + (32*momIn[18])/(nIn - nIn**2) + (4*momIn[26])/(nIn - nIn**2) + (4*momIn[27])/(nIn - nIn**2) + (16*momIn[28])/(nIn - nIn**2) + (28*momIn[29])/(nIn - nIn**2) + (32*momIn[30])/(nIn - nIn**2) + (4*momIn[33])/(nIn - nIn**2)
	covarOut[9,0] = 6*momIn[0]**5 - 8*momIn[0]**3*momIn[1] + 2*momIn[0]*momIn[1]**2 - 4*momIn[0]**3*momIn[2] + momIn[0]*momIn[2]**2 + 4*momIn[0]**2*momIn[5] - momIn[0]*momIn[9] + momIn[33]*(1 + 4/(-1 + nIn) - 12/nIn) + momIn[41]*(-4 - 456/(-1 + nIn) + 536/nIn) + (8*momIn[9])/((-1 + nIn)*nIn) + (64*momIn[17])/((-1 + nIn)*nIn) + (4*momIn[19])/((-1 + nIn)*nIn) + (16*momIn[39])/((-1 + nIn)*nIn) - (16*momIn[37]*(-14 + nIn))/((-1 + nIn)*nIn) - (16*momIn[35]*(-10 + nIn))/((-1 + nIn)*nIn) - (32*momIn[38]*(-8 + nIn))/((-1 + nIn)*nIn) + (8*momIn[43]*(-13 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) - (3*momIn[44]*(-9 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) + (16*momIn[40]*(-7 + nIn))/((-1 + nIn)*nIn) - (2*momIn[42]*(-38 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (8*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) + (8*momIn[23]*(-4 + nIn))/((-1 + nIn)*nIn) + (32*momIn[15])/(nIn - nIn**2) + (16*momIn[16])/(nIn - nIn**2) + (24*momIn[18])/(nIn - nIn**2) + (4*momIn[27])/(nIn - nIn**2) + (32*momIn[28])/(nIn - nIn**2) + (16*momIn[29])/(nIn - nIn**2) + (48*momIn[30])/(nIn - nIn**2) + (16*momIn[31])/(nIn - nIn**2) + (8*momIn[32])/(nIn - nIn**2)
	covarOut[10,0] = 6*momIn[0]**5 - 12*momIn[0]**3*momIn[1] + 3*momIn[0]*momIn[1]**2 + 4*momIn[0]**2*momIn[4] - momIn[0]*momIn[10] + momIn[34]*(1 + 60/(-1 + nIn) - 78/nIn) + (8*momIn[10])/((-1 + nIn)*nIn) + (96*momIn[17])/((-1 + nIn)*nIn) + (12*momIn[20])/((-1 + nIn)*nIn) + (192*momIn[37])/((-1 + nIn)*nIn) + (24*momIn[39])/((-1 + nIn)*nIn) + (48*momIn[41]*(-13 + nIn))/((-1 + nIn)*nIn) - (24*momIn[35]*(-10 + nIn))/((-1 + nIn)*nIn) - (24*momIn[38]*(-10 + nIn))/((-1 + nIn)*nIn) + (12*momIn[43]*(-15 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) - (6*momIn[44]*(-9 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) + (8*momIn[26]*(-7 + nIn))/((-1 + nIn)*nIn) - (3*momIn[42]*(-38 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (4*momIn[40]*(-12 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (28*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) + (2*momIn[25]*(-5 + nIn))/((-1 + nIn)*nIn) + (32*momIn[14])/(nIn - nIn**2) + (24*momIn[16])/(nIn - nIn**2) + (48*momIn[18])/(nIn - nIn**2) + (6*momIn[27])/(nIn - nIn**2) + (72*momIn[29])/(nIn - nIn**2) + (24*momIn[30])/(nIn - nIn**2) + (24*momIn[31])/(nIn - nIn**2) + (12*momIn[32])/(nIn - nIn**2)
	covarOut[11,0] = 6*momIn[0]**5 - 8*momIn[0]**3*momIn[1] + momIn[0]*momIn[1]**2 - 4*momIn[0]**3*momIn[2] + 2*momIn[0]*momIn[1]*momIn[2] + momIn[0]**2*momIn[4] + 2*momIn[0]**2*momIn[5] + momIn[0]**2*momIn[6] - momIn[0]*momIn[11] + momIn[43]*(5 + 434/(-1 + nIn) - 536/nIn) + momIn[40]*(-1 - 90/(-1 + nIn) + 112/nIn) + momIn[41]*(-2 - 276/(-1 + nIn) + 320/nIn) + (8*momIn[11])/((-1 + nIn)*nIn) + (40*momIn[17])/((-1 + nIn)*nIn) + (2*momIn[20])/((-1 + nIn)*nIn) + (4*momIn[21])/((-1 + nIn)*nIn) + (2*momIn[22])/((-1 + nIn)*nIn) + (4*momIn[23])/((-1 + nIn)*nIn) + (10*momIn[39])/((-1 + nIn)*nIn) - (8*momIn[37]*(-16 + nIn))/((-1 + nIn)*nIn) + (2*momIn[29]*(-15 + nIn))/((-1 + nIn)*nIn) + (momIn[35]*(-14 + nIn)*(-11 + nIn))/((-1 + nIn)*nIn) + (4*momIn[28]*(-9 + nIn))/((-1 + nIn)*nIn) - (2*momIn[44]*(-9 + nIn)*(-8 + nIn))/((-1 + nIn)*nIn) + (2*momIn[26]*(-7 + nIn))/((-1 + nIn)*nIn) - (momIn[42]*(-46 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) + (2*momIn[27]*(-6 + nIn))/((-1 + nIn)*nIn) - (2*momIn[34]*(-6 + nIn))/((-1 + nIn)*nIn) - (8*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) - (8*momIn[38]*(-17 + 2*nIn))/((-1 + nIn)*nIn) + (8*momIn[14])/(nIn - nIn**2) + (16*momIn[15])/(nIn - nIn**2) + (8*momIn[16])/(nIn - nIn**2) + (16*momIn[18])/(nIn - nIn**2) + (24*momIn[30])/(nIn - nIn**2) + (14*momIn[31])/(nIn - nIn**2) + (4*momIn[32])/(nIn - nIn**2) + (4*momIn[33])/(nIn - nIn**2)
	covarOut[12,0] = 6*momIn[0]**5 - 6*momIn[0]**3*momIn[1] + momIn[0]*momIn[1]**2 - 6*momIn[0]**3*momIn[2] + momIn[0]*momIn[1]*momIn[2] + momIn[0]*momIn[2]**2 + 2*momIn[0]**2*momIn[5] + 2*momIn[0]**2*momIn[6] - momIn[0]*momIn[12] + momIn[43]*(3 + 238/(-1 + nIn) - 296/nIn) + momIn[37]*(1 + 108/(-1 + nIn) - 126/nIn) + momIn[44]*(-1 - 56/(-1 + nIn) + 72/nIn) + (8*momIn[12])/((-1 + nIn)*nIn) + (24*momIn[17])/((-1 + nIn)*nIn) + (2*momIn[21])/((-1 + nIn)*nIn) + (4*momIn[22])/((-1 + nIn)*nIn) + (4*momIn[23])/((-1 + nIn)*nIn) + (2*momIn[24])/((-1 + nIn)*nIn) + (6*momIn[39])/((-1 + nIn)*nIn) + (2*momIn[28]*(-13 + nIn))/((-1 + nIn)*nIn) + (4*momIn[30]*(-11 + nIn))/((-1 + nIn)*nIn) - (8*momIn[35]*(-9 + nIn))/((-1 + nIn)*nIn) + (4*momIn[29]*(-7 + nIn))/((-1 + nIn)*nIn) + (6*momIn[40]*(-7 + nIn))/((-1 + nIn)*nIn) - (momIn[42]*(-30 + nIn)*(-7 + nIn))/((-1 + nIn)*nIn) - (4*momIn[36]*(-6 + nIn))/((-1 + nIn)*nIn) - (8*momIn[38]*(-15 + 2*nIn))/((-1 + nIn)*nIn) + (16*momIn[15])/(nIn - nIn**2) + (8*momIn[16])/(nIn - nIn**2) + (8*momIn[18])/(nIn - nIn**2) + (2*momIn[27])/(nIn - nIn**2) + (8*momIn[31])/(nIn - nIn**2) + (4*momIn[32])/(nIn - nIn**2) + (4*momIn[33])/(nIn - nIn**2) + momIn[41]*(216/nIn - (2*(89 + nIn))/(-1 + nIn))
	return covarOut
