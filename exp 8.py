import random

# Define lists of possible values for each column
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Fiona", "George"]
occupations = ["Doctor", "Engineer", "Teacher", "Lawyer", "Programmer", "Artist", "Musician"]
posts = ["Manager", "Supervisor", "Analyst", "Specialist", "Associate", "Intern", "Trainee"]

# Generate a random number of rows (adjust as needed)
num_rows = 10

# Create an empty list to store the table data
table_data = []

# Generate random values for each row
for _ in range(num_rows):
  name = random.choice(names)
  occupation = random.choice(occupations)
  post = random.choice(posts)
  table_data.append({"Name": name, "Occupation": occupation, "Post": post})

# Print the table in a readable format
print("+--------+--------------+----------+")
print("|Name     |Occupation     |Post      |")  # Remove extra space
print("+--------+--------------+----------+")
for row in table_data:
  print("| {:7} | {:14} | {:8} |".format(row['Name'], row['Occupation'], row['Post']))
print("+--------+--------------+----------+")
