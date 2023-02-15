# Here I will code some things
#Exercise 2.1

john_salary = 1000.50
marta_salary = 921.2
print('John salary:', john_salary, 'Marta salary', marta_salary);

#Exercise 2.2

john_age = 33
marta_age = 45
print('John`s age:', john_salary, 'Marta`s age:', marta_age);

#Exercise 2.3

john_name = "John Malkovitch"
marta_name = "Marta Kaufman"
print(john_name, marta_name);

#Exercise 2.4

john_gender = False
marta_gender = True
print(john_gender, marta_gender);

#Exercise 2.5

john_friends =["Garry", "Kristine", "Lola", "Jack"]
marta_friends = ["Janine", "Marci", "Opra"]
print('John`s friends are', *john_friends, 'and Marta`s friends are', *marta_friends, sep=",");
# так и не получилось сделать красиво, не понял как в итоге убрать запятую перед "are" и после "and ":(

#Exercise 2.6

random_people_names = ["George", "Melisa", "Ross", "George", "Karen", "Karen", "Melisa", "Ross"]
set_unique_names = set(random_people_names)
print('Unique manes list:', *set_unique_names, sep="\n");
# second variation
"""
set_unique_names = set(random_people_names)
print("List of unique names:\n")
list_of_unique_names = (list(set_unique_names))
for item in list_of_unique_names:
    print(item);
"""
#Exercise 2.7

my_location_coordinates = (43.2141, 27.9147)
print("Latitude:", my_location_coordinates[0], "Longitude:", my_location_coordinates[1]);

#Exercise 2.8

john = {
    "Full name": "John Malkovitch",
    "Age": 33,
    "Salary": 1000.50,
    "Gender": False,
    "Friends": ["Garry", "Kristine", "Lola", "Jack"],
    "Coordinates": [43.2141, 27.9147]
}
marta = {
    "Full name": "Marta Kaufman",
    "Age": 45,
    "Salary": 921.2,
    "Gender": True,
    "Friends": ["Janine", "Marci", "Opra"],
    "Coordinates": [43.2141, 27.9147]
}
john_friends_list = {"Garry", "Kristine", "Lola", "Jack"},
marta_friends_list = {"Janine", "Marci", "Opra"}
print(john, marta, sep="\n");
print("John friends:", john_friends_list, "Marta friends:", marta_friends_list, sep="\n");