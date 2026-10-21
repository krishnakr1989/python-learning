# Main lesson:

# Shallow copy: only copies the outer structure
# Deep copy: copies everything recursively

from copy import copy, deepcopy

# Shallow copy append
lst1=[1,2,3]
lst2=lst1.copy();
lst1.append(20)
print("lst1",lst1)
print("lst2",lst2)

#replacement
lst1=[1,2,3]
lst2=lst1.copy();
lst1[1]=99
print("lst1",lst1)
print("lst2",lst2)

print("======================")

# deep copy append
lst1=[1,2,3]
lst2=deepcopy(lst1);
lst1.append(30)
print("lst1",lst1)
print("lst2",lst2)

# replacement
lst1=[1,2,3]
lst2=deepcopy(lst1);
lst1[1]=9999
print("lst1",lst1)
print("lst2",lst2)
