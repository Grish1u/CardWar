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
		return message		

class Deck(object):
	def __init__(self):
		self.cards = []
		for i in range(1, 53):
		 	self.cards.append(Card(i))
	
	def getSize(self):
		return len(self.cards)
	
	def getTopCard(self):
		print('getting top card from deck ' + self.cards[0].printCard())
		return self.cards[0]
	
	def removeTopCard(self):
		print(self.cards[0].printCard() + ' from deck removed ')
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
	def giveCard(self):
		print("%s, %d/hand, %d/taken" % (self.name, len(self.hand), len(self.taken)))
		if self.handEmpty():
			self.takenToHand()
			card = self.hand[0]
			self.hand.remove(self.hand[0])
			return card
		else:
			card = self.hand[0]
			self.hand.remove(self.hand[0])
			return card
	
	def handEmpty(self):
		if self.returnHandLen() < 1:
			return True
		else:
			return False
	
	def receiveCard(self, card):
		self.taken.append(card)

	# second time I have to make shuffle method - add this in todo list. To make only 1 shuffle methiods for all lists of card.
	# might have to change the player card and taken lists to some kind of a deck object in order to do the Todo
	def shuffleTaken(self):
		print('SHUFFLING ' + self.name + "'s taken cards")
		random.shuffle(self.taken)
	
	def takenToHand(self):

		self.shuffleTaken()
		for card in range(1, len(self.taken) + 1):
			self.hand.append(self.taken[0])
			self.taken.remove(self.taken[0])
		print('for ' + self.name + " taken to hand done ")

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
		total = self.returnHandLen() + len(self.taken)
		print(self.name + ' has ' + str(total) + ' cards')
	def returnNumCards(self):
		return self.returnHandLen() + len(self.taken)
	def returnHandLen(self):
		return len(self.hand)
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
		print('Dealing cards')
		while deck.getSize() > 0:
			
			self.p1.receiveCard(deck.getTopCard())
			self.deck.removeTopCard()
			
			self.p2.receiveCard(deck.getTopCard())
			self.deck.removeTopCard()
		
		print('deck lenght: ' + str(deck.getSize()))

		
		#print(self.p1.printTaken())
		#print(self.p2.printTaken())

	# This method will reward the player with stronger card
	# with the cards in the playzone
	def winnerSituation(self, player):
		# rewards a player a list of cards
		# deletes these cards from the playzone
		for card in self.playZone:
			player.receiveCard(card)	
		
		self.playZone.clear() # equivalent to self.playZone = [] or del self.playzone[:]


	def checkWinningCard(self, cardP1, cardP2):

		if cardP1.compareWith(cardP2) == True:
			self.winnerSituation(self.p1)
		
		elif cardP1.compareWith(cardP2) == False:
			self.winnerSituation(self.p2)
		
		else: # when its neither True nor False then they are the same
			self.war(self.p1, self.p2)

	def turn(self, p1, p2):
	 	
	 	p1Card = p1.giveCard()
	 	p2Card = p2.giveCard()
	 	self.playZone.append(p1Card)
	 	self.playZone.append(p2Card)

	 	self.checkWinningCard(p1Card, p2Card)
	
	def war(self, p1, p2):
		for i in range(1, 3): # 2 times
			card = p1.giveCard()
			card2 = p2.giveCard()
			self.playZone.append(card)
			self.playZone.append(card2)
		self.turn(p1, p2)

	 		

while True:
	# init the two players
    player1 = Player('grigor')
    player2 = Player('teodor')

    # init the deck
    deck = Deck()

    # init the table
    table = Table(deck, player1, player2)
    
    # the cards from deck to players
    table.deckDeals()
    # printout to check for errors
    player1.printNumCards()
    player2.printNumCards()

    print('STARTING GAME')
    
    counter = 0
    winner = ''
   
    while player1.returnNumCards() > 0 or player2.returnNumCards() > 0:
    	counter += 1
    	print('Turn ' + str(counter) + " *************************************************")
    	table.turn(player1, player2)
    	input('press ENTER for next turn')
    	if player1.returnNumCards() < 1:
    		print ('Congratulations player ' + player1.name)
    	elif player2.returnNumCards() < 1:
    		print ('Congratulations player ' + player2.name)
    	else:
    		pass	
    print('Game finished')		



    
 

    again = input('q to quit: ')
    if again == 'q' or again == 'Q':
    	break
