

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3, 4]

def sumlist(l1, l2):
    return [
        x+y for x, y in zip(l1,l2)
    ]

print(sumlist(list1, list2))