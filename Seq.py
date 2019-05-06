class Seq:
	def __init__(self, strbase):
		self.strbase = strbase
	def len (self):
		return len (self.strbase)
	def complement (self):
		output = ''
		for letter in self.strbase:
			if letter == 'A':
				output += 'T'
			elif letter == 'T':
				output += 'A'
			elif letter == 'G':
				output += 'C'
			else:
				output += 'G'
		return Seq (output)

	def reverse (self):
		return Seq(self.strbase[::-1])

	def count (self, base):
		cont=0
		for letter in self.strbase:
			if (base==letter):
				cont=cont+1
		return cont
	def perc (self, base):
		return round ((float (self.count (base)) / float (self.len ())) * 100, 1)

	def get_strbase (self):
		return self.strbase