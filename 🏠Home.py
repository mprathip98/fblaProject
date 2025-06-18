#importing library
import streamlit as sl
from fpdf import FPDF
import base64
import unicodedata
from sqlalchemy import text

database = sl.connection("neon", type="sql")

#streamlit run 🏠Home.py


page_bg_img = f"""
<style>
.st-emotion-cache-bm2z3a {{
    background-image: url("https://images.unsplash.com/photo-1675180126549-4f7ebf96f66a?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
}}

.st-emotion-cache-h4xjwg {{
    background-color: rgba(0, 0, 0, 0);
}}

.st-emotion-cache-qcpnpn{{
    background-color: rgba(0, 0, 0, 0.65);
}}

#get-ready-for-your-adventure-in-the-enchanted-village{{
    font-size: 30px;
    text-align: center;
    padding: 20px;
}}

.st-emotion-cache-1xksg61{{
    align-items: center;
    padding_left: 50px;
}}

</style>
"""

sl.markdown(page_bg_img, unsafe_allow_html=True)


#tab title and page title
#sl.set_page_config(page_title="Home")

if "slide_key" not in sl.session_state:
    sl.session_state.slide_key = 0

# assigning variables
if "story_stage" not in sl.session_state:
    sl.session_state.story_stage = "-2"
    sl.session_state.story_text = "Welcome to the Enchanted Village, a place where every day is filled with wonder and surprises! Today, you find yourself standing at the edge of the village square. Two paths stretch before you, each offering its own peculiar charm."
    sl.session_state.name = ""
    sl.session_state.titleName = ""
    sl.session_state.slide_chosen = False
    sl.session_state.new_story_stage = ""
    sl.session_state.new_story_text = ""
    sl.session_state.pdfText = ""
    sl.session_state.storyList = {}
    sl.session_state.background = ["https://images.unsplash.com/photo-1675180126549-4f7ebf96f66a?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "backgroundCarnival.png"]


titleName = sl.title(f"{sl.session_state.titleName}")

#list for the placement of the restart column
stopColumn = [1,1,3]

#for creating a pdf
def create_pdf(story: dict) -> bytes:
    #print(story)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for k,v in story.items():
        clean_line =  unicodedata.normalize("NFKD", f"{k}\n \t You Chose: {v[0]}\n\n\n").encode("ascii", "ignore").decode("ascii")
        pdf.multi_cell(0, 7, txt=clean_line)

    # Save to bytes
    pdf_output = bytes()
    pdf_bytes = pdf.output(dest="S").encode("latin1")
    return pdf_bytes

#function for the ending options
def endResult():
    # creates a container
    with sl.container(border=True):
        # setting stage and text
        sl.write(sl.session_state.story_text)
        sl.text("")

        # reset button
        colStop, colStop2, colStop3 = sl.columns(stopColumn)
        with colStop3:
            restartButton = sl.button("Restart", type='primary')
            sl.session_state.storyList[sl.session_state.story_text] = "Restart"
            if restartButton:
                sl.session_state.storyList.clear()
                # reseting stage and text
                sl.session_state.story_stage = "-2"
                #sl.session_state.story_text = "Welcome to the Enchanted Village, a place where every day is filled with wonder and surprises! Today, you find yourself standing at the edge of the village square. Two paths stretch before you, each offering its own peculiar charm."
                sl.session_state.titleName = ""
                sl.rerun()

        colStops, colStops2, colStops3 = sl.columns([1,1,4.3])
        with colStops3:
            text2 = sl.session_state.storyList
            pdf_data = create_pdf(text2)
            sl.download_button(
                label="📄 Download Your Story",
                data=pdf_data,
                file_name="story.pdf",
                mime="application/pdf"
            )
            sl.text(" ")
    with database.session as session:
        session.execute(
            text("INSERT INTO storydata (name, story) VALUES (:name, :story)"),
            {"name": sl.session_state.name, "story": str(sl.session_state.storyList)}
        )
        session.commit()

def background1():
    page_bg_img = f"""
        <style>
        .st-emotion-cache-bm2z3a {{
            background-image: url("https://i.imgur.com/MO7twhK.jpeg");
            background-size: cover;
        }}
    """
    sl.markdown(page_bg_img, unsafe_allow_html=True)

def background2():
    page_bg_img = f"""
        <style>
        .st-emotion-cache-bm2z3a {{
            background-image: url("https://i.imgur.com/OQ8XxUQ.jpeg");
            background-size: cover;
        }}
    """
    sl.markdown(page_bg_img, unsafe_allow_html=True)

#reusable stop button
def stopButton():
    stopButton = sl.button("Stop", type='primary')
    sl.text(" ")

    if stopButton:
        # reseting stage and text
        sl.session_state.story_stage = "-2"
        sl.session_state.storyList.clear()
        #sl.session_state.story_text = "Welcome to the Enchanted Village, a place where every day is filled with wonder and surprises! Today, you find yourself standing at the edge of the village square. Two paths stretch before you, each offering its own peculiar charm."
        sl.session_state.titleName = ""

        sl.rerun()

if sl.session_state.slide_chosen:
    sl.session_state.story_stage = sl.session_state.new_story_stage
    sl.session_state.story_text = sl.session_state.new_story_text
    sl.session_state.slide_chosen = False
    sl.rerun()

#Reusable prompt
def stageSetter():
    # setting stage and text
    slideOptions = []
    for items in range(0,len(sl.session_state.storyList)):
        #print(items)
        slideOptions.append(f"Slide {items+1}")
    modification = sl.selectbox(
        "Change Slide", 
        slideOptions,
        index=None,
        placeholder="choose a slide to change",
        key=f"slide_selector_{sl.session_state.slide_key}"
    )

    if modification != None:
        currentSlides = []
        currentText = []
        slide = int(modification[-1])-1
        for k, v in sl.session_state.storyList.items():
            currentSlides.append(v[1])
            currentText.append(k)
        print(currentSlides)
        print(currentText)
        print(slide)
        sl.session_state.new_story_stage = currentSlides[slide]
        sl.session_state.new_story_text = currentText[slide]
        sl.session_state.slide_chosen = True
        sl.session_state.slide_key += 1
        sl.rerun()


    sl.write(sl.session_state.story_text)
    sl.write("What do you do?")
    sl.text("")



if sl.session_state.story_stage == "-2":
    with sl.container(border=True):

        sl.title("Get Ready For Your Adventure in The Enchanted Village!")
        sl.text(" ")
        col1, col2, col3 = sl.columns(3)
        with col2:
            nameInput = sl.text_input("Enter Your Name to Start", placeholder="bigManJohn")
        sl.text(" ")
        sl.text(" ")
        sl.session_state.name = nameInput
        
    if nameInput != "":
        sl.session_state.story_text = f"Welcome to the Enchanted Village, {nameInput}, a place where every day is filled with wonder and surprises! Today, you find yourself standing at the edge of the village square. Two paths stretch before you, each offering its own peculiar charm."
        sl.session_state.story_stage = "-1"
        sl.session_state.titleName = f"Welcome, {nameInput}!"
        sl.rerun()


#into slide
if sl.session_state.story_stage == "-1":
    #creates a container
    with sl.container(border=True):
        sl.text("")
        #stage text
        sl.write(sl.session_state.story_text)

        sl.text("")
        colStop, colStop2, colStop3 = sl.columns([1,1,4])
        with colStop3:
            #button to continue
            if sl.button(" Click to Continue"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Click to Continue", "-1"]
                #sets the next stage and text
                sl.session_state.story_stage = "0"
                sl.session_state.story_text = "You see a sign that says, 'Traveler! Adventure awaits you. But first, you must choose: will you take the path of Curiosity or the path of Excitement?'"
                sl.rerun()
        sl.text("")
        colStop1, colStops2, colStops3 = sl.columns([1,1.45,4])
        with colStops3:
            goBackButton = sl.button("Go Back", type='primary')

            if goBackButton:
                sl.session_state.story_stage = "-2"
                sl.session_state.titleName = ""
                sl.rerun()
                
        sl.text("")
   
    

#first set
elif sl.session_state.story_stage == "0":
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,9,7])
        with col1:
            #option one
            if sl.button("Follow the Path of Curiosity"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Follow the Path of Curiosity", "0"]
                sl.session_state.story_stage = "1"
                sl.session_state.story_text = "You arrive at the Golden Library, its giant doors creaking open as you approach. Inside, a talking book flutters down from the highest shelf and exclaims, 'Ah, a seeker of knowledge! Will you solve my puzzle or go deeper into the labyrinth of learning?'"
                sl.rerun()

        with col2:
            #option two
            if sl.button("Follow the Path of Excitement"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Follow the Path of Excitement", "0"]
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
    with sl.container(border=True):
        stageSetter()

        background1()


        #column for the two options
        col, col1, col2 = sl.columns([1,7,6.6])
        with col1:
            #option one
            if sl.button("Solve the talking book’s puzzle."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Solve the talking book’s puzzle.", "1"]
                sl.session_state.story_stage = "1a"
                sl.session_state.story_text = "The book challenges you to a word game: 'What word begins and ends with ‘E,’ but only has one letter?' "
                sl.rerun()

        with col2:
            #option two
            if sl.button("Explore deeper into the library."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Explore deeper into the library.", "1"]
                sl.session_state.story_stage = "1b"
                sl.session_state.story_text = "The library's labyrinth leads you to a towering telescope with constellations glowing in its lens."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.6])
        with colStop3:
            stopButton()

#Option 1A
elif sl.session_state.story_stage == "1a":
    background1()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3.2])
        with col1:
            #option one
            if sl.button("Answer 'envelope.'"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Answer 'envelope.'", "1a"]
                sl.session_state.story_stage = "1a1"
                sl.session_state.story_text = "The book giggles with delight and rewards you with a magical quill that writes in glowing ink."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Answer incorrectly."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Answer incorrectly.", "1a"]
                sl.session_state.story_stage = "1a2"
                sl.session_state.story_text = "The book bursts into laughter and sends you to the library’s maze of knowledge."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.69])
        with colStop3:
            stopButton()

