# This code will take the complete Federalist paper txt file and extract out
# The title, the author and year for each paper





with open("hu-Corpus/hu-TheFederalistPapers/complete-Federalist-Paper.txt", mode="r") as file:

    # Get the text into a format 
    completePapers = file.read()
    completePapers_lines = completePapers.split('\n')

    
    # Skip until the program find the first paper
    index = 0
    while completePapers_lines[index] != "FEDERALIST No. 1":
        
        # Let find the index
        index = index+1
        
        
        
    for line in completePapers_lines:
        
        # Add a break clause
        if line[:13] == "FEDERALIST No.":
            print(line)
        
        