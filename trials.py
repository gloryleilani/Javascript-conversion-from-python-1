"""Python functions for JavaScript Trials 1."""


items1 = [1, 'hello', 'true']

def output_all_items(items):

    for item in items:
        
        print(item)

output_all_items(items1)


nums1 = [7, 8, 10, 1, 2, 2]

def get_all_evens(nums):
    
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

get_all_evens(nums1)


items2 = [1, 'hello', true, 500]

def get_odd_indices(items):
    
    result = []

    for i in enumerate(items):
        if i % 2 != 0:
            result.append(items[i])

    return result

get_odd_indices(items2)


items3 = [1, 'hello', true]

def print_as_numbered_list(items):
    
    i = 1
    for item in items:
        print (f'{i}. {item}')
        i += 1

print_as_numbered_list(items3)


start1 = 0
stop1 = 5

def get_range(start, stop):
    
    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums

get_range(start1, stop1)


word1 = 'hello world'

def censor_vowels(word):
    
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append("*")
        else:
            chars.append(letter)

    return "".join(chars)

censor_vowels(word1)


string1 = 'hello_world'

def snake_to_camel(string):
    
    camel_case = []

    string = string.split("_")

    for word in string:
        camel_case.append(f'{word[0].upper()}{word[1:]}')
        
    return "".join(camel_case)

snake_to_camel(string1)


words1 = ['hello', 'world']

def longest_word_length(words):
    
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

longest_word_length(words1)


string2 = 'aaaabbbbcccca'

def truncate(string):
    
    result = []

    for char in string:
        if len(result) == 0 or char != result[len(result)-1]:
            result.append(char)

    return "".join(result)

truncate(string2)


string3 = '(Oh no!)('
def has_balanced_parens(string):
    
    parens = 0

    for char in string:
        if char == "(":
            parents +=1
        elif char == ")":
            parens -=1

        if parens < 0 or parens > 0:
            return False

    return (parens == 0)

has_balanced_parens(string3)


string4 = 'Hello, world! Cows go moooo...'

def compress(string):
    
    compressed = []

    curr_char = ""

    char_count = 0

    for char in string:

        # if char iterating on is diff from prior char
        if char != curr_char:
            compressed.append(curr_char)

            #If 2 or more chars are the same, append the number:
            if char_count>1:
                compressed.append(str(char_count))

            #Set the char iterating on to be the "prior char"
            curr_char = char

            #reset the char count
            char_count = 0

        # if char iterating on is the same as prior char
        char_count += 1

    #No longer in loop: 
    compressed.append(curr_char)

    if char_count > 1:

        compressed.append(str(char_count))

    return "".join(compressed)

compress(string4)
