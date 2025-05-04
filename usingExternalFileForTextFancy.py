import json

# this function reads the phrases from the file and returns them as a dictionary

def readPhrases():
    # open the file called phrases.json
    with open("phrases.json") as file:
        # load the file into a variable
        phrases = json.load(file)
    return phrases

# create a function to read the text file someRandomStoryText.txt and display the contents
def readTextFile():
    # open the file called someRandomStoryText.txt
    with open("someRandomStoryText.txt") as file:
        # load the file into a variable
        text = file.read()
    return text

# create a funtion to read the text and pause after each sentence
def readTextFileWithPauses():
    # open the file called someRandomStoryText.txt
    with open("someRandomStoryText.txt") as file:
        # load the file into a variable
        text = file.read()
    # split the text into sentences
    sentences = text.split(".")
    # loop through the sentences
    for sentence in sentences:
        # print the sentence
        print(sentence)
        print('\npress any key to continue')
        # wait for the user to press enter
        input()

# print out what we have read from the files
phrases=readPhrases()
storyLine=readTextFile()
print(f"the phrases are: {phrases}")

# call the function to read the text file with pauses
readTextFileWithPauses()