import random
import itertools

playerList = []

print("Time to play Old Maid! \n\n Menu \n 1. New Game \n 2. Play Again \n 3. How to Play")

menuChoose = input('')
menuChoose = int(menuChoose)

class Player:
    cardList = []

    def __init__(self, playerID, name, card):
        self.id = playerID
        self.name = name
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getName(self):
        return self.name

    def getCards(self):
        return self.cards

    def getValue(self, value):
        return self.cards.index(value)

    def getId(self):
        return self.id


def CreatePlayers():
    playerObjList = []
    playerCount = 0

    for player in range(playerNum):
        if playerCount == 0:
            playerObjList.append(Player(playerCount,'Player',''))
        else:
            playerObjList.append(Player(playerCount,'Computer ' + str(playerCount), ''))
        playerCount = playerCount + 1

        # for player in players:
        # print(player)
    return playerObjList

if menuChoose == 1:
    playerNum = input("How many players? ")
    playerNum = int(playerNum)
    playerList = CreatePlayers()


def BuildDeck():
    deck = []
    # Shortcut codes for diamonds hearts clubs spades
    suits = ['\u2662', '\u2661', '\u2663', '\u2660']
    for suit in suits:
        for value in range(2,15):
            if value == 11:
                value = 'J'
            elif value == 12:
                value = 'Q'
            elif value == 13:
                value = 'K'
            elif value == 14:
                value = 'A'
            deck.append(str(value) + " " + suit)
    deck.append(15)
    random.shuffle(deck)
    for card in deck:
        print(card)
    return deck

# def BuildDeck():
#     deck = []
#     # Shortcut codes for diamonds hearts clubs spades
#     suits = ['\u2662', '\u2661', '\u2663', '\u2660']
#     for suit in suits:
#         for value in range(2,15):
#             if value == 11:
#                 value = 'J'
#             elif value == 12:
#                 value = 'Q'
#             elif value == 13:
#                 value = 'K'
#             elif value == 14:
#                 value = 'A'
#             deck.append(str(value) + " " + suit)
#     deck.append(15)
#     random.shuffle(deck)
#     for card in deck:
#         print(card)
#     return deck

def FaceCard(card):
    hand = []
    for value in range(2,15):
        if value == 11:
            card = 'J'
        elif value == 12:
            card = 'Q'
        elif value == 13:
            card = 'K'
        elif value == 14:
            card = 'A'
        return card



deck = BuildDeck()

tempHand = []

# class OldMaid():
#     nothing = 'nothing'


# def __init__(self,PlayerNumber):
#     self.__init__(playerNum)
#     self.Players = []

class OldMaid:
    def Start(self):
        p = 0
        # Deals cards out
        for c in range(len(deck)):
            for pl in range(len(playerList)):
                try:
                    drawCard = deck.pop()
                    Player.addCard(playerList[pl], drawCard)
                    print(Player.getName(playerList[pl]) + " draws a " + drawCard)
                    # print(drawCard + " was drawn from deck.")
                    # print(players[p])
                    p = p + 1
                except Exception:
                    break

        while 1==1:
            for p in range(len(playerList)):
                if p == 0:
                    cards = []
                    values = []
                    pairs = []
                    for c in range(len(Player.getCards(playerList[p]))):
                        cardList = Player.getCards(playerList[p])
                        # for i in c:
                        #     Player.getCards(playerList[p]))
                        card = cardList[c]
                        cardValue = card.split(' ')
                        cards.append(cardValue)

                    print(cards)
                    for i in cards:
                        for value in i:
                            values.append(value)
                    print(values)
                    for v in range(2,10):
                        if values.count(str(v)) == 2:
                            print("Found one")

                    values.count(1)
            break



        # First move is rolled for
        # playerRolls = [0,0,0,0]
        # highRoll = 0
        # highRoller = 0
        # winners = []
        # for p in range(playerNum):
        #     rollNum = random.randint(1,6)
        #     playerRolls[p] = rollNum
        #     if rollNum > highRoll:
        #         highRoll = rollNum
        #         highRoller = Player.getName(playerList[p])
        #     if rollNum == highRoll:
        #         while 1==1:
        #
        #     print(Player.getName(playerList[p]) + " rolled a " + str(rollNum))
        # # for r in range(len(playerRolls)):
        # #     if playerRolls[r] > highRoll:
        # #         highRoll = playerRolls[r]
        # #         highRoller = playerRolls.index(r)
        # #     # if playerRolls[r] == highRoll:
        # print("High roller is " + str(highRoller))







OldMaid().Start()


print(Player.getName(playerList[0]))
print(Player.getCards(playerList[0]))
print(Player.getId(playerList[0]))



# ANSI escape sequences for terminal output
# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
# class suitColors:
#     DIAMONDS = '\u2662'
#     HEARTS = '\u2661'
#     CLUBS = '\u2663'
#     SPADES = '\u2660'
#     GRAY = '\033[90m'
#     YELLOW = '\033[93M'
#     BLUE = '\033[94m'
#     GREEN = '\033[92m'
#     RED = '\033[93m'
#     WHITE = '\033[0m'
#     UNDERLINE = '\033[4m'




# playDeck = BuildDeck()
# playDeck = random.shuffle(BuildDeck())
#
# print(playDeck)

# print(suitColors.DIAMONDS + suitColors.HEARTS + suitColors.CLUBS + suitColors.SPADES)