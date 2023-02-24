# new_dict = {new_key:new_value for item in list}

# new_dict = {new_key:new_value for (key, value) in dict.items()}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student:random.randint(1,100) for student in names}

passed_students = {student:score for (student, score) in students_score.items() if score >= 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:sentence.split().index(word) for word in sentence.split()}

print(result)