#Option 1A1
elif sl.session_state.story_stage == "1a1":
    background1()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,6,5])
        with col1:
            #option one
            if sl.button("Write a wish with the quill"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Write a wish with the quill", "1a1"]
                sl.session_state.story_stage = "1a1a"
                sl.session_state.story_text = "As you write, the quill glows brighter, and your wish begins to manifest. You’re transported to a garden where your heart's desire lies hidden. A fox offers to guide you to it if you solve its riddle."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Save the quill for later."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Save the quill for later.", "1a1"]
                sl.session_state.story_stage = "1a1b"
                sl.session_state.story_text = "The quill hums as you keep it, glowing faintly. In the shimmering cavern, it begins to write on its own, guiding you to a mysterious map."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.59])
        with colStop3:
            stopButton()

#Option 1A1A
elif sl.session_state.story_stage == "1a1a":
    background1()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,6,5])
        with col1:
            #option one
            if sl.button("Solve the riddle."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Solve the riddle.", "1a1a"]
                sl.session_state.story_stage = "1a1a1"
                sl.session_state.story_text = "The fox leads you to a magical gem that grants your wish, making your dreams a reality."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse the riddle."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Refuse the riddle.", "1a1a"]
                sl.session_state.story_stage = "1a1a2"
                sl.session_state.story_text = "The garden offers hidden gifts, including herbs that grant wisdom and strength for your journey."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 3.2])
        with colStop3:
            stopButton()

