
#----------------------------------------------------------------------
# Poker Squares
# by Michal Burgunder 
# 
# Version 1.0 10th December 2017:
	#Created a functioning game with comments and exception handling

# Version 1.1 22nd April 2018
	# -Added plenty more comments
	# -Fixed an issue with calculating mean score
	# -Fixed another issue that didn't calculate the final mean score
	# -Fixed a bug that didn't show final score when quitting at the 
	#		the end of a game
	# -Allowed to quit from the very first input
	# -Added saving scores to a text file
	# -Reformatted for better readability

# To be done:
#	-Catch keyboard exception at any point in the game
#	-Allow to display all statistics from saved file
#----------------------------------------------------------------------
import random
import itertools
import statistics
import time
import datetime
#-----------------------------------------------------------------------

def WelcomingScreen():
#This is the opening screen.
	global quitOnStart
	
	print()
	print(" _       _  _____  _	  _____	 _____  _________  _____")
	print("| |     | ||  ___|| |    |  ___||  _  ||  _   _  ||  ___|")
	print("| |  _  | || |_   | |    | |    | | | || | | | | || |_")
	print("| | | | | ||  _|  | |    | |    | | | || | | | | ||  _|")
	print("\ \_| |_/ /| |___ | |___ | |___ | |_| || | |_| | || |___")
	print(" \_______/ |_____||_____||_____||_____||_|     |_||_____|\n")
	print("                     _______  _____")
	print("                    |__   __||  _  |")
	print("                       | |   | | | |")
	print("                       | |   | | | |")
	print("                       | |   | |_| |")
	print("                       |_|   |_____|\n")
	print("            _____  _____  _   _  _____  _____")
	print("           |  _  ||  _  || | / /|  ___||  _  | ")
	print("	   | |_| || | | || |/ / | |_   | |_| |")
	print("           |  ___|| | | ||   |  |  _|  |    _|")
	print("           | |    | |_| || |\ \ | |___ | |\ \\")
	print("           |_|    |_____||_| \_\|_____||_| \_\\\n")
	print("      _____  _____  _   _  _____  _____  _____  _____ ")
	print("     |  ___||  _  || | | ||  _  ||  _  ||  ___||  ___|")
	print("     | |___ | | | || | | || |_| || |_| || |_   | |___")
	print("     |___  || | | || | | ||  _  ||    _||  _|  |___  |")
	print("      ___| || |_| || |_| || | | || |\ \ | |___  ___| |")
	print("     |_____||____ ||_____||_| |_||_| \_\|_____||_____|")
	print("                 \_\ \n")

	WelcomeInput = input("Press 'q' at any time to quit the game, " +
	"'help' and press 'enter' to start. Have fun! ")
	print()
	if WelcomeInput == 'help':
		Options()
	if WelcomeInput == 'q':
		quitOnStart = True
#-----------------------------------------------------------------------
def clearBoard():
	#Resets all of the positions variables and prints the board.
	global quitOnStart
	if quitOnStart == True:
		return
		
	global a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, c1, c2, c3, c4, c5
	global d1, d2, d3, d4, d5, e1, e2, e3, e4, e5, a, b, c, d, e, one
	global two, three, four, five, cumScore
	#These are the position variables, which allow the player to set the
	#card value equal to these, and make them appear on the board. The 
	#last eleven variables are the displayed scores for each row and 
	#column. The finalCumulative variable adds all these score variables
	#together.
	
	a1 = a2 = a3 = a4 = a5 = b1 = b2 = b3 = b4 = b5 = c1 = c2 = '  '
	c4 = c5 = d1 = d2 = d3 = d4 = d5 = e1 = e2 = e3 = e4 = e5 = '  '
	c3 = a = b = c = d = e = one = two = three = four = five = '  '
	oneCalc = twoCalc = threeCalc = fourCalc = fiveCalc = '  '
	cumScore = '  '
