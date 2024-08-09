#student_dict = {
   # "student": ["Angela", "James", "Lily"],
    #"score": [56, 76, 98]
#}

#Looping through dictionaries:
#for (key, value) in student_dict.items():
    #Access key and value
 #   pass

#import pandas
#student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict=data.to_dict()
data_df=pandas.DataFrame(data_dict)

dict={row.letter:row.code for (index,row) in data_df.iterrows() }
print(dict)

user_input=input("Enter word: ").upper()
user_input.split()
list=[dict.get(n) for n in user_input]
print(list)