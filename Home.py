#importing library
import streamlit as sl









#tab title and page title
sl.set_page_config(page_title="Home")
title = sl.title("Welcome")

# assigning variables
if "story_stage" not in sl.session_state:
    sl.session_state.story_stage = "-1"
    sl.session_state.story_text = "Welcome to the Enchanted Village, a place where every day is filled with wonder and surprises! Today, you find yourself standing at the edge of the village square. Two paths stretch before you, each offering its own peculiar charm."

#list for the placement of the restart column
stopColumn = [1,1,3]

#function for the ending options
def endResult():

    # creates a container
    with (sl.container(border=True)):
        # setting stage and text
        sl.write(sl.session_state.story_text)
        sl.text("")

        # reset button
        colStop, colStop2, colStop3 = sl.columns(stopColumn)
        with colStop3:
            restartButton = sl.button("Restart", type='primary')

            if restartButton:
                # reseting stage and text
                sl.session_state.story_stage = "-1"
                sl.session_state.story_text = "Welcome to the Enchanted Village, a place where every day is filled with wonder and surprises! Today, you find yourself standing at the edge of the village square. Two paths stretch before you, each offering its own peculiar charm."
                sl.rerun()

#reusable stop button
def stopButton():
    stopButton = sl.button("Stop", type='primary')

    if stopButton:
        # reseting stage and text
        sl.session_state.story_stage = "-1"
        sl.session_state.story_text = "Welcome to the Enchanted Village, a place where every day is filled with wonder and surprises! Today, you find yourself standing at the edge of the village square. Two paths stretch before you, each offering its own peculiar charm."
        sl.rerun()

#Reusable prompt
def stageSetter():
    # setting stage and text
    sl.write(sl.session_state.story_text)
    sl.write("What do you do?")
    sl.text("")


#into slide
if sl.session_state.story_stage == "-1":
    #creates a container
    with sl.container(border=True):

        #stage text
        sl.write(sl.session_state.story_text)

        sl.text("")
        colStop, colStop2, colStop3 = sl.columns([1, 1, 4])
        with colStop3:
            #button to continue
            if sl.button(" Click to Continue"):
                #sets the next stage and text
                sl.session_state.story_stage = "0"
                sl.session_state.story_text = "You see a sign that says, 'Traveler! Adventure awaits you. But first, you must choose: will you take the path of Curiosity or the path of Excitement?'"
                sl.rerun()

#first set
elif sl.session_state.story_stage == "0":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,9,7])
        with col1:
            #option one
            if sl.button("Follow the Path of Curiosity"):
                sl.session_state.story_stage = "1"
                sl.session_state.story_text = "You arrive at the Golden Library, its giant doors creaking open as you approach. Inside, a talking book flutters down from the highest shelf and exclaims, 'Ah, a seeker of knowledge! Will you solve my puzzle or go deeper into the labyrinth of learning?'"
                sl.rerun()

        with col2:
            #option two
            if sl.button("Follow the Path of Excitement"):
                sl.session_state.story_stage = "2"
                sl.session_state.story_text = "You take the Excitement Path down to the carnival. The carnival is filled with lively music and games. As you walk through the carnival, a clown greets you to play a game."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

# ----------- START OF OPTION 1 -------------

#first option
elif sl.session_state.story_stage == "1":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,7,6.6])
        with col1:
            #option one
            if sl.button("Solve the talking book’s puzzle."):
                sl.session_state.story_stage = "1a"
                sl.session_state.story_text = "The book challenges you to a word game: 'What word begins and ends with ‘E,’ but only has one letter?' "
                sl.rerun()

        with col2:
            #option two
            if sl.button("Explore deeper into the library."):
                sl.session_state.story_stage = "1b"
                sl.session_state.story_text = "The library's labyrinth leads you to a towering telescope with constellations glowing in its lens."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 1A
elif sl.session_state.story_stage == "1a":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3.2])
        with col1:
            #option one
            if sl.button("Answer 'envelope.'"):
                sl.session_state.story_stage = "1a1"
                sl.session_state.story_text = "The book giggles with delight and rewards you with a magical quill that writes in glowing ink."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Answer incorrectly."):
                sl.session_state.story_stage = "1a2"
                sl.session_state.story_text = "The book bursts into laughter and sends you to the library’s maze of knowledge."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.69])
        with colStop3:
            stopButton()

