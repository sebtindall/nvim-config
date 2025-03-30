#!/bin/python3

#STRINGS
#Print string
print("hello world.")
print('hello world!')
print("""this string runs
multiple lines""")#triple quote for multi-line
print("This string is "+"awesome!")#We can also concatenate
print('\n') #new line
print("Test that new line out.")

print('\n')
#MATH
print(50+50) #add
print(50-50) #subtract
print(50*50) #multiply
print(50/50) #divide
print(50+50-50*50/50) #pemdas
print(50**2) #exponents
print(50%6) #modulo - takes what is left over
print(50/6) #division with remainder (or float)
print(50//6) #no remainder

print('\n')
#VARIABLES AND METHODS

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) # title case
print(len(quote)) #counts characters

name = "Shoe" #string
age = 20 #int
atar =  60.5 #float - has a decimal

print(int(age))
print(int(30.2))
print(int(30.6)) #Will it round? NO.

print("My name is " + name + " and I am " + str(age) + " years old.")

age +=1
print(age)

birthday=1
age +=birthday
print(age)


print('\n')
#FUNCTIONS

def who_am_i(): #this is a finction without parameters
	name="Shoe" #local variable
	age = 20
	print("My name is " + name + " and I am " + str(age) + " years old.")
	
who_am_i()

def add_one_hundred(num):
	print(num+100)
	
add_one_hundred(100)

def add(x,y):
	print(x+y)

add(8,2)

def multiply(x,y):
	return x*y

multiply(8,2)
print(multiply(8,2))

def square_root(x):
	print(x ** .5)
	
square_root(64)

def nl(): #new line
	print('\n')
	
nl()
#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 !=9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5="True"
print(type(bool5))

nl()
#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7>5
less_than = 5 > 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 >= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 >5) or (5 >7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False


nl()
#CONDITIONAL STATEMENTS - if/else

def drink(money):
	if money >=2:
		return "Here if your Ramune sir!"
	else:
		return "Sorry, it appears you're broke."

print(drink(3))
print(drink(1))
nl()
def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "Here's you're Soju!"
	elif (age >= 21) and (money < 5):
		return "Gimme Mula"
	elif (age < 21) and (money >=5):
		return "I'm calling the feds."
	else:
		return "You're bloke plus im calling the feds."
		
print(alcohol(21,1))
print(alcohol(20,6))
print(alcohol(20,1))
print(alcohol(27,6))


nl()
#LISTS - Have brackets []
movies = ["The Dark Knight", "Your Name", "Godzilla:Minus One", "Nope"]

print(movies[0]) #returns first item in list
print(movies[1]) #returns second item in list
print(movies[1:3]) #returns the first index number right until the last number, but not including the last number
print(movies[1:])
print(movies[:1])
print(movies[-1]) #return last item in list

print(len(movies)) #count items in list

movies.append("Gamer Girl")
print(movies) #appends to the end of the list

movies.insert(2, "Anarchy")
print(movies)

movies.pop() #removes the last item from list
print(movies)

movies.pop(0) #removes first item from list
print(movies)

liyah_movies = ["Suzume", "Greenland", "Brave"]
our_favourite_movies = movies + liyah_movies
print(our_favourite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)
grades[0][1] = 83
print(grades)


nl()
#TUPLES - Do no change, ()
grades = ("a", "b", "c", "d", "f")

print(grades[1])


nl()
#LOOPING

#For loops - start to finish of an iterate
vegetables = ["cucumber", "lettuce", "carrot"]
for x in vegetables:
	print (x)


#WHILE LOOPS - execute as long as True
i = 1

while i < 10:
	print(i)
	i += 1


nl()
#ADVANCED STRINGS

my_name = "Shoe"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:1])
print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "         hello       "
print(too_much_space.strip())

print("a" in "apple") #True
print("A" in "apple") #False

letter = "a"
word = "apple"
print(letter.lower() in word.lower()) #improved

movie = "Nope"
print("My favourite movie is {}.".format(movie))
print("My favourite movie is %s."% movie)
print(f"My favourite movie is {movie}.")


nl()
#DICTIONARIES - key/value pairs {} 

drinks = {"Mojito": 8, "Beeru": 9, "Pina Colada Shake": 11} #drink is the key, price is the value
print(drinks)
employees = {"Finance": ["Kevin", "Oscar", "Angela"], "IT": ["Dwight", "Jim", "Michael"], "HR": ["Toby", "Temp"]}
print(employees)
employees['Legal'] = ["Frond"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andy", "Pam"]})
print(employees)

drinks['Mojito'] = 9
print(drinks)

print(drinks.get("Mojito"))

