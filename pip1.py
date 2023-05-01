# 1 .Write a Python function that takes two arguments 
#(a and b) and returns their sum.

def add_values(a,b):
    
    sum = a+b
    print(8,7)

    # 2 Write a Python function that takes a string as input and returns the string reversed.

def reverse(string):
        string = list(string)
        string.reverse()
        return "".join(string)
 
s = "Watermellon"

print(reverse(s))
 
 # 3 Write a Python function that takes a list of integers as input and returns the sum of all 
#the integers in the list.

def sum_of_numbers(values):
    count = 0
    for number in values:
        count += number
    return count

values = [1, 2, 3, 4, 5]
print(f'The sum of the list({15})')

# 4Write a Python function that takes a list of integers 
# as input and returns a new list with all the even numbers removed.
def remove_even_numbers(even_numbers):
 
 print(list(filter(lambda checks: checks % 2 == 0, even_numbers)))





# 5Write a Python function that takes a list of integers as input and returns the highest 
#value in the list.
# ​Without using max() function of the list
def largestNum(list1):
  length = len(list1)
num = 0
for i in range(length):
 if(i == 0 or list1[i] > num):
  num = list1[i]
#   return num

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_num = largestNum(list1)
print(max_num)

# 6 Write a Python function that takes a list of strings
#as input and returns a new list with all the strings capitalized.

def return_to_uppercase(message):
   x = ["a,b,o,u,t,u,u"]
   text = x.upper() 
   print(text)

   
