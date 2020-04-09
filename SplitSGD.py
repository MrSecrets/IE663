import math
import torch
from optimizer import Optimizer, required

class SplitSGD(Optimizer):

	def __init__(self, params, config= {}):
	# def __init__(self, params, lr. w, l, q, B, t1, theta0, gamma, config= {}):
		# lr == learining rate, ita
		# w == windows
		# l == length of each window, has the same function as mini batch parameter as in mini batch SGD
		# theta0 == starting point of Splitting Diagnostic
		defaults = dict(lr=0.01, w=0, l=0, q=0, B=0, t1=0, theta0=0, gamma=0 )
		
		for k in defaults:
			if config.get(k,None) is None:
				config[k] = defaluts[k]
		super(SplitSGD, self).__init__(params, config)
		self.config = config		

	def SplittingDiagnostic(self, w, l, q, theta):
		theta0_1 = theta
		theta0_2 = theta
		checker = 0 # for stationary checking

		for i in range(1,w+1):

			for k in range(1,3):

				for j in range(l):

					# TODO rest of the stuff

			checker = checker + (1-sign(Q(i)))/2

		theta_D = (theta_1_wl + theta_2_wl)/2
		bool TD = 1 if checker >= q else 0
			# TD == 1 indicates S(stationary) and 0 indicates N
		return theta_D, TD

	def main(self,): #TODO rest 
		# this is the main SPlitSGD

		ita = lr
		theta_1_in = theta0

		for b in range(1,B+1):
			# TODO SGD stuff
			theta_last = SGD(theta_in[b])
			Theta_Db,Td = self.SplittingDiagnostic()

			if Td:
				lr = gamma.lr
				t(i+1) = t(i)/gamma
			else:
				t(i+1) = t(i)
			


