# The goal of this code is to run the delta algorthim, comparing a human written corpus to an ai impersonation of said corpus

#Section 1: Modules

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

# Section 2: Paramater
hu_corpus_path = "hu-Corpus/hu-TheFederalistPapers"
ai_corpus_path = "ai-Corpus/ai-FederalistPaper"
outputDataPath = "outputData/TheFederalistPapers/"
showHeatmap = False #True # Make True if you would like a matplotlib window appear.


# Section 3: Helped functions


# Create a function to takes a camelCase string and seperate it by " "
def camelCaseToNormal(string):
    
    outputString = ""
    
    for letter in string:
        
        # Check if there is a capital letter, if so add a space
        if re.search("[A-Z]", letter): outputString = outputString + " "
            
        # add the letter to the output
        outputString = outputString + letter


    return outputString

# This functions extracts the author from the title of a file
def getAuthorFromTitle(authorAndTitle):
    
    author = ""
    # Get the Author
    for letter in authorAndTitle:
        if letter == "-": break

        author = author + letter
    
    return author[1:-1]
    


#Section 4: Add the corpus to faststylometry's corpus

# First add the  Human corpus
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

# Secondly add the AI corpus to it own file
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


# Section 5: Calculate Delta


# Now that we got our data we can cacluclate burrows delta.

# Tokenisation is nesseary
hu_corpus.tokenise(tokenise_remove_pronouns_en)
ai_corpus.tokenise(tokenise_remove_pronouns_en)


# We used the AI, traing data as our test data. 
burrows_delta_score = calculate_burrows_delta(hu_corpus, ai_corpus)


# Section 6: Calculate the dela mean values
# Unfortuntly this data is way to dens to esaly desplay. 
# To avoid this were going to condence the data.
# Instead of showing each indivdual text were going to use who the AI was impersentaing 


authors = [] # create a list of authors 
previousAuthor = "" # set a temp value for the previous author


# Get a list of every authors
for authorAndTitle in burrows_delta_score.head():
    
    # Extract just the author name
    author = getAuthorFromTitle(authorAndTitle)
    
    # Check if this is the first round
    if previousAuthor == "": 

        # if so set, the current author as previous author
        previousAuthor = author
        
        # add the previous author to the list of authors
        authors.append(previousAuthor)
        
    # When a new author apears, add it to the list
    if author != previousAuthor:
        authors.append(author)
        # update the previous author
        previousAuthor = author
        
    
# First were going to transpose the data frame, to make it more readble
trans_probablities = burrows_delta_score.transpose()

# Add the tilse as a new coloumn
trans_probablities.insert(0, "Title", trans_probablities.index)
trans_probablities.reset_index()


# Now lets extract the names, and give it a seperat coloum
names = trans_probablities["Title"].apply(lambda title: getAuthorFromTitle(title))
trans_probablities.insert(1, "Author", names)

# Create an empty Dataframe, to store the csv values
avg_burrows_delta_score = pd.DataFrame(index=authors, columns=authors, dtype="float64")




# Now we can avreage out the probalities where the author is the same.
for author in authors:
    author_data = trans_probablities[trans_probablities["Author"] == author]
    
    # Now for each author we must calculat the mean for every author
    for j_author in authors:
        # Add them to the avg burrows delta score
        avg_burrows_delta_score[author][j_author] = author_data[" " + j_author].mean()
        

    
    
# Section 6: Visulise the data.
 


# Visulise and save the data

# Save the values to csv
avg_burrows_delta_score.to_csv(outputDataPath+"avr_prob.csv")
burrows_delta_score.to_csv(outputDataPath+"spreadsheet.csv")

pd.set_option("display.max_columns", None)

# Save the pandas . descirbe values
with open(outputDataPath+"avg_burrows_delta_score.txt", "w") as savefile: 
    savefile.write(str(avg_burrows_delta_score.describe() ))
with open(outputDataPath+"burrows_delta_score.txt", "w") as savefile:
    savefile.write(str(burrows_delta_score.describe(include= 'all') ))




# Were going to use seaborn as our visulsation data as a heatmap.
plot = sns.heatmap(avg_burrows_delta_score, annot=True, square=True, cmap="YlGnBu" , fmt=".5f" ) 

# Add lables to the plot.
plot.set_title("Burros Delta Similarity Score (lower = more similar)", pad=20)
plot.set_xlabel("Actual Human Author", labelpad=5)
plot.set_ylabel("Delta Score, for impersonated author",labelpad=10)


# Save the figers
if showHeatmap: plt.show()
plt.savefig(outputDataPath+"burrows_mean_probaltities.png", format="png")