#Option 1A1B
elif sl.session_state.story_stage == "1a1b":
    background1()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,6,5])
        with col1:
            #option one
            if sl.button("Follow the map."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Follow the map.", "1a1b"]
                sl.session_state.story_stage = "1a1b1"
                sl.session_state.story_text = "The map leads to a hidden library where you uncover a book holding answers to your deepest questions."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Explore the cavern instead."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Explore the cavern instead.", "1a1b"]
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
    background1()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,6,5])
        with col1:
            #option one
            if sl.button("Search for the maze’s exit."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Search for the maze’s exit.", "1a2"]
                sl.session_state.story_stage = "1a2a"
                sl.session_state.story_text = "You navigate through the maze using the constellations from the book as a guide. Along the way, you encounter a glowing doorway marked with mysterious runes."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Explore the maze further."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Explore the maze further.", "1a2"]
                sl.session_state.story_stage = "1a2b"
                sl.session_state.story_text = "You delve deeper into the maze and discover a hidden chamber glowing with warm, golden light. In the center stands a talking mirror. The mirror offers a choice: gaze into it to see your true self or continue exploring the chamber for other wonders."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.59])
        with colStop3:
            stopButton()

#Option 1A2A
elif sl.session_state.story_stage == "1a2a":
    background1()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,9,11])
        with col1:
            #option one
            if sl.button("Enter the glowing doorway."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Enter the glowing doorway.", "1a2a"]
                sl.session_state.story_stage = "1a2a1"
                sl.session_state.story_text = "The doorway leads to a lush meadow where the maze’s guardian gifts you a star-shaped pendant that grants you safe passage through any future magical challenges."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Ignore the doorway and continue searching."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Ignore the doorway and continue searching.", "1a2a"]
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
    background1()
    # creates a container
    with sl.container(border=True):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Gaze into the mirror."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Gaze into the mirror.", "1a2b"]
                sl.session_state.story_stage = "1a2b1"
                sl.session_state.story_text = "The mirror reveals a vision of your future, showing you holding a glowing key. The key unlocks a hidden door in the maze, leading to a place filled with magical tools and a map marking your next great adventure."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Continue exploring the chamber."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Continue exploring the chamber.", "1a2b"]
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
    background1()
    with sl.container(border=True):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Peer through the telescope."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Peer through the telescope.", "1b"]
                sl.session_state.story_stage = "1b1"
                sl.session_state.story_text = "You peer into the telescope and see dazzling constellations, but one star shines brighter than the rest. It pulses gently, drawing you in. Suddenly, you feel the telescope’s magic pulling you toward a decision."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Ignore the telescope"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Ignore the telescope", "1b"]
                sl.session_state.story_stage = "1b2"
                sl.session_state.story_text = "The shelves are filled with curious objects: shimmering trinkets, glowing potions, and dusty tomes. One item catches your eye—a small, intricately carved music box with a key beside it."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.8])
        with colStop3:
            stopButton()

