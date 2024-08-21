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

def getAuthorFromTitle(authorAndTitle):
    
    author = ""
    # Get the Author
    for letter in authorAndTitle:
        if letter == "-": break

        author = author + letter
    
    return author[1:-1]
    



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


# We can save the data as csv so that it can be view later
probatlities.to_csv(outputDataPath+"spreadsheet.csv")

# Unfortuntly this data is way to dens to esaly desplay. 
# To avoid this were going to condence the data.
# Instead of showing each indivdual text were going to use who the AI was impersentaing 


authors = []
previousAuthor = ""


# We need to get every author and calculate a tally
for authorAndTitle in probatlities.head():
    
    author = getAuthorFromTitle(authorAndTitle)
    
    # Check if the author is the same the previous one
    # We can add 
    if previousAuthor == "": 
        previousAuthor = author
        authors.append(previousAuthor)
        
    if author != previousAuthor:
        authors.append(author)
        previousAuthor = author
        
    
# First were going to transpose the data frame
trans_probablities = probatlities.transpose()



# print(trans_probablities)
trans_probablities.insert(0, "Title", trans_probablities.index)
trans_probablities.reset_index()


# Now lets extract the names, and give it a seperat coloum
names = trans_probablities["Title"].apply(lambda title: getAuthorFromTitle(title))
trans_probablities.insert(1, "Author", names)



avr_prob = pd.DataFrame(index=authors, columns=authors, dtype="float64")




# Now we can avreage out the probalities where the author is the same.
for author in authors:
    author_data = trans_probablities[trans_probablities["Author"] == author]
    
    # Now for each author we must calculat the mean for every author
    for j_author in authors:
        avr_prob[author][j_author] = author_data[" " + j_author].mean()
        
    # print(author_data[" Alexander Hamilton"].mean())

avr_prob.to_csv(outputDataPath+"avr_prob.csv")



# Visualise

# Were going to use seaborn as our visulsation data


plot = sns.heatmap(avr_prob, annot=avr_prob, cmap="YlGnBu" ) 

plot.set_title("Burros Delta Similarity Score (lower = more similar)", pad=20)
plot.set_xlabel("Actual Human Author", labelpad=5)
plot.set_ylabel("Delta Score, for impersonated author",labelpad=10)



# Save the figers
plt.savefig(outputDataPath+"burrows_mean_probaltities_svg", format="svg" )
