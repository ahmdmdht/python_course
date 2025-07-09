###program that prints the locations of "i" character in any string you added.

def i_location(word):
    c=0
    for index, i in enumerate(word):
        if i=='i':
         c+=1
         print(f"Index: {index}, count letter i: {c}")
        
        else:
            continue
    print(f"sum of i {c}")
    
word=input("enter the word : ")
i_location(word)