#-----------------------------------------------------------------------
def showBoard():
#This function shows the current state of the board to the player. Each 
#box is 6 characters across, 3 in height
	global optionsBreak
	global OptionFirstRound
	if quitOnStart == True or optionsBreak == True:
		optionsBreak = False
		return
		
	print("       1      2      3      4      5   ")
	print("    __________________________________")
	print("   |      |      |      |      |      |")
	print("a  |  " + a1 + "  |  " + a2 + "  |  " + a3 + "  |  " + a4 +
	"  |  " + a5 + "  |      " + str(a))
	print("   |______|______|______|______|______|")
	print("   |      |      |      |      |      |")
	print("b  |  " + b1 + "  |  " + b2 + "  |  " + b3 + "  |  " + b4 +
	"  |  " + b5 + "  |      " + str(b))
	print("   |______|______|______|______|______|")
	print("   |      |      |      |      |      |")
	print("c  |  " + c1 + "  |  " + c2 + "  |  " + c3 + "  |  " + c4 +
	"  |  " + c5 + "  |      " + str(c))
	print("   |______|______|______|______|______|")
	print("   |      |      |      |      |      |")
	print("d  |  " + d1 + "  |  " + d2 + "  |  " + d3 + "  |  " + d4 +
	"  |  " + d5 + "  |      " + str(d))
	print("   |______|______|______|______|______|")
	print("   |      |      |      |      |      |")
	print("e  |  " + e1 + "  |  " + e2 + "  |  " + e3 + "  |  " + e4 +
	"  |  " + e5 + "  |      " + str(e))
	print("   |______|______|______|______|______|\n")
	print("      " + str(one) + "     " + str(two) + "     " + str(three) + 
	"     " + str(four) + "     " + str(five) + "         " + str(cumScore))
	print()
	OptionFirstRound = False
	optionsBreak = False
#-----------------------------------------------------------------------
def calculateScore(var1, var2, var3, var4, var5):
	
	global fullHouseThreeKind
	global fullHousePair
	global StraightFlushFlush
	global StraightFlushStraight
	global RoyalStraightFlush
		
	fullHouseThreeKind = False
	fullHousePair = False
	StraightFlushFlush = False
	StraightFlushStraight = False
	RoyalStraightFlush = False
	
	global lineScore	
	lineScore = 0
	
	global lineScoreFunc
	hand = []
	tempList = []
	
	global allChars
	allChars = []
	RanksCalc = [
		'2', '3', '4', '5', '6', '7', 
		'8', '9', 'T', 'J', 'Q', 'K', 'A'
		]
	SuitsCalc = ['C', 'D', 'H', 'S']
	charRank = []
	lineScoreFunc = 0
	
	hand.append(var1)
	hand.append(var2)
	hand.append(var3)
	hand.append(var4)
	hand.append(var5)

	for variable in hand:
		tempList = list(variable.upper())
		for char in tempList:
			allChars.append(char)
			
	#calculates scores using nested functions
	#Royals flush --> Straightflush --> flush + straight
	#FullHouse --> Pair + ThreeKind
	#TwoPair
	#FourKind
	RoyalFlush(allChars)
	FullHouse(allChars)
	TwoPair(allChars)
	FourKind(allChars)
	
	lineScore = lineScoreFunc
#-----------------------------------------------------------------------
def RoyalFlush(array):
#This function runs most of the other functions that calculate the 
#score. Also runs: StraightFlush(array).	
	
	global lineScoreFunc
	global RoyalStraightFlush
	global RF

	StraightFlush(array)
	
	if RoyalStraightFlush == True and charRank[9] == 14:
		print('ROYAL\nFLUSH')
		lineScoreFunc = RF
	return
#-----------------------------------------------------------------------	
def StraightFlush(array):
	#Also runs: Straight(array) and Flush(array).	
	global lineScoreFunc
	global RoyalStraightFlush
	global SF
	
	Flush(array)
	Straight(array)
	
	if (StraightFlushStraight == True and 
	StraightFlushFlush == True and 
	lineScoreFunc < SF):
		lineScoreFunc = SF
		RoyalStraightFlush = True
	return	