#Option 1A1
elif sl.session_state.story_stage == "1a1":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,6,5])
        with col1:
            #option one
            if sl.button("Write a wish with the quill"):
                sl.session_state.story_stage = "1a1a"
                sl.session_state.story_text = "As you write, the quill glows brighter, and your wish begins to manifesl. You’re transported to a garden where your heart's desire lies hidden. A fox offers to guide you to it if you solve its riddle."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Save the quill for later."):
                sl.session_state.story_stage = "1a1b"
                sl.session_state.story_text = "The quill hums as you keep it, glowing faintly. In the shimmering cavern, it begins to write on its own, guiding you to a mysterious map."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.59])
        with colStop3:
            stopButton()

#Option 1A1A
elif sl.session_state.story_stage == "1a1a":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,6,5])
        with col1:
            #option one
            if sl.button("Solve the riddle."):
                sl.session_state.story_stage = "1a1a1"
                sl.session_state.story_text = "The fox leads you to a magical gem that grants your wish, making your dreams a reality."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse the riddle."):
                sl.session_state.story_stage = "1a1a2"
                sl.session_state.story_text = "The garden offers hidden gifts, including herbs that grant wisdom and strength for your journey."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 3.2])
        with colStop3:
            stopButton()

#Option 1A1B
elif sl.session_state.story_stage == "1a1b":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,6,5])
        with col1:
            #option one
            if sl.button("Follow the map."):
                sl.session_state.story_stage = "1a1b1"
                sl.session_state.story_text = "The map leads to a hidden library where you uncover a book holding answers to your deepest questions."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Explore the cavern instead."):
                sl.session_state.story_stage = "1a1b2"
                sl.session_state.story_text = "You stumble upon an artifact that grants knowledge of ancient languages, opening new opportunities."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 3.1])
        with colStop3:
            stopButton()

#Option 1A1A1
elif sl.session_state.story_stage == "1a1a1":
    endResult()

#Option 1A1A2
elif sl.session_state.story_stage == "1a1a2":
    endResult()

#Option 1A1B1
elif sl.session_state.story_stage == "1a1b1":
    endResult()

#Option 1A1B2
elif sl.session_state.story_stage == "1a1b2":
    endResult()

#Option 1A2
elif sl.session_state.story_stage == "1a2":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,6,5])
        with col1:
            #option one
            if sl.button("Search for the maze’s exit."):
                sl.session_state.story_stage = "1a2a"
                sl.session_state.story_text = "You navigate through the maze using the constellations from the book as a guide. Along the way, you encounter a glowing doorway marked with mysterious runes."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Explore the maze further."):
                sl.session_state.story_stage = "1a2b"
                sl.session_state.story_text = "You delve deeper into the maze and discover a hidden chamber glowing with warm, golden light. In the center stands a talking mirror. The mirror offers a choice: gaze into it to see your true self or continue exploring the chamber for other wonders."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.59])
        with colStop3:
            stopButton()

#Option 1A2A
elif sl.session_state.story_stage == "1a2a":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,9,11])
        with col1:
            #option one
            if sl.button("Enter the glowing doorway."):
                sl.session_state.story_stage = "1a2a1"
                sl.session_state.story_text = "The doorway leads to a lush meadow where the maze’s guardian gifts you a star-shaped pendant that grants you safe passage through any future magical challenges."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Ignore the doorway and continue searching."):
                sl.session_state.story_stage = "1a2a2"
                sl.session_state.story_text = "You find the maze’s exit, emerging into a breathtaking land of vibrant skies and endless possibilities, where your next adventure awaits."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 3.3])
        with colStop3:
            stopButton()

#Option 1A2A1
elif sl.session_state.story_stage == "1a2a1":
    endResult()

#Option 1A2A2
elif sl.session_state.story_stage == "1a2a2":
    endResult()

