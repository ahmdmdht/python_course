####program that counts up the number of vowels [a, e, i, o, u]contained in the string

def vowelcount(y):
  list=['a','e','i','o','u','A','E','I','O','U'] 
  c=0 
  for i in y:
        
        if i in list:
            c+=1
            i+=i
            
        else:
            continue  
  print(c)
    
y=input("enter the word : ")
vowelcount(y)