#-----------------------------------------------------------------------		
def Straight(array):
	#Does not further functions
	global lineScoreFunc
	global StraightFlushStraight
	global charRank
	global S
	
	rank = {
	'A': 14,
	'K': 13,
	'Q': 12,
	'J': 11,
	'T': 10,
	'9': 9,
	'8': 8,
	'7': 7,
	'6': 6,
	'5': 5,
	'4': 4,
	'3': 3,
	'2': 2,
	'C': -10,
	'D': -10,
	'H': -10,
	'S': -10
	}
	charRank = []
	
	for char in allChars:
		charRank.append(rank[char])
		
	charRank.sort()
	
	if (charRank[5] + 1 == charRank[6] and
	 charRank[6] + 1 == charRank[7] and
	  charRank[7] + 1 == charRank[8] and
	   charRank[8] + 1 == charRank[9]):	
		if lineScoreFunc < S:
			lineScoreFunc = S
		StraightFlushStraight = True
	return	
#-----------------------------------------------------------------------
def FourKind(array):
	#Does not any further functions
	global lineScoreFunc
	
	if lineScoreFunc > FK:
		return
		
	for char in array:
		charCount = array.count(char)
		if charCount == 4 and lineScore < FK and char in RanksCalc:
			lineScoreFunc = FK
			return
#-----------------------------------------------------------------------			
def Flush(array):
	#Does not run any further functions
	global lineScoreFunc
	global StraightFlushFlush
	global F
	
	for char in array:
		charCount = array.count(char)
		if charCount == 5 and lineScore < F and char in SuitsCalc:
			lineScoreFunc = F
			StraightFlushFlush = True
			return
#-----------------------------------------------------------------------			
def FullHouse(array):
	#Also runs: Pair(array) and ThreeKind(array)
	global lineScoreFunc
	global FH
	
	Pair(array)
	ThreeKind(array)
	
	if fullHouseThreeKind == True and fullHousePair == True and lineScore < FH:
		lineScoreFunc = FH
		return
#-----------------------------------------------------------------------		
def ThreeKind(array):
	#Does not run any further functions
	global lineScoreFunc
	global fullHouseThreeKind
	global TK
	
	for char in array:
		charCount = array.count(char)
		if charCount == 3 and lineScore < TK and char in RanksCalc:
			if lineScoreFunc < TK:
				lineScoreFunc = TK
			fullHouseThreeKind = True
			return	
#-----------------------------------------------------------------------					
def Pair(array):
	global fullHousePair
	global lineScoreFunc
	global P
	
	for char in array:
		charCount = array.count(char)
		if charCount == 2 and lineScore == 0 and char in RanksCalc:
			if lineScoreFunc < P:
				lineScoreFunc = P
			fullHousePair = True
			return
#-----------------------------------------------------------------------						
def TwoPair(array):
	global lineScoreFunc
	global TP
	
	if lineScoreFunc > TP:
		return	
		
	twoPair = 0
	rankCollector = []
	
	for char in array:
		if char in RanksCalc and char not in rankCollector:
			rankCollector.append(char)
				
	for char in rankCollector:	
		charCount = array.count(char)
		if charCount == 2 and lineScoreFunc < TP and char in RanksCalc:
			twoPair += 1
			
	if twoPair == 2:
		lineScoreFunc = TP
		return
#-----------------------------------------------------------------------