#Option 1B1
elif sl.session_state.story_stage == "1b1":
    background1()
    with sl.container(border=True):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Focus on the brightest star."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Focus on the brightest star.", "1b1"]
                sl.session_state.story_stage = "1b1a"
                sl.session_state.story_text = "The star becomes a guiding light, revealing hidden paths within the library. It leads you to a mysterious glowing chest."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Look for patterns in the constellations."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Look for patterns in the constellations.", "1b1"]
                sl.session_state.story_stage = "1b1b"
                sl.session_state.story_text = "The constellations rearrange into a map of the library. You notice two marked locations on the map."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.8])
        with colStop3:
            stopButton()

#Option 1B1A
elif sl.session_state.story_stage == "1b1a":
    background1()
    with sl.container(border=True):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 3.5, 3.5])
        with col1:
            # option one
            if sl.button("Open the chest."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Open the chest.", "1b1a"]
                sl.session_state.story_stage = "1b1a1"
                sl.session_state.story_text = "Inside, you find a magical mirror that shows the safest routes through the library."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Leave the chest untouched."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Leave the chest untouched.", "1b1a"]
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
    background1()
    with sl.container(border=True):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1,11.5, 12.5])
        with col1:
            # option one
            if sl.button("Head to the nearest marked location."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Head to the nearest marked location.", "1b1b"]
                sl.session_state.story_stage = "1b1b1"
                sl.session_state.story_text = "You get navigated to the hidden aclove and discover multiple tools to aid your future journeys. The constellations also rearrange to create a safe path out of the library."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Venture to the farthest marked location."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Venture to the farthest marked location.", "1b1b"]
                sl.session_state.story_stage = "1b1b2"
                sl.session_state.story_text = "You uncover a room with ancient symbols that offers knowledge about any questions you have. \n\n Well, that was a quick adventure."
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
    background1()
    with sl.container(border=True):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Wind up the music box."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Wind up the music box.", "1b2"]
                sl.session_state.story_stage = "1b2a"
                sl.session_state.story_text = "The music box plays a hauntingly beautiful tune, and a portal shimmers into view."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Open a dusty tome instead."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Open a dusty tome instead.", "1b2"]
                sl.session_state.story_stage = "1b2b"
                sl.session_state.story_text = "The tome reveals a spell that can summon a guide to help you through the library."
                sl.rerun()

            # setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1, 1, 2.8])
        with colStop3:
            stopButton()

