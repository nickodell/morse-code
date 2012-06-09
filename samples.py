# Name is somewhat misleading, actually stores coefficients from detect_tone



class Sample_Storage():
	def append_samples(l):
		self.samples.extend(l)
	
class Sample_Storage_Window():
	"""Wrap Sample_Storage() so that it's simpler to keep track of how many samples you've looked at so far."""
	def __init__(self, stor):
		self.stor = stor
		self.current = 0
	def get_sample(self):
		"""Convienience function wrapping get_samples"""
		sample = self.get_samples(1)
		assert len(sample) == 1
		return sample[0] #unwrap list that was returned
	def get_samples(self, num):
		"""Attempt to get num samples from provided Sample_Storage instance"""
		if self.current + num > self.stor.samples:
			raise IndexError()
		else:
			start = self.current
			end = start + num
			self.current = end
			return self.stor.samples[start:end]
