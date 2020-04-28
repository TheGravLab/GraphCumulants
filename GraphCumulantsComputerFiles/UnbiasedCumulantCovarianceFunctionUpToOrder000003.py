import numpy as np
def moments_to_unbiased_cumulants_covariance(momIn,nIn):
	covarOut = np.zeros((3,3)) # Disconnected will be zero.
	covarOut[0,0] = -momIn[0]**2 + momIn[2]*(1 + 2/(-1 + nIn) - 6/nIn) + (2*momIn[0])/((-1 + nIn)*nIn) + (4*momIn[1]*(-2 + nIn))/((-1 + nIn)*nIn)
	covarOut[0,1] = momIn[0]**3 - momIn[0]*momIn[1] + momIn[6]*(1 + 30/(-1 + nIn) - 44/nIn) + momIn[7]*(-1 - 12/(-1 + nIn) + 20/nIn) + (4*momIn[1])/((-1 + nIn)*nIn) + (2*momIn[3])/((-1 + nIn)*nIn) + (4*momIn[5]*(-5 + nIn))/((-1 + nIn)*nIn) + (2*momIn[4]*(-3 + nIn))/((-1 + nIn)*nIn) + (4*momIn[2])/(nIn - nIn**2)
	covarOut[1,0] = momIn[0]**3 - momIn[0]*momIn[1] + momIn[6]*(1 + 30/(-1 + nIn) - 44/nIn) + momIn[7]*(-1 - 12/(-1 + nIn) + 20/nIn) + (4*momIn[1])/((-1 + nIn)*nIn) + (2*momIn[3])/((-1 + nIn)*nIn) + (4*momIn[5]*(-5 + nIn))/((-1 + nIn)*nIn) + (2*momIn[4]*(-3 + nIn))/((-1 + nIn)*nIn) + (4*momIn[2])/(nIn - nIn**2)
	return covarOut
