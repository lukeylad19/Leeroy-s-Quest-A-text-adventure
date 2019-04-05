import itemHandle

LThasBeen = 1
RChasBeen = 0
BhasBeen = 0
HPhasBeen = 0
MChasBeen = 0
WWhasBeen = 0
ThasBeen = 0
FKhasBeen = 0

def findLocale(userLocale, direction):
    currentState = locale_dict[userLocale]
    cardinalState = direction_dict[direction]

    stateMachine = [
#         N, S, E, W
        [ 1, 5, 7, 2 ],       # Room 0-leeroy's tower
        [ -1, 0, 7, 2 ],      # Room 1-treasureland
        [ 3, 0, 1, 5 ],       # Room 2-heaven's peak
        [ -1, 2, -1, -1 ],    # Room 3-mermaid cove
        [ -1, -1, 5, -1 ],    # Room 4-wish well
        [ 2, 7, 0, 4 ],       # Room 5-the red chasm
        [ 0, 7, 1, 5 ],       # Room 6-braids
        [ -1, -1, 6, -1 ]     # Room 7-falcon keep
    ]

    roomNumber = stateMachine[currentState][cardinalState]
    if roomNumber == -1:
        print "You cannot go that way."
        roomNumber = currentState
    new_locale = new_locale_dict[roomNumber]

    if new_locale == "treasureland":
        if ThasBeen == 0:
            print "You have enter the forest known as treasureland!"
            print "You see beautiful trees and wildlife, but a group of squirrels catch you eye.\n"
            print "\nThey seem to be gathered around a shiny scale from some kind of ocean animal.\n"

        else:
            print "You arrive back in treasureland"
            print "\nThe squirrels are still gathered around the mermaid scale. Occasionally tossing it around the circle.\n"
        global ThasBeen
        ThasBeen = 1
#        print ThasBeen
    elif new_locale == "the red chasm":
        if RChasBeen == 0:
            print "You are standing in the red chasm!"
            print "The air here is humid and the temperature is red hot!!\n"
            print "You see a troll off to the left of the chasm who appears to be very upset."
            print "\nTo the right of the troll you see a bell with some rope attached to one end.\n"
        else:
            print "You arrive back at the red chasm"
            print "\nThe troll is still moping in the corner. The bell hasn't moved.\n"
        global RChasBeen
        RChasBeen = 1
#        print RChasBeen
    elif new_locale == "braids":
        if BhasBeen == 0:
            print "\nYou walk into the mystical forest of braids..."
            print "You hear what appear to be whispers...it is as if the trees are talking!"
            print "\nA glinting object in one of the mystical braid trees catches your attention."
            print "It's a golden acorn!! The braid tree appears to be....holding it?"
            print "\nTHESE TREES ARE ALIVE!\n"
        else:
            print "\nYou arrive back at braids\n"
            print "The trees still appear to be talking and moving as if they are alive."
            print "The golden acorn is still at the top of the same tree\n"
        global BhasBeen
        BhasBeen = 1
#        print BhasBeen
    elif new_locale == "heaven's peak":
        if HPhasBeen == 0:
            print "\nYour journey has brought you to heaven's peak! You make your way up the winding path in front of you."
            print "\nYou stop when you see a goat upon a ridge looking at you."
            print "\nThis goat has what appear to be oversized hair ties at his feet."
            print "Aren't those useful for braiding hair?\n"
        else:
            print "You arrive back at heaven's peak\n"
            print "The goat is still on the ridge guarding the hair ties.\n"
        global HPhasBeen
        HPhasBeen = 1
#        print HPhasBeen
    elif new_locale == "mermaid cove":
        if MChasBeen == 0:
            print "You have arrived at the legendary mermaid cove! The water reflects a flickering light off the ceiling."
            print "This place truly is as peaceful and beautiful as they say.\n"
            print "It looks like there is only one mermaid here right now."
            print "She is sitting on a rock right next to a large key... the key has a large FK written on it.\n"
        else:
            print "You arrive back at mermaid cove\n"
            print "The mermaid is still here sitting next to that big key.\n"
        global MChasBeen
        MChasBeen = 1
