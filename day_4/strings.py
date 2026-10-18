#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
"""st1= 'Thirty'
st2= 'Days'
st3= 'Of'
st4= 'Python'
sentence = '{} {} {} {}.'.format(st1,st2,st3,st4)
print(sentence)
"""
#2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
"""st1 = 'Coding'
st2 = 'For'
st3 = 'All'
sentence = '{} {} {}'.format(st1,st2,st3)
print(sentence)"""
#3.Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'
#4.Print the variable company using print().
print(company)
#5.Print the length of the company string using len() method and print().
lon= len(company)
print(lon)
#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())
#7.Change all the characters to lowercase letters using lower() method.
print(company.lower())
#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9. Cut(slice) out the first word of Coding For All string.
cut = company [7:]
print(cut)
#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
#12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
com = 'Python for Everyone'
print(com.replace('for Everyone', 'for All'))
#13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split( ' '))
#14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
st = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(st.split(', '))
#15.What is the character at index 0 in the string Coding For All.
print(company[0]) 
#16. What is the last index of the string Coding For All.
print(company[-1]) 
#17. What character is at index 10 in "Coding For All" string.
print(company[10]) 
#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
va = 'Python For Everyone'
print(va[0:14:4])
#19. Create an acronym or an abbreviation for the name 'Coding For All'.
print(company[0:14:4])
#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
#21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
code = 'Coding For All People'
print(company.rfind('l'))
#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sen = 'You cannot end a sentence with because because because is a conjunction'
print(sen.find('because'))
#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
sen1 = 'You cannot end a sentence with because because because is a conjunction'
print(sen.rindex('because'))
#25.Slice out the phrase 'because because because' in the following sentence: 
#'You cannot end a sentence with because because because is a conjunction'
print(sen[31:55])
#26. Find the position of the first occurrence of the word 'because' in the following sentence: 
# 'You cannot end a sentence with because because because is a conjunction'
print(sen.find('because'))
#27. Slice out the phrase 'because because because' in the following sentence:
#'You cannot end a sentence with because because because is a conjunction'
print(sen[31:55])
#28.Does 'Coding For All' start with a substring Coding?
#29.Does 'Coding For All' start with a substring Coding?
#30.'   Coding For All      '  , remove the left and right trailing spaces in the given string.
st21='   Coding For All      '
print(st21.strip())
#31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print('The variable which return True is \"thirsty_days_of_python\"')
#32.The following list contains the names of some of python
# libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result= ' '.join(libraries)
print(result)
#33. Use the new line escape sequence to separate the following sentence
seq = """
I am enjoying this challenge.\n
I just wonder what is next."""
print(seq)
#34. Use a tab escape sequence to write the following lines
"""Name      Age     Country   City
Asabeneh  250     Finland   Helsinki"""
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")
#35. Use the string formatting method to display the following:
print('{} = {}'.format('radius',10))
print('{} = {} * {} ** {}'.format('area',3.14, 'radius', 2))
print('The area of a circle with radius {} is {} meters square'.format(10, 314))
#36. Make the following using string formatting methods:
print('{} + {} = {}'.format(8,6,8+6))
print('{} - {} = {}'.format(8,6,8-6))
print('{} * {} = {}'.format(8,6,8*6))
print('{} / {} = {}'.format(8,6,8/6))
print('{} % {} = {}'.format(8,6,8%6))
print('{} // {} = {}'.format(8,6,8//6))
print('{} ** {} = {}'.format(8,6,8**6))