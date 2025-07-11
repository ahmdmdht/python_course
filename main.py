import email_validation
import letter_location_with_index
import multiplication
import sorted_elements
import vowel_count
import mario_pyramid

## check name correcteness
user_input = input("Enter your name: ")
print(email_validation.name_validation(user_input))


## define letter i locator and sum number of i letters
word=input("enter the word : ")
print(letter_location_with_index.i_location(word))


#### make mario pyramid in list and its height given by user
numOfList=int(input("num of elements in list:  "))
list=[]
print(mario_pyramid.pyramid_in_list(numOfList))


### give the result of POWER OF ELEMENT given by the user
user_input=int(input("enter rhe elements :  "))
print(multiplication.power_of_nums(user_input))


### sort elements given by the user ascending or descending
num_Of_elements=int(input("num of elements in list :  "))
list=[]
print(sorted_elements.sorted_elements(num_Of_elements))


### count the vowel letters in word given by user
y=input("enter the word : ")
print(vowel_count.vowelcount(y))