#        print MChasBeen
    elif new_locale == "wish well":
        if WWhasBeen == 0:
            print "You arrive at the legendary wish well!\n"
            print "The landscape is barren desert except for one area surrounding this myseteroius well which is littered with flowers and beautiful green grass\n"
            print "As you approach the well you smell dirty troll underwear coming from within..."
        else:
            print "You arrive back at wish well\n"
            print "The smell of troll laundry seems to have gotten stronger since last you came...\n"
        global WWhasBeen
        WWhasBeen = 1
#        print WWhasBeen
    elif new_locale == "falcon keep":
        if FKhasBeen == 0:
            print "You arrive at the dastardly falcon keep!\n\n"
            print "Feeroy circles above your head cackling! Annoying bird!!\n"
            print "As you approach the keep you see that it has a large glass door that is too thick to break."
            print "The center of the door has a large keyhole. Inside the door you see a pedastal."
            print "THE PEDASTAL HAS YOUR DIGNITY!! YOU'VE GOT TO GET IT LEEROY!!\n"
            print "Before you know it Feeroy has landed on the ridge of the keep overlooking the door."
            print "He cackles, 'you will never get your dignity leeroy!! HAHAHA!!' He then flys back up into the sky.\n"
        else:
            print "You arrive back at falcon keep\n"
            print "That nasty falcon feeroy is still circling overhead. You hear him laughing...still\n"
        global FKhasBeen
        FKhasBeen = 1
#        print FKhasBeen

    return new_locale_dict[roomNumber]

def goLocale(locationInput, userLocale):
    if locationInput == "treasureland":
        if ThasBeen == 1:
            print "You arrive back in treasureland"
            print "\nThe squirrels are still gathered around the mermaid scale. Occasionally tossing it around the circle.\n"
            return locationInput
        else:
            print ThasBeen
            print "You have yet to discover that location."
            return userLocale
    if locationInput == "braids":
        if BhasBeen == 1:
            print "\nYou arrive back at braids\n"
            print "The trees still appear to be talking and moving as if they are alive."
            print "The golden acorn is still at the top of the same tree\n"
            return locationInput
        else:
            print "You have yet to discover that location."
            return userLocale
    if locationInput == "the red chasm":
        if RChasBeen == 1:
            print "You arrive back at the red chasm"
            print "\nThe troll is still moping in the corner. The bell hasn't moved.\n"
            return locationInput
        else:
            print "You have yet to discover that location."
            return userLocale
    if locationInput == "heaven's peak":
        if HPhasBeen == 1:
            print "You arrive back at heaven's peak\n"
            print "The goat is still on the ridge guarding the hair ties.\n"
            return locationInput
        else:
            print "You have yet to discover that location."
            return userLocale
    if locationInput == "mermaid cove":
        if MChasBeen == 1:
            print "You arrive back at mermaid cove\n"
            print "The mermaid is still here sitting next to that big key.\n"
            return locationInput
        else:
            print "You have yet to discover that location."
            return userLocale
    if locationInput == "wish well":
        if WWhasBeen == 1:
            print "You arrive back at wish well\n"
            print "The smell of troll laundry seems to have gotten stronger since last you came...\n"
            return locationInput
        else:
            print "You have yet to discover that location."
            return userLocale
    if locationInput == "falcon keep":
        if FKhasBeen == 1:
            print "You arrive back at falcon keep\n"
            print "That nasty falcon feeroy is still circling overhead. You hear him laughing...still\n"
            return locationInput
        else:
            print "You have yet to discover that location."
            return userLocale
    if locationInput == "leeroy's tower":
        if LThasBeen == 1:
            return locationInput
        else:
            print "You have yet to discover that location."
            return userLocale


locale_dict = {
    "leeroy's tower": 0,
    "the red chasm": 5,
    "braids": 6,
    "heaven's peak": 2,
    "mermaid cove": 3,
    "wish well": 4,
    "treasureland": 1,
    "falcon keep": 7,
}

direction_dict = {
    "n": 0,
    "s": 1,
    "e": 2,
    "w": 3,
    }

new_locale_dict = {
    0:"leeroy's tower",
    5:"the red chasm",
    6:"braids",
    2:"heaven's peak",
    3:"mermaid cove",
    4:"wish well",
    1:"treasureland",
    7:"falcon keep",
}
