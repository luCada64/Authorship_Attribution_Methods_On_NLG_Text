# Section 1: Packages

from openai import OpenAI

# To run this code you must create a .py file with a global varabile named "OPENAI_API_KEY"
# This variable must contain you're OpenAI API ley
# documentation: https://platform.openai.com/docs/introduction
from chatgptApiKey import OPENAI_API_KEY


# Section 2: Creating Prompts 



# This seciton of willl recive the information

authorInformation = [{'author':"Charles Dickens", 'title':"Why Scrooge Was Mean", 'year':1888},
                         {'author':"Wes Anderson", 'title':"Is a square aspect ration better for comtemporay cinema?", 'year':2016}, 
                         {'author':"Alan Turing", 'title':"Evaluating romantic attraction in Robots", 'year':1956}]



# This section of the code will generate the messages for chat gpt.
chatGPTcommands = []

# # for every abstract
# for abstract in authorInformation:
    
#     # Exctract that abstract metadata.
#     author = abstract["author"]
#     title = abstract["title"]
#     year = abstract["year"]
    
#     # Creates the unique promt for the particular paper
#     question = """Write a scientifc abstract in the style of {} with the title "{}" published in the year {}""".format(author, title, year)
    
#     # Format the question for chatGPT to be intrepered
#     prompt = dict(role = "user", content = question)
    
#     # prompt = {"role": "user", "content": question},
    
#     # Append our probmt to the list
#     chatGPTcommands.append(prompt)



# Section 3: Creating Abstract


# Now that we have the prompts lets generate our reponese

# Create a client for openAI chatGPT
client = OpenAI(api_key=OPENAI_API_KEY)


aiAbstracts = []


# Let Generate our abstracts
for abstract in authorInformation:
    
    # Exctract that abstract metadata.
    author = abstract["author"]
    title = abstract["title"]
    year = abstract["year"]
    
    
    # Creates the unique promt for the particular paper
    question = """Write a scientifc abstract in the style of {} with the title "{}" published in the year {}""".format(author, title, year)
    
    prompt = dict(role= "user", content= question)
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= [prompt]
    )
    
    
    
    abstractText = completion.choices[0].message.content
  
    currentAiAbstract = dict(title = title, author = author, text = abstractText)
    
    aiAbstracts.append(currentAiAbstract)
    

print("\n")
for n in aiAbstracts:
    print("{} by ai {}".format(n['title'], n['author'] ))
    print(n['text'])
    print("\n\n\n")


# Section 4: Saving prompt


for abstract in aiAbstracts:
    
    author = abstract["author"]
    title = abstract["title"]
    text = abstract["text"]
    
    fileName = "ai"+author+title
    
    # Lets Write the file
    with open( "aiText/"+fileName+".txt" , "w") as savefile:
    
            # save the jason
            savefile.write(text)
            
