# The goal of this code is to run the data algorithm

# Packages
import os
import re

from faststylometry import Corpus
from faststylometry.burrows_delta import calculate_burrows_delta
from faststylometry.util import load_corpus_from_folder
from faststylometry.en import tokenise_remove_pronouns_en
from faststylometry.burrows_delta import calculate_burrows_delta


hu_corpus_path = "hu-Corpus/hu-TheFederalistPapers"
ai_corpus_path = "ai-Corpus/ai-FederalistPaper"


# Reads in the authors
data = [
    dict(author="Fred", title="Fred's wonderfull life", text="Fred had a good life"),
    dict(author="ai", title="Fred's wonderfull life", text="Computer made Fred's life better"),
    dict(author="Steve", title="Steve: the dud", text="Steve knows Fred was really a dud") 
]


# Load the text into corpus:

# Human corpus
hu_corpus = Corpus()

for root, _, files in os.walk(hu_corpus_path):
    for filename in files:
        if filename.endswith(".txt") and (filename.startswith("hu") or filename.startswith("ai")):
            
            with open(os.path.join(root, filename), "r", encoding="utf-8") as f:
                text = f.read()
                
            _, author, title, year= re.split("---", re.sub(r'\.txt', '', filename))

            hu_corpus.add_book(author, title, text)

# AI Corpus
ai_corpus = Corpus()

for root, _, files in os.walk(hu_corpus_path):
    for filename in files:
        if filename.endswith(".txt") and (filename.startswith("hu") or filename.startswith("ai")):
            
            with open(os.path.join(root, filename), "r", encoding="utf-8") as f:
                text = f.read()
                
            _, author, title, year= re.split("---", re.sub(r'\.txt', '', filename))

            hu_corpus.add_book(author, title, text)




# # Load the human data form the the folder
# hu_corpus = load_corpus_from_folder("")
# ai_corpus = load_corpus_from_folder("ai-Corpus/ai-FederalistPaper")

# print(hu_corpus.books)


# hu_corpus.tokenise(tokenise_remove_pronouns_en)
# ai_corpus.tokenise(tokenise_remove_pronouns_en)



# probatlities = calculate_burrows_delta(hu_corpus, ai_corpus)

# print(probatlities)




# Visualise