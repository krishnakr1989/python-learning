# b=[1,2,3]
# a = b
# a = b.copy()
# print("a",a)
# a = b.deepcopy(b)
# print("a",a)


# from copy import deepcopy

# b = [1, 2, 3]
# a = b
# print("a", a)

# a = b.copy()
# print("a", a)

# a = deepcopy(b)
# print("a", a)

# Main lesson:

# Shallow copy: only copies the outer structure
# Deep copy: copies everything recursively

from copy import copy, deepcopy

# Shallow copy append
lst1=[[1,2,3],[4,5,6]]
lst2=lst1.copy();
lst1.append([7,8,9])
print("lst1",lst1)
print("lst2",lst2)

#replacement
lst1=[[1,2,3],[4,5,6]]
lst2=lst1.copy();
lst1[1][2]=99
print("lst1",lst1)
print("lst2",lst2)

print("======================")

# deep copy append
lst1=[[1,2,3],[4,5,6]]
lst2=deepcopy(lst1);
lst1.append([7,8,9])
print("lst1",lst1)
print("lst2",lst2)

# replacement
lst1=[[1,2,3],[4,5,6]]
lst2=deepcopy(lst1);
lst1[1][2]=9999
print("lst1",lst1)
print("lst2",lst2)
