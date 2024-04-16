#Tien Tran
#Cite: concatenation - https://careerkarma.com/blog/python-operator/ 

def printnums(lst): #this function takes in integers and adds them together to compute the sum
    sum = 0         #initialize variable sum
    for val in lst: 
        sum += val  #adds the values within the list together 
    print(sum)      #prints sum 
    return sum

def get_first_letters(words):
    lst = []                            #initialize empty list
    result = str()                      #initialize variable result
    for word in words:          
        result += word[0]               #'+=' to concatenate the first letter from every word from  'word[0]'
    print(f"First letters: {result}")   #prints first letters 
    return result
    

# Test functions
assert printnums([1,2,3,4,5]) == 15
print("correct")
assert printnums([2,4,6,8,10]) == 30
print("correct")
assert printnums([3,6,9,12,15]) == 45
print("correct")


assert get_first_letters(["dog", "cat", "sheep", "bunny"]) == "dcsb"
print("correct")
assert get_first_letters(["apple","banana","pineapple","mango"]) == "abpm"
print("correct") 
assert get_first_letters(["pink","blue","yellow","green"]) == "pbyg"
print("correct")


    