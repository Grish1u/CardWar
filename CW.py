import random
import time
class Card(object):
	suits = ['C', 'D', 'H', 'S' ] 
	names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
	
	def __init__(self, value):
		self.value = value
		self.name = self.names[(value % 13) - 1] # formula to get name from value is (value % 4) - 1
		self.suit = self.suits[int((value - 1)/ 13)]
	# returns true if name is bigger
	def compare(self, another):
		if self.name > another.name:
			return True
		elif self.name == another.name:
			msg = str(self.printself()) + ' and ' + str(another.printself()) + ' are equal'
			return msg
		else:
			return False

	def printself(self):
		msg = self.name + 'of' + self.suit + ' v' + str(self.value) + '/ '
		return msg
		# print(self.name + ' of ' + self.suit + ' - value of ' + str(self.value))
	def getNameValue(self):
	 	return self.names.index(self.name)
class Deck(object):
	def __init__(self):
		self.cards = []
		for i in range(1, 53):
			self.cards.append(Card(i))

	def shuffleDeck(self):
		print('Deck : Shuffling cards in deck ')
		random.shuffle(self.cards)
	
	def getSize(self):
		return len(self.cards)
	
	def getTopCard(self):
		return self.cards[0]
	
	def removeTopCard(self):
		self.cards.remove(self.cards[0])
	
	
	def printCards(self):
		print('Deck : Printing cards in deck ')
		msg = ''
		for card in self.cards:
			msg = msg + (card.printself() + '/')
		print (msg)

class User(object):
	def __init__(self, name):
		self.name = name
		self.hcards = []
		self.tcards = []
		self.flag = True
	
	def turn(self):
		self.fixCards()
		
		if self.flag:
			print('User: {} puts {}'.format(self.name, self.hcards[0].printself()))
			return self.giveCard()
		else:
			msg = 'User:{} Im out of cards'.format(self.name)
			print('User: {}: {}'.format(self.name, msg))
			return(Card(0)) # So atm it creates an Ace card for the loser but since it is used after user flag set to False, it won't do anything
	# fixcards()
	# if user has no cards initates end screen winner resolution
	# if user has no cards in hand then hcard takes all cards from tcards
	def fixCards(self):
		if(len(self.hcards) + len(self.tcards) < 1):
			self.resign() # needs to initiate end screen and out of current game process
		if(len(self.hcards) < 1):
			while(len(self.tcards) > 0):
				k = self.tcards.pop(0)
				self.hcards.append(k)

	def giveCard(self):
 		k = self.hcards.pop(0) # the pop is supposed to remove it from handcards list
 		return k
	
	def resign(self):
		print('User: {} resigned'.format(self.name))
		self.flag = False
	
	def getWins(self):		
		return self.wins

	def getNumCards(self):
		msg = len(self.hcards) + len(self.tcards)
		return msg
	
	def aboutMe(self):
		msg = "User: {}, hcards:{}, tcards:{}".format(self.name, len(self.hcards), len(self.tcards))
		print(msg)

	def getMe(self):
		return self
class Table(object):
	def __init__(self, pA, pB):
		self.deck = Deck()
		self.pA = pA
		self.pB = pB
		self.playzone = []

	def deckDeals(self):
		self.deck.shuffleDeck()
		while(len(self.deck.cards) > 0):
			k = self.deck.cards.pop(0)
			self.pA.tcards.append(k)
			h = self.deck.cards.pop(0)
			self.pB.tcards.append(h)	
			
	# fight() decides the stronger card
	# the card of the second player to put in playzone will be indexed 0
	def fight(self):
		print('{} vs {}'.format(self.playzone[-2].printself(), self.playzone[-1].printself()))
		if self.playzone[-2].compare(self.playzone[-1]) == True: # p1 card stronger
			print(self.pA.name + "'s card wins")
			self.playzoneToPlayer(self.pA)
		elif self.playzone[-2].compare(self.playzone[-1]) == False: # p2 card stronger
			print(self.pB.name + "'s card wins")
			self.playzoneToPlayer(self.pB)
		else:
			print('Table: EEEEEENTERIIIIIINNNGGGGGG WAAAAAAAAAAAAAAAAAAAAARRRRRR')
			self.war()
	
	def war(self): # 4 times each player gives card
		for i in range(0, 5):
			self.playzone.append(self.pA.turn())
			self.playzone.append(self.pB.turn())

	def turnLoop(self):
		a = self.pA.turn()
		b = self.pB.turn()
		self.playzone.append(a)
		self.playzone.append(b)
		self.fight()

	
	# when player wins he activates this method to get the cards from the playzone
	def playzoneToPlayer(self, player):
		while (len(self.playzone) > 0):
			k = self.playzone.pop(0)
			if (player.name == self.pA.name):
				self.pA.tcards.append(k)
			elif (player.name == self.pB.name):
				self.pB.tcards.append(k)
			else:
				print ('Table: error')


	def aboutMe(self):
		pac = self.pA.getNumCards()
		pbc = self.pB.getNumCards()
		msg = "Table: deck:{} cards, pA:{} total cards, pB:{} total cards, playzone: {} cards".format(str(len(self.deck.cards)), pac, pbc, len(self.playzone) )
		print(msg)

	
