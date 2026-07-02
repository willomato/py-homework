#variables, strings, etc.
name = "alex" # must have quotes
age = 19
uoftstatus = True

# first attempt: print(name + " is " + age + " and is a UofT student: " + uoftstatus) >> you cannot "+" a string with an int or a bool
# you have to explicitly convert str():
print(name + " is " + str(age) + " and is a UofT student:" + str(uoftstatus)) 
# OR... you can use f-strings which doesn't require str() at all. but you will need to use {} on variables: 
print(f"{name} is {age} and is a UofT student:{uoftstatus}") 
# do not include "+" or needing to seperate strings with quotes

#doing another example with f-string
course = "CSC108"
numstudents = 230
average = 87.2

print(f"in this course, {course}, there are about {numstudents} students. the class average is {average}.")

# there are 4 types of data types to remember: 
print(type(age))
print(type(uoftstatus))
print(type(name))
print(type(average))