import random
import itertools

playerList = []

print("Time to play Old Maid! \n\n Menu \n 1. New Game \n 2. Play Again \n 3. How to Play")

menuChoose = input('')
menuChoose = int(menuChoose)

class Player:
    cards = []

    def __init__(self, playerID, name, cards):
        self.id = playerID
        self.name = name
        self.cards = cards

    def addCard(self, cards):
        self.cards.append(cards)

    def getName(self):
        return self.name

    def getCards(self):
        return self.cards


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
    suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
    for suit in suits:
        for value in range(2,15):
            if value == 11:
                value = 'Jack'
            elif value == 12:
                value = 'Queen'
            elif value == 13:
                value = 'King'
            elif value == 14:
                value = 'Ace'
            deck.append(str(value) + ' of ' + suit)
    deck.append('The Old Maid')
    random.shuffle(deck)
    for card in deck:
        print(card)
    return deck

deck = BuildDeck()

# class OldMaid():
#     nothing = 'nothing'


# def __init__(self,PlayerNumber):
#     self.__init__(playerNum)
#     self.Players = []

class OldMaid:
    def Start(self):
        p = 0
        for card in range(len(deck)):
            for player in range(len(playerList)):
                try:
                    drawCard = deck.pop()
                    
                    print(drawCard + " was drawn from deck.")
                    # print(players[p])
                    p = p + 1
                except Exception:
                    break





OldMaid().Start()

for i in range(len(playerList)):
    print(Player.getName(playerList[i]))
    print(Player.getCards(playerList[i]))


# ANSI escape sequences for terminal output
# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class colors:
    GRAY = '\033[90m'
    YELLOW = '\033[93M'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[93m'
    WHITE = '\033[0m'
    UNDERLINE = '\033[4m'




# playDeck = BuildDeck()
# playDeck = random.shuffle(BuildDeck())
#
# print(playDeck)

print(colors.GRAY + "\u2660 "
      + colors.RED + "Another test")

