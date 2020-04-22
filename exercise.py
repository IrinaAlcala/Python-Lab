# Branching & Looping Exercises

color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')
# Write the if...elif...else statement as described in the lesson

if color == 'green':
  print('Go')
elif color == 'yellow':
  print('slow_down')
elif color == 'red':
  print('stop')
else:
  print('bogus')


while True:
  color = input('Enter "green", "yellow", "red" or "quit": ' ).lower()
  print(f'The user entered {color}')

if color == 'quit':
  break
elif color == 'green':      
  print('Go')
elif color == 'yellow':
  print('slow_down')
elif color == 'red':
  print('stop')
else:
  print('bogus')


Exercise 1

letter = input('Enter a letter (a-z): ').lower()
if letter in 'a e u i o':
  print(f'The letter {letter} is a vowel')
else:
  print(f'The letter {letter} is a consonant')


Exercise 2

phrase = ''
while phrase != 'quit':
  phrase = input('Enter a phrase: ')
  print(f'What you entered is {len(phrase)}
  charaters long')

    Exercise 3

human_years = int(input("Input a dog's age in human years:"))
if human_years < 3:
  dog_years = human_years * 10
else:
  dog_years = 20 + (human_years - 2) * 7
print(f"The dog's age in dog years is {dog_years}")


Exercise 4

print('Enter the lengths of three side of a triangle:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == b and b == c:
  print(f'A triangle with sides of {a}; {b} & {c} is an equalateral triangle')
elif a != b and a != c and b != c:
  print(f'A triangle with sides of {a}; {b} & {c} is a scalene triangle')
else:
  print(f'A triangle with sides of {a}; {b} & {c} is a isosceles triangle')


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





        
