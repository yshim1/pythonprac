#Python Gotcha - counterintuitive feature of programming

def createStudent(name, age, grades=[]):    #Create Student method that takes name, age, and list of grades (default empty list)
    return {
        'name': name,                       #Returns dictionary object
        'age': age,
        'grades': grades
    }
    
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])

#Look at what calling addGrade function returns
addGrade(chrisley, 90) #OUTPUT>> [90]
addGrade(dallas, 100) #OUTPUT>> [90,100]



#Both objects have the same memory id
print(id(chrisley['grades']))
print(id(dallas['grades']))

#When using a mutable data type in function arguments: 
"""
Default parameter values are evaluated from left to right when the function definition is executed. 
This means that the expression is evaluated once, when the function is defined, and that the same 
“pre-computed” value is used for each call.
Mutable data types: Set, list, dictionaries
Immutable data types: int, float, tuples, strings
"""
#In the previous example, the list is made once and each time function is called it uses that same created list

#The solution is to use grades=None
def createPerson(name, age, hobby = None):
    if hobby is None:
        hobby = []
    return {
        'name':name,
        'age':age,
        'hobby':hobby
    }
def addHobby(person, hobby):
    person['hobby'].append(hobby)
    print(person['hobby'])
    
yamlak = createPerson('Yamlak', 22)
yonathan = createPerson('Yonathan', 22)
addHobby(yamlak,'Weightlifting')
addHobby(yonathan,'Soccer')
print(id(yamlak))
print(id(yonathan))