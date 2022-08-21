# implementation of binary search

# naive search: scan the entire list and ask if it's equal to the target
# if yees, return the index
# if no, then return -1

def naive_search(l, target):
    # example l = [1, 3 ,12, 78, 90]
    for i in range(len(l)):
        if l[i] == target
            return i
     return -1