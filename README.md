# DatSciS24_HW_repo

Week 1 - HW 1

HW 1 (dshw1.py)
Write a function count_vowels(word) that takes a word as an argument and returns the number of vowels in the word
Iterate through the following list of animals and print each one in all caps. animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.

HW 2 (dshw2.py)
1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
3) How to get the rows of a dataframe with row sum > 100?
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
4)Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, reshape this array into two separate 2D arrays, where one represents the rows and the other represents the columns. Write a function, preferably using a lambda function, to calculate the sum of each row and each column separately, and return the results as two separate NumPy arrays