class App(object):
	menu = {
		1: 'Play',
		2: 'See all time scores',
		3: 'Quit game',
		4: 'Login as different players'
	}
	# there is a default init method
	def __init__(self):
		self.name = 'Card War Game'
		self.users = []
		self.scores = []
		self.initUsers()
		self.initScores()

	def displayMenu(self):
		options = sorted(self.menu.keys())

		for option in options:
			print (option, self.menu[option])
		self.applyChoice()
	
	def applyChoice(self):
		choice = input('Menu : Your selection: ')
		if choice == '1':
			print('Menu : you selected 1')
			print('Menu : Game starting..')
			self.playWar()
		elif choice == '2':
			print('Menu : you selected 2')
			print('Menu : All time scores')
			self.showScores()
		elif choice == '3':
			print('Menu : you selected 3')
			print('Menu : quitting and saving scores')
			self.writeUsers()
			self.writeScores()
			quit()
	
	
	def showScores(self):
		for user in self.users:
			print('{} {} wins'.format(user, self.scores[self.users.index(user)]))
		# 	print('{} has {} wins'.format(self.users[i]), self.scores[i])

	
	def playWar(self):
			# load users with ones from usrnms.txt
			print('App: scores {}'.format(self.scores))
			print('App: all users {}'.format(self.users))

			# choose users and login
			a = input('App: p1 name: ') #
			indA = self.loginUser(a) # if useer in users returns its index if not appends a new name in users and returns last index
			b = input('App: p2 name: ') #
			indB = self.loginUser(b)
			print('App: all users after login {}'.format(self.users))

			# I need to prepare for this
			table = Table(User(self.users[indA]), User(self.users[indB])) # creating a new user straight here passing the index from users as name
			table.deckDeals()
			table.aboutMe()
			input('App: press enter to begin..')
			print('App: Game Starts')
			time.sleep(0.8)
			
			# THIS SHOULD END WHEN A PLAYER HAS NO CARDS
			count = 0
			while table.pA.flag and table.pB.flag:
				#input('App: enter to continue')
				print('Turn ' + str(count))
				table.aboutMe()
				table.turnLoop()
				count += 1
				if count > 900 :
					print('App: Game might have entered an infinite loop')
					time.sleep(0.5)
					break

			# Winner resolution
			if table.pA.flag == False:
				print('App: congrats p2')
				self.scores[indB] += 1
				print('App: users list is: {}, {}'.format(str(len(self.users)), str(self.users)))
				del table
			elif table.pB.flag == False:
				print('App: congrats p1')
				self.scores[indA] += 1
				print('App: users list is: {}, {}'.format(str(len(self.users)), str(self.users)))
				del table	 
			else:

				print('App: unknown winner - error or something')
	
	


	# initUsers and initScores()
	# checks if a file is made
	def initUsers(self):
		try:
			file = open('usrnms.txt', 'r')
			for line in file:
				nm = line
				nm = nm[:-1] # removing the new line symbol
				self.users.append(nm)
			file.close()
			del file
			print('App: Users file loaded') 
		except IOError:
			print('App: Users file not found')
	
	def initScores(self):
		try:
			file = open('scores.txt', 'r')
			for line in file:
				num = line
				num = num[:-1] # deletes the new line symbol
				#print(type(num))
				self.scores.append(int(num))
			file.close()
			del file
			print('App: Scores file loaded')
		except IOError:
			file = open('scores.txt', 'w')
			file.close()
			del file
			print('App: Scores file not found\n... created a file called scores.txt')	
	
	# At the end we need to write them again
	def writeUsers(self):
		file = open('usrnms.txt', 'w')
		for user in self.users:
			file.write('{}\n'.format(user))
		file.close()
		del file
	
	def writeScores(self):
		file = open('scores.txt', 'w')
		for num in self.scores:
			file.write('{}\n'.format(num))
		file.close()
		del file

	def writeTurns(self, turnscount): # this method will write the turns count to a separate text files so if I want to make something later out of the info
		turnsfile = open('turns.txt', 'a+')
		turnsfile.write('{}:(warx5)-\n'.format(str(turnscount - 1)))
		turnsfile.close()
	
	# returns the name's index in list of users
	# if name not there it appends it to users end and returns index -1 (last)
	def loginUser(self, name):
		if name in self.users:
			indexinusers = self.users.index(name)
			print('App: User found in {} index'.format(str(indexinusers)))
			return indexinusers
		else:
			self.users.append(name)
			self.scores.append(0)
			print('App: User name appended to users list')
			theindex = self.users.index(name)
			return theindex # this is the last index where we append to

app = App() # With init of app I have loaded its users and scores fields

while True:
	app.displayMenu()


input('enting')
quit()

# ATM

# only works if I have set the 2 files first
# if I add another player it doesnt add another 0 to scores.txt and maybe list scores
