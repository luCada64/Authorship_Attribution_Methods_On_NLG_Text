# Section 1: Packages
import pandas as pd
from openai import OpenAI

# To run this code you must create a .py file with a global varabile named "OPENAI_API_KEY"
# This variable must contain you're OpenAI API ley
# documentation: https://platform.openai.com/docs/introduction
from chatgptApiKey import OPENAI_API_KEY


# Section 2: Creating Prompts 



# This seciton of willl recive the information

authorInformation = [] # This will store all the author information

# We will use the CSV file hummanBibliograthy, which contains the author name, title and year.
humanPoems = pd.read_csv("bibligorath.csv", escapechar='"')


for index, row in humanPoems.iterrows():
    poemData = dict(author=row["Author"], title=row["Title"]  ,year=row["Year"])
    
    authorInformation.append(poemData)


# This section of the code will generate the messages for chat gpt.
chatGPTcommands = []




# Section 3: Creating Abstract


# Now that we have the prompts lets generate our reponese

# Create a client for openAI chatGPT
client = OpenAI(api_key=OPENAI_API_KEY)


aiPoems = []

print("Communicating with chatGPT")
# Let Generate our Poems
for poem in authorInformation:
    
    # Exctract that abstract metadata.
    author = poem["author"]
    title = poem["title"]
    year = poem["year"]
    
    
    print("generating: {} by {} in the year {}".format(title, author, year))
    
    # Creates the unique promt for the particular paper
    question = """Write a poem in the style of {} with the title "{}" published in the year {}""".format(author, title, year)
    
    prompt = dict(role= "user", content= question)
    
    completion = client.chat.completions.create(
        model="gpt-4o",#"gpt-3.5-turbo",
        messages= [prompt]
    )
    
    
    poemText = completion.choices[0].message.content
  
    currentAiPoem = dict(title = title, author = author, text = poemText)
    
    aiPoems.append(currentAiPoem)
    


print("Saving AI Data")

# Section 4: Saving prompt

# For every AI Poem
for poem in aiPoems:
    
    # remove the metadata
    author = poem["author"]
    title = poem["title"]
    text = poem["text"]
    
    # Format The Title and Author So It may be used for file name
    # removes illegal characters: https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/
    formatedAuthor = ''.join(letter for letter in author if letter.isalpha())
    formatedTitle = ''.join(letter for letter in title.title() if letter.isalpha()) #Made Each word upercase for legiblity

    
    
    print(formatedAuthor,formatedTitle)
    
    
    # create a file name
    fileName = "ai---{}---{}".format(formatedAuthor,formatedTitle)
    
    # Lets Write the file
    with open( "ai-Corpus/"+fileName+".txt" , "w") as savefile:
    
            # save the jason
            savefile.write(text)
            
