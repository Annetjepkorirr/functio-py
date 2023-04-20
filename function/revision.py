
# Write a Python function that takes a string and returns the reverse of the string.
def word(string):
   return string[::-1]

#string ="eclipsecross","rush","bmw"
# print(word("string"))

# Write a Python function that takes a list of strings and 
# returns the longest string in the list.
def longest_string(string_list):
    max_lenth =0
    longest_string =""
    for string in string_list:
      if len(string) > max_lenth:
         max_lenth = len(string)
         longest_string(string)
    return longest_string     

   #  strings =["audi","eclipsecross","rogue","rush","bmw"]
   #  print(longest_string(strings))

# write a Python function that takes a list of integers and returns the sum of all 
# the numbers in the list.
def sum_of_list(lst):
    return sum(lst)

# lst = [1, 2, 3, 4, 5]
# print(sum_of_list(lst))


# Write a Python function that takes a list of numbers and returns the product of all 
# the numbers in the list.    
def product_of_numbers(numbers_list):
    product = 1
    for number in numbers_list:
        product *= number
    return product