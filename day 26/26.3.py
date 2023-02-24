student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.



d = pandas.read_csv("day 26/nato_phonetic_alphabet.csv", index_col="letter")

print(d.to_dict()["code"])

nato_dict = d.to_dict()["code"]

user_input = input("Write the words").upper()
user_input_list = user_input.split()
print(user_input_list)

convert_sentence = []
for i in user_input_list:
    for j in i:
        if j in nato_dict.keys():
            convert_sentence.append(nato_dict[j])

print(" ".join(convert_sentence))