#option 1B2A
elif sl.session_state.story_stage == "1b2a":
    background1()
    with sl.container(border=True):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 4.5, 5])
        with col1:
            # option one
            if sl.button("Step through the portal."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Step through the portal.", "1b2a"]
                sl.session_state.story_stage = "1b2a1"
                sl.session_state.story_text = "You automaticaly get transported out of the library and back to the beginining. \n\n Well, that was a quick adventure."
                sl.rerun()

        with col2:
            # option two
            if sl.button(" Ignore the portal and stay."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Ignore the portal and stay.", "1b2a"]
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
    background1()
    with sl.container(border=True):
        stageSetter()

        # column for the two options
        col, col1, col2 = sl.columns([1, 6, 7])
        with col1:
            # option one
            if sl.button("Use the spell to summon a guide."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Use the spell to summon a guide.", "1b2b"]
                sl.session_state.story_stage = "1b2b1"
                sl.session_state.story_text = "A glowing figure appears, offering to lead you to the library’s exit, safely."
                sl.rerun()

        with col2:
            # option two
            if sl.button("Keep the spell for emergencies."):
                sl.session_state.storyList[sl.session_state.story_text] = ["Keep the spell for emergencies.", "1b2b"]
                sl.session_state.story_stage = "1b2b2"
                sl.session_state.story_text = "The tome glows faintly, alerting you when dangers are near, a great for all of your future adventures."
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

    background2()

    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Accept and Play"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Accept and Play", "2"]
                sl.session_state.story_stage = "2a"
                sl.session_state.story_text = "Surprisingly, all the stalls are full, except the one with the clown. The clown presents you with a simple ring toss game. However, the bottles seem to move."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse to Play"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Refuse to Play", "2"]
                sl.session_state.story_stage = "2b"
                sl.session_state.story_text = "As you pass the carnival game, you spot a circus. However, the circus seems oddly empty too. The acrobat asks you to come inside for a fun experience."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.7])
        with colStop3:
            stopButton()

#Option 2a
elif sl.session_state.story_stage == "2a":
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Aim and Toss"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Aim and Toss", "2a"]
                sl.session_state.story_stage = "2a1"
                sl.session_state.story_text = "You successfully win the game by tossing all three rings on the bottles. The clown presents two prizes for you to choose from."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Miss the Bottles"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Miss the Bottles", "2a"]
                sl.session_state.story_stage = "2a2"
                sl.session_state.story_text = "You hit the table and the clown laughs at you hysterically. However, he still offers you a consolation prize, a glass dragon egg."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.9])
        with colStop3:
            stopButton()

#Option 2a1
elif sl.session_state.story_stage == "2a1":
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.5])
        with col1:
            #option one
            if sl.button("Glowing Crystal"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Glowing Crystal", "2a1"]
                sl.session_state.story_stage = "2a1a"
                sl.session_state.story_text = "Though both of the options seem similar, you were attracted to the glowing crystal. Something in the glowing crystal makes you not take your eyes off the crystal."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Crystal Ball"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Crystal Ball", "2a1"]
                sl.session_state.story_stage = "2a1b"
                sl.session_state.story_text = "Though both of the options seem similar, you were attracted to the crystal ball. Something in the crystal ball makes you not take your eyes off the crystal."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.45])
        with colStop3:
            stopButton()

#Option 2a1a
elif sl.session_state.story_stage == "2a1a":
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,3,2.3])
        with col1:
            #option one
            if sl.button("Keep Looking"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Keep Looking", "2a1a"]
                sl.session_state.story_stage = "2a1a1"
                sl.session_state.story_text = "As you keep looking into the crystal, you notice something. The crystal can create safe paths out of anywhere, a necessity for future adventures."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Look Away"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Look Away", "2a1a"]
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
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.7])
        with col1:
            #option one
            if sl.button("Keep Looking"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Keep Looking", "2a1b"]
                sl.session_state.story_stage = "2a1b1"
                sl.session_state.story_text = "As you keep looking into the crystal ball, you notice something. The crystal can show you the future, inspiring your next move."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Look Away"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Look Away", "2a1b"]
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
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.4])
        with col1:
            #option one
            if sl.button("Accept it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Accept it", "2a2"]
                sl.session_state.story_stage = "2a2a"
                sl.session_state.story_text = "You accept the prize. The charming egg lures your eyes with its appearance, not letting you look away."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Refuse it", "2a2"]
                sl.session_state.story_stage = "2a2b"
                sl.session_state.story_text = "The clown insists you take the egg. You take the egg and put it in your pocket. As you are walking, the egg starts to twitch."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.7])
        with colStop3:
            stopButton()