def changePoints():
#changes scoring pattern at the beginning of the game

	global P, TP, TK, S, F, FH, SF, FK, RF, quitOnStart, changePointsBlock
	
	if changePointsBlock == True:
		print("You can't change the scoring pattern during the game.")
		return
		
	print("To what point system would you like to change?\n")
	
	while True:
		UserInputPoints = input("\t'a' - Choose American scoring" +
								"\n\t'b' - Choose English scoring\n")
		if UserInputPoints == 'a':
			P = 2
			TP = 5
			TK = 10
			S = 15
			F = 20
			FH = 25
			FK = 50
			SF = 75
			RF = 100
			#These define the points for the American system.
			print("Point system changed to: American\n")
			return
		elif UserInputPoints == 'b':
			P = 1
			TP = 3
			TK = 6
			S = 12
			F = 5
			FH = 10
			FK = 16
			SF = 30
			RF = 30
			#These define the points for the British system.
			print("Point system changed to: English\n")
			return
		elif UserInputPoints == 'q':
			quitOnStart = True
			quitInPoints = True
			return
		else:
			print("Invalid input.")
			continue			
#-----------------------------------------------------------------------
def Options():
#This function allows the user to see different options before they are 
#starting the game (this includes the Rules, Credits, Changing of the
#Point system and starting the Game), or when they are in the middle of 
#it.
	global UserInOption
	global OptionFirstRound
	global quitOnStart
	global optionsBreak
	global quitInPoints
	global changePointsBlock
	
	optionsBreak = False
	UserInOption = 'ttttt'
	print("What do you need help with? " +
	"Please type in the desired function:\n")
	print("\tr -Rules & how the game works\n\tc -Credits\n\tp " + 
	"-Changing of point system")
	
	InOptions = ['r', 'p', 'g', 'c', 'q']
	while True:
		if OptionFirstRound == True:
			UserInOption = input("\nIs there anything else you need " +
			"help with?\n" +
			"\tr -Rules & how the game works\n" +
			"\tc -Credits\n" +
			"\tp -Changing of point system\n" +
			"\tg - Return to the game\n")
		else:
			UserInOption = input()
		#print(UserInOption)
		if UserInOption == 'q':
			quitOnStart = True
			return
		elif UserInOption == 'r':
			print("Rules of the game:\n")
			time.sleep(0.4)
			print("The goal of the game is to place the cards, one by" +
			" one, into a 5x5 box. For each column and each line, you" +
			" can score different card combinations that will give " +
			"you points depending on the combination.")
			print("\nThis is the point distribution: \n")
			time.sleep(0.4)
			print(" \t8♥ 8♠ J♥ 2♠ 6♦ (pair): 2 points\n" +
			"\t7♣ 7♦ 3♥ 3♠ 9♥ (two pair): 5 points\n" +
			"\tK♠ K♣ K♦ 5♣ 4♦ (three of a kind): 10 points\n" +
			"\t2♠ 3♣ 4♦ 5♥ 6♠ (straight): 15 points\n" +
			"\t7♥ 2♥ A♥ 5♥ J♥ (flush): 20 points\n" +
			"\t9♣ 9♦ 9♥ 3♠ 3♣ (full house): 25 points\n" +
			"\tQ♣ Q♦ Q♥ Q♠ 8♣ (four of a kind): 50 points\n" +
			"\t5♣ 6♣ 7♣ 8♣ 10♣ (straight flush): 75 points\n" +
			"\t10♥ J♥ Q♥ K♥ A♥ (royal flush): 100 points\n")
			print("")
			print("In the British scoring system, scoring works a " + 
			"little differently, although the different combinations " + 
			"that give points is still the same:\n")
			print(" \t8♥ 8♠ J♥ 2♠ 6♦(pair): 1 points\n" +
			"\t7♣ 7♦ 3♥ 3♠ 9♥ (two pair): 3 points \n" +
			"\t7♥ 2♥ A♥ 5♥ J♥ (flush): 5 points\n" +
			"\tK♠ K♣ K♦ 5♣ 4♦ (three of a kind): 6 points\n" + 
			"\t9♣ 9♦ 9♥ 3♠ 3♣ (full house): 10 points\n" +
			"\t2♠ 3♣ 4♦ 5♥ 6♠(straight): 12 points\n" + 
			"\tQ♣ Q♦ Q♥ Q♠ 8♣ (four of a kind): 16 points\n" + 
			"\t5♣ 6♣ 7♣ 8♣ 10♣ (straight flush): 30 points\n" + 
			"\t10♥ J♥ Q♥ K♥ A♥ (royal flush): 30 points\n")
			print("\nThe standard scoring system is the American " +
					"system. To change between systems, press 'p'. ")
			print("")
		elif UserInOption == 'g':
			print("Have fun!")
			optionsBreak = True
			showBoard()
			return
		elif UserInOption == 'c':
			print("Michal Burgunder. Thanks playing! <33 Email: " + 
			"michal_burgunder@yahoo.com")
		elif UserInOption == 'p':
			changePoints()
			if quitOnStart == True:
				break
			if quitInPoints == True:
				return
		elif UserInOption in Positions:
			break
		else:
			print("Not a valid input. Place the card in an " +
													"empty position:\n")
			continue
		
		OptionFirstRound = True