#Option 1A2B
elif sl.session_state.story_stage == "1a2b":
    # creates a container
    with (sl.container(border=True)):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Gaze into the mirror."):
                sl.session_state.story_stage = "1a2b1"
                sl.session_state.story_text = "The mirror reveals a vision of your future, showing you holding a glowing key. The key unlocks a hidden door in the maze, leading to a place filled with magical tools and a map marking your next great adventure."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Continue exploring the chamber."):
                sl.session_state.story_stage = "1a2b2"
                sl.session_state.story_text = "Beyond the mirror, you find a pedestal holding an ancient. You take the portal, which guides you out safely."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 3.1])
        with colStop3:
            stopButton()

#Option 1A2B1
elif sl.session_state.story_stage == "1a2b1":
    endResult()

#Option 1A2B2
elif sl.session_state.story_stage == "1a2b2":
    endResult()

#-----1B-------

#Option 1B
elif sl.session_state.story_stage == "1b":
    with (sl.container(border=True)):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Peer through the telescope."):
                sl.session_state.story_stage = "1b1"
                sl.session_state.story_text = "You peer into the telescope and see dazzling constellations, but one star shines brighter than the resl. It pulses gently, drawing you in. Suddenly, you feel the telescope’s magic pulling you toward a decision."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Ignore the telescope"):
                sl.session_state.story_stage = "1b2"
                sl.session_state.story_text = "The shelves are filled with curious objects: shimmering trinkets, glowing potions, and dusty tomes. One item catches your eye—a small, intricately carved music box with a key beside it."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.8])
        with colStop3:
            stopButton()

#Option 1B1
elif sl.session_state.story_stage == "1b1":
    with (sl.container(border=True)):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Focus on the brightest star."):
                sl.session_state.story_stage = "1b1a"
                sl.session_state.story_text = "The star becomes a guiding light, revealing hidden paths within the library. It leads you to a mysterious glowing chesl."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Look for patterns in the constellations."):
                sl.session_state.story_stage = "1b1b"
                sl.session_state.story_text = "The constellations rearrange into a map of the library. You notice two marked locations on the map."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.8])
        with colStop3:
            stopButton()

#Option 1B1A
elif sl.session_state.story_stage == "1b1a":
    with (sl.container(border=True)):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 3.5, 3.5])
        with col1:
            # option one
            if sl.button("Open the chesl."):
                sl.session_state.story_stage = "1b1a1"
                sl.session_state.story_text = "Inside, you find a magical mirror that shows the safest routes through the library."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Leave the chest untouched."):
                sl.session_state.story_stage = "1b1a2"
                sl.session_state.story_text = "The chest vanishes, leaving behind a glowing amulet that grants you insight into hidden dangers."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 3.1])
        with colStop3:
            stopButton()

#Option 1B1A1
elif sl.session_state.story_stage == "1b1a1":
    endResult()

#Option 1B1A2
elif sl.session_state.story_stage == "1b1a2":
    endResult()

#Option 1B1B
elif sl.session_state.story_stage == "1b1b":
    with (sl.container(border=True)):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1,11.5, 12.5])
        with col1:
            # option one
            if sl.button("Head to the nearest marked location."):
                sl.session_state.story_stage = "1b1b1"
                sl.session_state.story_text = "You discover a hidden alcove filled with tools to aid your journey."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Venture to the farthest marked location."):
                sl.session_state.story_stage = "1b1b2"
                sl.session_state.story_text = "You uncover a room with ancient symbols that offer knowledge about the library’s origins."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.7])
        with colStop3:
            stopButton()

#Option 1B1B1
elif sl.session_state.story_stage == "1b1b1":
    endResult()

#Option 1B1B2
elif sl.session_state.story_stage == "1b1b2":
    endResult()

#option 1B2
elif sl.session_state.story_stage == "1b2":
    with (sl.container(border=True)):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Wind up the music box."):
                sl.session_state.story_stage = "1b2a"
                sl.session_state.story_text = "The music box plays a hauntingly beautiful tune, and a portal shimmers into view."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Open a dusty tome instead."):
                sl.session_state.story_stage = "1b2b"
                sl.session_state.story_text = "The tome reveals a spell that can summon a guide to help you through the library."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.8])
        with colStop3:
            stopButton()

