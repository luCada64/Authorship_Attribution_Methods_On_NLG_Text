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


# If you'd like to update the promt you must edit the string named "prompt"


# Section 2: Extracting Biblograthy


# This seciton of willl recive the information
authorInformation = [] # This will store all the author information

# We will use the CSV file hummanBibliograthy, which contains the author name, title and year.
humanBib = pd.read_csv(bibligorathy_loc, escapechar='"')

# Extract all the information from the h
for index, row in humanBib.iterrows():
    paper = dict(author=row["Author"], title=row["Title"]  ,year=row["Year"])
    
    authorInformation.append(paper)





# Section 3: Creating AI corpus


# Now that we have the prompts lets generate our reponese

# Create a client for openAI chatGPT
client = OpenAI(api_key=OPENAI_API_KEY)

# This section of the code will generate the messages for chat gpt.
aiCorpus = [] # this list will store the list before saving


print("Communicating with chatGPT")
# Let Generate our abstracts
for abstract in authorInformation:
    
    # Exctract that abstract metadata.
    author = abstract["author"]
    title = abstract["title"]
    year = abstract["year"]
    
    
    # Creates the unique promt for the particular paper.
    
    question = """Write a political paper in the style of {} with the title "{}" published in the year {}""".format(author, title, year)
    
    prompt = dict(role= "user", content= question)
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages= [prompt]
    )
    
    
    # Once the result is recived, save the data to the list of cropuses
    abstractText = completion.choices[0].message.content
  
    currentAiAbstract = dict(title = title, author = author, text = abstractText)
    
    aiCorpus.append(currentAiAbstract)
    


# Section 4: Saving prompt

print("Saving Data")
# For every AI abstract
for abstract in aiCorpus:
    
    # extract the metadata
    author = abstract["author"]
    title = abstract["title"]
    text = abstract["text"]
    
    # Format The Title and Author So It may be used for file name
    # removes illegal characters: https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/
    formatedAuthor = ''.join(letter for letter in author if letter.isalpha())
    formatedTitle = ''.join(letter for letter in title.title() if letter.isalpha()) #Made Each word upercase for legiblity

    
    # Print the autohr and title to inform the user what accruings
    print(formatedAuthor,formatedTitle)
    
    
    # create a file name
    fileName = "ai---{}---{}".format(formatedAuthor,formatedTitle)
    
    # Lets Write the file
    with open( output_loc+fileName+".txt" , "w") as savefile:
    
            # save the jason
            savefile.write(text)
            
