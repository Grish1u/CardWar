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
		message = self.valueName + ' of ' + self.color + '(' + str(self.cardValue) + ')'
		print(message)
		return message		

class Deck(object):
	def __init__(self):
		self.cards = []
		for i in range(1, 53):
		 	self.cards.append(Card(i))
	
	def getSize(self):
		return len(self.cards)
	
	def getTopCard(self):
		print('GETTING TOP CARD ' + self.cards[0].printCard() )
		return self.cards[0]
	
	def removeTopCard(self):
		print(self.cards[0].printCard() + ' TOP CARD FROM DECK - REMOVED')
		self.cards.remove(self.cards[0])
	
	def shuffleDeck(self):
		print('SHUFFLING CARDS ')
		random.shuffle(self.cards)
	
	def printCards(self):
		print('PRINTING CARDS IN DECK ')
		for card in self.cards:
			card.printCard()

class Player(object):
	def __init__(self, name):
		print('A player has been initialized')
		self.name = name
		self.hand = []
		self.taken = []
		self.wins = 0
	
	# giveCard() 
	# returns top card and del removes it from the hand list
	def giveCard():
		card = self.hand[0]
		self.hand.remove(self.hand[0])
		return card
	
	def receiveCard(self, card):
		self.taken.append(card)

	# second time I have to make shuffle method - add this in todo list. To make only 1 shuffle methiods for all lists of card.
	# might have to change the player card and taken lists to some kind of a deck object in order to do the Todo
	def shuffleTaken(self):
		print('SHUFFLING ' + self.name + "'s cards")
		random.shuffle(self.taken)
	
	def takenToHand(self):
		print("TAKEN TO HAND CONVERTION")

		self.shuffleTaken()
		for card in range(1, len(self.taken) + 1):
			self.hand.append(self.taken[0])
			self.taken.remove(self.taken[0])

	def printHand(self):
		print( self.name + "'s hand: ")
		for c in self.hand:
			c.printCard()
		if len(self.hand) == 0:
			print("No cards in Hand")
		
	def printTaken(self):
		print( self.name + "'s taken: ")
		for c in self.taken:
			c.printCard()
		if len(self.taken) == 0:
			print("No cards in Taken")
	
	def printNumCards(self):
		total = len(self.hand) + len(self.taken)
		print(self.name + ' has ' + str(total) + ' cards')

	def gainAWin(self):
		self.wins += 1

	def scores(self):
		# maybe some more robust type of scoring pane
		return wins

class Table(object):
	def __init__(self, deck, player1, player2):
		self.deck = deck
		self.p1 = player1
		self.p2 = player2
		self.playZone = []
	
	# This method gives 26 cards yeach player 1 by 1
	# The Deck will have 0 elements after this operation
	def deckDeals(self):
		#self.deck.shuffleDeck()
		while deck.getSize() > 0:
			
			self.p1.receiveCard(deck.getTopCard())
			self.deck.removeTopCard()
			
			self.p2.receiveCard(deck.getTopCard())
			self.deck.removeTopCard()
		
		print('deck lenght: ' + str(deck.getSize()))
		print(self.p1.printTaken())
		print(self.p2.printTaken())

	# This method will reward the player with stronger card
	# with the cards in the playzone
	def winnerSituation(player):
		# rewards a player a list of cards
		# deletes these cards from the playzone
		for card in self.playZone:
			player.receiveCard(card)	
		
		self.playZone.clear() # equivalent to self.playZone = [] or del self.playzone[:]




	def turn(self, p1, p2):
	 	
	 	card = p1.giveCard()
	 	card2 = p2.giveCard()
	 	playZone.append(card)
	 	playZone.append(card2)
	 	
	 	if card.compareWith(card2) == True:
			winnerSituation(p1)
		
		elif card.compareWith(card2) == False:
			winnerSituation(p2)
		
		else: # when its neither True nor False then they are the same
			war()
	
	def war(self, p1, p2):



		




while True:
	# init the two players
    grigor = Player('grigor')
    teodor = Player('teodor')

    # init the deck
    deck = Deck()

    # init the table
    table = Table(deck, grigor, teodor)
    
    # the cards from deck to players
    table.deckDeals()
    # printout to check for errors
    grigor.printNumCards()
    teodor.printNumCards()




    
 

    again = input('q to quit: ')
    if again == 'q' or again == 'Q':
    	break