#option 1B2A
elif sl.session_state.story_stage == "1b2a":
    with (sl.container(border=True)):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Step through the portal."):
                sl.session_state.story_stage = "1b2a1"
                sl.session_state.story_text = "You automaticaly get transported out of the library and back to the beginining."
                sl.rerun()

        with col2:
            # option two
            if sl.button(" Ignore the portal and stay."):
                sl.session_state.story_stage = "1b2a2"
                sl.session_state.story_text = "The music box transforms into a helpful companion that offers advice on navigating the library."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.8])
        with colStop3:
            stopButton()

#Option 1b2a1
elif sl.session_state.story_stage == "1b2a1":
    endResult()

#Option 1b2a2
elif sl.session_state.story_stage == "1b2a2":
    endResult()

#option 1B2B
elif sl.session_state.story_stage == "1b2b":
    with (sl.container(border=True)):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 6, 7])
        with col1:
            # option one
            if sl.button("Use the spell to summon a guide."):
                sl.session_state.story_stage = "1b2b1"
                sl.session_state.story_text = "A glowing figure appears, offering to lead you to the library’s exit."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Keep the spell for emergencies."):
                sl.session_state.story_stage = "1b2b2"
                sl.session_state.story_text = "The tome glows faintly, alerting you when dangers are near."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.7])
        with colStop3:
            stopButton()


#Option 1b2b1
elif sl.session_state.story_stage == "1b2b1":
    endResult()

#Option 1b2b2
elif sl.session_state.story_stage == "1b2b2":
    endResult()

#-------End of Choice 1 -----------

#---------Start of Choice 2 ------------

#second option
elif sl.session_state.story_stage == "2":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Accept and Play"):
                sl.session_state.story_stage = "2a"
                sl.session_state.story_text = "Surprisingly, all the stalls are full, except the one with the clown. The clown presents you with a simple ring toss game. However, the bottles seem to move."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse to Play"):
                sl.session_state.story_stage = "2b"
                sl.session_state.story_text = "As you pass the carnival game, you spot a circus. However, the circus seems oddly empty too. The acrobat asks you to come inside for a fun experience."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.7])
        with colStop3:
            stopButton()

#Option 2a
elif sl.session_state.story_stage == "2a":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Aim and Toss"):
                sl.session_state.story_stage = "2a1"
                sl.session_state.story_text = "You successfully win the game by tossing all three rings on the bottles. The clown presents two prizes for you to choose from."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Miss the Bottles"):
                sl.session_state.story_stage = "2a2"
                sl.session_state.story_text = "You hit the table and the clown laughs at you hysterically. However, he still offers you a consolation prize, a glass dragon egg."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.9])
        with colStop3:
            stopButton()

#Option 2a1
elif sl.session_state.story_stage == "2a1":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.5])
        with col1:
            #option one
            if sl.button("Glowing Crystal"):
                sl.session_state.story_stage = "2a1a"
                sl.session_state.story_text = "Though both of the options seem similar, you were attracted to the glowing crystal. Something in the glowing crystal makes you not take your eyes off the crystal."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Crystal Ball"):
                sl.session_state.story_stage = "2a1b"
                sl.session_state.story_text = "Though both of the options seem similar, you were attracted to the crystal ball. Something in the crystal ball makes you not take your eyes off the crystal."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.45])
        with colStop3:
            stopButton()

#Option 2a1a
elif sl.session_state.story_stage == "2a1a":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,3,2.3])
        with col1:
            #option one
            if sl.button("Keep Looking"):
                sl.session_state.story_stage = "2a1a1"
                sl.session_state.story_text = "As you keep looking into the crystal, you notice something. The crystal can create safe paths out of anywhere, a necessity for future adventures."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Look Away"):
                sl.session_state.story_stage = "2a1a2"
                sl.session_state.story_text = "The crystal keeps twitching rapidly. As you look into it, you get informed that the crystal can create safe paths out of anywhere, a necessity for future adventures."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 2a1a1
