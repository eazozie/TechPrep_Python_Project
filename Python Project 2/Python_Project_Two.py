#Flow chart 
#Read and open the csv file 
#Calculate the average of several columns and generate new columns based on the calculated values
#Write a function to determine the letter grades based on the final grades and apply to the new column
#Save the the new file 


#pip3 install pandas --upgrade (Already executed on the VS Code Terminal) 
#imorting pandas pd

import pandas as pd

#Open and read the excel csv file

df = pd.read_csv("Grades_Short.csv")

#Calculate the average of several columns and generate new columns based on the calculated values called 'Average'

df["Average"] = (df["Assignment_1"] + df["Assignment_2"] + 
                 df["Quiz_1"] + df["Quiz_2"] + 
                 df["Mid_Term_Exam"] + df["Final_Exam"]) / 6

# writing a function with a conditional statement on the Calculated Average
# I used 'if' statement together with a logical operator of 'and' to capture the desired range of values in the grade

def Letter_Grades(Average):
        if Average >= 90:
                return "A+"
        elif Average >= 80 and Average < 90:
                return "A"          
        elif Average >= 70 and Average < 80:
                return "B"
        elif Average >= 60 and Average < 70:
                return "C"
        elif Average >= 55 and Average < 60:
                return "D"
        elif Average < 55:
                return "F"

#Applying the function to create a new column
df["Final_Grades"] = df["Average"].apply(Letter_Grades)

#Saving to a new excel csv file
df.to_csv("New_Grades_Short.csv", index=False)

#print to view the excel csv file to verify
print(df)


