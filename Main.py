import random

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

    def removeCard(self, card):
        self.cards.pop(card)

    def getCardIndex(self, card):
        return self.cards.index(card)

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
    deck.append(str(15) + " OM")
    random.shuffle(deck)
    for card in deck:
        print(card)
    return deck

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
                cards = []
                values = []
                pairs = []
                for c in range(len(Player.getCards(playerList[p]))):
                    cardList = Player.getCards(playerList[p])
                    # for i in c:
                    #     Player.getCards(playerList[p]))
                    card = str(cardList[c])
                    cardValue = card.split(' ')
                    cards.append(cardValue)

                print(Player.getName(playerList[p]) + str(cards))
                for i in cards:
                    for value in i:
                        values.append(value)
                del values[1::2]
                print(Player.getName(playerList[p]) + str(values))
                # Checks for pairs and discards them
                for v in range(len(values)):
                    numCount = 0
                    #todo fix
                    if values.count(str(v)) == 2 and v in range(2,10):
                        numCount = 0
                        for m in values:
                            while numCount < 2:
                                if m == str(m):
                                    Player.removeCard(playerList[p], values.index(m))
                                    numCount = numCount + 1
                        print(str(Player.getName(playerList[p])) + " discarded a pair of " + str(v) + "'s")
                if values.count('J') == 2:
                    jCount = 0
                    for m in values:
                        while jCount < 2:
                            if str(m) == 'J':
                                Player.removeCard(playerList[p], values.index(m))
                                jCount = jCount + 1
                    print(str(Player.getName(playerList[p])) + " discarded a pair of Jacks")
                if values.count('Q') == 2:
                    qCount = 0
                    for m in values:
                        while qCount < 2:
                            if str(m) == 'Q':
                                Player.removeCard(playerList[p], values.index(m))
                                qCount = qCount + 1
                    print(str(Player.getName(playerList[p])) + " discarded a pair of Queens")
                if values.count('K') == 2:
                    kCount = 0
                    for m in values:
                        while kCount < 2:
                            if str(m) == 'K':
                                Player.removeCard(playerList[p], values.index(m))
                                kCount = kCount + 1

                    print(str(Player.getName(playerList[p])) + " discarded a pair of Kings")
                if values.count('A') == 2:
                    aCount = 0
                    for m in values:
                        while aCount < 2:
                            if str(m) == 'A':
                                Player.removeCard(playerList[p], values.index(m))
                                aCount = aCount + 1

                    print(str(Player.getName(playerList[p])) + " discarded a pair of Aces")
                    # values.count(1)
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


print(Player.getName(playerList[1]))
print(Player.getCards(playerList[1]))
print(Player.getId(playerList[1]))


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