elif sl.session_state.story_stage == "2a1a1":
    endResult()

#Option 2a1a2
elif sl.session_state.story_stage == "2a1a2":
    endResult()

#Option 2a1b
elif sl.session_state.story_stage == "2a1b":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.7])
        with col1:
            #option one
            if sl.button("Keep Looking"):
                sl.session_state.story_stage = "2a1b1"
                sl.session_state.story_text = "As you keep looking into the crystal ball, you notice something. The crystal can show you the future, inspiring your next move."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Look Away"):
                sl.session_state.story_stage = "2a1b2"
                sl.session_state.story_text = "You look away and secure the crystal ball in your backpack until your next adventure."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.65])
        with colStop3:
            stopButton()

#Option 2a1b1
elif sl.session_state.story_stage == "2a1b1":
    endResult()

#Option 2a1b2
elif sl.session_state.story_stage == "2a1b2":
    endResult()

#Option 2a2
elif sl.session_state.story_stage == "2a2":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.4])
        with col1:
            #option one
            if sl.button("Accept it"):
                sl.session_state.story_stage = "2a2a"
                sl.session_state.story_text = "You accept the prize. The charming egg lures your eyes with its appearance, not letting you look away."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse it"):
                sl.session_state.story_stage = "2a2b"
                sl.session_state.story_text = "The clown insists you take the egg. You take the egg and put it in your pocket. As you are walking, the egg starts to twitch."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.7])
        with colStop3:
            stopButton()

#Option 2a2a
elif sl.session_state.story_stage == "2a2a":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.6])
        with col1:
            #option one
            if sl.button("Keep Looking"):
                sl.session_state.story_stage = "2a2a1"
                sl.session_state.story_text = "Right before your eyes, the egg cracks and a tiny dragon appears. You look back but cannot spot the stall or the clown anywhere. Looks like your egg could be a great companion for future adventures"
                sl.rerun()

        with col2:
            #option two
            if sl.button("Look Away"):
                sl.session_state.story_stage = "2a2a2"
                sl.session_state.story_text = "You secure the egg for future uses and continue to look for more adventures."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 2a2a1
elif sl.session_state.story_stage == "2a2a1":
    endResult()

#Option 2a2a2
elif sl.session_state.story_stage == "2a2a2":
    endResult()

#Option 2a2b
elif sl.session_state.story_stage == "2a2b":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.3])
        with col1:
            #option one
            if sl.button("Inspect it"):
                sl.session_state.story_stage = "2a2b1"
                sl.session_state.story_text = "As you inspect it, you notice that the egg is hatching and a tiny dragon appears. You look back but cannot spot the stall or the clown anywhere. Looks like your egg could be a great companion for future adventures"
                sl.rerun()

        with col2:
            #option two
            if sl.button("Ignore it"):
                sl.session_state.story_stage = "2a2b2"
                sl.session_state.story_text = "Even though the egg starts to twitch even faster, you ignore it. You throw it in your back for future adventures."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 2a2b1
elif sl.session_state.story_stage == "2a2b1":
    endResult()

#Option 2a2b2
elif sl.session_state.story_stage == "2a2b2":
    endResult()

#-----2B------

#Option 2B
elif sl.session_state.story_stage == "2b":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.4])
        with col1:
            #option one
            if sl.button("Enter the Circus"):
                sl.session_state.story_stage = "2b1"
                sl.session_state.story_text = "The circus seems big. It is decorated with colorful lights and balloons. The acrobat presents you with a challenge."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Ignore it"):
                sl.session_state.story_stage = "2b2"
                sl.session_state.story_text = "The acrobat insists you come inside. You are left with no choice but to go inside the circus. It is decorated with colorful lights and balloons. The acrobat presents you with a challenge."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.5])
        with colStop3:
            stopButton()

#Option 2B1
elif sl.session_state.story_stage == "2b1":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.3])
        with col1:
            #option one
            if sl.button("Accept it"):
                sl.session_state.story_stage = "2b1a"
                sl.session_state.story_text = "The acrobat challenges you to walk on the rope balancing over a deep pit of feathers. It seems tough."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse it"):
                sl.session_state.story_stage = "2b1b"
                sl.session_state.story_text = "You refuse the challenge. However, the acrobat gives you a riddle instead. “What has hands, but can’t clap.”"
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.7])
        with colStop3:
            stopButton()

