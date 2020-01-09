
player toTaken(arrayOfCards):
	for each card in arrayOfCards
		here = arrayOfCards.pop(card) # this is supposed to remove from playzone because it pops but im not sure because we are working with a copy of the variable here
		self.taken.append(here)

player checkcars()
	if no cards:
		self.flag = false
	# maybe here we can add a generic card just so we escape the possibility for crash 
	# no because we would enter an endless wormhole of comparing with generic cards

player TURN()
	check check cards()
	if flag = true:
		self.givecard() # to put card in table.playzone
	else : 
		pass

table decideStrongest()
	if self.playzone[0] > self.playzone[1]:
		player[0].toTaken(playzone)
	elif : # same for when p2 s card is bigger
		player[1].toTaken(playzone)
	else:
		print('entering war')
		self.turnx3
table turnx3() # equivalent of war
	for range(0, 3)
		player[0].turn()
		player[1].turn()

table turnlusCheck(): # we should check after each turn because we want to be able to give 3 not compared cards during war
	p1.turn
	p2.turn
	decideStrongest


# LOOP
do while both players flag true:
	table.player[0].turn()
	table.player[1].turn()
print('bravo')

if player[0].flag = false:
	player 2 winning
elif player[1].flag == false:
	# player 1 winning

	