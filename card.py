class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.suit+'_'+str(self.rank)

	def __eq__(self, comp):
		return self.suit == comp.suit and self.rank == comp.rank
