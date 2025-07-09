#### program that make mario pyramid in list

numOfList=int(input("num of elements in list:  "))
list=[]
def pyramid_in_list(x):
  for i in range(1,numOfList+1): 
     list.append(" ")
  for i in range(numOfList+1):
      list.remove(" ")
      list.append("*")  
      print(list)
pyramid_in_list(numOfList)


########## another example but make a pyramid without lists

userInput=int(input("enter the number : "))
def marioPyramid(value):
 for i in range(1,userInput):
     print(' '*(userInput-i),'*'*i)
     
marioPyramid(userInput)