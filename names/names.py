import time
from binary_search_tree import BinarySearchTree
import sys
sys.path.append('./binary_search_tree.py')

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# insert all names into a BST
# each name is a new BST in the BST
bst = BinarySearchTree(names_1[0][1])
# loop through the names and insert into the bst DS
for name in names_1:
    bst.insert(name)

# then check if names in name_2 are contained in the bst. if so append them to list
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

# effectively changing the complexity from a O(n^2) to just O(2n) = O(n)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