#-----------------------------------------------------------------------	
def scoreCheck():
#scoreCheck checks the inputted score at the end of the game to see if 
#the score given in by the user is a number, and not an invalid input.
	global score2

	while True:
		try:
			print("Congratulations you got " + str(cumScore) + 
															" points!")
			score2 = input("Press 'enter' to play again, " +
												"or enter q to quit:\n")
			scoreList = list(score2)
			if score2 == 'q':
				break
			for number in scoreList:
				numNumber = int(number)
			break
		except ValueError:		
			print("\nInvalid input! Try again")			
#-----------------------------------------------------------------------
def mean(score):
    return float(sum(score)) / max(len(score), 1)
#----------------------------------------------------------------------- 	
def FinalRemarks():
	global resultScore
	global cumScore

	print("\nYou have finished playing poker squares!\n")
	print("You have played " + str(t) + " times. " +
									"These are all of your scores: \n")
	resultScore.append(cumScore)
	try:
		resultScore = [int(score) for score in resultScore]
	except: resultScore = []
	print(resultScore)
	print()

	dt = datetime.datetime.now()

	finalScoresDoc = open("finalScores_Pokersquares.txt","a")

	finalScoresDoc.write(str(dt.day) + '/' + 
						 str(dt.month) + '/' + 
						 str(dt.year) + '  ' + 
						 str(dt.hour) + ':' + 
						 str(dt.minute) + ':' + 
						 str(dt.second) + '  ' + 
						 str(resultScore) + '\n')

	try:
		print("Mean score: " + 
			str(statistics.mean((list(map(float, resultScore))))) + "\n")
			#scoreMean = list(map(float, score))
	except: print("Mean score: 0")
	print("Have an awesome day! <3")

#-----------------------------------------------------------------------

