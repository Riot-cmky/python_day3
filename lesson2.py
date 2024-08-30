#create a function that prints hello world
# # out the string "Hello, World"
# print("Hello, World")
# # ask the user for the day of the week
# # # day_of_week = input("What day of the week is it?")
# # print("Today is" + day_of_week)

# # #concatation is when you  and two strings togethger
# # using a plus sign (+)
# movies_this_week = input("What movies are you watching this week?")
# print("I am watching " + movies_this_week + " this week")
# mood = input("How are you feeling today?")
# print("I am feeling " + mood  )

# # data types for variables in python

# #strings - text
# name = "John" # this ias a string daya type
# #whenever it is wrapped in quotes its a string
# year = '2024'

# #integers - whole numbers
# year = 2024 # this is an integer data type
# # does not need to be wrapped in quotes
# yearFourfromNow = 2028
# subtract = yearFourfromNow - year
# print(subtract)

# #floats - decimal numbers
# priceBigMac = 3.99 # this is a float data set
# priceDoublePounder = 4.99
# totalPrice = priceBigMac + priceDoublePounder

# #booleans - True or False
# isRaining = False # this is a boolean data type
# print(isRaining)

# #Lists - a collection of items
# groceries = ["apples","bananas","carrots"]
# print(groceries)

#Challenge #1
#you and your family are going to a movie and dinner.
#You need a list of movies to Choose from
# the address of the resturant
#the time of the movie
#the time of dinner
#the name of the movie
#the price of the movie
# check to see if the movie is playing in the evening
#how many people are going
#print the entire output in one sentence

movieLists = ["Deadpool","Twisters","Alien:Romulus", "Afraid"]#lists data type
resturantaddress = "37 Lees Creek Ave"
chosenMovie = "Twisters"
movieTime = 6
dinnerTime = 8
moviePrice = 12.99# float data type
inEvening = True
peopleGoing = input("How many people are going? ")
#type coversion converting from one data type to another
number_of_people = 5
print("We are going to see" + chosenMovie + "at" + movieTime + "and then eat dinner at" + resturantaddress + "at" + dinnerTime + "with" + peopleGoing)