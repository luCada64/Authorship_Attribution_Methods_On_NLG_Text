# Section 1: Packages and files
import pandas as pd
from openai import OpenAI

# To run this code you must create a .py file with a global varabile named "OPENAI_API_KEY"
# This variable must contain you're OpenAI API ley
# documentation: https://platform.openai.com/docs/introduction
from chatgptApiKey import OPENAI_API_KEY

# Define the bibligorathy file location and where you want the ouput to be
bibligorathy_loc = "hu-Corpus/fedBiblograthy.csv"
output_loc = "ai-Corpus/ai-FederalistPaper/"

# Romantic poem example
# bibligorathy_loc = "hu-Corpus/poemsBiblograthy.csv"
# output_loc = "ai-Corpus/ai-poem/"




# this is the prompt that is sent chatGPT to be generated, must included {} with the order author, title, year. 
# If you want to change the order edited the ".format(…)" that output to the varible "question"

prompt = """Write a political paper in the style of {} with the title "{}" published in the year {}"""

# prompt = 'Write a scientifc abstract in the style of {} with the title "{}" published in the year {}' # Scientific abstract examples 
# prompt = """Write a poem in the style of {} with the title "{}" published in the year {}""" # Romantic Poetry example

# Section 2: Creating Prompts 


# This seciton of willl recive the information
authorInformation = [] # This will store all the author information

# We will use the CSV file hummanBibliograthy, which contains the author name, title and year.
humanPoems = pd.read_csv(bibligorathy_loc, escapechar='"')


for index, row in humanPoems.iterrows():
    poemData = dict(author=row["Author"], title=row["Title"]  ,year=row["Year"])
    
    authorInformation.append(poemData)



# This section of the code will generate the messages for chat gpt.
chatGPTcommands = []




# Section 3: Creating Abstract


# Now that we have the prompts lets generate our reponese

# Create a client for openAI chatGPT
client = OpenAI(api_key=OPENAI_API_KEY)


aiAbstracts = []


print("Communicating with chatGPT")
# Let Generate our abstracts
for abstract in authorInformation:
    
    # Exctract that abstract metadata.
    author = abstract["author"]
    title = abstract["title"]
    year = abstract["year"]
    
    
    # Creates the unique promt for the particular paper.
    
    question = prompt.format(author, title, year)
    
    prompt = dict(role= "user", content= question)
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages= [prompt]
    )
    
    
    
    abstractText = completion.choices[0].message.content
  
    currentAiAbstract = dict(title = title, author = author, text = abstractText)
    
    aiAbstracts.append(currentAiAbstract)
    


# Section 4: Saving prompt

# For every AI abstract
for abstract in aiAbstracts:
    
    # remove the metadata
    author = abstract["author"]
    title = abstract["title"]
    text = abstract["text"]
    
    # Format The Title and Author So It may be used for file name
    # removes illegal characters: https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/
    formatedAuthor = ''.join(letter for letter in author if letter.isalpha())
    formatedTitle = ''.join(letter for letter in title.title() if letter.isalpha()) #Made Each word upercase for legiblity

    
    
    print(formatedAuthor,formatedTitle)
    
    
    # create a file name
    fileName = "ai---{}---{}".format(formatedAuthor,formatedTitle)
    
    # Lets Write the file
    with open( output_loc+fileName+".txt" , "w") as savefile:
    
            # save the jason
            savefile.write(text)
            
