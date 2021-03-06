"""
Module for the Points class.

It provides an easy interface to collect parametric points.
"""
import numpy as np
import scipy


class Points(object):
	"""
	Documentation

	:cvar numpy.ndarray _values: the matrix that contains the points stored
		by column.
	"""

	def __init__(self):

		self._values = np.ndarray(shape=(0, 0))

	def append(self, point):
		"""
		Add a new point.

		:param array_like point: the coordinates of the point to add.
		"""
		array = np.asarray(point).reshape(-1, 1)
		try:
			self._values = np.append(self._values, array, 1)
		except ValueError:
			self._values = array

	def __getitem__(self, val):
		ret = Points()
		ret._values = self._values[:, val]
		return ret

	@property
	def values(self):
		"""
		The matrix that contains all the points, stored by column.
		"""
		return self._values

	@property
	def size(self):
		"""
		The number of the points
		"""
		return self.values.shape[1]

	@property
	def dimension(self):
		"""
		The dimension of the points
		"""
		return self.values.shape[0]

	@property
	def triangulation(self):
		"""
		The Delaunay tasselation built from the points.

		:type: scipy.spatial.Delaunay
		"""
		return scipy.spatial.Delaunay(self.values.T)
