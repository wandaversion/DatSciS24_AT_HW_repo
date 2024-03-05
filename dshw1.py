# Data Science Bootcamp | Spring 2024 | HW # 1 | A.T.
#!/usr/bin/env python3

vowels = ['a', 'e', 'i', 'o', 'u']
def vowel_count(word):
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    print(f'There are {count} vowels in {word}')
    return count

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']       # list to iterate through for # 2
def capitalize_all():
    print("The animals are ")
    for word in animals:
        w = word.upper()
        print(w)

def odd_or_even():
    for num in range(21):                                   # inclusive of 20
        if num % 2 == 0 :
            print(f'{num} is even')
        else:
            print(f'{num} is odd')

def sum_of_integers(a, b):
    a = int(a)                                              # str value from input to int for arithmetic
    b = int(b)
    total = a + b
    print('Total is ' + str(total))
    return total


if __name__ == '__main__':
    print("Selection which function you'd like to demo (0 -4)")
    print("Enter 0 for all ")
    print("Enter 1 for vowels ")
    print("Enter 2 for animals in CAPS ")
    print("Enter 3 for odd or even ")
    print("Enter 4 for sum_of_integers ")
    selection = int(input("Please show me: "))              # Map
    function_map = {                                        # more streamlined than if/else
        1: lambda: vowel_count(input("Please provide a word for vowel count: ")),
        2: lambda: capitalize_all(),
        3: lambda: odd_or_even(),
        4: lambda: sum_of_integers(input("What is integer a? "), input("What is integer b? ")),
    }
    if selection == 0:       # print(f'Vowels (provide input), Animals, Odd/Even, Sum of Ints (provide inputs)')
        for key in range (1, 5):
            function_map[key]()
    elif selection in function_map:
        function_map[selection]()

'''
1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
2. Iterate through the following list of animals and print each one in all caps.
  animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

def all_prompt():
    word = input("Please provide a word for vowel count: ")
    vowel_count(word)
    a = input("What is integer a? ")
    b = input("What is integer b? ")
    sum_of_integers(a, b)'''