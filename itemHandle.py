
itemList = "leeroy's dignity", "golden acorn", "troll underwear", "bucket", "mermaid scale", "hair ties", "falcon keep key" , "bell"

# leeroy's tower item = bucket (NOTHING)
# treasureland item = mermaid scale (golden acorn)
# heaven's peak item = hair ties (bell)
# mermaid cove item = falcon keep key (mermaid)
# wish well item = troll underwear (bucket)
# the red chasm item = bell (troll underwear)
# braids item = golden acorn (hair ties)
# falcon keep item = leeroy's dignity (falcon keep key)
hasUsedBE = 0
hasUsedBU = 0
hasUsedGA = 0
hasUsedHT = 0
hasUsedTU = 0
hasUsedMS = 0
hasUsedFKK = 0

def pickupItem(userLocale, item, userInventory):
    UIlength = len(userInventory)
    ILlength = len(itemList)

    possibleItem = []
    for i in range(0, UIlength):
        if item == userInventory[i]:
            print "You already have that item"
            return
#    print "item",item
    for f in range(0, ILlength):
        if item == itemList[f]:
            possibleItem = item
#    print "PI", possibleItem
    if possibleItem:
        item = item_dict[possibleItem](userLocale)
    else:
        print "\nThat's not an item leeroy..."
#    print "item", item

    return item


def LD(userLocale):
    if userLocale == "falcon keep" and hasUsedFKK == 1:
        item = "leeroy's dignity"
        print "\nYou have finally gotten your digity back!!\n"
        print "Return to leeroy's tower to end your quest!!\n"
        return item
    else:
        print "You cannot get this item"
        return

def GA(userLocale):
    if userLocale == "braids" and hasUsedHT == 1:
        item = "golden acorn"
        print "\nYou recieved the golden acorn!!"
        print "\nOnward to treasureland!!!\n"
        return item
    else:
        print "\nThe trees of braids hold the acorn just above your reach mockingly as if playing a game."
        print "\nThey seem to be in dire need of hair ties...\n"
        return

def TU(userLocale):
    if userLocale == "wish well" and hasUsedBU == 1:
        item = "troll underwear"
        print "\n\nYou now have the troll underwear! YUCK!"
        print "\nLets get that troll his undies back!\n"
        return item
    else:
        print "\nYou lower the rope down but it fails to cling to the troll underwear!"
        print "\nIf only you had something to tie onto the end of the rope that could scoop up the undies..."
        return

def BU(userLocale):
    if userLocale == "leeroy's tower":
        item = "bucket"
        print "\nYou picked up the bucket!"
        print "\nI wonder what this is for.\n"
        return item

def MS(userLocale):
    if userLocale == "treasureland" and hasUsedGA == 1:
        item = "mermaid scale"
        print "\nYou got the mermaid scale! So shiny!\n"
        print "The squirrels lift you into the air and begin to sing...\n"
        print "TREASURELAND IS THE PLACE TO BE!"
        print "TREASURELAND, WHERE THE ACORNS ARE FREE!"
        print "TREASURELAND IS FOR YOU AND ME AND"
        print "ALL THE FUZZY CREATURES IN THE WORLD!!!!!"
        return item
    else:
        print "\nYou try to grab the mermaid scale, but a squirrel gets it before you and tosses it to his squirrel friend."
        print "\nAfter a twenty minute game of monkey in the middle you are forced to give up."
        print "\nMaybe if you get something for them they'll give up the scale?\n"
        return

def FKK(userLocale):
    if userLocale == "mermaid cove" and hasUsedMS == 1:
        item = "falcon keep key"
        print "\nThe mermaid gave you the falcon keep key!"
        print "\nTime to get your dignity back!!\n"
        return item
    else:
        print "\nThe mermaid snatches the key before you can grab it and laughs."
        print "\nYou can hear her set it back down as you turn your back to her."
        print "\nShe seems to be missing a scale... I wonder where it went.\n"
        return

def HT(userLocale):
    if userLocale == "heaven's peak" and hasUsedBE == 1:
        item = "hair ties"
        print "\nYou recieved the hair ties from the goat!"
        print "\nThe goat says, 'Thaaaanks for the beeeeell leeeroooy'\n"
        return item
    else:
        print "\nThe goat baaaas angrily at you and blocks your way."
        print "\nYou can't get to the hair ties right now as the goat blocks your way"
        print "\nHe has a rope around his neck which seems to have once held something...\n"
        return

def BE(userLocale):
    if userLocale == "the red chasm" and hasUsedTU == 1:
        item = "bell"
        print "\nThe troll screeches,'MY UNDIES! THANK YOU LEEROY!'"
        print "\nThe troll tossed you the bell!\n"
        return item
    else:
        print "\nThe troll jumps in front of you before you can reach the bell and snarls!"
        print "\nI'd figure out a different way to get the bell if I were you..."
        print "\nHe seems to be missing his underwear... weird huh?\n"
        return


def itemUse(userLocale, userInventory, item):
    possibleItemUsage = []
    UIlength = len(userInventory)
    for f in range(0, UIlength):
        if item == userInventory[f]:
            possibleItemUsage = item
    print "PIU", possibleItemUsage
    if possibleItemUsage:
        used_dict[possibleItemUsage](userLocale)
    else:
        print "\nThat's not something you can use..."
        print "Or maybe ya just don't have it?"



def hasUsedBE(userLocale):
    if userLocale == "heaven's peak":
            global hasUsedBE
            hasUsedBE = 1
            print "\nYou can now pickup the hair ties!"
    else:
        print "\nThat item has no use here. Try somewhere else."
def hasUsedBU(userLocale):
    if userLocale == "wish well":
        global hasUsedBU
        hasUsedBU = 1
        print "\nYou can pickup the troll underwear now!"
    else:
        print "\nThat item has no use here. Try somewhere else."
def hasUsedGA(userLocale):
    if userLocale == "treasureland":
        global hasUsedGA
        hasUsedGA = 1
        print "\nYou can pickup the mermaid scale now!"
    else:
        print "\nThat item has no use here. Try somewhere else."
def hasUsedHT(userLocale):
    if userLocale == "braids":
        global hasUsedHT
        hasUsedHT = 1
        print "\nYou can pickup the golden acorn now!"
    else:
        print "\nThat item has no use here. Try somewhere else."
def hasUsedTU(userLocale):
    if userLocale == "the red chasm":
        global hasUsedTU
        hasUsedTU = 1
        print "\nYou can pickup the bell now!"
    else:
        print "\nThat item has no use here. Try somewhere else."
def hasUsedMS(userLocale):
    if userLocale == "mermaid cove":
        global hasUsedMS
        hasUsedMS = 1
        print "\nYou can pickup the falcon keep key now!"
    else:
        print "\nThat item has no use here. Try somewhere else."
def hasUsedFKK(userLocale):
    if userLocale == "falcon keep":
        global hasUsedFKK
        hasUsedFKK = 1
        print "\nYou can pickup your dignity now!"
    else:
        print "\nThat item has no use here. Try somewhere else."

#global used item dictionary
used_dict = {
    "bell":hasUsedBE,
    "bucket":hasUsedBU,
    "golden acorn":hasUsedGA,
    "hair ties":hasUsedHT,
    "troll underwear":hasUsedTU,
    "mermaid scale":hasUsedMS,
    "falcon keep key":hasUsedFKK,
}

#item dictionary
item_dict = {
    "leeroy's dignity": LD,
    "golden acorn": GA,
    "troll underwear": TU,
    "bucket": BU,
    "bell": BE,
    "falcon keep key": FKK,
    "mermaid scale":MS,
    "hair ties": HT,
}
