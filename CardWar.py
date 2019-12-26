import random


# cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
class Card(object):
	cardColors = ['Clubs', 'Diamonds', 'Hearts', 'Spades' ]	
	cardValuesNames = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
	
	def __init__(self, cardValue): # need to guard againgst invalid values
		self.cardValue = cardValue
		self.color = self.cardColors[int((self.cardValue - 1 )/ 13)]
		self.valueName = self.cardValuesNames[(cardValue % 13 - 1)]

	# returns True if current card value is bigger
	def compareWith(self, anotherCard):
		if self.valueName > anotherCard.valueName:
			print("TRUE")
			return True
		elif (self.valueName == anotherCard.valueName):
			print("VALUE IS EQUAL")
		else:
			print("FALSE")
			return False
	# card info
	def printCard(self):
		print(self.valueName + ' of ' + self.color + '(' + str(self.cardValue) + ')')		

class Deck():
	def __init__(self):
		self.cards = []
		for i in range(1, 53):
		 	self.cards.append(Card(i))
	
	def getTopCard(self):
		return self.cards[0]
	
	def removeTopCard(self):
		self.cards.remove(self.cards[0])
	
	def shuffleDeck(self):
		print('SHUFFLING CARDS ')
		random.shuffle(self.cards)
	
	def printCards(self):
		for card in self.cards:
			card.printCard()


#	def giveCard()
#class deck(obect):
#	
#	cards = [];
#	facedUp 

while True:
	# val1 = 20
	# val = input('what card: ')
	# val = int(val)
	# c1 = Card(val)
	# c2 = Card(val1)
	# print(c1.color)
	# print(c1.valueName)
	# print(' with ')
	# print(c2.color)
	# print(c2.valueName)
	# c1.compareWith(c2)
	myDeck = Deck()
	myDeck.printCards()
	
	print('\n\n')
	myDeck.shuffleDeck()
	myDeck.printCards()
	print('Num of cards in deck: ' + str(len(myDeck.cards)))
	
	print('\n1Getting topCard 2Removing topCard\n')
	myDeck.getTopCard()
	myDeck.removeTopCard()
	myDeck.printCards()
	print('Num of cards in deck: ' + str(len(myDeck.cards)))
	
#	del myDeck
	myDeck.getTopCard()
	
	again = input('q for quit: ')
	if again == 'q' or again == 'Q':
		break