# CMPT 120 Yet Another Image Processer
# Author(s): Ronney Lok, Kevin Hau
# Date: Dec 7th, 2020
# Description: An image processor that has a user interface 
# the user interface displays a variety of functions that the user can input
# to perform their desired output/perform manipulations to the image

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.display.init()
pygame.font.init()



# list of system options
system = [
            "Q: Quit", "O: Open Image", "S: Save Current Image", "R: Reload Original Image"
         ]

# list of basic operation options
basic = [
          "1: Invert","2: Flip Horizontal", "3: Flip Vertical", "4: Switch to Intermeidate Functions",
          "5: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                  "1: Remove Red Channel", "2: Remove Green Channel", "3: Remove Blue Channel", "4: Convert to Grayscale", "5: Apply Sepia Filter", "6: Decrease Brightness", "7: Increase Brightness", "8: Switch to Basic Functions",
                  "9: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [
                "1: Rotate Left", "2: Rotate Right", "3: Pixelate", "4: Binarize","5: Switch to Basic Functions",
                "6: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-5)...")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-9)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        elif userInput == "O":
            tkinter.Tk().withdraw()
            state["lastOpenFilename"]= tkinter.filedialog.askopenfilename()
            img = cmpt120imageProj.getImage(state["lastOpenFilename"])

        elif userInput == "S":
            tkinter.Tk().withdraw()
            state["lastSaveFilename"] = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProj.saveImage(img, state["lastSaveFilename"])
        elif userInput =="R":
            img = cmpt120imageProj.getImage(state["lastOpenFilename"])
        # ***add the rest to handle other system functionalities***

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        
        #create a black image with the lengths and widths of the original img
        newImg = cmpt120imageProj.createBlackImage(len(img), len(img[0]))
        if state["mode"] == "basic":
          if userInput == "1":
            img = cmpt120imageManip.invert(img, newImg)
          elif userInput == "2":
            img = cmpt120imageManip.flipHorizontal(img, newImg)
          elif userInput == "3":
            img = cmpt120imageManip.flipVertical(img, newImg)
          elif userInput == "4":
            state["mode"] = "intermediate"
          elif userInput == "5":
            state["mode"] = "advanced"
    
        elif state["mode"] == "intermediate":
          if userInput == "1":
            img = cmpt120imageManip.remove_red(img, newImg)
          elif userInput == "2":
            img = cmpt120imageManip.remove_green(img, newImg)
          elif userInput == "3":
            img = cmpt120imageManip.remove_blue(img, newImg)
          elif userInput == "4":
            img = cmpt120imageManip.gray_scale(img)
          elif userInput == "5":
            img = cmpt120imageManip.sepia_filter(img, newImg)
          elif userInput == "6":
            img = cmpt120imageManip.decrease_brightness(img, newImg)
          elif userInput == "7":
            img = cmpt120imageManip.increase_brightness(img, newImg)
          elif userInput == "8":
            state["mode"] = "basic"
          elif userInput == "9":
            state["mode"] = "advanced"

        elif state["mode"] == "advanced":
          if userInput == "1":
            img = cmpt120imageManip.rotate_left(img, newImg)
          elif userInput == "2":
            img = cmpt120imageManip.rotate_right(img, newImg)
          elif userInput == "3":
            img = cmpt120imageManip.pixelate(img, newImg)
          elif userInput == "4":
            img = cmpt120imageManip.binarize(img, newImg)
          elif userInput == "5":
            state["mode"] = "basic"
          elif userInput == "6":
            state["mode"] = "intermediate"
        else: # unrecognized user input
                print("Log: Unrecognized user input: " + userInput)
    
    cmpt120imageProj.showInterface(img, "Image", generateMenu(state))
    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) 
# create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) 
# note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")