
class Limits:
	def __init__(self, function, variable, limit):
		self.f = function
		self.x = variable
		self.l = limit
	def lim(f, x, l):
		for i in range(f):
			if i == x:
				f[i] = "\(" +  l + "\)"
		return f
	def __main__ (self):
		return lim(f, x, l)
print Limits("3x", "x", "0")