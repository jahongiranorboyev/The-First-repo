# 1
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# print(a-b,a+b,a/b,a*b,a//b,a%b)

# 2
# a = "John"
# print("the best one is " + a)

# 3
# name = input("What is your name? ")
# print("Hello " + name + "!")

# 4
# name = input("What is your name? ")
# surname = input("What is your surname? ")
# print("Hello " + name)
# print("Hello " + surname)

# 5
# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))
# result = a+b
# print(result)

# 6
# a = int(input('Enter a number: '))
# b = int(input('Enter another number: '))
# c = int(input('Enter another number: '))
# res = (a+b)*c
# print(res)

# 7
# a = int(input("Enter the number of pizza before having pizza:"))
# b = int(input("Enter the number of pizza after having pizza:"))
# c = a-b
# print(c,"The number of pizzas left : ")

# 8
# a = int(input('Enter  your age : '))
# print('the next year ,your age will be  ',a+1)

# 9
# a = int(input('Enter the total amount of money that they should pay for their meal: '))
# b = int(input('Enter the total amount of people to pay for their meal: '))
# print('The money for every person is $   ',a//b)

# 10
# a = int(input('Enter a number of days that you would like to count : '))
# print('There are', a*24, 'hours ',a*24*60,'minutes',a*24*60*60,'seconds')

# 11
# a = int(input("Enter kg : "))
# print('the pounds of your kg entered :',a*2.204)

# 12
# a = int(input('please enter an integer which is greater than 100: '))
# b = int(input('please enter an integer which is less than 10: '))
# print( 'The frequency of the number ',b,'occurring within the range of 1 to ',a,':  ', a//b)

# 13
# a = int(input('Enter a number: '))
# b = int(input('Enter another number:'))
# if a>b :
#     print(a,b,sep='\t')
# else:
#     print(b,a,sep='\t')

# 14
# num = int(input("Enter a number between 10 and 20 : "))
# if 10 <= num <= 20:
#     print('thank you for using')
# else:
#     print('''an incorrect choice !
#      please try again''')

# 15
# favorite_colors = input("What color is your favorite color? ")
# if favorite_colors == "green"=="Green"=="GREEN":
#     print(" my favorite color is also ", favorite_colors)
# else:
#     print(" my favorite color is not ", favorite_colors,'''
#     I do like green''')


# 16
# inquiry_rain = input("Is it raining? ")
#
# if inquiry_rain == "yes":
#     print("Take your umbrella with you.")
# elif inquiry_rain == "I have no idea":
#     print("Find out to clarify whether it is raining or not.")
# else:
#     print("Have a good day!")

# 17
# age_election = input("What is your age? ")
# if int(age_election) >= 18:
#     print("You can elect !!! ")
# else:
#     print("You are not allowed to elect  !!! ")

# 18
# num = int(input("Enter a number: "))
# if num < 10:
#     print("very small!")
# elif 10<=num<=20:
#     print("correct!")
# else:
#     print("very huge !")

# 19
# num = int(input("Enter a number which can be only 1 ,2 and 3: "))
# if num == 1:
#     print("thanks!")
# elif num == 2 :
#     print("correct!")
# else:
#     print("incorrect!")

# # 20
# surname_name_user = input("What is your surname and name? ")
# age_user = int(input("What is your age? "))
# if age_user < 18:
#     print("You have been joined to teenth group ")
# elif 18<= age_user < 35:
#     print("You have been joined  to middle adult group ")
# elif 35<= age_user < 55:
#     print("You have been joined to adult group ")
# else:
#     print("you have been joined  to adult group and more ")

# 21
# num = int(input("Enter a number: "))
# hundred_num = num//100
# ten_num = num//10 % 10
# unit_num = num % 10
# result = hundred_num + ten_num + unit_num
# print(result)
# if hundred_num > ten_num and hundred_num > unit_num:
#     print("hundred_num")
# elif ten_num > hundred_num and ten_num>unit_num:
#     print("ten_num")
# elif unit_num > hundred_num and unit_num> ten_num:
#     print("unit_num")

# 22
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("even")
# elif num % 2 != 0:
#     print("odd")

# 23/24
# num1 = int(input("please enter a number: "))
# num2 = int(input("please enter another number: "))
# if num2 % num1 == 0:
#     print("the 2nd entered number is  divisible by the 1st entered ")
# else:
#     print("the 2nd entered number is not  divisible by the 1st entered")

# 25
# temperature_celsius = float(input("please enter temperature in Celsius: "))
# temperature_fahrenheit  = float(input("please enter temperature in Fahrenheit: "))
# print("the temperature in celsius is ", (temperature_celsius * 9 / 5)+32 )
# print("the temperature in fahrenheit is ", (temperature_fahrenheit - 32) * 5 / 9)

# 26
# a_side_triangle = int(input("Enter a side triangle: "))
# b_side_triangle = int(input("Enter another side triangle: "))
# c_side_triangle = int(input("Enter a third side triangle: "))
# if a_side_triangle + b_side_triangle < c_side_triangle:
#     print("The triangle can be made using those three sides ")
# elif a_side_triangle + c_side_triangle < b_side_triangle:
#     print("The triangle can be made using those three sides ")
# elif b_side_triangle + c_side_triangle < a_side_triangle:
#     print("The triangle can be made using those three sides ")
# else:
#     print("The triangle can not be made using those three sides ")

