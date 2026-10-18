#1. DEclare an empty list
lista = []
#2.Declare a list with more than 5 items
list2 = ['Hola', 'Cris', 'Emo','Bonjour', 'Hallo']
#3. Find the length more than 5 items
lon= len(list2)
#4. Get the first item, the middle item and the last item of the list
it1= list2[0]
#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Cristian',21,1.75, 'Single', 'Acer 1454']
#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
#7. Print the list using print()
print(it_companies)
#8. Print the number of companies in the list
print(len(it_companies))
#9. Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[-1] )
#10. Print the list after modifying one of the companies
it_companies[0] = 'Tesla'
print(it_companies)
#11. Add an IT company to it_companies
it_companies.append('Walmart')
print(it_companies)
#12.Insert an IT company in the middle of the companies list
it_companies.insert(4, 'CarreFood')
print(it_companies)
#13.Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0]=it_companies[0].upper()
print(it_companies)
#14. Join the it_companies with a string '#;  '
string = '#; '
it_companies.extend(string)
print(it_companies)
#15.Check if a certain company exists in the it_companies list.
ex = 'Tesla' in it_companies
ex1 = 'TESLA' in it_companies
print(ex)
print(ex1)
#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)
#17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse = True)
print(it_companies)
#18. Slice out the first 3 companies from the list
print(it_companies[0:3])
#19. Slice out the first 3 companies from the list
print(it_companies[-3:])
#20. Slice out the middle IT company or companies from the list
midd = len(it_companies)//2
print(it_companies[midd])
#21.Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
#22. Remove the middle IT company or companies from the list
it_companies.pop(midd)
print(it_companies)
#23. Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)
#24. Remove all IT companies from the list
it_companies.clear()
print(it_companies)
#25. Destroy the IT companies list
del it_companies
#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
ne = front_end + back_end
print(ne)
#27. After joining the lists in question 26. 
#Copy the joined list and assign it to a variable full_stack
#then insert Python and SQL after Redux.
full_stack = ne.copy()
print(full_stack)


#Exercises: Level 2
#1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
print(ages.sort())
#Add the min age and the max age again to the list
mino = min(ages)
maxi = max(ages)
print(mino)
print(maxi)
#Find the median age (one middle item or two middle items divided by two)
medi = ages[0] + ages[1] / 2
print(medi)
#Find the average age (sum of all items divided by their number )
average   = sum (ages) /len(ages)
print(average)
#Find the range of the ages (max minus min)
ranges = max (ages) - min(ages)
print(ranges)
#Compare the value of (min - average) and (max - average), use abs() method
print(abs(min(ages) - average))
print(abs(max(ages) - average))
#1. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
middle = len(countries) // 2

print(countries[middle])
#2. Divide the countries list into two equal lists 
# if it is even if not one more country for the first half.
div = len(countries) // 2
pri_mit = countries[:div]
seg_mit = countries[div:]
print(pri_mit)
print(seg_mit)
#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
# Unpack the first three countries and the rest as scandic countries.
coun = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third,*scandinc_countries = coun
print(first)
print(second)
print(third)
print(scandinc_countries)