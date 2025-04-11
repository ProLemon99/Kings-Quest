import json

# this function reads the phrases from the file
# and returns them as a dictionary

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

# print out what we have read from the files
phrases=readPhrases()
storyLine=readTextFile()
print(f"the phrases are: {phrases}")
print(f"the story is: {storyLine}")