#Option 2b1a
elif sl.session_state.story_stage == "2b1a":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3.1])
        with col1:
            #option one
            if sl.button("Walk on the Rope"):
                sl.session_state.story_stage = "2b1a1"
                sl.session_state.story_text = "The acrobat says he is proud of you and gifts you a bag of rings. He says that they could create a magical portal to anywhere. You thank him and carry on to your future adventures."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Fall Purposefully"):
                sl.session_state.story_stage = "2b1a2"
                sl.session_state.story_text = "The acrobat laughs at you hysterically. However, he still gives you a consolation prize and wishes you luck in your next adventure."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 2b1a1
elif sl.session_state.story_stage == "2b1a1":
    endResult()

#Option 2b1a2
elif sl.session_state.story_stage == "2b1a2":
    endResult()

#Option 2b1b
elif sl.session_state.story_stage == "2b1b":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Answer “Clock”"):
                sl.session_state.story_stage = "2b1b1"
                sl.session_state.story_text = "The acrobat says he is proud of you and grants you a bag of rings, which he says can open portals to anywhere. You throw them in your backpack for future use. "
                sl.rerun()

        with col2:
            #option two
            if sl.button("Answer Incorrectly"):
                sl.session_state.story_stage = "2b1b1"
                sl.session_state.story_text = "The acrobat laughs at you hysterically. However, he still gives you a consolation prize and wishes you luck in your next adventure."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 2b1b1
elif sl.session_state.story_stage == "2b1b1":
    endResult()

#Option 2b1b1
elif sl.session_state.story_stage == "2b1b1":
    endResult()

#Option 2B2
elif sl.session_state.story_stage == "2b2":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.5])
        with col1:
            #option one
            if sl.button("Accept it"):
                sl.session_state.story_stage = "2b2a"
                sl.session_state.story_text = "The acrobat challenges you to walk on the rope balancing over a deep pit of feathers. It seems tough."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse it"):
                sl.session_state.story_stage = "2b2b"
                sl.session_state.story_text = "You refuse the challenge. However, the acrobat gives you a riddle instead. “What has hands, but can’t clap.”"
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.8])
        with colStop3:
            stopButton()

#Option 2b2a
elif sl.session_state.story_stage == "2b2a":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Walk on the Rope"):
                sl.session_state.story_stage = "2b2a1"
                sl.session_state.story_text = "The acrobat says he is proud of you and gifts you a bag of rings. He says that they could create a magical portal to anywhere. You thank him and carry on to your future adventures."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Fall Purposefully"):
                sl.session_state.story_stage = "2b2a2"
                sl.session_state.story_text = "The acrobat laughs at you hysterically. However, he still gives you a consolation prize and wishes you luck in your next adventure."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 2b2a1
elif sl.session_state.story_stage == "2b2a1":
    endResult()

#Option 2b2a2
elif sl.session_state.story_stage == "2b2a2":
    endResult()

#Option 2b2b
elif sl.session_state.story_stage == "2b2b":
    #creates a container
    with (sl.container(border=True)):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Answer “Clock”"):
                sl.session_state.story_stage = "2b2b1"
                sl.session_state.story_text = "The acrobat says he is proud of you and grants you a bag of rings, which he says can open portals to anywhere. You throw them in your backpack for future use. "
                sl.rerun()

        with col2:
            #option two
            if sl.button("Answer Incorrectly"):
                sl.session_state.story_stage = "2b2b2"
                sl.session_state.story_text = "The acrobat laughs at you hysterically. However, he still gives you a consolation prize and wishes you luck in your next adventure."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 2b2b1
elif sl.session_state.story_stage == "2b2b1":
    endResult()

#Option 2b2b2
elif sl.session_state.story_stage == "2b2b2":
    endResult()


col1, col2 = sl.columns([1,3])
with col2:
    #option two
    sl.image("pic.png", width=300)