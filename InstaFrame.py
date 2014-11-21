#!/usr/bin/env python

# Author : Jonathan Lurie
# Date : 20th of November 2014
# Licence : GPL


# used for reading args
import sys

# used for checking file existance
import os

# for taking image files
import glob

#from TileMerger import *
from PIL import Image


# return the argument value
def findArgValue(argName, mandatory=True):
    argValue = None

    # checking if help was asked or if no arg
    if(len(sys.argv)==1 or "-help" in sys.argv[1]):
        printInfo()
        exit()

    try:
        argNameIndex = sys.argv.index(argName)
        argValue = sys.argv[argNameIndex + 1]

    except ValueError, e:
        if(mandatory):
            print("ERROR: " + str(e))
            printInfo()
            exit()

    except IndexError, e:

        #print(e)
        print("ERROR: a value for the argument " + str(argName) + " was not found.")
        printInfo()
        exit()

    return argValue



def printInfo():
    print("\nInstaFrame makes your pictures square-shaped by adding margin, not by croping.")
    print("\nInstaFrame needs an input folder, containing jpg and/or png images.")
    print("\t-input <folder>\t(mandatory)")
    print("\t-color <hexadecimal color>\t(optional, default: FFFFFF)")
    print("\t-size <size in pixel>\t(optional, default: largest from width or height of each file)")
    print("An \"InstaFramed\" subdirectory will be created, containing outputs.\n")




# open the input, create a white file, paste at the right position
# and save the image
def frameAndSave(inputFile, outputFile, BackgroundColor, size=-1):

    # open image
    inputData = Image.open(inputFile)
    #print(inputData.format, inputData.size, inputData.mode)

    # creating the white square output
    outputData = Image.new(inputData.mode, (max(inputData.size), max(inputData.size)) , BackgroundColor)

    isLandscape = None
    xOriginWithinOutput = 0
    yOriginWithinOutput = 0

    # which side is bigger?
    if(inputData.size[0] >= inputData.size[1]):
        # width is bigger
        biggestSide = inputData.size[0]
        smallestSide = inputData.size[1]
        yOriginWithinOutput = (biggestSide - smallestSide)/2
    else:
        # height is bigger
        biggestSide = inputData.size[1]
        smallestSide = inputData.size[0]
        xOriginWithinOutput = (biggestSide - smallestSide)/2


    # pasting cotent to output
    outputData.paste(inputData, (xOriginWithinOutput, yOriginWithinOutput))
    
    # Resizing if needed
    if(size != -1):
	    outputData = outputData.resize((size, size), Image.ANTIALIAS)

    # Save file
    outputData.save(outputFile, "JPEG", quality=90)





if __name__ == '__main__':
    print("________________________________________________________________________________")
    print("                                InstaFrame")


    # fetching input folder
    inputFolder=findArgValue("-input")

    # fetching the color (optional)
    color = findArgValue("-color", False) or "FFF"
    color = "#" + str(color)

    # Fetching the output size (optional)
    try:
        size = max(int(findArgValue("-size", False)), -1)
    except:
        size = -1

    # existance of it
    if(not os.path.exists(inputFolder)):
        print("ERROR: The input folder must exist.")
        exit()

    # Adding the file separator, in cae it was forgotten
    inputFolder = inputFolder + os.sep

    # making a list of all files from this folder
    imageTypes = ('*.jpg', '*.JPG', '*.jpeg', '*.JPEG', '*.png', '*.PNG', '*.tif', '*.TIF', '*.tiff', '*.TIFF', '*.bmp', '*.BMP')
    imageList = []
    for files in imageTypes:
        imageList.extend(glob.glob(inputFolder + files))

    # check if some files where found
    if(not imageList):
        print("No image found. Bye.\n")
        exit()

    # creating the subdir InstaFramed
    subdir = inputFolder + "/InstaFramed/"
    if(not os.path.exists(subdir)):
        os.makedirs(subdir)

    # displaying the list of found files
    # and process them
    print("Processing files:")
    for img in imageList:
        imageBasename = os.path.basename(img)
        frameImageFile = subdir + imageBasename
        print("\t" + imageBasename + "\t..."),

        frameAndSave(img, frameImageFile, color, size)

        print("\tDONE")


    print('\nINFO: all the InstaFramed file are in the "InstaFramed" subdirectory:')
    print(subdir + "\n")
