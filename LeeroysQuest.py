import string
import locationHandle
import itemHandle


gameEnd = 0

userLocale = "leeroy's tower"

userInventory = []


#command processing
def preProccess(userCommand, userLocale):
    userCommand = string.lower(userCommand)
    userCommand = string.strip(userCommand)
    userCommand = userCommand.split(" ")
#    print "in pre-process"
#    print userCommand , '\n'
    return userCommand

def processCMD(userCommand, userLocale):
    possibleCommands = ("look","n","s","e","w","inv","help","exit","use","go", "pickup")
#    print "In processCMD"
#   checks to see how many words the user enters and
#   deletes any non-commands
    PClength = len(possibleCommands)
    UClength = len(userCommand)
#    print "UClength:" , UClength
    realCommand = list()
#    i= 0
#    print "userCommand:" , userCommand
#    print "userCommand[i]" , userCommand[i] , "\n"

#   2 or more "commands"
    i = 0
    if UClength >= 2:
        for i in range(0, UClength):
            for j in range(0, PClength):
                if userCommand[i] == possibleCommands[j]:
                    realCommand.append(userCommand[i])
#                    print "UClength:" , UClength
#                    print realCommand
        if realCommand:
            return realCommand
        else:
            randomResponse()
#   single commands
    if UClength == 1:
#       exit handling

        userCommand = ''.join(userCommand)
        for i in range(0, 1):
            for j in range(0, PClength):
                if userCommand == possibleCommands[j]:
                    realCommand.append(userCommand)
#                    print "UClength:" , UClength
#                    print "realCommand:", realCommand
        if realCommand:
            return realCommand
        else:
            randomResponse()

#command handling
def commandHandle(realCommand, userCommand, userLocale):
    cmdNum = len(realCommand)
    if cmdNum == 2:
#        print "There are 2 commands."
#        print realCommand , '\n'
        i= 0
        if realCommand[i] == "go" and realCommand[i+1] == 'n' or 'w' or 's' or 'e':
            userLocale = cmd_dict[realCommand[i+1]](userCommand, userLocale)
            return userLocale
        else:
            cmd_dict[realCommand[i]](userCommand, userLocale)
            cmd_dict[realCommand[i+1]](userCommand, userLocale)
            return userLocale

    elif cmdNum == 1:
#        print "There is 1 command"
        realCommand = ''.join(realCommand)
#        print realCommand
        userLocale = cmd_dict[realCommand](userCommand, userLocale)
        return userLocale

    elif cmdNum > 2:
#        print "In commandHandle"
#        print "userCommand:" ,userCommand
#        print "reaCommand:" ,realCommand , '\n'
        print "\nThat's one too many commands there sailor."
        print "Tone it down a bit eh? Try one or two commands at a time.\n"
        return userLocale


#command functions
def randomResponse():
    print "You can't do that!\n"
    return
#      Location Functions
def look(userCommand, userLocale):
    startLocale = locationHandle.getStartLocale()
    print "ayo you looked\n"
    return userLocale

def n(userCommand, userLocale):
#    print "NORTH\n"
    direction = "n"
    userLocale = locationHandle.findLocale(userLocale, direction)
#    print "New:" , userLocale
    return userLocale

def s(userCommand, userLocale):
#    print "SOUTH\n"
    direction = "s"
    userLocale = locationHandle.findLocale(userLocale, direction)
#    print "New:" , userLocale
    return userLocale

def e(userCommand, userLocale):
#    print "EAST\n"
    direction = "e"
    userLocale = locationHandle.findLocale(userLocale, direction)
#    print "New:" , userLocale
    return userLocale

def w(userCommand, userLocale):
#    print "WEST\n"
    direction = "w"
    userLocale = locationHandle.findLocale(userLocale, direction)
#    print "New:" , userLocale
    return userLocale

def go(userCommand, userLocale):
    possibleLocales =     "leeroy's tower", "the red chasm","braids", "heaven's peak", "mermaid cove", "wish well", "treasureland", "falcon keep"
    PLlength = len(possibleLocales)
    locationInput = ''
    if userCommand[0] == "go":
        del userCommand[0]
        userCommand = ' '.join(userCommand)
