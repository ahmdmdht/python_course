import email_validation as e_v
import letter_location_with_index as lli
import multiplication
import sorted_elements as s_e
import vowel_count as v_c
import mario_pyramid as m_p

## check name correcteness
user_input = input("Enter your name: ")
print(e_v.name_validation(user_input))


## define letter i locator and sum number of i letters
word=input("enter the word : ")
print(lli.i_location(word))


#### make mario pyramid in list and its height given by user
numOfList=int(input("num of elements in list:  "))
list=[]
print(m_p.pyramid_in_list(numOfList))


### give the result of POWER OF ELEMENT given by the user
user_input=int(input("enter rhe elements :  "))
print(multiplication.power_of_nums(user_input))


### sort elements given by the user ascending or descending
num_Of_elements=int(input("num of elements in list :  "))
list=[]
print(s_e.sorted_elements(num_Of_elements))


### count the vowel letters in word given by user
y=input("enter the word : ")
print(v_c.vowelcount(y))


