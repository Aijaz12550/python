
#########################
##### remove method #####
#########################

list1 = [ 1, 2, True, "aijaz", "test"]
""" 
list.remove(arg) it will take one item of list 
as a argument to remove from list 
"""

list1.remove(1) # it will remove 1 from list1
#list1.remove(99) # it will throw error  because 99 is not exist
print("list1",list1)



#########################
##### sorting list  #####
#########################

sorting_list = [1,2 ,33, -44, 108, 9876, -44545, 444]

sorting_list.sort() # it will sort the original list
print(" sorting_list =",sorting_list)

sorted_list = sorted(sorting_list) # it will return the sorted list without changing the original.
print("sorted_list = ",sorted_list)



#########################
##### slicing list  #####
#########################

s_l1 = [0, 1, 2, 3]

s_c = s_l1[:]

print("s_c",s_c)





list2 = [1] * 3 # [1, 1, 1]
list3 = [2,3]
list4 = list2 + list3 # [ 1, 1, 1, 2, 3 ]
print("list4",list4)
