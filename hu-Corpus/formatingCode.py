# This code will take the complete Federalist paper txt file and extract out
# The title, the author and year for each paper
# An assumption we are making is that all paper credide as "Madison with Hamiloton" as just madison for consitency


# =========== Helper functions ==============

# Saves the file, in the corect format, location with all the metadata
def saveFile(title, author, year, text):

    # Sets the file name
    file = "hu---{}---{}---{}.txt".format(author, title, str(year))
    
    # Saves the file
    path = "hu-Corpus/hu-TheFederalistPapers/"
    with open( path+file , "w") as savefile:
            text = "\n".join(text)
            savefile.write(text)
    
    
    print("Saving file: {} by {} in the year {}".format(title, author, year))


# Updates the biligohathy so that the informaiton can be used for AI generation
def saveBib(title, author, year):
    
    file = "hu-Corpus/fedBiblograthy.csv" # Sets the path
    
    with open( file , "a+") as savefile:
    
            # Foramts the metadata to be saved.
            text = "{}, {}, {}\n".format(author,title,year)
            savefile.write(text)



# ===========  Starting to sanitsize  ==============


# Opens the complet collection of the federalist prpare
with open("hu-Corpus/hu-TheFederalistPapers/complete-Federalist-Paper.txt", mode="r") as file:

    # Get the text into a readble format 
    completePapers = file.read()
    completePapers_lines = completePapers.split('\n')
        
    
    # Remove the unseary lines
    completePapers_lines = completePapers_lines[36:]
    
    # Create bib file and formating it
    bib = open('hu-Corpus/fedBiblograthy.csv', 'w')
    bib.write("Author,Title,Year\n")
    bib.close()
    
    # Define tempoary default values
    index = 0
    paperNum = ""
    author = ""
    title = ""
    year = "0000"
    
    # Were using the while look, to search thought the hole documents
    while True:
        
        # Seth the deafults values
        index = 0
        line = completePapers_lines[index]
        
    
            
        # If the current line is equals to the start of anew paper, start extaring information
        if line[:14] == "FEDERALIST No.":
            
            # Extract metaa data
            paperNum = line
            title = completePapers_lines[2]
            year = completePapers_lines[4][-4:]  #Extracting the year is more complicated
            author = completePapers_lines[6]
            
            # Increase the index
            index = index + 7
            
            # Format the title to include the paper number
            title = "{}: {}".format(paperNum, title)
            
            
            # Set up a blank text box
            text = []
        
            
            
            # Let's Extract the content, a while loop is used to keep extracting the content untils the next paper
            while completePapers_lines[index][:10] != "FEDERALIST":
                
                # Add A break clause in when it reace the end of the paper
                if completePapers_lines[index][:3] == "***":
                    break
                
                # Added the line to the text
                text.append(completePapers_lines[index])
                
                # Increase the index
                index = index + 1
                
               
            
            # We also must update the Author name to be consitent.
            if author == "HAMILTON":
                author = "Alexander Hamilton"
            elif author == "JAY": 
                author = "John Jay"
            else: #We are assuming all paper marke Madison, with Hamilotn as just madison
                author = "James Madison"
            
            
            # Save the information to the bilogthay
            saveBib('"'+title+'"', author, year)
        
            
        
            # This code update the author and title to insure no special character are used
            author = ''.join(letter for letter in author if letter.isalpha())
            title = ''.join(letter for letter in title.title() if letter.isalpha() or letter.isdigit())
    
        
        
            # Now that we got all the conent we may save it
            saveFile(title, author, year, text )
            
    
            # Now we need to remove all the lines up to that point
            completePapers_lines = completePapers_lines[index:]
        
    
exit()