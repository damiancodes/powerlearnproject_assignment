# Step 1: Create an empty list
my_list = []

# Step 2: Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from the list
my_list.pop()

#Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Print the final list
print("Final List:", my_list)
