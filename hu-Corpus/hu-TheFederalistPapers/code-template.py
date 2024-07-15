# Please insure you have installed the requierment 
import re

# ======== PLEASE UPDATE =======


# Please Insure you Update your Path To match your os standar
path = "data/"

# ==============================



# Part 1: Opeing The File
# First Thing We Need To Do Is Open All The data
# To make sure are reading is safe we used the with meothd


# First we open the file 
with open(path+"pg5050-State-of-the-Union-Addresses.txt", mode="r") as input_file:
 
    # Now let get it into a string so we can manipulate it
    State_Of_The_Union_RAW = input_file.read()


    # ====== Part 2: Sorting The String ====== #

    # To making parsing the data easier we will the text into lines
    State_Of_The_Union_LINES = State_Of_The_Union_RAW.split('\n')

    # First we are going to read the text until we find the CONTENT section
    index = 0
    while State_Of_The_Union_LINES[index] != "CONTENTS":
        
        # Let find the index
        index = index+1
    

    
    # Now we have the index Let's strip the text of this metadata
    State_Of_The_Union_LINES = State_Of_The_Union_LINES[index+1:]
    
    # Let Create A List With The Year Of Each Union
    State_Of_The_Union_Titles = []
    
    
   
    index = 0 # Keep track of an index so that we can get rid of this section when we are done
    StateNum = 1 #So we can count which union it was, as we can't use year
    

    # Now we are going get the titles
    for StateTitle in  State_Of_The_Union_LINES:
        
        # If the title is *** it mean were at the end
        if StateTitle == '***':
            break
        
        index = index +1
        
        # Most state of the union, can be identiy by the year. (EXCEPT THE FIRST 2 as there both in 1790 :( )
        yearOfState = StateTitle[-4:]
        
        # Now We will check that the the title in fact a number not something else
        if not re.search("[0-2][0-9][0-9][0-9]", yearOfState):
            continue

        
        # Finaly Let add it to the list of speach, 
        # Unfortunaly MRrGeorge washington did two speach in a year so I am going to have to had an index
        formating = "StateOfTheUnion-"+yearOfState+"-"+str(StateNum)
        
        
        State_Of_The_Union_Titles.append(formating)
        
        #Increase the StateNum
        StateNum = StateNum+ 1 
    

    # lets now remove the reduantant section
    State_Of_The_Union_LINES = State_Of_The_Union_LINES[index:]
    
    
    # ====== Part 3 ======= #
    # Now that we have the tittle were going to add the adderss into the dictionary
    
    # So for every State of the union
    for State in State_Of_The_Union_Titles:
        
        # Let's Create The File We Will Save To, were using a for append
        SavedFile = open( "data/"+ State + ".txt", mode='a+') 
        
        
        # Each Adress Starts light this:
        # ***
        # 
        # State of the Union Address
        # by [Insert President Name]
        # [Date]
        # 
        # 
        # [Speach Starts]
        # This is irrelivant so we can get rid of these 5 lines
        
        State_Of_The_Union_LINES = State_Of_The_Union_LINES[8:]
        
        # Lets now get the speach
        
        speach = []
        
        index = 0
        while State_Of_The_Union_LINES[index] != "***":
            
            # Lets now save the file
            
            
            # Add a space bettwen each line, except on the first index
            if index != 0:
                SavedFile.write(" ")
            
            # Save the line to the file
            SavedFile.write(State_Of_The_Union_LINES[index])
            
            
            
            index = index +1
      
        
        
        # Let now remove these used lines
        State_Of_The_Union_LINES = State_Of_The_Union_LINES[index:]
        
        SavedFile.close() #close the file for safty
    

    
    
    