#Option 2a2a
elif sl.session_state.story_stage == "2a2a":
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.6])
        with col1:
            #option one
            if sl.button("Keep Looking"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Keep Looking", "2a2a"]
                sl.session_state.story_stage = "2a2a1"
                sl.session_state.story_text = "Right before your eyes, the egg cracks and a tiny dragon appears. You look back but cannot spot the stall or the clown anywhere. Looks like your egg could be a great companion for future adventures"
                sl.rerun()

        with col2:
            #option two
            if sl.button("Look Away"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Look Away", "2a2a"]
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
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.3])
        with col1:
            #option one
            if sl.button("Inspect it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Inspect it", "2a2b"]
                sl.session_state.story_stage = "2a2b1"
                sl.session_state.story_text = "As you inspect it, you notice that the egg is hatching and a tiny dragon appears. You look back but cannot spot the stall or the clown anywhere. Looks like your egg could be a great companion for future adventures"
                sl.rerun()

        with col2:
            #option two
            if sl.button("Ignore it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Ignore it", "2a2b"]
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
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.4])
        with col1:
            #option one
            if sl.button("Enter the Circus"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Enter the Circus", "2b"]
                sl.session_state.story_stage = "2b1"
                sl.session_state.story_text = "The circus seems big. It is decorated with colorful lights and balloons. The acrobat presents you with a challenge."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Ignore it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Ignore it", "2b"]
                sl.session_state.story_stage = "2b2"
                sl.session_state.story_text = "The acrobat insists you come inside. You are left with no choice but to go inside the circus. It is decorated with colorful lights and balloons. The acrobat presents you with a challenge."
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.5])
        with colStop3:
            stopButton()

#Option 2B1
elif sl.session_state.story_stage == "2b1":
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.3])
        with col1:
            #option one
            if sl.button("Accept it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Accept it", "2b1"]
                sl.session_state.story_stage = "2b1a"
                sl.session_state.story_text = "The acrobat challenges you to walk on the rope balancing over a deep pit of feathers. It seems tough."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Refuse it", "2b1"]
                sl.session_state.story_stage = "2b1b"
                sl.session_state.story_text = "You refuse the challenge. However, the acrobat gives you a riddle instead. “What has hands, but can’t clap.”"
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.7])
        with colStop3:
            stopButton()

#Option 2b1a
elif sl.session_state.story_stage == "2b1a":
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3.1])
        with col1:
            #option one
            if sl.button("Walk on the Rope"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Walk on the Rope", "2b1a"]
                sl.session_state.story_stage = "2b1a1"
                sl.session_state.story_text = "The acrobat says he is proud of you and gifts you a bag of rings. He says that they could create a magical portal to anywhere. You thank him and carry on to your future adventures."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Fall Purposefully"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Fall Purposefully", "2b1a"]
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
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Answer “Clock”"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Answer “Clock”", "2b1b"]
                sl.session_state.story_stage = "2b1b1"
                sl.session_state.story_text = "The acrobat says he is proud of you and grants you a bag of rings, which he says can open portals to anywhere. You throw them in your backpack for future use. "
                sl.rerun()

        with col2:
            #option two
            if sl.button("Answer Incorrectly"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Answer Incorrectly", "2b1b"]
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
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,2.5])
        with col1:
            #option one
            if sl.button("Accept it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Accept it", "2b2"]
                sl.session_state.story_stage = "2b2a"
                sl.session_state.story_text = "The acrobat challenges you to walk on the rope balancing over a deep pit of feathers. It seems tough."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Refuse it"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Refuse it", "2b2"]
                sl.session_state.story_stage = "2b2b"
                sl.session_state.story_text = "You refuse the challenge. However, the acrobat gives you a riddle instead. “What has hands, but can’t clap.”"
                sl.rerun()

        #setting for the stop button
        colStop, colStop2, colStop3 = sl.columns([1,1, 2.8])
        with colStop3:
            stopButton()

#Option 2b2a
elif sl.session_state.story_stage == "2b2a":
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Walk on the Rope"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Walk on the Rope", "2b2a"]
                sl.session_state.story_stage = "2b2a1"
                sl.session_state.story_text = "The acrobat says he is proud of you and gifts you a bag of rings. He says that they could create a magical portal to anywhere. You thank him and carry on to your future adventures."
                sl.rerun()

        with col2:
            #option two
            if sl.button("Fall Purposefully"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Fall Purposefully", "2b2a"]
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
    background2()
    #creates a container
    with sl.container(border=True):
        stageSetter()

        #column for the two options
        col, col1, col2 = sl.columns([1,4,3])
        with col1:
            #option one
            if sl.button("Answer “Clock”"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Answer “Clock”", "2b2b"]
                sl.session_state.story_stage = "2b2b1"
                sl.session_state.story_text = "The acrobat says he is proud of you and grants you a bag of rings, which he says can open portals to anywhere. You throw them in your backpack for future use. "
                sl.rerun()

        with col2:
            #option two
            if sl.button("Answer Incorrectly"):
                sl.session_state.storyList[sl.session_state.story_text] = ["Answer Incorrectly", "2b2b"]
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
