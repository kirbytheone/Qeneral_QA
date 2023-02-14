# Here I will code some things
john_salary = 1000.50
marta_salary = 921.2
print('John salary:', john_salary, 'Marta salary', marta_salary);

john_age = 33
marta_age = 45
print('John`s age:', john_salary, 'Marta`s age:', marta_age);

john_name = "John Malkovitch"
marta_name = "Marta Kaufman"
print(john_name, marta_name);

john_gender = False
marta_gender = True
print(john_gender, marta_gender);

john_friends =["Garry", "Kristine", "Lola", "Jack"]
marta_friends = ["Janine", "Marci", "Opra"]
print('John`s friends are', *john_friends, 'and Marta`s friends are', *marta_friends, sep=",");
# так и не получилось сделать красиво, не понял как в итоге убрать запятую перед "are" и после "and ":( может через луп, хз


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
