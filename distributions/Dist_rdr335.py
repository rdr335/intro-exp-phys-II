import numpy as np
from base_distribution import BaseDistribution

#defining a reoccuring number
c = np.sqrt(2/np.pi)
class Dist_rdr335(BaseDistribution):
	def __init__(self):
		self.f_max = c
		self.x_min = -c
		self.x_max = c
		
	def pdf(self, x):
		"""This is your PDF"""
		return np.sqrt(c**2 - x**2)

	def mean(self):
		"""This is the mean of the PDF"""
		return (c**3)*np.pi/8

	def std(self):
		"""This is the standard deviation of the pdf"""
		return (c**3)*np.pi/2
