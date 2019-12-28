#Coppy and paste the code from this while loop into the while loop in the main file
while True:
	# TEST 1
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

	#TEST 2
    # myDeck = Deck()
    # myDeck.printCards()
    # print('deck length ' + str(myDeck.getSize()))
    # print('-----------------------------------------------------------------')
    # myDeck.getTopCard()
    # myDeck.removeTopCard()
    # myDeck.printCards()
    # print('deck length ' + str(myDeck.getSize()))

    #TEST 3
    # myDeck = Deck()
    # myDeck.shuffleDeck()
    # myDeck.printCards()
    # p1 = Player('player 1')

    #Givvning the player cards from the deck
    # p1.receiveCard(myDeck.getTopCard())
    # myDeck.removeTopCard()
    # p1.receiveCard(myDeck.getTopCard())
    # myDeck.removeTopCard()
    # p1.receiveCard(myDeck.getTopCard())
    # myDeck.removeTopCard()

    # p1.printTaken()
    # p1.printHand()
    # print(" ")
    # myDeck.printCards()
    # print(" ")
    # p1.takenToHand()
    # p1.printTaken()
    # p1.printHand()
    
    #TEST 4
		# init the two players
    # player1 = Player('grigor')
    # player2 = Player('teodor')

    # # init the deck
    # deck = Deck()

    # # init the table
    # table = Table(deck, player1, player2)
    
    # # the cards from deck to players
    # table.deckDeals()
    # # printout to check for errors
    # player1.printNumCards()
    # player2.printNumCards()

    # print('STARTING GAME')
    
    # counter = 0
    # winner = ''
   
    # while player1.returnNumCards() > 0 or player2.returnNumCards() > 0:
    # 	counter += 1
    # 	print('Turn ' + str(counter) + " *************************************************")
    # 	table.turn(player1, player2)
    # 	input('press ENTER for next turn')
    # 	if player1.returnNumCards() < 1:
    # 		print ('Congratulations player ' + player1.name)
    # 	elif player2.returnNumCards() < 1:
    # 		print ('Congratulations player ' + player2.name)
    # 	else:
    # 		pass	
    # print('Game finished')
    again = input('q to quit: ')
    if again == 'q' or again == 'Q':
    	break
