import numpy as np
def moments_to_unbiased_cumulants_covariance(momIn,nIn):
	covarOut = np.zeros((1,1)) # Disconnected will be zero.
	covarOut[0,0] = -momIn[0]**2 + momIn[2]*(1 + 2/(-1 + nIn) - 6/nIn) + (2*momIn[0])/((-1 + nIn)*nIn) + (4*momIn[1]*(-2 + nIn))/((-1 + nIn)*nIn)
	return covarOut