def game():
	global a, b, c, d, e, one, two, three, four, five
	global aCalc, bCalc, cCalc, dCalc, eCalc
	global oneCalc, twoCalc, threeCalc, fourCalc, fiveCalc
	global a1, a2, a3, a4, a5, b1, b2, b3, b4, b5, c1, c2, c3, c4, c5 
	global d1, d2, d3, d4, d5, e1, e2, e3, e4, e5
	global aSwitch,  bSwitch, cSwitch, dSwitch, eSwitch
	global oneSwitch, twoSwitch, threeSwitch, fourSwitch, fiveSwitch
	global cumScore, cumScoreCalc, cumSwitch, score, score2
	global t
	global play, used_Positions
	
	global quitOnStart
	global used_cards
	global UserInOption
	global changePointsBlock
	changePointsBlock = True

	i = 0 #Used to regulate amount of cards given out (25)
	while play == True:
		if quitOnStart == True:
			break
		for card in CARDS:	
			card = random.sample(CARDS, 1)
			flippedCard = card[0]
			used_cards.append(card[0])
			print("Card: " + card[0])
			print("Type in a valid position (e.g. a4, e2, etc.):\n")
			CARDS.remove(card[0])
			while True:
				try:
					UserIn = input()
				except:
					print("Scores to be saved - to be developed")
					UserIn = 'q'
					break
				if UserIn == 'help':
					Options()
				if UserInOption == 'g':
					showBoard()
					print("Card: " + card[0])
					print("Type in a valid position (e.g. a4, e2, etc.): \n")
					UserInOption = 'sample'
					continue
				if UserIn == 'q':
					break	
				if UserIn in Positions:
					break
				if (UserIn not in Positions or 
				 UserIn != 'q' or 
				  UserIn != 'g' or 
				   UserIn != 'help'):
					print("Your input is not a valid input. " +
												"Please try again:\n")
					continue
			used_Positions.append(UserIn)
			try:
				Positions.remove(UserIn)
			except (ValueError):
				print("Quitting the game...")
				break
			i = i + 1
	
			result = [character for character in UserIn]
			horizontal = result[0]
			vertical = result[1]

			if horizontal == 'a':
				if vertical == '1':
					a1 = flippedCard
				elif vertical == '2':
					a2 = flippedCard
				elif vertical == '3':
					a3 = flippedCard
				elif vertical == '4':
					a4 = flippedCard
				elif vertical == '5':
					a5 = flippedCard
			elif horizontal == 'b':
				if vertical == '1':
					b1 = flippedCard
				elif vertical == '2':
					b2 = flippedCard
				elif vertical == '3':
					b3 = flippedCard
				elif vertical == '4':
					b4 = flippedCard
				elif vertical == '5':
					b5 = flippedCard
			elif horizontal == 'c':
				if vertical == '1':
					c1 = flippedCard
				elif vertical == '2':
					c2 = flippedCard
				elif vertical == '3':
					c3 = flippedCard
				elif vertical == '4':
					c4 = flippedCard
				elif vertical == '5':
					c5 = flippedCard
			elif horizontal == 'd':
				if vertical == '1':
					d1 = flippedCard
				elif vertical == '2':
					d2 = flippedCard
				elif vertical == '3':
					d3 = flippedCard
				elif vertical == '4':
					d4 = flippedCard
				elif vertical == '5':
					d5 = flippedCard
			elif horizontal == 'e':
				if vertical == '1':
					e1 = flippedCard
				elif vertical == '2':
					e2 = flippedCard
				elif vertical == '3':
					e3 = flippedCard
				elif vertical == '4':
					e4 = flippedCard
				elif vertical == '5':
					e5 = flippedCard


			if (a1  != '  ' and 
				 a2 != '  ' and 
				  a3 != '  ' and 
			       a4 != '  ' and 
				    a5 != '  ' and 
					 aSwitch == False):
				calculateScore(a1, a2, a3, a4, a5)
				a = lineScoreFunc
				if a < 10:
					a = ' ' + str(lineScoreFunc)
				else:
					a = lineScoreFunc
				aSwitch = True

			if (b1  != '  ' and
				 b2 != '  ' and 
				  b3 != '  ' and 
			       b4 != '  ' and 
				    b5 != '  ' and 
					 bSwitch == False):
				cumSwitch = True
				calculateScore(b1, b2, b3, b4, b5)
				b = lineScoreFunc
				if b < 10:
					b = ' ' + str(lineScoreFunc)
				else:
					b = lineScoreFunc
				bSwitch = True
				
			if (c1  != '  ' and 
				 c2 != '  ' and 
				  c3 != '  ' and 
			       c4 != '  ' and 
				    c5 != '  ' and 
					 cSwitch == False):
				cumSwitch = True
				calculateScore(c1, c2, c3, c4, c5)
				c = lineScoreFunc
				if c < 10:
					c = ' ' + str(lineScoreFunc)
				else:
					c = lineScoreFunc
				cSwitch = True
				
			if (d1 != '  ' and 
				 d2 != '  ' and 
				  d3 != '  ' and 
			 	   d4 != '  ' and 
				    d5 != '  ' and 
				     dSwitch == False):
				cumSwitch = True
				calculateScore(d1, d2, d3, d4, d5)
				d = lineScoreFunc
				if d < 10:
					d = ' ' + str(lineScoreFunc)
				else:
					d = lineScoreFunc
				dSwitch = True
				
			if (e1  != '  ' and 
				 e2 != '  ' and 
				  e3 != '  ' and 
			       e4 != '  ' and 
			        e5 != '  ' and 
					 eSwitch == False):
				cumSwitch = True
				calculateScore(e1, e2, e3, e4, e5)
				e = lineScoreFunc
				if e < 10:
					e = ' ' + str(lineScoreFunc)
				else:
					e = lineScoreFunc
				eSwitch = True
				
			if (a1  != '  ' and 
				 b1 != '  ' and 
				  c1 != '  ' and 
			       d1 != '  ' and
				    e1 != '  ' and 
					 oneSwitch == False):
				cumSwitch = True
				calculateScore(a1, b1, c1, d1, e1)
				oneCalc = lineScoreFunc
				if oneCalc < 10:
					one = ' ' + str(lineScoreFunc)
				else:
					one = lineScoreFunc
				oneSwitch = True
				
			if (a2  != '  ' and 
				 b2 != '  ' and
				  c2 != '  ' and 
			       d2 != '  ' and
				    e2 != '  ' and 
					 twoSwitch == False):
				cumSwitch = True
				calculateScore(a2, b2, c2, d2, e2)
				twoCalc = lineScoreFunc
				if twoCalc < 10:
					two = ' ' + str(lineScoreFunc)
				else:
					two = lineScoreFunc
				twoSwitch = True
				
			if (a3  != '  ' and 
				b3 != '  ' and 
				 c3 != '  ' and 
			      d3 != '  ' and 
				   e3 != '  ' and 
				    threeSwitch == False):
				cumSwitch = True
				calculateScore(a3, b3, c3, d3, e3)
				threeCalc = lineScoreFunc
				if threeCalc < 10:
					three = ' ' + str(lineScoreFunc)
				else:
					three = lineScoreFunc
				threeSwitch = True
				
			if (a4  != '  ' and
				 b4 != '  ' and
				  c4 != '  ' and
			       d4 != '  ' and
				    e4 != '  ' and
					 fourSwitch == False):
				cumSwitch = True
				calculateScore(a4, b4, c4, d4, e4)
				fourCalc = lineScoreFunc
				if fourCalc < 10:
					four = ' ' + str(lineScoreFunc)
				else:
					four = lineScoreFunc
				fourSwitch = True
				
			if (a5  != '  ' and
				 b5 != '  ' and
				  c5 != '  ' and
				   d5 != '  ' and
					e5 != '  ' and
					 fiveSwitch == False):
				cumSwitch = True
				calculateScore(a5, b5, c5, d5, e5)
				fiveCalc = lineScoreFunc
				if fiveCalc < 10:
					five = ' ' + str(lineScoreFunc)
				else:
					five = lineScoreFunc
				fiveSwitch = True
				
			if (aSwitch == True or bSwitch == True or cSwitch == True or
			 dSwitch == True or eSwitch == True or oneSwitch == True or 
			 twoSwitch == True or threeSwitch == True or 
			 fiveSwitch == True and cumSwitch == True):
				 
				cumScore = 0
				cumScoreCalc = 0
				ScoreVars = [a, b, c, d, e, 
						oneCalc, twoCalc, threeCalc, fourCalc, fiveCalc]
						
				for scoreLine in ScoreVars:
					if scoreLine == '  ':
						scoreLine = 0
						cumScore += int(scoreLine)
						scoreLine = '  '
					else:
						cumScore += int(scoreLine)
						
				if cumScore < 10:
					cumScoreCalc = cumScore
					cumScore = ' ' + str(cumScore)
				else:
					cumScore = cumScore		
					cumScoreCalc = cumScore
			
				cumSwitch = False
			
			showBoard()

			if i == 25:
				break	
			UserInput = ''
		if UserIn == 'q':
			break
		scoreCheck()
																						
		if score2 == 'q':
			play = False
		if score2 != 'y' and score2 != 'q':
			print("Here we go!")
			a = b = c = d = e = one = two = three = four = five = '  '
			cumScore = '  '
			oneCalc = twoCalc = threeCalc = fourCalc = fiveCalc = 0
			aSwitch = bSwitch = cSwitch = dSwitch = eSwitch = False
			oneSwitch = twoSwitch = threeSwitch = fourSwitch = False
			fiveSwitch = False
		
			time.sleep(0.8)
		
			Positions.extend(used_Positions)
			used_Positions = []
			t = t + 1
		
			resultScore.append(cumScoreCalc)
			score2 = ''
		
			print("\nPrevious scores: " + str(resultScore))
			time.sleep(1.5)
			print("\nRolling average: ")
		
			try:
				scoreMean = list(map(float, resultScore))
			except (ValueError):
				print("Value Error, something went wrong." +
									"You might have typed in a blank.")
			
			print(statistics.mean((scoreMean)))
				
			print()
			print("Clearing board...\n")
			clearBoard()
			time.sleep(3)
			showBoard()
			time.sleep(0.4)
		i = 0
		for trash_cards in used_cards:
			CARDS.append(trash_cards)
			used_cards = []

