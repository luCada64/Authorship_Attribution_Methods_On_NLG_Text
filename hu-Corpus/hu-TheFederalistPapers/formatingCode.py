# This code will take the complete Federalist paper txt file and extract out
# The title, the author and year for each paper

# An assumption we are making is that all paper credide as "Madison with Hamiloton" as just madison for consitency


def saveFile(title, author, year, text):


    file = "hu---{}---{}---{}.txt".format(author, title, str(year))
    path = "hu-Corpus/hu-TheFederalistPapers/"
    
    with open( path+file , "w") as savefile:
    
            text = "\n".join(text)
    
            savefile.write(text)
    
    
    print("Saving file: {} by {} in the year {}".format(title, author, year))







with open("hu-Corpus/hu-TheFederalistPapers/complete-Federalist-Paper.txt", mode="r") as file:

    # Get the text into a format 
    completePapers = file.read()
    completePapers_lines = completePapers.split('\n')
        
    
    # Remove the unseary lines
    completePapers_lines = completePapers_lines[36:]
    
        
    
    index = 0
    paperNum = ""
    author = ""
    title = ""
    year = "0000"
    
    # temp 
    completePapers_lines = completePapers_lines
    
    for line in completePapers_lines:
        
        # Stop the code if when you run out of lines  
        if line[:3] == "***":
            break
        
        
        # Get the current title
        if line[:14] == "FEDERALIST No.":
            # Extract metaa data
            paperNum = line
            
            title = completePapers_lines[2]
            
            # TO fix year code
            year = completePapers_lines[4][-4:] 
            
            author = completePapers_lines[6]
            
            index = index + 7
            
            # Comidn paper number into tittle
            title = "{}: {}".format(paperNum, title)
            
            text = []
            
            # Let's Extract the content
            while completePapers_lines[index][:14] != "FEDERALIST No.":
            
                text.append(completePapers_lines[index])
                
                index = index + 1
                
            
        
            # Changed the character to fixe fomat
            author = ''.join(letter for letter in author if letter.isalpha())
            title = ''.join(letter for letter in title.title() if letter.isalpha() or letter.isdigit())
    
        
        
            # Now that we got all the conent we may save it
            saveFile(title, author, year, text )
            
    
            # Now we need to remove all the lines up to that point
            completePapers_lines = completePapers_lines[index:]
            