# 27
# density_item = int(input("Enter the density of item "))
# volume_item = int(input("Enter the volume of item "))
# mass_item = density_item * volume_item
# print("The mass of item is ", mass_item)

# 28
# text = input("Enter any text")
# print(text[::-1])

# 29
# it had been done!!!

# 30
# text = input("Enter any text that you would like to >>> ")
# print(text.split(','))

# 31
# Write a program that calculates the percentage of uppercase and lowercase letters in an input string
# def calculate_letter_percentage(input_string):
#     total_letters = len(input_string)
#     uppercase_count = sum(1 for char in input_string if char.isupper())
#     lowercase_count = sum(1 for char in input_string if char.islower())
#
#     uppercase_percentage = (uppercase_count / total_letters) * 100
#     lowercase_percentage = (lowercase_count / total_letters) * 100
#
#     return uppercase_percentage, lowercase_percentage
#
# input_string = input("Enter a string: ")
# uppercase_percentage, lowercase_percentage = calculate_letter_percentage(input_string)
#
# print(f"Percentage of uppercase letters: {uppercase_percentage:.2f}%")
# print(f"Percentage of lowercase letters: {lowercase_percentage:.2f}%")

# 32
# text = input("Enter a name: ")
# print(text.upper())

# 33
# surnames = '''
# Eshmatov toshmat
# Olimov Olim
# Nodirov Anvar
# Sardor Toshtemirov'''
# looking_name = input('What is your name:')
# if looking_name in surnames:
#     print(looking_name,'is in surnames')
# else:
#     print(looking_name,'is not in surnames')

# 34
# text = input("Enter any text :")
# print('\n'.join(text))

# 35
# text = input("Enter your text")
# print(' '.join(text))

# 36/37
# text = input("Enter a name:")
# print('\n'.join(text))\\

# 38
# text = input("Enter  any text:")
# start = int(input("Enter the start index:"))
# end = int(input("Enter the end index:"))
# print(text[start:end])

# 39
# number_ = input("Enter a number: ")
# print(number_[::-1])

# 40/41
# text = input(" enter your text")
# if "apple" in text :
#     print("apple is available")
# else:
#     print("apple is not available")

# 42
# it has been done on class!!

# 43 similar to last ones

# 44
# matn = "Bu yerda apple mavjud"
#
# if "apple" in matn and len("apple") > 5:
#     print("Matnda uzun 'apple' mavjud")
# else:
#     print("Matnda qisqa 'apple' mavjud")

# 45
# it is similar to last one

# 46
# text = input("Enter any text:")
# print(text.replace("apple", "orange"))

# 47
# text = input("Enter any text")
# print(text.replace("banana","kiwi").replace("orange","kivi"))

# 48
# text = input("Enter your text")
# if 'apple' in text:
#     print(text.index('apple'))
# else:
#     print("Sorry!! apple is not in the list")

# 49
# text = input("Enter your text")
# if 'banana' in text:
#     print(text.index('banana'))
# else:
#     print("Sorry!! apple is not in the list")

# 50
# text = input("Enter your text")
# if "apple" in text:
#     print(len("apple"))
# else:
#     print('sorry no apple')

# 51
# text = input("Enter your text")
# if "apple" in text:
#     length_apple = len("apple")
#     print(length_apple)
# else:
#     print('sorry no apple')

# 52/53
# text = input("Enter your text")
# if "apple" in text:
#     print(text.replace("apple", "Apple"))
# else:
#     print('no apple here')

# 54\55
# text = input('Enter a string: ')
# if "apple" in text:
#     print(text.replace("apple", "APPLE"))
# else:
#     print('Not a APPLE')

# 56/57/58/59 are similar to ones expressed above

# 60
# text  = input("Enter any string:")
# if "apple" in text:
#     print(text.replace("apple", "apple"*3))
# else:
#     print("Not apple")

# 61
# text = input('Enter a string: ')
# if 'banana' in text:
#     print(text.replace('banana', 'banana'*4))
# else:
#     print('Not a banana')


# from 62 to 69 is similar
# text = input('Enter a string: ')
# if "apple" in text and "banana" in text:
#     print(text.replace("apple", "apple" * 3).replace("banana", "banana" * 4))
# else:
#     print("sorry!! there is no apple or banana")
# 70
# text = input('Enter a string: ')
# if "o" in text or "i" in text or "u" in text or "a" in text or "e" in text:
#     print(text.replace("o", "O" ).replace("i", "I" ).replace("u", "U" ).replace("a", "A" ).replace("e", "E"))
# else:
#     print("sorry!! no o or i or u or a e")

# 71
# surname_name_user = input("What is your surname and name ? ")
# age_user = int(input("What is your age ? "))
# for letter in range(age_user):
#     print(surname_name_user)

# 72/73
# they had already  been done!text'


# 1
# a program that calculate the length of string entered
# text = input("Enter any text :")
# print(len(text))

# 2
# def count_characters(string):
#     # Create an empty dictionary to store character frequencies
#     char_frequency = {}
#
#     # Iterate through each character in the string
#     for char in string:
#         # Increment the count for the character in the dictionary
#         char_frequency[char] = char_frequency.get(char, 0) + 1
#
#     return char_frequency
#
# # Example usage:
# input_string = input("Enter a string: ")
# frequency_dict = count_characters(input_string)
#
# # Print the character frequencies
# for char, freq in frequency_dict.items():
#     print(f"'{char}' appears {freq} times")