#-----------------------------------------------------------------------
#Creates the cards
SUITS = 'CHDS'
RANKS = '23456789TJQKA'
CARDS = [''.join(card) for card in itertools.product(RANKS, SUITS)]

#These constants are used to calculate straights
RanksCalc = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SuitsCalc = ['C', 'D', 'H', 'S']
	
#Creates all possible positions  (see clearboard())
#bove and used_Positions below)
HPos = 'abcde'
VPos = '12345'
Positions = [''.join(position) for position in itertools.product(HPos, VPos)]

used_Positions = [] #Regulates placement of cards to avoid doubles pos.
used_cards = [] #Repository for used cards.

score = [] #Container for your scores
t = 1 #Tell you how many times you have played

#These variables are used to calculate row and column scores, as well as
#regulate the calculation thereof.
oneCalc = twoCalc = threeCalc = fourCalc = fiveCalc = 0
aSwitch = bSwitch = cSwitch = dSwitch = eSwitch = cumSwitch = False
oneSwitch = twoSwitch = threeSwitch = fourSwitch = fiveSwitch = False

#These variables generate the cards on the board: [letter]# designates 
#row [letter] and column #. a, b, c, d, e and the written numbers 
#designate the final row and column scores. cumScore designates the
#final score.
a1 = a2 = a3 = a4 = a5 = b1 = b2 = b3 = b4 = b5 = c1 = c2 = '  '
c4 = c5 = d1 = d2 = d3 = d4 = d5 = e1 = e2 = e3 = e4 = e5 = '  '
c3 = a = b = c = d = e = one = two = three = four = five = '  '
cumScore = '  '

#Starting scores for each poker hand. This can be changed in Options().
P = 2
TP = 5
TK = 10
S = 15
F = 20
FH = 25
FK = 50
SF = 75
RF = 100

scoreMean = [0] #Rolling average score
resultScore = [] #Final scores
UserIn = '' #User Input for when the player is placing cards. 

changePointsBlock = False #This blocks changing of points.
quitInPoints = False #Blocks going back to changing points ingame.
quitOnStart = False #Allows the player to quit upon start.
optionsBreak = False #Helps to switch between Options() and game().
UserInOption = '' #Input variable for Option()	
OptionFirstRound = False #Prints an extra line in Options().

UserInOption = 'sample' #Variable for player input.
play = True


WelcomingScreen()
showBoard()
game()
FinalRemarks()