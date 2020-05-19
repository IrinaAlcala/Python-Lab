

Exercise 1


   
   letter = input('Please enter a letter from the alphabet (a-z or A-Z)')
if letter in 'A a E e I i O o U u Y y' == True :
    print(f'the letter {letter} is a vowel')
else: 
    print(f'the letter {letter} is a consonant')


Exercise 2


   phrase = ' '
while phrase != 'quit':
    phrase = input('Please enter a word or phrase')
    print(f'what you entered is {len(phrase)} characters long')

    Exercise 3

human_years = int(input("Input a dog's age in human years: "))
if human_years < 3:
   dog_years = human_years * 10
else:
   dog_years = 20 + (human_years - 2) * 7
print(f"The dog's age in dog years is {dog_years}")



Exercise 4



side_a = input('Enter the length of the first side of a triangle ')
side_b = input('Enter the length of the second side of a triangle ')
side_c = input('Enter the length of the third side of a triangle ')

if side_a == side_b and side_b == side_c : 
    print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is an equalateral triangle')
elif side_a != side_b and side_b != side_c : 
    print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a scalene triangle')
else:
    print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a isosceles triangle')


Exercise 5

term = 0
a = 0
b = 1
while term < 50:
  if term < 2:
    print(f'term: {term} / number: {term}')
  else:
    num = a + b
    print(f'term: {term} / number: {num}')
    a = b
    b = num
  term += 1


    Exercise 6

mo = input('Enter the month of the season (Jan - Dec): ')
day = int(input('Enter the day of the month: '))
if mo in ('Jan', 'Feb', 'Mar'):
  season = 'Winter'
elif mo in ('Apr', 'May', 'Jun'):
  season = 'Spring'
elif mo in ('Jul', 'Aug', 'Sep'):
  season = 'Summer'
else:
  season = 'Fall'
if mo == 'Mar' and day > 19:
  season = 'Spring'
elif mo == 'Jun' and day > 20:
  season = 'Summer'
elif mo == 'Sep' and day > 21:
  season = 'Fall'
elif mo == 'Dec' and day > 20:
  season = 'Winter'
print(f'{mo} {day} is in {season}')





        
