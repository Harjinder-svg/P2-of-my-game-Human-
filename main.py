# importing random for the choices inputed by the player
import random

# Intro of the game
def Intro():
    print("Welcome to the war cadit.")
    print(" ")
    print(" \n Where plastic has consumed us to live in barrows while the skies fills with corruption.")
    print(" \n The other cadits has left their posts to scanvage amongest the wasteland for resoucres.")
    print(" \n Your task will be to investigate and record any findings about the enviroment outside to see how much damage has been cause ")
    print(" \n Choose any path you wish to go cadit")
    print()


def Path1():
    path = ""
    while path != "1" and path != "2":  #Inputing validations
        path = input("Choose one of your paths shown? (1 or 2): ")

    return path

def Checkpath(Path1):
    print()
    print("You walk down this path through the radioactive forest with your suit")
    print("You gaze upon the destruction plastic has wrecked across this world")
    print("Pieces of plastic shrouds the trees, trapping their life while seeing the unfortunate creatures mutated or engulfing pieces of trash for survival.")
    print()

    # Randomize the choice made by the player
    correctPath = random.randint(1, 2,)

    if Path1 == str(correctPath):
        print()
        print("At the end of your journey, You realise that the world has to be changed in a greener atomsphere for the creatures and humans who inhabits on earth.")
        print("You approach to a high cliff, gazing upon the rainbow coloured rivers to the trails of trash descending from the skies.")
    else:
        print()
        print("While reaching back to headquarters with your finding, You found a busted robot on your trail.")
        print("Damaged by the corrosive from the acid rains, geting up close, the robot suddenly spoke, saying one sentence over and over again. ")
        print("Humans have brought their own down fall as their creation rises.")





playAgain = "yes"
# This will intiate the functions and decide for the player if they want to play again or not
while playAgain == "yes" or playAgain == "y":
    Intro()
    choice = Path1()
    Checkpath(choice)    #Choice will always be equal to "1" or "2"
    print()
    playAgain = input("Do you want to play again (Continue by typing 'yes' or 'y'): ")