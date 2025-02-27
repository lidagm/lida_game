def island_story():
    print ("You wake up shipwrecked on a tiny desert island, you look around and see nothing but a single palm tree, and land in the distance. You are releived to see land but quickly realize you need a way to reach it, what do you do?")
    print ("Do you:", "Search the shipwreck", "OR", "Climb the tree for food")
    option1_intro = [
        "Search the shipwreck",
        "Search shipwreck", 
        "Search", 
        "search the shipwreck", 
        "search shipwreck", 
        "search"
        ]
    option2_intro = [
        "Climb the tree for food",
        "Climb tree",
        "Climb the tree",
        "Climb tree for food",
        "climb the tree for food",
        "climb tree", 
        "climb the tree", 
        "climb tree for food"
        ]
    user_input = input()
    def search_scene():
        print ("You look around and find an old map. You inspect the map. The map has a picture of the island you're on, as well as a scribbled out area to the far north. You see a broken off peice of wood from the side of the ship which you decide would work perfectly as a raft.")
        print ("Do you:", "Head North", "OR", "Head elsewhere")
    def coconut_scene():
        print ("You decide to climb the tree and find plently of coconuts, however as you reach to grab them, the coconuts begin to fall onto you. You get knocked off of the tree by coconuts and fall to your death.")
        print ("ENDING: DEATH BY COCONUT")
        island_story()
    if user_input in option1_intro:
        search_scene()
    elif user_input in option2_intro:
        coconut_scene()
    else:
        print("Please choose a viable option.")
        island_story()
    option1_scene1 = [
        "Head North",
        "head north",
        "north",
        "North"
    ]
    option2_scene1 = [
        "Head elsewhere",
        "head elsewhere",
        "elsewhere",
        "Elsewhere"
    ]
    user_input = input()
    def north_scene():
        print ("You use the raft to head North, after days of very slow travel, you finally reach the land. You look around and notice that the land is covered in thick jungle. You see a path leading into a fork, the left looks promising, with clearer land and open patches. The right is crowded with shrubbery but you think that you can make out some sort of structure in the distance.")
        print ("Do you:", "Go left", "OR", "Go right")
    def opposite_scene():
        print ("You head in the opposite direction, you assume that the scribbled out land was hidden for a reason and set off South. After weeks of aimess floating, you reach a luscious tropical island with a tall mountain in the center, you leave your raft to explore the land and notice a river flowing to the right of the mountain.")
        print ("Do you:", "Follow the river", "OR", "Head up the mountain")
    if user_input in option1_scene1:
        north_scene()
    elif user_input in option2_scene1:
       opposite_scene()
    else:
        print ("Please choose a viable option.")
        search_scene()
    option1_scene2 = [
        "Go left",
        "go left",
        "Left",
        "left"
    ]
    option2_scene2 = [
        "Go right",
        "go right",
        "right",
        "Right"
    ]
    user_input = input()
    def leftpath_scene():
        print("You decide to go left. You're greeted by a beautiful opening filled with flowers and animals, the path leads through the meadow back into the forest. You continue. The sounds of the jungle intimidate you, the hisses and purs cause you to quicken your pace. Soon enough, you spot an unusual movement in the trees. A snake drops ontop of you and bites you in the neck, you fall to the ground in pain with the shadow of a human being the last thing you see.")
        print("ENDING: ???")
        island_story()
    def rightpath_scene():
        print("After trekking through the dense jungle, you reach a structure which appears to be a large stone pyramid. The entrance is a dark tunnel, you head in and come across two different doors in each direction.")
        print ("Do you:", "Go left", "OR", "Go right")
    if user_input in option1_scene2:
        leftpath_scene()
    elif user_input in option2_scene2:
        rightpath_scene()
    else:
        print("Please choose a viable option.")
        north_scene()
    option1_scene3 = [
        "Go left",
        "go left",
        "Left",
        "left"
    ]
    option2_scene3 = [
        "Go right",
        "go right",
        "right",
        "Right"
    ]
    user_input = input()
    def leftdoor_scene():
        print("The door opens to an empty stone room with a chest towards the back, you walk in, unsuspecting and the door slams behind you. You attempt to open it again but it has now been locked and you are trapped, you head over to the chest in hopes of something to help you escape but as you open it, something horrifying happens. A murky purple gas is released from the chest, you try to shut it, but it wont close, now the gas has filled the room. You struggle to breathe, then collapse onto the floor, dead. ")
        print("ENDING: POISONED")
        island_story()
    def rightdoor_scene():
        print("Upon entering the right door, you find a long twisting hallway. You decide to walk down the hallway, and you notice the walls become wider until you have foumd yourself in a large cave opening out to the sea. You see a large ship in much better condition than your flimsy raft waiting for you at the bay, you take this as your opportunity to leave and quickly set out for civilization. After days, you finally reach a city skyline which you make out to be San Fransisco...")
        print("ENDING: SHIP ESCAPE")
        island_story()
    if user_input in option1_scene3:
        leftdoor_scene()
    if user_input in option2_scene3:
        rightdoor_scene()
    else:
        print("Please choose a viable option.")
        rightpath_scene()
    option1_scene4 = [
        "Follow the river",
        "follow the river",
        "Follow",
        "follow",
        "Follow river",
        "follow river",
        "River",
        "river"
    ]
    option2_scene4 = [
        "Head up the mountain",
        "head up the mountain",
        "Head up mountain",
        "head up mountain",
        "Mountain",
        "mountain"
    ]
    user_input = input()
    def village_scene():
        print("Along the river you spot an abandoned campsite, in hopes of finding another person, you continue following the river. Eventually, you see the roofs of some wooden houses in the distance, as you get closer you confirm that the roofs you saw were indeed part of a village. You find a local and ask him where you are, after being told that you are on the island of St Vincent, the local offers to rake you to the airport. Before you know it, you've booked a flight off of the island and back home. :)")
        print("ENDING: AIRPORT")
        island_story()
    def volcano_scene():
        print("You head up the mountain in search of a better view of the land, however, the higher you get, the warmer you feel the temperature getting. You ignore this oddity and continue to head towards the top, but you soon realize that you've made a grave mistake. Suddenly, the top of the 'mountain' explodes in smoke and a splurt of lava comes flying towards you. Good luck next time I guess. ")
        print("ENDING: VOLCANO")
        island_story()
    if user_input in option1_scene4:
        village_scene()
    if user_input in option2_scene4:
        volcano_scene()
island_story() 