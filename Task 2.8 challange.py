john = {
    "John info": {
    "Full name": "John Malkovitch",
    "Age": 33,
    "Salary": 1000.50,
    "Gender": False,
    "Coordinates": [43.2141, 27.9147]},
    "John friends": {"Garry", "Kristine", "Lola", "Jack"}
},
marta = {
    "Marta info": {
    "Full name": "Marta Kaufman",
    "Age": 45,
    "Salary": 921.2,
    "Gender": True,
    "Coordinates": [43.2141, 27.9147]},
    "Marta friends": {"Janine", "Marci", "Opra"}
}
print(john);
print(marta);

"""
Need to understand how to do this iteration with 'for' loop in nested dictionaries, like in this example:

people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])
"""