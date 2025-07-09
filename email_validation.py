## a program that user enter number of emails then check if validated
def validEmail(email):
 try:
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        
        if username and domain:
            if "." in domain:
                x,*y=domain.split('.')
                if x and y:
                    return True
                else : 
                    return False
            else :
                return False
        else : 
            return False
    else :
        return False
 except:
     return False
  

 
num_of_emails = int(input("enter the number of emails: "))
for i in range(1 ,num_of_emails+1):
     email = input("Enter your email: ")
     if validEmail(email):
      print("valid email")
      break
     else:
       print("unvalid email")
       
       
       
print("*"*50)     
########## a program that check if user enter name correctly without spaces or empty


user_input = input("Enter your name: ")
def name_validation(x):

 if user_input.isalpha():
    print("Valid name entered.")
 elif len(user_input)==0:
    print("error: Name cannot be empty.")
    
 else:
     print("Invalid input. Please use alphabetic characters only.")
     
name_validation(user_input)


### a program that check if the name and pass is correct using dictionary


user = [{"name":"omar","pass":"123"},{"name":"ahmed","pass":"456"}]
userInput=input("enter ur name:  ")
for i in user:
    if i["name"] ==userInput:
        userPass=input("enter ur pass:  ")
        if i["pass"] ==userPass:
            print("ur pass correct")
            break
        else:
            print("uncorrect password")
        break
    
    else:
        continue
else:
    print("not found")
