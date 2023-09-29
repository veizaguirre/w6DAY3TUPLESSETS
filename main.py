import requests

response = requests.get("https://randomuser.me/api")
#print(response.json())

gender = response.json()['results'][0]['gender']
print(gender)

first_name = response.json()['results'][0]['name']['first']
print(first_name)

postcode = response.json()['results'][0]['location']['postcode']
print(postcode)

login = response.json()['results'][0]["login"]["username"]
print(login)

login2 = response.json()['results'][0]['login']['password']
print(login2)

# Unique Elements:

# Given a list of integers, return a set containing only the unique integers.
# python
# Copy code
# example_input = [1, 2, 2, 3, 4, 4, 4] **
# unique_elements = set(example_input)
# print(unique_elements) **

# # # Expected Output: {1, 2, 3, 4}

# # Set Operations:

# # Given two sets, perform the following operations:
# set1 = {1, 2, 3, 4, 5} **
# set2 = {3, 4, 5, 6, 7} **
# # Union #joins them
# print(set1.union(set2)) **
# # Intersection //shows where they intersect
# print(set1.intersection(set2)) **
# # Difference (Set 1 - Set 2) #gives difference
# print(set1.difference(set2)) **

# # Symmetric Difference
# # Is Subset?:
# #apart of a larger group of things


# # Given two sets, check if the first set is a subset of the second set.
# # Remove Duplicates:
# def isThis_subset(set1, set2): **
#   return set1.issubset(set2) **


# print(isThis_subset(set1, set2)) **


# # Given a string, return a new string with duplicate characters removed. Use a set to help you with this.
# def remove_duplicates(set1): **
#   return ''.join(sorted(set(set1))) **


#Sets remove duplicates
