class Q:
	def __lt__(self, n):
		return False
	def __le__(self,n):
		return False
	def __eq__(self, n):
		return True
	def __gt__(self, n):
		return True
	def __ge__(self, n):
		return True
		
q = Q()
print(1000<q)