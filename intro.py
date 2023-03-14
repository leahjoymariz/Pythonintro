
print("Hello World!")

# this is a comment

# create variables
name = "Leah"
last_name = 'Duco'
age = 99
total = 12.34
found = False

# print each variable, save and run the script
print(name)
print(last_name)
print(age)
print(total)
print(found)

# contact string
print(name + " " + last_name)

# math
print(1+2)
print(3*3)
print(10-3)
print(7/4)

# error
#print("name" + 3)

#condtional statements
if(age < 100):
    print("don't worry you are super young!!")
    #print("inside the if")
    #print("still in the if")
elif (age == 100):
    print("congratulations, you got to live a century")
else:
    print("Sorry, you are getting old")




# functions

def say_hello():
    print("Hello there")
    print("from a function")


def say_hi(name):
    print("Hi " + name)


def get_day():
    return "Monday"


# call a function
say_hello()
say_hello()

say_hi("Jane")
say_hi(name)

day = get_day()
print("Today is " + day)





