# Task 5.1
# While loop
pregnant = True

while pregnant:
  print("I'm gonna be a dad!")
  pregnant = False

my_number = 33

while my_number < 41:
  print(my_number)
  my_number = my_number + 1


# For loop
header = "What is your favourite back flip variation:"
standing_back_flip_variations = ["Basic", "Arabian", "Full twist", "Iron man", "X-out"]
print(header)
for back_flip_type in standing_back_flip_variations:
  print(back_flip_type, "?")

# Nested loop

groups = [["Epictetus", "Marcus Aurelius"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

for group in groups:
  for name in group:
    print(name)

# Break and continue in loops

numbers_list = [0, 254, 2, 1, -13, 34, 87, 13]

for num in numbers_list:
  if (num < 0):
    print("Here is negative!")
    break
  print(num)

big_number_list = [1, 29, -1, 4, -5, 15, 2, -9, 99]

for number in big_number_list:
  if number < 0:
    continue
  print(number)

#Task 5.2
#2. You have a variable var=10. Write other variable 'result' which
#will get string True if var == 10 and False in other case. Using Tern operators

var = 10
result = True
if var == 10:
    print(result)
else:
    print(False)

#Task 5.3
#3. You have a list of elements [1, 2, 3, 4, 5, 6, 7, 8].
#Loop through the list using the foreach loop.
#The element with an odd index is put into a new list of tuples where the first element is the index and the second is the value.
#[(index, value)]. accordingly, elements with an even index are placed in another list of tuples with the same format as in the case with odd indices.

elements_list = [1, 2, 3, 4, 5, 6, 7, 8]
for number in elements_list:
  print(number)

odd_elements_list = []
even_elements_list = []

list_length = len(elements_list)

for number in elements_list:
  if number % 2 ==0:
    odd_elements_list.append(number)
  else:
    even_elements_list.append(number)
#for index in range(list_length):
for index, number in enumerate(elements_list):
    print('Index:', index, 'Number:', number)

#[number for number in elements_list if number % 2 ==0: odd_elements_list.append(elements_list[index])]

# Task 5.4
#4. You have 2 lists of names friends = ["John", "Marta", "James"] and enemies = ["John", "Johnatan", "Artur"].
#Loop through the names of friends and write the message f"{friend} we are the best friends" if the friend is not in the list of enemy names.
#And display the message f"{friend} we are not friends anymore" if the friend is on the list of enemies.
#If the friend's name is James, we don't check him because he is the best friend.

friends_list = ["John", "Marta", "James"]
enemies_list = ["John", "Johnatan", "Artur"]
#

names_list = friends_list + enemies_list
[print(f"We are the best friends with {name}") for name in friends_list]
#[print(f"{name} we are not friends anymore") for name in enemies_list]
for name in names_list:
  if name in enemies_list and friends_list:
   print(f"{name} we are not friends anymore")