#           print userCommand
    for n in range(0,1):
        for q in range(0,PLlength):
            if userCommand == possibleLocales[q]:
                locationInput = userCommand
    if locationInput:
        userLocale = locationHandle.goLocale(locationInput, userLocale)
    else:
        print "That isn't somewhere you can go...."
    return userLocale


#   Item/Help Functions
def inv(userCommand, userLocale):
    print "This is what ya got: ", userInventory, '\n'
    return userLocale

def pickup(userCommand, userLocale):
    item = ''
    if userCommand[0] == "pickup":
        del userCommand[0]
        userCommand = ' '.join(userCommand)
#        print userCommand
    item = userCommand
    item = itemHandle.pickupItem(userLocale, item, userInventory)
    global userInventory
    if item != None and item != '':
        userInventory.append(item)
    return userLocale




def help(userCommand, userLocale):
    print "All commands are as follows:\n"
    print "look- looks around the current room.\n"
    print "n, s, e, w- sends your character North, South, East, or West respectivly.\n"
    print "inv- looks through your character's current inventory.\n"
    print "exit- exits out of the game.\n"
    print "pickup- adds an item to your inventory if that item is in the room you are currently in"
    print "use- uses an item of your choosing from your inventory.\n"
    print "go- sends your character to a specific location of your choosing.\n"
    print "help- displays all commands you can enter.\n"
    print "\nNOTE:\n"
    print "help, use, inv, pickup, and exit are all single commands."
    print "This means they should not be used with other commands."
    print "Instead use them with locations or items depending on what they do.\n"
    print "If you type exit at anytime all other commands will be ignored and you"
    print "will be asked if you would like to exit."
    print "\ngo will work with n, s, e, or w, but not with any other command."
    print "go is intended to be used with n, s, e, w, or with a location of your choosing."


    return userLocale

def use(userCommand, userLocale):
    item = ''
    if userCommand[0] == "use":
        del userCommand[0]
        userCommand = ' '.join(userCommand)
        print userCommand
    item = userCommand
    itemHandle.itemUse(userLocale, userInventory, item)

    return userLocale


#command dictionary
cmd_dict = {
    'look': look,
    'n': n,
    's': s,
    'e': e,
    'w': w,
    "inv": inv,
    "help": help,
    "use": use,
    "go": go,
    "pickup": pickup,
}
#   cmd_dict[realCommand]()


#GAME LOOP
print "\nYou are leeroy. A robot who lives on a huge island called 'Nowhere' in a big tower!"
print "The only things in your tower are your bed and your trusty bucket for which you have no use...\n"
print "Recently you lost your dignity to a falcon named feeroy whom always mocks you."
print "You must go on a quest to get your dignity back from that annoying ball of feathers!!"
print "\nBy the way, I am your concience and I will be accompanying you on this journey."
print "Just tell me what ya wanna do and I'll show you how to do it! Can you get leeroy's dignity back?\n"


while gameEnd == 0:


    print "\nYou are in" , userLocale
    print "\nWhat do you do?\n"
    userCommand = raw_input(">")
    userCommand = preProccess(userCommand, userLocale)
    realCommand = processCMD(userCommand, userLocale)
    if realCommand:
        RClength = len(realCommand)
        #exit handling
        if RClength == 1:
            if realCommand[0] == "exit":
                user_input = raw_input("Are you sure you want to exit?: ")
                if user_input == "yes" or user_input == "Yes":
                    break
        if RClength == 2:
            if realCommand[0] == "exit" or realCommand[1] == "exit":
                user_input = raw_input("Are you sure you want to exit?: ")
                if user_input == "yes" or user_input == "Yes":
                    break

        userLocale = commandHandle(realCommand, userCommand, userLocale)
        UIlength = len(userInventory)
        for i in range (0,UIlength):
            if userLocale == "leeroy's tower" and userInventory[i] == "leeroy's dignity":
                print "\nCongratulations!! You got your dignity back!\n"
                print "I hope you had fun!!"
                print "\nTune in next week when leeroy has to fight The Great and Powerful Famous Amos!!!\n"
                gameEnd = 1
