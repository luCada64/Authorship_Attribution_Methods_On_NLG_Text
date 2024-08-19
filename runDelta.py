# The goal of this code is to run the data algorithm

# Modules

# Genral modules
import os
import re

# To Run Detal
from faststylometry import Corpus
from faststylometry.burrows_delta import calculate_burrows_delta
from faststylometry.en import tokenise_remove_pronouns_en
from faststylometry.burrows_delta import calculate_burrows_delta

# For Visulisation
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


hu_corpus_path = "hu-Corpus/hu-TheFederalistPapers"
ai_corpus_path = "ai-Corpus/ai-FederalistPaper"
outputDataPath = "outputData/TheFederalistPapers/"


# Create a function to takes a camelCase string and seperate it by " "
def camelCaseToNormal(string):
    
    outputString = ""
    
    for letter in string:
        
        # Check if there is a capital letter, if so add a space
        if re.search("[A-Z]", letter): outputString = outputString + " "
            
        # add the letter to the output
        outputString = outputString + letter


    return outputString


# Load the text into corpus:

# Human corpus
hu_corpus = Corpus()

for root, _, files in os.walk(hu_corpus_path):
    for filename in files:
        if filename.endswith(".txt") and (filename.startswith("hu") or filename.startswith("ai")):
            
            with open(os.path.join(root, filename), "r", encoding="utf-8") as f:
                text = f.read()
                
            _, author, title, year= re.split("---", re.sub(r'\.txt', '', filename))

            # Remove the spaces
            title = camelCaseToNormal(title)
            author = camelCaseToNormal(author)
        

            hu_corpus.add_book(author, title, text)

# AI Corpus
ai_corpus = Corpus()

for root, _, files in os.walk(hu_corpus_path):
    for filename in files:
        if filename.endswith(".txt") and (filename.startswith("hu") or filename.startswith("ai")):
            
            with open(os.path.join(root, filename), "r", encoding="utf-8") as f:
                text = f.read()
                
            _, author, title, year= re.split("---", re.sub(r'\.txt', '', filename))

            # Remove the spaces
            title = camelCaseToNormal(title)
            author = camelCaseToNormal(author)
            

            ai_corpus.add_book(author, "AI" + title, text)









# Now that we got our data we can cacluclate burrows delta and visulise it

# Tokenisation is nesseary
hu_corpus.tokenise(tokenise_remove_pronouns_en)
ai_corpus.tokenise(tokenise_remove_pronouns_en)


# We used the AI, traing data as our test data. 
probatlities = calculate_burrows_delta(hu_corpus, ai_corpus)

print(probatlities)

# We can save the data as csv so that it can be view later
probatlities.to_csv(outputDataPath+"spreadsheet.csv")

# Unfortuntly this data is way to dens to esaly desplay. 
# To avoid this were going to condence the data.
# Instead of showing each indivdual text were going to use who the AI was impersentaing 

# So the way were going to do this is a bit silly, because the data is in altthecical order we will use a loop

humanReadableProbablity = probatlities

i = 0
previousAuthor = ""

for authorAndTitle in probatlities.head():
    
    author = ""
    # Get the Author
    for letter in authorAndTitle:
        if letter == "-": break

        author = author + letter
    
    author = author[1:-1]
    
    # Check if the author is the same the previous one
    # We can add 
    if previousAuthor == "": 
        previousAuthor = author
    
    
    if author == previousAuthor:
        i = i + 1
    else:
        print(previousAuthor+": " + str(i))
        i = 0
        
        previousAuthor = author

print(previousAuthor+": " + str(i))




print(humanReadableProbablity)


# Visualise

# Were going to use seaborn as our visulsation data

# sns.heatmap(probatlities, cmap="YlGnBu", annot=True, fmt="0.0f")
# plt.savefig(outputDataPath+"AllData.png", dpi="700")