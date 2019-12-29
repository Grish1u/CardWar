# I will be using the following format of printing out data
# nameOfClass : whatever needs printing out
# This format of printing data will be used for testing purposes
# That way I know from which class comes the printing out

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
		if self.valueName > anotherCard.valueName: # TEST IT
			#print("Card : TRUE") -#TEST purpose
			return True
		elif (self.valueName == anotherCard.valueName):
			print("Card : VALUE IS EQUAL")
		else:
			#print("Card : FALSE")
			return False
	# card info
	def printCard(self):
		message = "Card : " +  self.valueName + ' of ' + self.color + '(' + str(self.cardValue) + ')'
		return message      

class Deck(object):
	def __init__(self):
		self.cards = []
		for i in range(1, 53):
			self.cards.append(Card(i))
	
	def getSize(self):
		return len(self.cards)
	
	def getTopCard(self):
		#print('getting top card from deck ' + self.cards[0].printCard()) # - Testing purposes
		return self.cards[0]
	
	def removeTopCard(self):
		#print(self.cards[0].printCard() + ' from deck removed ') # - Testing purposes
		self.cards.remove(self.cards[0])
	
	def shuffleDeck(self):
		print('Deck : Shuffling cards in deck ')
		random.shuffle(self.cards)
	
	def printCards(self):
		print('Deck : Printing cards in deck ')
		for card in self.cards:
			card.printCard()

class Player(object):
	def __init__(self, name):
		print('Player : A player has been initialized')
		self.name = name
		self.hand = []
		self.taken = []
		self.wins = 0
		self.hasCards = True
	
	# giveCard() 
	# returns top card and del removes it from the hand list
	def giveCard(self):
		print("Player : %s, %d/hand, %d/taken" % (self.name, len(self.hand), len(self.taken)))
		if self.handEmpty():
			self.takenToHand()
			card = self.hand[0]
			self.hand.remove(self.hand[0]) # TEST IT ?
			return card
		else:
			card = self.hand[0]
			self.hand.remove(self.hand[0]) # TEST IT ?
			return card
		print("Player : after turn - %s, %d/hand, %d/taken" % (self.name, len(self.hand), len(self.taken)))
	
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
		random.shuffle(self.taken)
	
	def takenToHand(self):
		if len(self.taken) > 0:
			print('Player : ' + self.name + " - taken to hand and shuffling")
			self.shuffleTaken()
			for card in range(1, len(self.taken) + 1):
				self.hand.append(self.taken[0])
				self.taken.remove(self.taken[0])
			print('Player : ' + self.name + " - taken to hand done ")
		else:
			print('Player : ' + self.name + " taken to hand unsuccessful" )
			self.hasCards = False
			break

	def printHand(self):
		print( "Player : " + self.name + " - hand cards: ")
		for c in self.hand:
			c.printCard()
		if len(self.hand) == 0:
			print("Player :  - No cards in Hand")
		
	def printTaken(self):
		print("Player : " + self.name + " - taken cards: ")
		for c in self.taken:
			c.printCard()
		if len(self.taken) == 0:
			print("Player : - No cards in Taken")
	
	def printNumCards(self):
		total = self.returnHandLen() + len(self.taken)
		print("Player : " + self.name + ' has ' + str(total) + ' cards')
	
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
		print('Table : deck lenght BEFORE dealing: ' + str(deck.getSize()))

		while deck.getSize() > 0:
			
			self.p1.receiveCard(deck.getTopCard())
			self.deck.removeTopCard()
			
			self.p2.receiveCard(deck.getTopCard())
			self.deck.removeTopCard()
		
		print('Table : deck lenght AFTER dealing: ' + str(deck.getSize()))

		
		#print(self.p1.printTaken())
		#print(self.p2.printTaken())

	# This method will reward the player with stronger card
	# with the cards in the playzone
	def winnerSituation(self, player):
		# rewards a player a list of cards
		# deletes these cards from the playzone
		print('Table : Play zone length before clear ' + str(len(self.playZone)))
		for card in self.playZone:
			player.receiveCard(card)    
		
		self.playZone.clear() # equivalent to self.playZone = [] or del self.playzone[:]
		print('Table : Play zone cleared')

	def checkWinningCard(self, cardP1, cardP2):
		if cardP1.compareWith(cardP2) == True:
			print("Table : " + str(player1.name) + ' wins with ' + cardP1.printCard())
			self.winnerSituation(self.p1)
		elif cardP1.compareWith(cardP2) == False:
			print("Table : " + str(player2.name) + ' wins with ' + str(cardP2.printCard()))
			self.winnerSituation(self.p2)
		else: # when its neither True nor False then they are the same
			cardsInWar = []
			for e in self.playZone:
				cardsInWar.append(e.printCard())

			print('Table : ' + str(cardsInWar) + ' WAR')
			self.war()

	def turn(self):
		# here we check for winning condition before each player gives a card
		if self.p1.hasCards:
			p1Card = self.p1.giveCard()
			self.playZone.append(p1Card)
		else:
			self.declareWinner(self.p2)
		
		if self.p2.hasCards:
			p2Card = self.p2.giveCard()
			self.playZone.append(p2Card)
		else:
			self.declareWinner(self.p1)
		self.checkWinningCard(p1Card, p2Card)


		

#elif p1.returnNumCards() < 1:
#self.declareWinner(self.p2)

	
	def war(self):
		for i in range(1, 3): # 2 times
			print('Table : card ' + str(i))
			card = self.p1.giveCard()
			card2 = self.p2.giveCard()
			self.playZone.append(card)
			self.playZone.append(card2)

		self.turn()
	
	def declareWinner(self, player):
		player.gainAWin()
		print('Congratulations ' + player.name)
		self.deck.cards.clear()
		del self.deck
		del self
		return 'We have a winner'

class menu():
	def __init__(self):
		self.atPlayers = []

while True:
	# init the two players
	player1 = Player('Gri')
	player2 = Player('Ted')

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
   
	while player1.returnNumCards() > 0 and player2.returnNumCards() > 0:
		counter += 1
		print('Main : Turn ' + str(counter) + " *************************************************")
		#input('Main : press ENTER for next turn')
		table.turn()
	if player1.returnNumCards() < 1:
		table.declareWinner(player2)
	elif player2.returnNumCards() < 1:
		table.declareWinner(player1)
	else:
		print('Main : The ELSE')   
	print('Main : Game finished')       



	
 

	again = input('q to quit: ')
	if again == 'q' or again == 'Q':
		break
