# Requierments
- A valid OpenAI API key, to be saved in the "chatgptApiKey-Example.py" but removed the "-Example".
- All python modules must be installed from "requirements.txt" using Python version Python 3.11.3
- This code was writen in Mac OS, it may not function with file paths.
- Save your human corpus files with the format: "hu---Author---Title---Year.txt"

# How to generate a NLG/AI text
1. Provide a csv file, with the headings: Author, Title and Year with not space bettwen
2. Update the paths for the Python program: aiTextGenerator.py
3. Update the prompt for ChatGPT, insuring you use string formatign to add the title, Author and Year.
3. Run the code, the filse will be oupted at your selecetd location.

# How to run delta.
1. Create an Output path for the resulting data.
2. Update Paths, to the corrisponding location, insuring the files follow the naming conventions 
    - If the Ai corpus was added manualy rather than via the program code insure it follows the standard: "ai---AuthorImpersonated---Title---Year.txt"
3. Update showHeatmap to False if you would like the heatmap to apear via the matplotlib interface, default = False for performance.
4. Run python file.
## Files produced 
- avr_prob.csv: Show the mean delta values for each impersonaion of an author. The header is the actual author, each row is the delta score for an AI impersonation.
- burrows_mean_probaltities.png: Heatmap of the values form avr_prob.csv
- spreadsheet.csv: Show the complete delta score for each AI file when compared to the actual author
- avg_burrows_delta_score.txt: show the cound, mean, std, min, percentiles and max value for the mean of the delta score per authors.
- burrows_delta_score.txt: show the cound, mean, std, min, percentiles and max value for the mean of the delta score for each AI impersonation.