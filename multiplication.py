##### program that generate a multiplication table from 1 to the number passed. 
user_input=int(input("enter rhe elements :  "))
def power_of_nums(x):
   tempList=[]
   for i in range(1,user_input):
    tempList2=[]
    
    for j in range(1,i+1):
         tempList2.append(f"{i*j}")  
         
    tempList.append(tempList2)
   print(tempList)
power_of_nums(user_input)


###### another shape of output show to user

num=int(input("enter the number"))
def multiply(num):
    for i in range(1,num+1):
     for j in range(1,i+1):
        print(f"{i}x{j}={i*j}")
        
multiply(num)
