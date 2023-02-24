student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)