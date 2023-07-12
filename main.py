import pyautogui
import time
import pyperclip

# New method to do quizzes
# Around a coin every second and a half
# Is faster than old method as instead of looping through and checking every pixel on screen
# It just gets the question text and compares it to the values

# Open Inspect Element for the values to be correct
blueX, blueY = 199, 631
redX, redY = 536, 631
yellowX, yellowY = 196, 786
greenX, greenY = 543, 781
questionX, questionY = 381, 374
continueX, continueY = 380, 901

answerArray = [
    ['What are the advantages of LANs?', 'RED'],
    ['Which band frequencies are used by Wi-Fi?', 'YELLOW'],
    ['What is the purpose of passwords in securing a network?', 'RED'],
    ['What is a LAN?', 'RED'],
    ['What is a PAN?', 'YELLOW'],
    ['What type of cable carries data via light signals, providing faster transmission and no interference?', 'RED'],
    ['What is the main disadvantage of LANs?', 'YELLOW'],
    ['What are the advantages of wireless networks?', 'BLUE'],
    ['What are the disadvantages of wireless networks?', 'RED'],
    ['Which topology connects all devices to a hub or switch?', 'GREEN'],
    ['What type of network covers a very short range?', 'BLUE'],
    ['What type of network covers a large geographical area?', 'YELLOW'],
    ['What type of cable carries electrical signals?', 'BLUE'],
    ['Which network topology has a single cable connecting all nodes?', 'BLUE'],
    ['What is the main disadvantage of wireless networks?', 'YELLOW'],
    ['Which type of cable is more expensive than Ethernet cables?', 'RED'],
    ['Which data transfer medium uses radio waves?', 'YELLOW'],
    ['Which topology is a fully connected network?', 'YELLOW'],
    ['What are the two main data transfer media used in networks?', 'BLUE']
]

CONTINUE_DELAY = 1 # How long the code waits to press 'Next Question'!
START_DELAY = 5 # How long the program waits before running!

def continueToNextQuestion():

    time.sleep(CONTINUE_DELAY)

    # Move and click
    pyautogui.moveTo(continueX, continueY)
    pyautogui.leftClick()

def initiateAnswer(answerIndex):
    
    # Find the array again
    currentAnswerArray = answerArray[answerIndex]
    for x in range(len(currentAnswerArray)):
        if x != 0:
            
            # Check card color
            cardColor = currentAnswerArray[x]

            # Press correct card
            if cardColor == 'RED':
                pyautogui.moveTo(redX, redY)
            elif cardColor == 'YELLOW':
                pyautogui.moveTo(yellowX, yellowY)
            elif cardColor == 'BLUE':
                pyautogui.moveTo(blueX, blueY)
            elif cardColor == 'GREEN':
                pyautogui.moveTo(greenX, greenY)
            
            # Left click the card
            pyautogui.leftClick()

        else:
            # Ignore the index 0
            pass

def findMatchingAnswerToStr():

    # Reading the question
    answerStr = pyperclip.paste()
    answerIndex = 0

    # Checking if arrays children matches with question
    for x in range(len(answerArray)):
        if answerArray[x][0] == answerStr:
            answerIndex = x
    
    return answerIndex

def copyQuestionStr():

    # Move to question 
    pyautogui.moveTo(questionX, questionY)
    for x in range(3):

        # Select the question
        pyautogui.leftClick()
    
    # Copy the question into clipboard
    pyautogui.hotkey('ctrl', 'c')

time.sleep(START_DELAY)
while True:
    
    # Loading
    time.sleep(.75)

    # Find question
    copyQuestionStr()

    # Find question index and answer
    Index = findMatchingAnswerToStr()
    initiateAnswer(Index)

    # Continue
    continueToNextQuestion()
