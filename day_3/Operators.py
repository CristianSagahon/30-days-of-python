"""
Addition (+)
Subtraction(-)
Multiplication (*)
Division (/)
Modulus (%)
Floor division (//)
Exponentiation(**)

"""
#1. Declare your age as integer variable
age = 21
#2. Declare your height as a float variable
height = 1.75
#3. Declare a variable that store a complex number
complex_number = 1 -1j
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""base = int(input("Enter base: ")) 
height_1= int(input("Enter height: "))
print("The area of the triangle is: ", int((base * height_1)/2)) 
"""
#5.Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""side_a = int(input("Enter side a: ")) 
side_b = int(input("Enter side b: ")) 
side_c = int(input("Enter side c: "))
print("The permeter of the triangle is ", side_a + side_b + side_c) """
#6.Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""lenght = int(input("Enter lenght: "))
width = int(input("Enter width: "))
print("==== AREA ====")
print("The areas is", lenght * width)
print("==== PERIMETER ====")
print("The perimeter is", 2*(lenght + width))
"""
#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
"""radius = float(input("Enter radius:"))
print("The area is ", round(3.14 * radius*radius ,2 ) )
print("The circumference is ", round( 2 * 3.14 * radius ,2))
"""
#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
"""m = 2
b = -2

slope = m
y_intercept = b
if m != 0:
    x_incercept = -b/m
else:
    x_intercept = None
print("Slope(m)", slope)
"""
#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
"""print("==== SLOPE ====")
slope = (10-2) / (6-2)
print(f"The slope is: {round(int(slope))}")
print("==== Euclidean distance ====")
print(f"The Euclidena distance between point: {round(((6-2)**2 + (10-2)**2)**0.5 ,2)}")"""
#10. Compare the slopes in tasks 8 and 9

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
"""py_len = len('python')
dra_len= len('dragon')
print(py_len != dra_len)"""

#13.Use and operator to check if 'on' is found in both 'python' and 'dragon'
"""print('on is python', 'on' in 'python')
print('on is python', 'on' in 'dragon')"""
#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
#print('jargon' in 'I hope this course is not full of jargon' )
#15. There is no 'on' in both dragon and python 
#print('on'not in 'dragon' and 'on' not in 'python')
#16. Find the length of the text python and convert the value to float and convert it to string
"""len_py = len(python)
n_len_py = float(len_py)
str_len_py = str(n_len_py)"""
#17.Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
#I would use % and == to check if really zero the remainder
#18.Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
"""floD= 7 // 3
divi= int(2.7)
print(floD is divi)"""
#19.Check if type of '10' is equal to type of 10
#print('10' == 10)
#20.Check if type of '10' is equal to type of 10
#print(type('10') == type(10))
#21.Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""hours = int(input("Enter hours: "))
rate = int(input('Enter rate per hour: '))
print(f'Your weekly earning is {hours*rate}')"""
#22.Write a script that prompts the user to enter number of years.
# Calculate the number of seconds a person can live. Assume a person can live hundred years
"""years = int(input('Enter number of year you have lived: '))
year = 60*60*24*365
print(f'You have lived for {year * years} seconds.')"""
#23. Write a Python script that displays the following table
"""for n in range(1,6):
     print(n, 1 , n , (n*n) , n*n*n )"""