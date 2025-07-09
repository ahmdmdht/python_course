######a program that user input some of elements then sort it Ascending or descending
#### without any change in the original list
num_Of_elements=int(input("num of elements in list :  "))
list=[]
def sorted_elements(x):
    for i in range(num_Of_elements):
     element_User=int(input("enter the new element:  "))
     list.append(element_User)
    print("the original list")
    print(list)
    print("the sorted list below")
    print(sorted(list))
    print("the reversed list below")
    print(sorted(list,reverse=True))

    
sorted_elements(num_Of_elements)