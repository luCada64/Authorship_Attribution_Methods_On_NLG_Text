# This code will take the complete Federalist paper txt file and extract out
# The title, the author and year for each paper


def saveFile(title, author, year, text):
    
    author = ''.join(letter for letter in author if letter.isalpha())
    title = ''.join(letter for letter in title.title() if letter.isalpha())
    
    
    file = "hu---{}---{}---{}".format(author, title, str(year))
    
    
    with open( file , "w") as savefile:
    
            text = "\n".join(text)
    
            savefile.write(text)
    
    
    print("Saving file: {} by {} in the year {}".format(title, author, year))







with open("hu-Corpus/hu-TheFederalistPapers/complete-Federalist-Paper.txt", mode="r") as file:

    # Get the text into a format 
    completePapers = file.read()
    completePapers_lines = completePapers.split('\n')

    
    # # Skip until the program find the first paper
    # index = 0
    # while completePapers_lines[index] != "FEDERALIST No. 1":
        
    #     # Let find the index
    #     index = index+1
        
    
    # Remove the unseary lines
    completePapers_lines = completePapers_lines[37:]
    
        
    currentPaper = []
    
    index = 0
    paperNum = ""
    current_author = ""
    currrent_title = ""
    current_year = 0000
    
    # temp 
    completePapers_lines = completePapers_lines[:500]
    
    for line in completePapers_lines:
        
        if line[:3] == "***":
            break
        
        
        # Add a break clause
        if line[:14] != "FEDERALIST No.":
            index = index +1
            
        
        if line[:14] == "FEDERALIST No.":
            
    
            # Lets get out the old text
            previous_text = completePapers_lines[:index-1]
            
            # save the data
            saveFile(currrent_title, current_author, current_year, previous_text)
            
            
            
            # Update complete Paper to remove all that come befroe
            completePapers_lines = completePapers_lines[index:]
            
            paperNum = line
            title = completePapers_lines
            
            print(completePapers_lines)
            
        

        