lst = list()
# empty list
print(id(lst))
"""
iterable can only be used in list - an object that can hold multiple object inside
"""
lst1 = list([1, 2, 3, 4])
lst2 = [10, 20, 30, 40]
print(lst1)
print(lst2)

lst.append(12)
lst.append(100)
lst.insert(1, 59)
print(lst)
lst.remove(59)
lst.clear()
print(lst)
"""
in extend method 
"""
lst.extend(lst1)
print(lst)

del (lst[-1])
print(lst)
print(lst1.index(3))

"""
copy the list
"""
lst1 = [10, [100]]
lst3 = lst1
print(lst1, lst2)
print(id(lst1), id(lst2))
"""
point to common list in memory
"""
lst2[0] = 2
lst2.append(21)
print(lst1, lst2)
print(id(lst1), id(lst2))

lst1 = [10, [100]]
lst2 = lst1.copy()
print(lst1, lst2)
print(id(lst1), id(lst2))
lst2[1].append(200)
print(id(lst1), id(lst2))
"""
reference id will be different after copy of the given list
"""
"""
deep copy - 
"""
import copy

lst1 = [10, [100]]
lst2 = copy.deepcopy(lst1)
print(lst1, lst2)
print(id(lst1), id(lst2))
lst2[1].append(200)
print(id(lst1), id(lst2))

"""
sorting technique
-element should be same type
"""
lst = [12, 23, 41, 10, 3, 25, 99]

"""
to preserve main list use global sort method
"""
newlist = sorted(lst)
print(newlist)
print(lst)

"""
sort in ascending order
"""
lst.sort()
print(lst)

"""
sort in descending order
"""
newlist1 = list(reversed(lst))
print(newlist1)

"""
or
"""
list2 = lst.sort(reverse=True)
print(list2)


'''
1.	Write a Python program to get the largest number from a list
'''
list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest number is:", list1[-1])

'''
2.	Write a Python program to multiplies all the items in a list.
'''


def multiplyList(myList):
    result = 1
    for i in myList:
        result = result * i
    return result


list1 = [1, 2, 3]
list2 = [5, 9, 5]
print(multiplyList(list1))
print(multiplyList(list2))

'''
3.	Write a Python program to get the second largest number from a list.
'''
list1 = [10, 20, 40, 45, 99, 101]
list1.sort()
print("Second Largest number is:", list1[-2])

'''
4.	Write a program to remove all the duplicate elements from list
'''


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


duplicate = [2, 4, 10, 20, 5, 2, 20, 5, 20, 4]
duplicate.sort()
print(Remove(duplicate))

'''
5.	Write a Python program to count the number of strings where the string length is 4 or  more and the first and last character are same from a given list of strings.
'''


def compare(a):
    ctr = 0
    for i in a:
        if len(i) > 4 and i[0] == i[-1]:
            ctr += 1
    return ctr


a = ['abc', 'xyz', 'aba', '1221', 'aaaaaaa', 'asdasdsada']
for i in a:
    z = compare(a)

print(z)

'''
6.	Write a Python program to find common items from two lists
'''


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")


a = [1, 2, 3, 4, 5]
b = [5, 6, 3, 8, 9]
print(common_member(a, b))

'''
7.	Write a Python program to find the list in a list of lists whose sum of elements is the highest.
'''


def maximumSum(list1):
    maxi = 0
    for x in list1:
        sum = 0
        for y in x:
            sum += y
        maxi = max(sum, maxi)

    return maxi


list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
list2 = [[10, 20, 30], [40, 50, 60]]
print(maximumSum(list1))
print(maximumSum(list2))
